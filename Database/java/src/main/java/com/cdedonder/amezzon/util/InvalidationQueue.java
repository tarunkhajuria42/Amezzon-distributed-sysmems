package com.cdedonder.amezzon.util;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.function.Consumer;

public class InvalidationQueue<E> {

    private Queue<E> validQueue, invalidQueue;

    public InvalidationQueue() {
        validQueue = new ArrayDeque<>();
        invalidQueue = new ArrayDeque<>();
    }

    public void add(E e) {
        validQueue.add(e);
    }

    public E get() {
        return validQueue.peek();
    }

    public synchronized void invalidate() {
        invalidQueue.add(validQueue.poll());
    }

    public boolean hasValid() {
        return !validQueue.isEmpty();
    }

    public synchronized void revalidateAll() {
        validQueue.addAll(invalidQueue);
        invalidQueue.clear();
    }

    public void forEach(Consumer<? super E> consumer) {
        validQueue.forEach(consumer);
        invalidQueue.forEach(consumer);
    }
}
