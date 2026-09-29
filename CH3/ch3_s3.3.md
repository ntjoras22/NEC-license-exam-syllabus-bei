# Section 3.3: C++ Language Constructs with Objects and Classes (ACtE0303)

## 📖 1. Introduction
C++ is a superset of the C programming language that introduces Object-Oriented Programming (OOP) paradigms. While C focuses on procedural programming, C++ allows developers to define custom data types through classes, encapsulating data and behavior. This section details the foundational language constructs that differentiate C++ from C, providing the necessary building blocks for robust software engineering.

## 2. Namespace
### Basic Concept
When building large applications or using multiple third-party libraries, name collisions can occur (e.g., two libraries define a `Node` class). A namespace provides a declarative region that serves as a scope for the identifiers inside it, grouping them logically and preventing conflicts.

### Definition
> A **namespace** is a mechanism for expressing logical grouping and preventing name collisions by encapsulating identifiers in a named scope.

### Physical/Logical Meaning
Think of namespaces like directories in a file system. You can have a file named `report.txt` in the `Sales` directory and another `report.txt` in the `HR` directory. They don't conflict because their full paths (`Sales/report.txt` and `HR/report.txt`) are different.

### Code Example
```cpp
#include <iostream>

// Creating a custom namespace
namespace MathLib {
    const double PI = 3.14159;
    double add(double a, double b) { return a + b; }
}

namespace PhysicsLib {
    const double PI = 3.14; // No conflict with MathLib::PI
}

int main() {
    // Accessing via scope resolution operator ::
    std::cout << "MathLib PI: " << MathLib::PI << std::endl;
    std::cout << "PhysicsLib PI: " << PhysicsLib::PI << std::endl;
    
    // Using directive brings everything from MathLib into current scope
    using namespace MathLib;
    std::cout << "Sum: " << add(5, 3) << std::endl;
    
    return 0;
}
```

## 3. Function Overloading
### Basic Concept
Function overloading allows multiple functions to share the same name, provided they have different parameter lists (different types, different number of parameters, or different order of parameters).

### Resolution Rules
When an overloaded function is called, the C++ compiler performs **Overload Resolution** to determine which function version to execute based on the arguments passed. 
> [!IMPORTANT]
> The return type alone is NOT sufficient for overloading. Two functions cannot have the same name and parameter list but different return types.

### Code Example
```cpp
#include <iostream>
using namespace std;

class Printer {
public:
    // Overload 1: Takes an int
    void print(int i) { cout << "Integer: " << i << endl; }
    
    // Overload 2: Takes a double
    void print(double f) { cout << "Float: " << f << endl; }
    
    // Overload 3: Takes a string
    void print(string s) { cout << "String: " << s << endl; }
};

int main() {
    Printer p;
    p.print(5);      // Resolves to print(int)
    p.print(5.5);    // Resolves to print(double)
    p.print("Hello"); // Resolves to print(string)
    return 0;
}
```

## 4. Inline Functions
### Basic Concept
Every time a function is called, the system incurs overhead (pushing arguments to the stack, jumping to the function address, returning). For very short, frequently called functions, this overhead can be significant. An **inline function** instructs the compiler to substitute the function call with the actual code of the function.

### Syntax
```cpp
inline return_type function_name(parameters) {
    // function body
}
```

### When to Use
- Best for small, frequently called functions (e.g., getters and setters).
- **Disadvantage**: Increases the size of the executable file if overused (code bloat).
- Note: `inline` is merely a request to the compiler; if the function is complex (contains loops, switch statements, or is recursive), the compiler will likely ignore the request and treat it as a normal function.

### Code Example
```cpp
#include <iostream>
using namespace std;

inline int square(int x) {
    return x * x;
}

int main() {
    // The compiler replaces the call with: (5 * 5)
    cout << "Square of 5: " << square(5) << endl; 
    return 0;
}
```

## 5. Default Arguments
### Rules
Functions can have default values for parameters. If the caller does not provide an argument, the default is used.
1. Default arguments must be specified from right to left. Once a parameter has a default argument, all subsequent parameters to its right must also have default arguments.
2. Default arguments should be specified in the function declaration, not necessarily in the definition.

### Comparison: Default Args vs Function Overloading
| Feature | Default Arguments | Function Overloading |
|---------|-------------------|----------------------|
| Definition | Single function with optional parameters | Multiple functions with same name |
| Code Size | Smaller (only one body) | Larger (multiple bodies) |
| Flexibility| Good for appending optional data | Good for entirely different data types |

