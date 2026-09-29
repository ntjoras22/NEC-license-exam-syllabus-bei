# Section 3.2: Pointers, Structure and Data Files in C Programming (ACtE0302)

## 📖 1. Introduction
While basic variables and arrays allow for simple data storage, pointers, structures, and files unlock the true power of C programming. Pointers provide direct memory access, enabling dynamic memory management and efficient array handling. Structures allow for grouping dissimilar data types, crucial for representing complex real-world entities. File I/O ensures data persistence, allowing programs to save and load data across executions.

## 💡 2. Basic Concept
*   **Pointers:** Variables that store memory addresses of other variables.
*   **Structures:** User-defined data types that bundle multiple variables of different types under a single name.
*   **Files:** Streams of bytes stored on a secondary storage device (like a hard drive).

## ✏️ 3. Definition
> **Pointer:** A variable whose value is the memory address of another variable.
> **Structure:** A composite data type declaration that defines a physically grouped list of variables under one name in a block of memory.

## 4. Physical/Logical Meaning
*   **Pointer:** Think of a pointer as a house address. If a variable is the house (storing people/data), the pointer is the piece of paper with the address written on it.
*   **Structure:** Think of a structure as a student ID card. It contains different types of data (Name: String, Roll No: Integer, Blood Group: Character) all grouped together for one entity.
*   **File:** A notebook where you permanently write down calculations so you don't lose them when you turn off your calculator (the program).

## 5. Detailed Explanation

### 5.1 Pointers
*   **Declaration:** `int *ptr;` (ptr is a pointer to an integer).
*   **Initialization:** `ptr = &var;` (`&` is the address-of operator).
*   **Dereferencing:** `*ptr` gives the value stored at the address pointed to by `ptr` (`*` is the value-at-address operator).
*   **NULL Pointer:** A pointer that does not point to any memory location. `int *ptr = NULL;`

### 5.2 Pointer Arithmetic
Pointers can be incremented, decremented, added to, or subtracted from integers.
*   `ptr++`: Moves pointer to the next memory location of its data type. If `ptr` is `int*` and `int` is 4 bytes, `ptr++` increases the address by 4.
*   Pointers can be compared (`==`, `<`, `>`) only if they point to elements of the same array.

### 5.3 Pointer and Array
The name of an array acts as a constant pointer to its first element.
*   If `int arr[5];`, then `arr` is equivalent to `&arr[0]`.
*   Traversing: `*(arr + i)` is exactly equivalent to `arr[i]`.

### 5.4 Passing Pointer to Function
C natively passes arguments by value. To modify the original variable inside a function, we pass its memory address (Call by Reference).
```c
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
// Called as: swap(&a, &b);
```

### 5.5 Structure
*   **Declaration:** Uses the `struct` keyword.
*   **Accessing members:** Using the dot (`.`) operator. `student1.marks = 95;`

### 5.6 Union
Similar to structures but all members share the same memory location. The size of a union is the size of its largest member. Only one member can contain a value at any given time.
*   **Declaration:** Uses the `union` keyword.

### 5.7 Array of Structure
Used to store records of multiple entities.
`struct Student class[50];` allows storing details of 50 students. `class[0].roll` accesses the first student's roll number.

### 5.8 Passing Structure to Function
*   **By Value:** Entire structure is copied. `void display(struct Student s);`
*   **By Reference:** Pointer to structure is passed. More efficient as it avoids copying large amounts of data. `void update(struct Student *s);`

### 5.9 Structure and Pointer
When a pointer points to a structure, members are accessed using the arrow operator (`->`).
`struct Student *ptr = &student1;` -> `ptr->roll = 10;` is equivalent to `(*ptr).roll = 10;`

### 5.10 File I/O
Operations involve File pointers (`FILE *fp;`).
*   `fopen("filename", "mode")`: Opens a file. Modes: `r` (read), `w` (write), `a` (append), `rb`, `wb` (binary modes).
*   `fclose(fp)`: Closes the file.
*   **Formatted:** `fprintf(fp, ...)` and `fscanf(fp, ...)`.
*   **String:** `fputs(str, fp)` and `fgets(str, n, fp)`.
*   **Binary/Block:** `fwrite(ptr, size, n, fp)` and `fread(ptr, size, n, fp)`.

### 5.11 Sequential vs Random Access
*   **Sequential Access:** Data is read/written strictly in order from beginning to end.
*   **Random Access:** Allows jumping to any part of the file.
    *   `fseek(fp, offset, origin)`: Moves the file pointer. Origins: `SEEK_SET` (start), `SEEK_CUR` (current), `SEEK_END` (end).
    *   `ftell(fp)`: Returns current position of the file pointer.
    *   `rewind(fp)`: Moves pointer back to the beginning.

