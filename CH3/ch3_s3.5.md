# Section 3.5: Pure Virtual Function and File Handling (ACtE0305)

## 📖 1. Introduction
This section explores two fundamental concepts in C++: **Runtime Polymorphism** through virtual functions and **Persistent Storage** through file handling. These topics are crucial for the NEC License Exam as they test both advanced object-oriented design and practical data management skills.

## 2. Virtual Function and Dynamic Binding

### 2.1 Basic Concept
A **virtual function** is a member function declared in a base class and redefined (overridden) by a derived class. It enables **dynamic binding** (runtime polymorphism), meaning the function call is resolved at runtime based on the actual object type pointed to by a base class pointer, rather than the pointer's static type.

> [!NOTE] 
> **Definition**: A virtual function is declared using the `virtual` keyword in the base class. It tells the compiler to perform **late binding** on this function.

### 2.2 Physical/Logical Meaning
Imagine a universal remote (base class pointer) that can control different devices like a TV or a DVD Player (derived classes). Pressing the "Power" button (virtual function) turns on the specific device the remote is currently pointing at, not a generic device.

### 2.3 Early Binding vs. Late Binding

| Feature | Early Binding (Static Binding) | Late Binding (Dynamic Binding) |
| :--- | :--- | :--- |
| **Resolution Time** | Compile time | Run time |
| **Mechanism** | Function overloading, operator overloading | Virtual functions |
| **Speed** | Faster execution | Slightly slower due to vtable lookup |
| **Flexibility** | Less flexible | Highly flexible for extending code |

### 2.4 Syntax and Example
To create a virtual function, prepend the `virtual` keyword to the function declaration in the base class.

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() {
        cout << "Base class show function" << endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived class show function" << endl;
    }
};

int main() {
    Base* bptr;       // Base class pointer
    Derived d;        // Derived class object
    bptr = &d;        // Pointer to derived object
    
    // Virtual function, bound at runtime (Late binding)
    bptr->show();     // Output: Derived class show function
    
    return 0;
}
```

### 2.5 The Virtual Table (VTable) Concept
When a class contains a virtual function, the compiler automatically creates a hidden table called the **VTable** containing function pointers to the virtual functions for that class. Every object of that class gets a hidden pointer (often called `vptr`) pointing to the VTable. This mechanism introduces a slight overhead in memory (for the `vptr`) and execution time (dereferencing the pointer).

---

## 3. Pure Virtual Function and Abstract Classes

### 3.1 Basic Concept
A **pure virtual function** is a virtual function that has no implementation in the base class. It forces any derived class to provide its own implementation. A class with at least one pure virtual function is an **Abstract Class**.

> [!IMPORTANT]
> **Definition**: An abstract class is a class designed only to act as a base class. You **cannot instantiate** objects of an abstract class.

### 3.2 Syntax
```cpp
virtual void functionName() = 0; // The "= 0" makes it purely virtual
```

### 3.3 Worked Example
```cpp
#include <iostream>
using namespace std;

// Abstract Base Class
class Shape {
public:
    // Pure virtual function
    virtual void draw() = 0; 
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Circle" << endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a Rectangle" << endl;
    }
};

int main() {
    // Shape s; // ERROR: Cannot instantiate abstract class
    
    Shape* shapePtr;
    Circle c;
    Rectangle r;
    
    shapePtr = &c;
    shapePtr->draw(); // Output: Drawing a Circle
    
    shapePtr = &r;
    shapePtr->draw(); // Output: Drawing a Rectangle
    
    return 0;
}
```

> [!TIP]
> **Exam Tip**: If a derived class fails to override the pure virtual function, the derived class also becomes an abstract class and cannot be instantiated.

---

## 4. Stream Class Hierarchy for Console Input/Output

C++ handles I/O through a hierarchy of classes, typically found in `<iostream>`.

```text
                           ios (Virtual Base Class)
                             |
         -----------------------------------------
         |                                       |
      istream                                 ostream
     (Input Stream)                        (Output Stream)
         |                                       |
         -----------------------------------------
                             |
                          iostream
                    (Input/Output Stream)
