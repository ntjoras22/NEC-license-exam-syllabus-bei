# Section 3.1: Introduction to C Programming (ACtE0301)

## 📖 1. Introduction
C is a general-purpose, procedural, imperative computer programming language developed in 1972 by Dennis M. Ritchie at the Bell Telephone Laboratories to develop the UNIX operating system. It is one of the most widely used programming languages and forms the foundation for many modern languages like C++, Java, and Python. For engineering students, C is crucial because it provides low-level memory access, a simple set of keywords, and a clean style, making it ideal for system programming and embedded systems.

## 💡 2. Basic Concept
At its core, a C program is a collection of functions and variables. A function contains statements that specify the computing operations to be done, and variables store values used during the computation. The execution of a C program always begins with a special function named `main`.

## ✏️ 3. Definition
> **C Programming Language:** A high-level, compiled, structured programming language that supports procedural programming and provides facilities for low-level memory manipulation.

## 4. Physical/Logical Meaning
Think of a C program as a highly organized factory. The `main` function is the factory manager. The variables are the storage boxes, the operators are the machines processing the materials, and the control statements are the conveyer belts routing the materials to different processing units based on conditions. Functions are specialized workshops that the manager can call upon to perform specific tasks.

## 5. Detailed Explanation

### 5.1 C Tokens
A C program consists of various tokens, which are the smallest individual units in a program.
*   **Keywords:** Reserved words with special meaning to the compiler (e.g., `int`, `return`, `if`, `while`). There are 32 standard keywords in C.
*   **Identifiers:** Names given to variables, functions, arrays, etc. (e.g., `count`, `calculateSum`). They must begin with a letter or underscore.
*   **Constants:** Fixed values that do not change during execution (e.g., `10`, `'A'`, `3.14`).
*   **Strings:** Sequence of characters enclosed in double quotes (e.g., `"Hello, World!"`).
*   **Operators:** Symbols that trigger an action when applied to C variables and other objects (e.g., `+`, `-`, `*`).
*   **Special Symbols:** Symbols like brackets `[]`, braces `{}`, parentheses `()`, and comma `,` having special meanings.

### 5.2 Operators
Operators are used to perform operations on variables and values.
*   **Arithmetic:** `+`, `-`, `*`, `/`, `%` (modulo)
*   **Relational:** `==`, `!=`, `>`, `<`, `>=`, `<=`
*   **Logical:** `&&` (AND), `||` (OR), `!` (NOT)
*   **Bitwise:** `&`, `|`, `^` (XOR), `~` (Complement), `<<` (Left shift), `>>` (Right shift)
*   **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`
*   **Conditional (Ternary):** `condition ? expression1 : expression2`
*   **Other:** `sizeof()` (returns size of data type), `,` (comma operator)

**Operator Precedence:**
Determines the grouping of terms in an expression and decides how an expression is evaluated.
Highest to lowest:
1. `()`, `[]`, `->`, `.`
2. Unary operators (`++`, `--`, `!`, `~`, `sizeof`)
3. `*`, `/`, `%`
4. `+`, `-`
5. Bitwise shifts (`<<`, `>>`)
6. Relational (`<`, `<=`, `>`, `>=`)
7. Equality (`==`, `!=`)
8. Bitwise AND, XOR, OR (`&`, `^`, `|`)
9. Logical AND, OR (`&&`, `||`)
10. Conditional (`?:`)
11. Assignment (`=`, `+=`, etc.)

### 5.3 Formatted and Unformatted I/O
**Formatted I/O:** Uses format specifiers to read/write data in a specific format.
*   `printf("format string", arg_list);` - Output
*   `scanf("format string", &arg_list);` - Input
*   Format Specifiers: `%d` (integer), `%f` (float), `%c` (character), `%s` (string).

**Unformatted I/O:** Deals with character and string input/output directly.
*   `getchar()` / `putchar()`: Reads/writes a single character.
*   `gets()` / `puts()`: Reads/writes a string. Note: `gets()` is dangerous and deprecated in newer C standards due to buffer overflow risks.
*   `getch()` / `getche()`: Console input functions (non-standard, defined in `<conio.h>`). `getch()` doesn't echo the character, `getche()` does.

### 5.4 Control Statements
Control flow determines the order in which statements are executed.
*   **if:** Executes a block of code if a condition is true.
*   **if-else:** Executes one block if true, another if false.
*   **nested if-else:** `if` statements inside other `if` statements.
*   **switch-case:** Tests a variable against a list of values (cases). Must use `break` to exit.
*   **goto:** Unconditional jump to a labeled statement (avoid using it as it creates "spaghetti code").

### 5.5 Looping
Loops execute a block of code repeatedly.
*   **for:** `for(initialization; condition; increment/decrement)`
*   **while:** `while(condition)` - entry-controlled loop.
*   **do-while:** `do { ... } while(condition);` - exit-controlled loop (guaranteed to execute at least once).
*   **break:** Exits the loop entirely.
*   **continue:** Skips the rest of the current iteration and proceeds to the next iteration.

### 5.6 User-Defined Functions
Functions modularize code.
*   **Declaration (Prototype):** Tells compiler about function name, return type, and parameters. `int add(int a, int b);`
*   **Definition:** Contains the actual body of the function.
*   **Calling:** Invoking the function to execute it. `sum = add(5, 10);`
*   **Pass by Value:** A copy of the actual argument is passed. Changes inside the function do not affect the original variable. (C only supports pass-by-value natively; pass-by-reference is simulated using pointers).

### 5.7 Recursive Functions
A function that calls itself is a recursive function.
*   **Concept:** Breaks a problem down into smaller sub-problems.
*   **Base Case:** A condition to stop the recursion. Without it, the program will crash (stack overflow).

### 5.8 Arrays
An array is a collection of variables of the same type stored in contiguous memory locations.
*   **1-D Array:** `int arr[5] = {1, 2, 3, 4, 5};` Access elements via index (0 to N-1).
*   **2-D Array:** Matrix representation. `int matrix[3][3];`
*   **Multi-dimensional Array:** Arrays of arrays. `int cube[3][3][3];`

### 5.9 String Manipulations
In C, a string is a 1-D array of characters terminated by a null character `\0`.
Standard library functions (in `<string.h>`):
*   `strlen(s)`: Returns the length of string `s` (excluding `\0`).
*   `strcpy(d, s)`: Copies string `s` into `d`.
*   `strcmp(s1, s2)`: Compares `s1` and `s2` lexicographically (0 if equal, <0 if s1<s2, >0 if s1>s2).
*   `strcat(d, s)`: Concatenates `s` to the end of `d`.
*   `strrev(s)`: Reverses string `s` (non-standard in some compilers).

## 6. ASCII Diagrams

**Control Flow Diagram (if-else)**
```text
       [Condition]
         |     \
    True |      \ False
         v       v
   [Block 1]  [Block 2]
         |       |
          \     /
           v   v
       [Next Statement]
