import cppyy

cppyy.cppdef(
    """
#include <iostream>
void helloWorld() {
    std::cout << "Hello world!\\n";
}
    """
)

from cppyy.gbl import helloWorld
helloWorld()