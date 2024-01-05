#include <iostream>
#include "MinIntHeap.h"

int main(){
    MinIntHeap myHeap;
    
    std::cout << "Adding 1, 10, 4 to the heap" << std::endl;
    myHeap.add(1);
    myHeap.add(10);
    myHeap.add(4);

    std::cout << "smallest: " << myHeap.poll() << std::endl;
    std::cout << "second smallest: " << myHeap.poll() << std::endl;

    return 0;
}