### Code Example
```cpp
#include <iostream>
using namespace std;

// Correct: Right-most parameters have defaults
int calculateVolume(int length, int width = 1, int height = 1) {
    return length * width * height;
}

int main() {
    cout << calculateVolume(5) << endl;         // 5*1*1 = 5
    cout << calculateVolume(5, 4) << endl;      // 5*4*1 = 20
    cout << calculateVolume(5, 4, 3) << endl;   // 5*4*3 = 60
    return 0;
}
```

## 6. Pass/Return by Reference
### Basic Concept
In C, functions usually use "pass by value" (copying data) or "pass by pointer" (using addresses). C++ introduces **references**, which act as aliases to existing variables. Passing by reference allows a function to modify the original variable without using cumbersome pointer syntax.

### Syntax and Swap Example
```cpp
#include <iostream>
using namespace std;

// Pass by reference using '&'
void swapValues(int &x, int &y) {
    int temp = x;
    x = y;
    y = temp;
}

int main() {
    int a = 10, b = 20;
    swapValues(a, b);
    cout << "a: " << a << ", b: " << b << endl; // Output: a: 20, b: 10
    return 0;
}
```

## 7. Class and Object
### Concept
> A **class** is a user-defined blueprint or prototype from which objects are created. It encapsulates data (attributes) and functions (methods).
> An **object** is an instance of a class, taking up memory space and holding specific values for its attributes.

### Memory Allocation
When a class is defined, no memory is allocated. Memory is only allocated when an object is instantiated. All objects of a class share the same member functions in memory, but each object has its own separate copy of the data members.

### Code Example
```cpp
#include <iostream>
using namespace std;

class Car {
public: // Access specifier
    string brand;
    int year;
    
    void display() {
        cout << brand << " (" << year << ")" << endl;
    }
};

int main() {
    Car car1; // Instantiating an object
    car1.brand = "Toyota";
    car1.year = 2022;
    car1.display();
    return 0;
}
```

## 8. Access Specifiers
Access specifiers control the visibility of class members.

| Specifier | Accessibility within Class | From Derived Class | From Outside Class |
|-----------|--------------------------|-------------------|--------------------|
| `private` | Yes | No | No |
| `protected`| Yes | Yes | No |
| `public` | Yes | Yes | Yes |

> [!NOTE]
> By default, all members of a `class` are `private`. In a `struct`, the default is `public`.

## 9. Defining Member Functions
Member functions can be defined:
1. **Inside the class**: Treated as inline implicitly.
2. **Outside the class**: Requires the scope resolution operator `::`.

```cpp
class Circle {
private:
    double radius;
public:
    void setRadius(double r); // Declaration
    double getArea();         // Declaration
};

// Outside definition
void Circle::setRadius(double r) {
    radius = r;
}

double Circle::getArea() {
    return 3.14159 * radius * radius;
}
```

## 10. Constructors and Destructors
### Constructors
A constructor is a special member function automatically executed when an object is created. Its name matches the class name, and it has no return type.

#### Types of Constructors
1. **Default Constructor**: Takes no arguments.
2. **Parameterized Constructor**: Takes arguments to initialize the object with specific values.
3. **Copy Constructor**: Initializes a new object as a copy of an existing object.

### Destructors
A destructor is automatically called when an object goes out of scope or is explicitly deleted. It cleans up resources (e.g., freeing memory). Name is preceded by `~`.

```cpp
#include <iostream>
using namespace std;

class Point {
private:
    int x, y;
public:
    // 1. Default Constructor
    Point() { 
        x = 0; y = 0; 
        cout << "Default Constructor called" << endl;
    }
    
    // 2. Parameterized Constructor
    Point(int xVal, int yVal) { 
        x = xVal; y = yVal; 
        cout << "Parameterized Constructor called" << endl;
    }
    
    // 3. Copy Constructor (Must pass by reference)
    Point(const Point &p) { 
        x = p.x; y = p.y; 
        cout << "Copy Constructor called" << endl;
    }
    
    // Destructor
    ~Point() {
        cout << "Destructor called for (" << x << "," << y << ")" << endl;
    }
};

int main() {
    Point p1;             // Default
    Point p2(10, 20);     // Parameterized
    Point p3 = p2;        // Copy
    return 0;
}
```

## 11. Dynamic Memory Allocation
C++ provides `new` and `delete` operators for dynamic memory management, replacing C's `malloc` and `free`. `new` automatically calls the constructor, and `delete` automatically calls the destructor.

```cpp
class Box {
public:
    Box() { cout << "Box created\n"; }
    ~Box() { cout << "Box destroyed\n"; }
};

int main() {
    // Single object dynamic allocation
    Box* bptr = new Box();
    delete bptr; // Calls destructor and frees memory
    
    // Array of objects
    Box* boxArray = new Box[3]; // Calls constructor 3 times
    delete[] boxArray; // MUST use delete[] for arrays
    
    return 0;
}
```

