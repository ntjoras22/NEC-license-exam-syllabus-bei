# Section 3.6: Generic Programming and Exception Handling (ACtE0306)

## 📖 1. Introduction
Generic programming and exception handling form the backbone of robust and reusable C++ software. **Generic programming** allows writing code that works with any data type, minimizing code duplication. **Exception handling** provides a structured way to handle runtime errors gracefully, replacing legacy C-style error codes. Both are heavily tested in the NEC exam.

## 2. Generic Programming with Templates

### 2.1 Basic Concept
Templates allow you to define functions and classes with generic types. Instead of writing multiple overloaded functions for `int`, `float`, `double`, etc., you write one template, and the compiler generates the specific versions as needed based on the types provided during function calls.

> [!NOTE] 
> **Definition**: A template is a blueprint or formula for creating a generic class or a function.

### 2.2 Function Template

#### Syntax
```cpp
template <typename T>  // or template <class T>
return_type function_name(arguments) {
    // function body
}
```

#### Worked Example: Generic Swap Function
```cpp
#include <iostream>
using namespace std;

template <typename T>
void swapValues(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    int i1 = 5, i2 = 10;
    swapValues(i1, i2);
    cout << "Ints: " << i1 << ", " << i2 << endl; // Output: 10, 5

    double d1 = 1.1, d2 = 2.2;
    swapValues(d1, d2);
    cout << "Doubles: " << d1 << ", " << d2 << endl; // Output: 2.2, 1.1

    return 0;
}
```

### 2.3 Overloading Function Template
Function templates can be overloaded either by non-template functions or by other function templates. The compiler follows a resolution priority:
1. Exact match with a non-template function.
2. Exact match with a function template.
3. Ordinary function overloading (with implicit conversions).

```cpp
#include <iostream>
using namespace std;

// Template function
template <typename T>
void display(T x) {
    cout << "Template: " << x << endl;
}

// Non-template (ordinary) function overloading the template
void display(int x) {
    cout << "Non-Template: " << x << endl;
}

int main() {
    display(5.5); // Calls Template
    display(10);  // Calls Non-Template (Exact match takes precedence)
    return 0;
}
```

### 2.4 Class Template
Class templates allow classes to have members of generic types. Common examples are data structures like stacks, queues, or arrays.

#### Syntax
```cpp
template <class T>
class ClassName {
    // class members
};
```

#### Worked Example: Stack Class
```cpp
#include <iostream>
using namespace std;

template <class T>
class Stack {
private:
    T arr[10];
    int top;
public:
    Stack() : top(-1) {}
    void push(T val);
    T pop();
};

// 2.5 Function Definition of Class Template Outside the Class
template <class T>
void Stack<T>::push(T val) {
    if (top == 9) {
        cout << "Stack Full!" << endl;
        return;
    }
    arr[++top] = val;
}

template <class T>
T Stack<T>::pop() {
    if (top == -1) {
        cout << "Stack Empty!" << endl;
        return T(); // return default value
    }
    return arr[top--];
}

int main() {
    Stack<int> intStack; // Instantiating class template
    intStack.push(10);
    intStack.push(20);
    cout << "Popped: " << intStack.pop() << endl; // Output: 20

    Stack<string> strStack;
    strStack.push("Hello");
    cout << "Popped: " << strStack.pop() << endl; // Output: Hello

    return 0;
}
```
> [!IMPORTANT]
> When defining a class template member function outside the class, you must prepend it with `template <class T>` and scope it with `ClassName<T>::`.

---

## 3. Standard Template Library (STL)

The STL is a powerful collection of C++ template classes providing general-purpose classes and functions. It consists of three core components:

### 3.1 Containers
Data structures that store collections of objects.
- **Sequence Containers**: Maintain linear arrangement. E.g., `vector`, `list`, `deque`.
- **Associative Containers**: Non-linear, usually implemented as trees. E.g., `set`, `map`, `multiset`, `multimap`.
- **Derived/Adapter Containers**: Based on sequence containers. E.g., `stack`, `queue`, `priority_queue`.

### 3.2 Algorithms
Functions that operate on containers to perform operations like searching, sorting, counting.
- Examples: `sort()`, `find()`, `reverse()`, `count()`, `accumulate()`.
- Algorithms operate through Iterators, uncoupling them from specific containers.

### 3.3 Iterators
Objects that act like pointers, allowing algorithms to traverse containers.
- **Input Iterator**: Read-only, forward moving.
- **Output Iterator**: Write-only, forward moving.
- **Forward Iterator**: Read/Write, forward moving.
- **Bidirectional Iterator**: Read/Write, forward and backward (e.g., `list`, `set`).
- **Random Access Iterator**: Jump to any element in O(1) time (e.g., `vector`, arrays).

---

## 4. Exception Handling

### 4.1 Basic Concept
Exceptions are runtime anomalies (e.g., division by zero, out of memory). The exception handling mechanism allows a program to detect the error where it occurs and "throw" it to a "handler" safely, avoiding program crashes.

