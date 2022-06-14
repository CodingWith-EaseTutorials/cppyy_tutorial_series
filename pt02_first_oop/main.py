import cppyy

cppyy.cppdef(
    """
class MyClass {
private:
    int myInt;
public:
    MyClass(int myInt) {
        this->myInt = myInt;
    }
    int getMyInt() {
        return myInt;
    }
};
    """
)

from cppyy.gbl import MyClass
my_var = MyClass(13)
print(my_var.getMyInt())