## 6. ASCII Diagrams

**Pointer Memory Model**
```text
Variable 'var' (Value = 10, Address = 0x100)
    [ 10 ] <-- Address 0x100

Pointer 'ptr' (Value = 0x100, Address = 0x200)
    [ 0x100 ] <-- Address 0x200
       |
       '-- Points to 'var'
```

**Structure Memory Allocation (e.g., char, int, float)**
```text
struct Example { char c; int i; float f; };
(Assuming no padding for simplicity)
Byte 0:  [char c]
Byte 1:  [int i ]
Byte 2:  [int i ]
Byte 3:  [int i ]
Byte 4:  [int i ]
Byte 5:  [float f]
...
```

## ⚖️ 7. Comparison Tables

| Feature | Structure (`struct`) | Union (`union`) |
| :--- | :--- | :--- |
| **Memory Allocation** | Each member has its own separate memory location. | All members share the same memory location. |
| **Size** | Sum of sizes of all members (plus potential padding). | Equal to the size of the largest member. |
| **Accessibility** | All members can be accessed simultaneously. | Only one member can be accessed at a time. |
| **Initialization** | Multiple members can be initialized at once. | Only the first member can be initialized at declaration. |

## 🔍 8. Worked Examples

### Example 1: Array of Structures
```c
#include <stdio.h>

struct Student {
    char name[50];
    int roll;
    float marks;
};

int main() {
    struct Student s[2];

    // Input
    for(int i=0; i<2; i++) {
        printf("Enter name, roll, and marks for student %d: ", i+1);
        scanf("%s %d %f", s[i].name, &s[i].roll, &s[i].marks);
    }

    // Output
    printf("\nStudent Records:\n");
    for(int i=0; i<2; i++) {
        printf("Roll: %d, Name: %s, Marks: %.2f\n", s[i].roll, s[i].name, s[i].marks);
    }
    return 0;
}
```

### Example 2: File I/O (Writing and Reading)
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    char text[100];

    // Writing to file
    fp = fopen("data.txt", "w");
    if(fp == NULL) {
        printf("Error opening file!");
        exit(1);
    }
    fprintf(fp, "Learning C File I/O is fun!\n");
    fclose(fp);

    // Reading from file
    fp = fopen("data.txt", "r");
    if(fp == NULL) {
        printf("Error opening file!");
        exit(1);
    }
    fgets(text, sizeof(text), fp);
    printf("Read from file: %s", text);
    fclose(fp);

    return 0;
}
```

## 📝 9. Key Formulas Summary

> [!NOTE]
> **Pointer Arithmetic Formulas:**
> *   `New_Address = Current_Address + (i * size_of_data_type)` (for `ptr + i`)
> *   Difference between two pointers of same type = `(Address1 - Address2) / size_of_data_type`

## 💡 10. Common Mistakes / Exam Tips

> [!WARNING]
> *   **Uninitialized Pointers:** Dereferencing an uninitialized pointer (wild pointer) causes segmentation faults (crashes).
> *   **Dangling Pointers:** Pointing to a memory location that has been freed or has gone out of scope.
> *   **Forgetting `&` in `scanf`:** A classic mistake! `scanf("%d", num);` instead of `scanf("%d", &num);` leads to crashes because `scanf` expects an address. Strings (`%s`) are an exception because the array name is already an address.
> *   **Not Closing Files:** Always use `fclose(fp);` after you are done. Failure to do so can result in data loss or file corruption.

> [!TIP]
> *   **Exam Strategy:** When asked to swap numbers, always write the Call by Reference (Pointer) version unless explicitly asked for something else. It demonstrates your understanding of pointers.
> *   Remember the arrow operator (`->`) is just syntactic sugar for `(*ptr).member`.

## ✏️ 11. Practice Problems

1.  **Question:** Explain how `fseek()` is used for random file access with a code snippet.
    *Answer Sketch:* Discuss `fseek(fp, offset, origin)`. Snippet: `fseek(fp, 0, SEEK_END); long size = ftell(fp);` (finds file size).
2.  **Question:** Differentiate between passing a structure by value and passing it by reference.
    *Answer:* By value copies data (slower, safe). By reference passes address (faster, original can be modified, uses `->`).
3.  **Question:** What is a NULL pointer?
    *Answer:* A pointer that intentionally points to nothing (`NULL` macro, typically value 0). Used for initialization and error checking.