```

1. **`ios`**: The base class for all stream classes. Contains formatting flags, error states, and basic operations.
2. **`istream`**: Handles input operations (e.g., `cin`). Contains `get()`, `getline()`, `read()`.
3. **`ostream`**: Handles output operations (e.g., `cout`). Contains `put()`, `write()`.
4. **`iostream`**: Inherits from both `istream` and `ostream`. Handles both input and output operations.

---

## 5. Unformatted Input/Output

Unformatted I/O functions process data character-by-character or as a raw byte stream without data interpretation (like formatting integers or floats).

### 5.1 Common Functions

| Function | Stream | Description |
| :--- | :--- | :--- |
| `get()` | `istream` | Reads a single character (including spaces) from input stream. |
| `put(char)` | `ostream` | Writes a single character to output stream. |
| `getline(buffer, size)`| `istream` | Reads a whole line of text until a newline or size limit. |
| `read(buffer, size)` | `istream` | Reads binary data into a buffer. |
| `write(buffer, size)` | `ostream` | Writes binary data from a buffer. |

### 5.2 Example
```cpp
#include <iostream>
using namespace std;

int main() {
    char ch;
    cout << "Enter a character: ";
    cin.get(ch);
    cout << "You entered: ";
    cout.put(ch);
    cout << endl;
    
    char name[50];
    // Need to clear newline from previous input if chaining
    cin.ignore();
    cout << "Enter your full name: ";
    cin.getline(name, 50);
    cout << "Name is: " << name << endl;
    
    return 0;
}
```

---

## 6. Formatted Input/Output and Manipulators

C++ provides ways to format I/O using `ios` member functions or manipulators (functions that can be used directly with the insertion `<<` and extraction `>>` operators).

### 6.1 `ios` Member Functions

- **`width(int)`**: Specifies minimum field width. (Applies only to the *next* output).
- **`precision(int)`**: Specifies number of digits after the decimal point.
- **`fill(char)`**: Specifies the padding character.
- **`setf()`**: Sets formatting flags.
- **`unsetf()`**: Unsets formatting flags.

### 6.2 Manipulators (`<iomanip>`)

| Manipulator | Description | Equivalent `ios` function |
| :--- | :--- | :--- |
| `setw(int)` | Sets field width | `width(n)` |
| `setprecision(int)` | Sets floating-point precision | `precision(n)` |
| `setfill(char)` | Sets fill character | `fill(c)` |
| `endl` | Inserts newline and flushes stream | `\n` + flush |
| `hex`, `oct`, `dec` | Sets base for integers | `setf(ios::hex)`, etc. |
| `fixed`, `scientific` | Floating point format | `setf(ios::fixed)`, etc. |
| `left`, `right` | Justification | `setf(ios::left)`, etc. |

### 6.3 Example
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.14159265;
    int num = 255;
    
    // Using manipulators
    cout << "Hexadecimal of 255: " << hex << num << endl;
    cout << "Decimal of 255: " << dec << num << endl;
    
    cout << "Pi to 3 decimal places: " << fixed << setprecision(3) << pi << endl;
    
    cout << "Formatted output:" << endl;
    cout << setfill('*') << setw(10) << "C++" << endl; // Output: *******C++
    
    return 0;
}
```

---

## 7. File Handling in C++

File handling requires the `<fstream>` library, which includes three main classes:
1. **`ifstream`**: Input file stream (read from a file).
2. **`ofstream`**: Output file stream (write to a file).
3. **`fstream`**: File stream (both read and write).

### 7.1 Opening and Closing a File
Files can be opened using constructors or the `open()` function.

```cpp
// Using constructor
ofstream outFile("data.txt");

// Using open() function
ifstream inFile;
inFile.open("data.txt");

// Closing a file
outFile.close();
inFile.close();
```

### 7.2 File Modes
File modes dictate how a file should be accessed. Multiple modes can be combined using the bitwise OR `|` operator.

