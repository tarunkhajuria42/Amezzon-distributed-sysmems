package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.parser.dto.QueryResult;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.UUID;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.LinkedBlockingDeque;

public class TransactionPool {

    private final ConcurrentHashMap<String, BlockingQueue<String>> map;
    private DataSource ds;

    //https://www.journaldev.com/2509/java-datasource-jdbc-datasource-example

    public TransactionPool(){
        map = new ConcurrentHashMap<>();
        ds = DataSourceFactory.getMySQLDataSource();
    }

    public synchronized String newTransactionInstance(){
        BlockingQueue<String> blockingQueue = new LinkedBlockingDeque<>();
        String uuid = UUID.randomUUID().toString();
        try {
            new TransactionThread(blockingQueue, ds.getConnection(), this, uuid);
            map.put(uuid, blockingQueue);
        }catch (SQLException e){
            e.printStackTrace();
        }
        return uuid;
    }

    public QueryResult processStatement(String token, String statement){
        map.get(token).offer(statement);
        //FIXME
        return null;
    }

    @SuppressWarnings("WeakerAccess")
    public synchronized void remove(String uuid, Connection connection){
        try {
            connection.close();
        }catch (SQLException e){
            e.printStackTrace();
        }
        map.remove(uuid);
    }
}