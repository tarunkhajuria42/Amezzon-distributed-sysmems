package com.cdedonder.amezzon.database;

import java.sql.*;
import java.util.concurrent.BlockingQueue;

public class TransactionThread extends Thread {

    private BlockingQueue<String> blockingQueue;
    private Connection connection;
    private TransactionPool pool;
    private String uuid;

    public TransactionThread(BlockingQueue<String> blockingQueue, Connection connection, TransactionPool pool, String uuid){
        this.blockingQueue = blockingQueue;
        this.connection = connection;
        this.pool = pool;
        this.uuid = uuid;
        start();
    }

    @Override
    public void run() {
        try {
            String statement;
            connection.setAutoCommit(false);
            while(!"COMMIT TRANSACTION".equals(statement = blockingQueue.take().toUpperCase())){
                try(PreparedStatement stmt = connection.prepareStatement(statement)){
                    if(stmt.execute()){
                        //QUERY
                        try(ResultSet resultSet = stmt.getResultSet()){

                        }
                    }else{
                        //UPDATE
                    }
                }
            }
            connection.commit();
            pool.remove(uuid, connection);
        }catch (SQLException | InterruptedException e){
            e.printStackTrace();
        }
    }
}
