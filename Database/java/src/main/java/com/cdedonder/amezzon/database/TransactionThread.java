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
        start();
    }

    @Override
    public void run() {
        String statement;
        try {
            connection.setAutoCommit(false);
            while (!"COMMIT TRANSACTION".equals(statement = transferQueue.receiveRequest().toUpperCase())) {
                QueryResultErrorMessageWrapper queryResultErrorMessageWrapper = new QueryResultErrorMessageWrapper();
                try (PreparedStatement stmt = connection.prepareStatement(statement)) {
                    if (stmt.execute()) {
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
                            queryResult.setColumn_names(column_names);
                            queryResult.setColumn_types(column_types);
                            while (resultSet.next()) {
                                List<String> row = new ArrayList<>(count);
                                for (int i = 1; i <= count; i++) {
                                    row.add(resultSet.getObject(i).toString());
                                }
                                rows.add(row);
                            }
                            queryResult.setRows(rows);
                        } finally {
                            queryResultErrorMessageWrapper.setQueryResult(queryResult);
                            transferQueue.offerResponse(queryResultErrorMessageWrapper);
                        }
                    }
                } catch (SQLException e1) {
                    connection.rollback();
                }
            }
            connection.commit();
            connection.setAutoCommit(true);
            pool.remove(uuid, connection);
        } catch (InterruptedException | SQLException e2) {
            LOGGER.severe(e2.getMessage());
        }
    }
}