| Mode Flag | Meaning |
| :--- | :--- |
| `ios::in` | Open for reading (default for `ifstream`) |
| `ios::out` | Open for writing (default for `ofstream`) |
| `ios::app` | Append mode (write at the end of the file) |
| `ios::ate` | Open file and move control to the end immediately |
| `ios::trunc` | Truncate the file (destroy contents) if it exists |
| `ios::binary` | Open file in binary mode |

**Example:**
```cpp
fstream file("data.bin", ios::out | ios::binary | ios::app);
```

### 7.3 I/O Operations on Files
You can use `<<` and `>>` for text files, and `read()` and `write()` for binary files.

#### Text File Example:
```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    // Writing to a file
    ofstream fout("sample.txt");
    if(!fout) {
        cerr << "Error opening file for writing." << endl;
        return 1;
    }
    fout << "Hello, File Handling in C++" << endl;
    fout.close();
    
    // Reading from a file
    ifstream fin("sample.txt");
    string line;
    if(fin.is_open()) {
        while(getline(fin, line)) {
            cout << "Read: " << line << endl;
        }
        fin.close();
    }
    return 0;
}
```

#### Binary File Example (Objects):
```cpp
#include <fstream>
#include <iostream>
using namespace std;

class Student {
    int id;
    char name[30];
public:
    void getData() {
        cout << "Enter ID and Name: ";
        cin >> id >> name;
    }
    void showData() const {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

int main() {
    Student s;
    s.getData();
    
    // Write object
    ofstream outFile("student.dat", ios::binary);
    outFile.write(reinterpret_cast<char*>(&s), sizeof(s));
    outFile.close();
    
    // Read object
    Student sRead;
    ifstream inFile("student.dat", ios::binary);
    inFile.read(reinterpret_cast<char*>(&sRead), sizeof(sRead));
    sRead.showData();
    inFile.close();
    
    return 0;
}
```

### 7.4 Error Handling During I/O Operations

The `ios` class provides several state flag functions to check for errors during file operations:

| Function | Returns true if... |
| :--- | :--- |
| `eof()` | End-Of-File has been reached. |
| `fail()` | A formatting error occurred (e.g., trying to read a char into an int), but stream is unbroken. |
| `bad()` | A critical stream error occurred (e.g., physical failure). |
| `good()` | No error flags are set (stream is perfectly fine). |
| `clear()` | Clears all error flags (resets the stream state). |

> [!WARNING] 
> **Common Mistake**: Looping with `while(!fin.eof())` often leads to processing the last read twice if the read fails just at the EOF. The correct idiom is `while(fin >> data)` or checking `fin.fail()` right after reading.

---

## 📝 8. Summary of Key Formulas and Concepts
> **Quick Reference**
> - Late Binding = `virtual` function + Base class pointer pointing to derived object.
> - Pure Virtual = `virtual return_type func() = 0;` => Abstract Class.
> - Formatted output priority: `setw` is transient (only next variable), while `setprecision` and `setfill` are persistent until changed.
> - Binary Read/Write requires `reinterpret_cast<char*>(&obj)` to treat objects as byte arrays.

---

## ✏️ 9. Practice Problems

**Q1: What happens if an abstract class is instantiated?**
A: A compile-time error occurs. Abstract classes cannot be instantiated because they have incomplete implementations (pure virtual functions).

**Q2: Differentiate between `ios::app` and `ios::ate`.**
A: Both move the file pointer to the end. However, `ios::app` forces all writes to occur at the end of the file (you cannot seek backwards to overwrite). `ios::ate` just starts at the end, but allows you to seek back and write anywhere.

**Q3: Write a snippet to check if opening a file was successful.**
```cpp
ifstream fin("data.txt");
if(fin.fail()) { // or if(!fin) or if(!fin.is_open())
    cout << "File failed to open!" << endl;
}
```

**Q4: Which function clears the error state flags of a stream?**
A: `stream_object.clear();` resets all flags (like failbit or eofbit) so the stream can be used again.

**Q5: Are constructors inherited? Can constructors be virtual?**
A: Constructors are not inherited and cannot be virtual. However, destructors CAN and SHOULD be virtual if a class is designed to be a base class, to ensure derived class destructors are called when deleted via a base class pointer.
