package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.logging.DatabaseLogger;
import com.cdedonder.amezzon.util.BidirectionalTransferQueue;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.logging.Logger;

public class TransactionPool {

    private static final Logger LOGGER = DatabaseLogger.getLogger();

    private final ConcurrentHashMap<String, BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper>> map;
    private DataSourceWrapper ds;

    public TransactionPool() {
        map = new ConcurrentHashMap<>();
        ds = new DataSourceWrapper();
    }

    public String newTransactionInstance() {
        BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper> transferQueue = new BidirectionalTransferQueue<>();
        String uuid = UUID.randomUUID().toString();
        try {
            new TransactionThread(transferQueue, ds.getConnection(), this, uuid);
            map.put(uuid, transferQueue);
            return uuid;
        } catch (Exception e) {
            LOGGER.severe(e.getMessage() + " (returning NULL)");
        }
        return null;
    }

    public QueryResultErrorMessageWrapper processStatement(String token, String statement) {
        QueryResultErrorMessageWrapper response;
        if (map.containsKey(token)) {
            BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper> transferQueue = map.get(token);
            try {
                transferQueue.offerRequest(statement, 300);
                response = transferQueue.receiveResponse(300);
                if (response == null) {
                    response = new QueryResultErrorMessageWrapper();
                    response.setError_message("Statement execution timed out");
                    LOGGER.severe("timed out");
                }
            } catch (InterruptedException e) {
                LOGGER.severe(e.getMessage());
                response = new QueryResultErrorMessageWrapper();
                response.setError_message(e.getMessage());
            }
        } else {
            response = new QueryResultErrorMessageWrapper();
            response.setError_message("Token not valid");
            LOGGER.info("Invalid token");
        }
        return response;
    }

    @SuppressWarnings("WeakerAccess")
    public void remove(String uuid, Connection connection) {
        try {
            connection.close();
        } catch (SQLException e) {
            LOGGER.severe(e.getMessage());
        } finally {
            map.remove(uuid);
        }
    }
}