### 4.2 Constructs: try, throw, catch
- **`try`**: A block of code that may generate an exception.
- **`throw`**: A keyword used to signal that an exception has occurred.
- **`catch`**: A block of code that catches the exception and handles it.

```cpp
#include <iostream>
using namespace std;

int main() {
    double numerator = 10, denominator = 0;
    
    try {
        if (denominator == 0)
            throw "Division by zero condition!"; // Throwing a string
        cout << numerator / denominator << endl;
    }
    catch (const char* msg) { // Catching a string
        cerr << "Error: " << msg << endl;
    }
    
    return 0;
}
```

### 4.3 Multiple Catch Blocks and Catch-All Handler
A single `try` block can have multiple `catch` blocks to handle different types of exceptions.
The **Catch-All Handler** `catch(...)` catches any exception that is thrown, regardless of its type. It should always be placed *last*.

```cpp
try {
    // code that might throw int, char, or custom object
}
catch (int x) {
    cout << "Integer exception caught." << endl;
}
catch (double d) {
    cout << "Double exception caught." << endl;
}
catch (...) { // Catch-All
    cout << "An unknown exception occurred." << endl;
}
```

### 4.4 Rethrowing Exceptions
A handler can partially handle an exception and pass it up to a higher-level `try/catch` block. This is done using `throw;` without any arguments inside a catch block.

```cpp
void process() {
    try {
        throw std::runtime_error("Error in process");
    }
    catch (std::exception& e) {
        cout << "Caught locally. Rethrowing..." << endl;
        throw; // Rethrows the exact same exception
    }
}
```

### 4.5 Exception with Arguments (Custom Exception Classes)
You can define classes to represent specific exceptions and carry arguments (data).

```cpp
#include <iostream>
#include <string>
using namespace std;

class MyException {
private:
    int code;
    string msg;
public:
    MyException(int c, string m) : code(c), msg(m) {}
    void printError() {
        cout << "Error Code " << code << ": " << msg << endl;
    }
};

int main() {
    try {
        throw MyException(404, "Not Found");
    }
    catch (MyException e) {
        e.printError(); // Output: Error Code 404: Not Found
    }
    return 0;
}
```

### 4.6 Exception Specifications for Functions
You can restrict which exceptions a function can throw using a **throw list** in the function declaration.
> [!WARNING]
> *Note for Exam:* While exception specifications like `void func() throw(int, char)` are deprecated in modern C++ (C++11 onwards replaced by `noexcept`), they frequently appear in older curricula and NEC exams.

```cpp
// This function promises to throw ONLY int or double.
void divide(int a, int b) throw(int, double) {
    if (b == 0) throw b; // allowed
    // if (b == -1) throw "Error"; // NOT allowed, causes unexpected()
}
```

### 4.7 Handling Uncaught and Unexpected Exceptions

If a program throws an exception that is NOT caught by any `catch` block, it calls the standard function `terminate()`, which by default calls `abort()`.
If a function with an exception specification throws an exception not in its list, it calls `unexpected()`, which by default calls `terminate()`.

You can override these default behaviors using:
- **`set_terminate()`**: Takes a pointer to a custom termination function.
- **`set_unexpected()`**: Takes a pointer to a custom unexpected behavior function.

```cpp
#include <iostream>
#include <exception>
#include <cstdlib>
using namespace std;

void myTerminate() {
    cout << "Uncaught exception! Custom terminate handler called." << endl;
    exit(1);
}

int main() {
    set_terminate(myTerminate); // Override default handler
    
    throw 42; // Not caught anywhere -> calls myTerminate()
    
    return 0;
}
```

---

## 📝 5. Summary of Key Formulas and Concepts
> **Quick Reference**
> - Template definition: `template <class T>`
> - Scope resolution for outside class template functions: `template<class T> return_type ClassName<T>::func() {...}`
> - Catch-all block: `catch(...)` MUST be the last catch block.
> - Rethrow syntax: `throw;` inside a catch block.
> - `set_terminate` handles unhandled exceptions.
> - `set_unexpected` handles exception specification violations.

---

## ✏️ 6. Practice Problems

**Q1: What happens if `catch(...)` is placed before `catch(int)`?**
A: A compile-time error occurs. The catch-all handler must always be the last catch block in a sequence.

**Q2: Can a class template inherit from another class template?**
A: Yes, generic classes can participate in inheritance.

**Q3: What is an Iterator in STL?**
A: An Iterator is a pointer-like object used to iterate through the elements of an STL container, decoupling the algorithms from the underlying container implementations.

**Q4: Explain the difference between `throw;` and `throw e;` inside a `catch(Exception& e)` block.**
A: `throw;` rethrows the current exception perfectly, preserving its exact polymorphic type and state. `throw e;` throws a copy of `e`, which might suffer from object slicing if `e` was actually a derived exception type caught by a base reference.

**Q5: What is the purpose of `set_unexpected()`?**
A: It sets a custom handler function to be executed when a function throws an exception that is not permitted by its exception specification (throw list).
