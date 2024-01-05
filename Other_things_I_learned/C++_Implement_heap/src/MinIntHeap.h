#ifndef MININTHEAP_H
#define MININTHEAP_H

#include <iostream>

class MinIntHeap{
private:
    int capacity{10};
    int size{0};

    int* items = new int[capacity];

    int getLeftChildIndex(int parentIndex);
    int getRightChildIndex(int parentIndex);
    int getParentIndex(int childIndex);

    bool hasLeftChild(int index);
    bool hasRightChild(int index);
    bool hasParent(int index);

    int leftChild(int index);
    int rightChild(int index);
    int parent(int index);

    void swap(int indexOne, int indexTwo);
    void ensureExtraCapacity();

public:
    int peek();
    int poll();
    void add(int item);

    void heapifyUp();
    void heapifyDown();
};

#endif