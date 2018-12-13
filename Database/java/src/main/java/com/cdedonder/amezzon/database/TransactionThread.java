package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.logging.DatabaseLogger;
import com.cdedonder.amezzon.parser.dto.QueryResult;
import com.cdedonder.amezzon.util.BidirectionalTransferQueue;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class TransactionThread extends Thread {

    private static Logger LOGGER = DatabaseLogger.getLogger();

    private BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper> transferQueue;
    private Connection connection;
    private TransactionPool pool;
    private String uuid;

    public TransactionThread(BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper> transferQueue, Connection connection, TransactionPool pool, String uuid) {
        this.transferQueue = transferQueue;
        this.connection = connection;
        this.pool = pool;
        this.uuid = uuid;
        LOGGER.info("Transaction thread started: " + Thread.currentThread().getName());
        start();
    }

    @Override
    public void run() {
        String statement;
        QueryResultErrorMessageWrapper outerWrapper = new QueryResultErrorMessageWrapper();
        try {
            connection.setAutoCommit(false);
            LOGGER.info("Waiting for statements ... " + Thread.currentThread().getName());
            while (!"commit transaction".equals(statement = transferQueue.receiveRequest())) {
                LOGGER.info("Statement received");
                QueryResultErrorMessageWrapper queryResultErrorMessageWrapper = new QueryResultErrorMessageWrapper();
                try (PreparedStatement stmt = connection.prepareStatement(statement)) {
                    if (stmt.execute()) {
                        LOGGER.info("Query received " + Thread.currentThread().getName());
                        QueryResult queryResult = new QueryResult();
                        try (ResultSet resultSet = stmt.getResultSet()) {
                            ResultSetMetaData metaData = resultSet.getMetaData();
                            int count = metaData.getColumnCount();
                            List<String> column_names = new ArrayList<>(count);
                            List<String> column_types = new ArrayList<>(count);
                            List<List<String>> rows = new ArrayList<>();
                            for (int i = 1; i <= count; i++) {
                                column_names.add(metaData.getColumnName(i));
                                column_types.add(metaData.getColumnTypeName(i));
                            }
                            queryResult.setColumnNames(column_names);
                            queryResult.setColumnTypes(column_types);
                            while (resultSet.next()) {
                                List<String> row = new ArrayList<>(count);
                                for (int i = 1; i <= count; i++) {
                                    if (resultSet.getObject(i) != null) {
                                        row.add(resultSet.getObject(i).toString());
                                    } else {
                                        row.add("");
                                    }
                                }
                                rows.add(row);
                            }
                            queryResult.setRows(rows);
                            LOGGER.info("Query gathered " + Thread.currentThread().getName());
                        } finally {
                            LOGGER.info("Query result sent");
                            queryResultErrorMessageWrapper.setQueryResult(queryResult);
                            transferQueue.offerResponse(queryResultErrorMessageWrapper);
                        }
                    }
                } catch (SQLException e1) {
                    LOGGER.info("Rolling back ...");
                    connection.rollback();
                    queryResultErrorMessageWrapper.setError_message(e1.getMessage());
                } finally {
                    transferQueue.offerResponse(queryResultErrorMessageWrapper);
                }
            }
            LOGGER.info("Committing" + Thread.currentThread().getName());
            connection.commit();
            connection.setAutoCommit(true);
            pool.remove(uuid, connection);
        } catch (InterruptedException e2) {
            LOGGER.severe(e2.getMessage());
            outerWrapper.setError_message(e2.getMessage());
        } catch (SQLException e3) {
            LOGGER.severe(e3.getMessage() + "\nSQL state: " + e3.getSQLState());
            outerWrapper.setError_message(e3.getMessage());
        } finally {
            LOGGER.info("Committed " + Thread.currentThread().getName());
            transferQueue.offerResponse(outerWrapper);
        }
    }

    @Override
    protected void finalize() throws Throwable {
        if (connection != null && !connection.isClosed()) {
            connection.rollback();
            connection.close();
        }
    }
}
