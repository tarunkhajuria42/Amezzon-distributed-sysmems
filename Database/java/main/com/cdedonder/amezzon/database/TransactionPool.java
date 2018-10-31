package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.parser.dto.QueryResult;
import com.cdedonder.amezzon.util.BidirectionalTransferQueue;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.UUID;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.LinkedBlockingDeque;

public class TransactionPool {

    private final ConcurrentHashMap<String, BidirectionalTransferQueue<String, QueryResult>> map;
    private DataSource ds;

    //https://www.journaldev.com/2509/java-datasource-jdbc-datasource-example

    public TransactionPool(){
        map = new ConcurrentHashMap<>();
        ds = DataSourceFactory.getMySQLDataSource();
    }

    public synchronized String newTransactionInstance(){
        BidirectionalTransferQueue<String, QueryResult> transferQueue = new BidirectionalTransferQueue<>();
        String uuid = UUID.randomUUID().toString();
        try {
            new TransactionThread(transferQueue, ds.getConnection(), this, uuid);
            map.put(uuid, transferQueue);
        }catch (SQLException e){
            e.printStackTrace(); //DEBUG
        }
        return uuid;
    }

    public QueryResult processStatement(String token, String statement){
        BidirectionalTransferQueue<String, QueryResult> transferQueue = map.get(token);
        transferQueue.offerRequest(statement);
        try{
            return transferQueue.receiveResponse(); //TODO implement timeout?
        }catch (InterruptedException e){
            e.printStackTrace(); //DEBUG
        }
        return null;
    }

    @SuppressWarnings("WeakerAccess")
    public synchronized void remove(String uuid, Connection connection){
        try {
            connection.close();
        }catch (SQLException e){
            e.printStackTrace(); //DEBUG
        }
        map.remove(uuid);
    }
}