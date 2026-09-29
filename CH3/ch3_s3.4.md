# Section 3.4: Features of Object-Oriented Programming (ACtE0304)

## 📖 1. Introduction
This section dives into the advanced and powerful features of C++ Object-Oriented Programming. We explore how to extend operators to work with custom objects, how to convert between data types natively, and how to create hierarchical class relationships through inheritance. These features allow for highly expressive, reusable, and maintainable code.

## 2. Operator Overloading
### Basic Concept
Operator overloading allows C++ operators (like `+`, `-`, `++`, `<<`) to have user-defined meanings when applied to user-defined data types (classes). This provides an intuitive interface for interacting with objects.

### Physical/Logical Meaning
If you have two `String` objects, `s1` and `s2`, it is much more intuitive to concatenate them with `s1 + s2` rather than `s1.concat(s2)`. Operator overloading makes this possible.

### Definition
> **Operator Overloading** is a compile-time polymorphism where an operator is overloaded to provide a special meaning to a user-defined data type.

### Syntax
```cpp
ReturnType operator OP (ArgumentList);
```
Where `OP` is the operator being overloaded.

### Unary Operator Overloading
Unary operators operate on a single operand. Examples include `++`, `--`, and unary `-`.
When overloading postfix increment/decrement, a dummy `int` parameter is used to distinguish it from prefix.

```cpp
#include <iostream>
using namespace std;

class Counter {
private:
    int count;
public:
    Counter() : count(0) {}
    
    // Prefix ++: Increments value and returns the updated object
    Counter operator++() {
        ++count;
        return *this;
    }
    
    // Postfix ++: Returns original object, then increments
    Counter operator++(int) {
        Counter temp = *this;
        count++;
        return temp;
    }
    
    void display() const { cout << "Count: " << count << endl; }
};

int main() {
    Counter c1;
    ++c1;
    c1.display(); // Count: 1
    c1++;
    c1.display(); // Count: 2
    return 0;
}
```

### Binary Operator Overloading
Binary operators operate on two operands. If overloaded as a member function, the left operand is the calling object (`this`), and the right operand is passed as an argument.

```cpp
class Complex {
private:
    float real, imag;
public:
    Complex(float r = 0, float i = 0) : real(r), imag(i) {}
    
    // Overloading + operator
    Complex operator+(const Complex& obj) {
        Complex res;
        res.real = real + obj.real;
        res.imag = imag + obj.imag;
        return res;
    }
    
    void display() const { cout << real << " + i" << imag << endl; }
};

int main() {
    Complex c1(3.5, 2.5), c2(1.5, 4.5);
    // Compiles to: c1.operator+(c2)
    Complex c3 = c1 + c2; 
    c3.display(); // 5 + i7
    return 0;
}
```

### Member vs Friend Functions in Overloading
> [!IMPORTANT]
> If the left operand of the operator is NOT an object of the class (e.g., when overloading `<<` for `ostream`), you MUST use a non-member friend function.

```cpp
class Distance {
private:
    int feet, inches;
public:
    Distance(int f = 0, int i = 0) : feet(f), inches(i) {}
    
    // Overloading << (must be friend because left operand is ostream)
    friend ostream& operator<<(ostream& os, const Distance& d);
};

ostream& operator<<(ostream& os, const Distance& d) {
    os << d.feet << " feet, " << d.inches << " inches";
    return os; // Return stream to allow chaining: cout << d1 << d2;
}
```

## 3. Data Conversion
C++ supports implicit and explicit conversions between basic types and class types.

### Basic to Class Conversion
Achieved using a parameterized constructor that takes a basic data type.
```cpp
class Time {
    int minutes;
public:
    Time(int m) { minutes = m; } // Int to Time
};
// Usage: Time t = 120; // Automatically converts 120 to Time object
```

### Class to Basic Conversion
Achieved using an overloaded casting operator. It has no return type specification.
```cpp
class Time {
    int minutes;
public:
    Time(int m) : minutes(m) {}
    // Class to Int conversion operator
    operator int() const { return minutes; } 
};
// Usage: Time t(120); int m = t; // m becomes 120
```

### Class to Class Conversion
Achieved using a 1-argument constructor in the target class or a conversion operator in the source class.