## 12. `this` Pointer
Every object has a hidden pointer called `this` which points to the object itself. It is passed as an implicit argument to all non-static member functions.

**Usage:**
- Disambiguating member variables from local parameters with the same name.
- Returning a reference to the calling object (`return *this;`).

```cpp
class Employee {
private:
    int id;
public:
    void setId(int id) {
        this->id = id; // 'this->id' is the member, 'id' is the parameter
    }
    
    Employee& setAndReturn(int id) {
        this->id = id;
        return *this; // Return the current object by reference
    }
};
```

## 13. Static Members
### Static Data Member
A static data member belongs to the class rather than any specific object. There is only one copy of it shared by all instances.
- Must be defined outside the class definition.

### Static Member Function
A static function can be called without an object (using `ClassName::functionName()`).
- It can ONLY access static data members and static member functions.
- It does not have a `this` pointer.

```cpp
#include <iostream>
using namespace std;

class Counter {
private:
    static int count; // Declaration
public:
    Counter() { count++; }
    static int getCount() { return count; }
};

// Definition of static member
int Counter::count = 0; 

int main() {
    cout << "Initial Count: " << Counter::getCount() << endl; // 0
    Counter c1, c2;
    cout << "Final Count: " << Counter::getCount() << endl; // 2
    return 0;
}
```

## 14. Constant Members
### Constant Member Functions
Declared with the `const` keyword at the end of the signature. A `const` function promises NOT to modify any member variables of the object.

### Constant Objects
An object declared as `const` cannot be modified after initialization. A `const` object can ONLY call `const` member functions.

```cpp
class MathModel {
private:
    int val;
public:
    MathModel(int v) : val(v) {}
    
    // Const member function
    int getValue() const { 
        // val = 10; // ERROR: Cannot modify member variables in a const function
        return val; 
    } 
    
    void setValue(int v) { val = v; }
};

int main() {
    const MathModel m(5);
    cout << m.getValue() << endl; // Allowed
    // m.setValue(10); // ERROR: Cannot call non-const function on a const object
    return 0;
}
```

## 15. Friend Function and Friend Classes
### Concept
Data hiding (encapsulation) prevents outside functions from accessing private data. However, C++ allows an exception: the `friend` keyword. 
- A **friend function** is NOT a member of the class but has full access to the class's private and protected members.
- A **friend class** has all its member functions as friend functions of another class.

### When to use
- Operator overloading (when the left operand is not an object of the class).
- Bridging two different classes.

```cpp
#include <iostream>
using namespace std;

class Rectangle; // Forward declaration

class Square {
private:
    int side;
public:
    Square(int s) : side(s) {}
    friend int calculateTotalArea(Square s, Rectangle r); // Friend declaration
};

class Rectangle {
private:
    int length, width;
public:
    Rectangle(int l, int w) : length(l), width(w) {}
    friend int calculateTotalArea(Square s, Rectangle r); // Friend declaration
};

// Friend function definition
// It can access private members of both Square and Rectangle
int calculateTotalArea(Square s, Rectangle r) {
    return (s.side * s.side) + (r.length * r.width);
}

int main() {
    Square sq(4);
    Rectangle rect(5, 6);
    cout << "Total Area: " << calculateTotalArea(sq, rect) << endl; // 16 + 30 = 46
    return 0;
}
```

## 💡 16. Common Mistakes / Exam Tips
1. **Semicolon missing**: Forgetting the semicolon `;` at the end of a class definition is a common compilation error.
2. **Copy Constructor Signature**: The copy constructor MUST take its argument by reference (`ClassA(const ClassA &obj)`). If it takes by value (`ClassA(ClassA obj)`), the pass-by-value mechanism will attempt to call the copy constructor, leading to infinite recursion.
3. **Static Member Initialization**: Static data members must be defined outside the class. Initializing them inside the class declaration will cause an error (unless they are `const static` integral types).
4. **Delete vs Delete[]**: Always use `delete[]` when freeing memory allocated with `new[]`. Using `delete` on an array leads to undefined behavior.

## ✏️ 17. Practice Problems
1. Write a C++ program defining a `Bank` class with static member `totalBalance`. Demonstrate the use of static member functions.
2. Differentiate between pass-by-value, pass-by-reference, and pass-by-pointer with clear code examples.
3. Explain the necessity of the `this` pointer in method chaining (e.g., `obj.setX(10).setY(20);`).
