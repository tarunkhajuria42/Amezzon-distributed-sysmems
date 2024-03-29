package com.cdedonder.amezzon.util;

import java.util.concurrent.LinkedTransferQueue;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TransferQueue;

@SuppressWarnings({"UnusedReturnValue", "unused"})
public class BidirectionalTransferQueue<A,B> {

    private final TransferQueue<A> requestQueue;
    private final TransferQueue<B> responseQueue;

    public BidirectionalTransferQueue(){
        responseQueue = new LinkedTransferQueue<>();
        requestQueue = new LinkedTransferQueue<>();
    }

    public boolean offerRequest(A a){
        return requestQueue.offer(a);
    }

    public void offerRequest(A a, long ms) throws InterruptedException{
        requestQueue.offer(a, ms, TimeUnit.MILLISECONDS);
    }

    public A receiveRequest() throws InterruptedException{
        return requestQueue.take();
    }

    public A receiveRequest(long ms) throws InterruptedException{
        return requestQueue.poll(ms, TimeUnit.MILLISECONDS);
    }

    public boolean offerResponse(B b){
        return responseQueue.offer(b);
    }

    public void offerResponse(B b, long ms) throws InterruptedException{
        responseQueue.offer(b, ms, TimeUnit.MILLISECONDS);
    }

    public B receiveResponse() throws InterruptedException{
        return responseQueue.take();
    }

    public B receiveResponse(long ms) throws InterruptedException {
        return responseQueue.poll(ms, TimeUnit.MILLISECONDS);
    }
}
