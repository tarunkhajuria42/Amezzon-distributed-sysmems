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

    //https://www.journaldev.com/2509/java-datasource-jdbc-datasource-example

    public TransactionPool(){
        map = new ConcurrentHashMap<>();
        ds = new DataSourceWrapper();
    }

    public synchronized String newTransactionInstance() { //TODO throw exception when connection not valid
        BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper> transferQueue = new BidirectionalTransferQueue<>();
        String uuid = UUID.randomUUID().toString();
        try {
            new TransactionThread(transferQueue, ds.getConnection(), this, uuid);
            map.put(uuid, transferQueue);
            return uuid;
        } catch (Exception e) {
            LOGGER.severe(e.getMessage() + "(returning NULL)");
            //LOGGER.severe("SQL state: " + e.getSQLState());
        }
        return null;
    }

    public QueryResultErrorMessageWrapper processStatement(String token, String statement) throws GenericServerError {
        BidirectionalTransferQueue<String, QueryResultErrorMessageWrapper> transferQueue = map.get(token);
        transferQueue.offerRequest(statement);

        try{
            return transferQueue.receiveResponse();
        } catch (InterruptedException e) {
            LOGGER.severe(e.getMessage());
            throw new GenericServerError(e);
        }
    }

    @SuppressWarnings("WeakerAccess")
    public synchronized void remove(String uuid, Connection connection){
        try {
            connection.close();
        }catch (SQLException e){
            LOGGER.severe(e.getMessage());
        }
        map.remove(uuid);
    }
}