package com.cdedonder.amezzon.database;


import com.mysql.cj.jdbc.MysqlDataSource;

import java.sql.Connection;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.LinkedBlockingDeque;

public class TransactionPool {

    private final ConcurrentHashMap<String, BlockingQueue<String>> map;
    private final ConnectionPool


    //https://www.journaldev.com/2509/java-datasource-jdbc-datasource-example

    public TransactionPool(){
        map = new ConcurrentHashMap<>();

        MysqlDataSource ds = new MysqlDataSource();
        //TODO
    }

    public String newTransactionInstance(){
        BlockingQueue<String> blockingQueue = new LinkedBlockingDeque<>();
        TransactionThread thread = new TransactionThread()
    }

    public void remove(String uuid, Connection connection){
        connection.close();
        map.remove(uuid);
    }
}