## 4. Inheritance
### Concept
Inheritance is the process by which a new class (derived class/child class) is created from an existing class (base class/parent class). It models an "IS-A" relationship and promotes code reuse.

### Access Control in Inheritance
| Base Class Member Specifier | Inherited as `public` | Inherited as `protected` | Inherited as `private` |
|---|---|---|---|
| `public` | `public` | `protected` | `private` |
| `protected` | `protected` | `protected` | `private` |
| `private` | Not Accessible | Not Accessible | Not Accessible |

### Types of Inheritance
#### Single Inheritance
One base class, one derived class.
```cpp
class Animal { // Base
public:
    void eat() { cout << "Eating..." << endl; }
};

class Dog : public Animal { // Derived
public:
    void bark() { cout << "Barking..." << endl; }
};
// Dog can both eat() and bark()
```

#### Multiple Inheritance
One derived class inherits from multiple base classes.
```cpp
class Printer {
public: void print() { cout << "Printing\n"; }
};
class Scanner {
public: void scan() { cout << "Scanning\n"; }
};

class Copier : public Printer, public Scanner {};
// Copier can both print() and scan()
```

#### Multilevel Inheritance
A class is derived from another derived class (A -> B -> C).
```cpp
class Grandparent {};
class Parent : public Grandparent {};
class Child : public Parent {};
```

#### Hybrid Inheritance
A combination of two or more types of inheritance.

#### Multipath Inheritance & The Diamond Problem
When a class inherits from two classes that have a common base class, the base class members are inherited twice, leading to ambiguity. This is known as the **Diamond Problem**.

```text
      A
     / \
    B   C
     \ /
      D
```
If `A` has `int data;`, `D` inherits two copies of `data` (one via `B`, one via `C`).

**Solution: Virtual Base Class**
By declaring the intermediate classes (`B` and `C`) as `virtual` derivatives of `A`, only one copy of `A` is shared among them.

```cpp
class A {
public:
    int data;
};

// Virtual inheritance solves diamond problem
class B : virtual public A {}; 
class C : virtual public A {};

class D : public B, public C {};

int main() {
    D obj;
    obj.data = 10; // NO AMBIGUITY: Only one copy of 'data' exists
    return 0;
}
```

## 5. Constructor/Destructor in Inheritance
### Order of Execution
- **Constructors**: Executed from Base to Derived (Top to Bottom).
- **Destructors**: Executed in reverse order, from Derived to Base (Bottom to Top).

### Passing Parameters to Base Class Constructor
When a base class does not have a default constructor, the derived class MUST explicitly call the base class constructor in its initialization list.

```cpp
#include <iostream>
using namespace std;

class Base {
protected:
    int baseVal;
public:
    Base(int v) : baseVal(v) { 
        cout << "Base Constructor called with " << v << "\n"; 
    }
    ~Base() { cout << "Base Destructor\n"; }
};

class Derived : public Base {
private:
    int derVal;
public:
    // Passing argument to base class constructor using initializer list
    Derived(int v1, int v2) : Base(v1), derVal(v2) {
        cout << "Derived Constructor called with " << v2 << "\n";
    }
    ~Derived() { cout << "Derived Destructor\n"; }
};

int main() {
    Derived d(10, 20);
    return 0;
}
/* OUTPUT:
Base Constructor called with 10
Derived Constructor called with 20
Derived Destructor
Base Destructor
*/
```

## 💡 6. Common Mistakes / Exam Tips
- **Virtual Base Class**: Essential concept for the NEC exam. Understand that `virtual public` prevents multiple copies of a base class from being inherited.
- **Constructor Execution Order**: Always Base first, then Derived. Destructors are the exact reverse. Think of it like building a house: foundation (Base) first, then roof (Derived). Tearing it down: roof first, then foundation.
- **Operator Overloading Constraints**: You cannot overload these operators:
  - Scope resolution `::`
  - Member selection `.`
  - Member pointer selection `.*`
  - Ternary conditional `?:`
  - `sizeof`

## ✏️ 7. Practice Problems
1. Write a complete C++ program to overload the `+` operator to concatenate two custom `String` objects.
2. Demonstrate multiple inheritance where a `TeachingAssistant` inherits from both `Student` and `Teacher`. Resolve any potential ambiguity.
3. Write a program showing data conversion from a class `Polar` (radius, angle) to a class `Rectangle` (x, y).
