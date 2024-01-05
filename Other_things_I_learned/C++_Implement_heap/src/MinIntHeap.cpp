#include "MinIntHeap.h"

int MinIntHeap::getLeftChildIndex(int parentIndex){return 2*parentIndex + 1;}
int MinIntHeap::getRightChildIndex(int parentIndex){return 2*parentIndex + 2;}
int MinIntHeap::getParentIndex(int childIndex){return (childIndex - 1)/2;}

bool MinIntHeap::hasLeftChild(int index){return getLeftChildIndex(index) < size;}
bool MinIntHeap::hasRightChild(int index){return getRightChildIndex(index) < size;}
bool MinIntHeap::hasParent(int index){return getParentIndex(index) >= 0;}

int MinIntHeap::leftChild(int index){return items[getLeftChildIndex(index)];}
int MinIntHeap::rightChild(int index){return items[getRightChildIndex(index)];}
int MinIntHeap::parent(int index){return items[getParentIndex(index)];}

void MinIntHeap::swap(int indexOne, int indexTwo){
    int temp = items[indexOne];
    items[indexOne] = items[indexTwo];
    items[indexTwo] = temp;
}

void MinIntHeap::ensureExtraCapacity(){
    if(size == capacity){
        int* newItems = new int[capacity * 2];
        std::copy(items, items + capacity, newItems);
        delete[] items;
        items = newItems;
        capacity *= 2;
    }
}

int MinIntHeap::peek(){
    if(size == 0) throw std::logic_error("Illegal State");
    return items[0];
}

int MinIntHeap::poll(){
    if(size == 0) throw std::logic_error("Illegal State");
    int item = items[0];
    items[0] = items[size - 1];
    size--;
    heapifyDown();
    return item;
}

void MinIntHeap::add(int item){
    ensureExtraCapacity();
    items[size] = item;
    size++;
    heapifyUp();
}

void MinIntHeap::heapifyUp(){
    int index = size - 1;
    while (hasParent(index) && parent(index) > items[index]){
        swap(getParentIndex(index), index);
        index = getParentIndex(index);
    }
}

void MinIntHeap::heapifyDown(){
    int index = 0;
    while(hasLeftChild(index)){
        int smallerChildIndex = getLeftChildIndex(index);
        if(hasRightChild(index) && rightChild(index) < leftChild(index)){
            smallerChildIndex = getRightChildIndex(index);
        }

        if(items[index] < items[smallerChildIndex]){
            break;
        }else{
            swap(index, smallerChildIndex);
        }
        index = smallerChildIndex;
    }
}