```

**Memory Representation of 1D Array `int arr[3] = {10, 20, 30};`**
```text
Index:      0       1       2
Value:    |  10  |  20  |  30  |
Address:  1000    1004    1008    (Assuming 4 bytes per int)
```

## ⚖️ 7. Comparison Tables

| Feature | `while` Loop | `do-while` Loop |
| :--- | :--- | :--- |
| **Type** | Entry-controlled loop | Exit-controlled loop |
| **Execution** | Condition checked before execution | Condition checked after execution |
| **Guarantee** | May not execute at all if condition is initially false | Guaranteed to execute at least once |
| **Syntax ending** | `while (cond) { ... }` | `do { ... } while (cond);` (Ends with semicolon) |

| Feature | `break` | `continue` |
| :--- | :--- | :--- |
| **Action** | Exits the nearest enclosing loop or switch | Skips current iteration, goes to next iteration |
| **Applicability** | Loops and `switch` statements | Only in loops |

## 🔍 8. Worked Examples

### Example 1: Recursive Function (Factorial)
```c
#include <stdio.h>

// Function prototype
int factorial(int n);

int main() {
    int num = 5;
    printf("Factorial of %d is %d\n", num, factorial(num));
    return 0;
}

// Function definition
int factorial(int n) {
    if (n == 0 || n == 1) // Base case
        return 1;
    else
        return n * factorial(n - 1); // Recursive call
}
```

### Example 2: Matrix Multiplication (2D Array)
```c
#include <stdio.h>

int main() {
    int r1 = 2, c1 = 2, r2 = 2, c2 = 2;
    int a[2][2] = {{1, 2}, {3, 4}};
    int b[2][2] = {{5, 6}, {7, 8}};
    int result[2][2] = {0};

    // Multiplication logic
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            for (int k = 0; k < c1; ++k) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Display
    printf("Resultant Matrix:\n");
    for (int i = 0; i < r1; ++i) {
        for (int j = 0; j < c2; ++j) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

## 📝 9. Key Formulas Summary

> [!NOTE]
> **Important Mathematical Formulas in C:**
> *   **Number of elements in an array:** `sizeof(arr) / sizeof(arr[0])`
> *   **Memory size of 1D Array:** `Number of elements * sizeof(data_type)`
> *   **Ternary Operator:** `Result = (Condition) ? Expression_if_True : Expression_if_False;`

## 💡 10. Common Mistakes / Exam Tips

> [!WARNING]
> *   **Confusing `=` and `==`:** Using `=` (assignment) inside an `if` condition instead of `==` (equality) is a classic mistake. `if(a = 5)` evaluates to true (5 is non-zero) and assigns 5 to `a`.
> *   **Forgetting `break` in `switch`:** Leads to "fall-through" where subsequent case blocks execute unexpectedly.
> *   **Array Index Out of Bounds:** C does not check bounds. Accessing `arr[5]` in `int arr[5]` leads to undefined behavior.
> *   **Uninitialized Variables:** Local variables contain garbage values by default. Always initialize them.

> [!TIP]
> *   **Exam Strategy:** When writing code snippets in the exam, always include header files `#include <stdio.h>` and `int main()`.
> *   Remember that `gets()` is highly discouraged in real-world programming, but you must know what it does for the exam.

## ✏️ 11. Practice Problems

1.  **Question:** Write a C program to find the Greatest Common Divisor (GCD) of two numbers using recursion.
    *Answer Sketch:* Use Euclidean algorithm: `gcd(a, b)` is `b == 0 ? a : gcd(b, a % b)`.
2.  **Question:** What will be the output of `printf("%d", (a > b) ? a : b);` if `a=10` and `b=20`?
    *Answer:* `20`.
3.  **Question:** Explain the difference between `getchar()` and `getche()`.
    *Answer:* `getchar()` buffers input (waits for Enter key) and is part of `<stdio.h>`. `getche()` reads immediately and echoes the character, part of `<conio.h>`.
