# Section 4.5: Real-Time Operating and Control System (ACtE0405)

## 📖 1. Introduction
The Real-Time Operating and Control System section covers the fundamental concepts of operating systems (OS), specifically tailored for embedded systems, real-time operating systems (RTOS), and the basics of control systems. These concepts are crucial for understanding how embedded devices manage hardware resources, schedule tasks to meet strict timing deadlines, and interface with the physical world through closed-loop and open-loop control mechanisms. 

---

## 2. Operating System Basics

### Basic Concept
An Operating System (OS) is the software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between the user of a computer and the computer hardware.

> **Definition**: An **Operating System (OS)** is a system software that manages hardware resources, controls program execution, and provides a user interface.

### Types of Operating Systems
1. **Batch Operating System**: Executes a series of jobs (batches) without manual intervention. Examples: Payroll systems.
2. **Time-Sharing (Multitasking) OS**: Allows multiple users to share system resources simultaneously by rapidly switching the CPU among tasks.
3. **Real-Time Operating System (RTOS)**: Guarantees a certain capability within a specified time constraint. Used in embedded systems where timing is critical (e.g., pacemakers, anti-lock braking systems).

### Kernel and System Calls
- **Kernel**: The core component of an OS. It resides in memory and manages the CPU, memory, and peripheral devices.
- **System Calls**: The programmable interface provided by the OS to applications. When a user program needs a privileged operation (like reading a file), it executes a system call, causing a context switch into *kernel mode*.

---

## 3. Task, Process, and Threads

### Process
A process is a program in execution. It includes the program code (text section), current activity (program counter, registers), process stack (temporary data), and data section (global variables).

> [!NOTE]
> **Process Control Block (PCB)**: A data structure used by the OS to store information about a process, including process state, program counter, CPU registers, memory management information, and accounting info.

**Process States**:
1. **New**: The process is being created.
2. **Ready**: The process is waiting to be assigned to a processor.
3. **Running**: Instructions are being executed.
4. **Waiting (Blocked)**: The process is waiting for some event to occur (e.g., I/O completion).
5. **Terminated**: The process has finished execution.

```text
       +---------+
       |   New   |
       +----+----+
            |
            v
     +------+------+         +-----------+
     |   Ready     | <------ |  Waiting  |
     +----+--^-----+         +-----^-----+
          |  |                     |
          v  |                     |
     +-------+-----+               |
     |   Running   | --------------+
     +----+--------+
          |
          v
    +-----+-------+
    | Terminated  |
    +-------------+
```

### Threads
A thread is the smallest sequence of programmed instructions that can be managed independently by a scheduler. A process can contain multiple threads.
- **Multithreading**: Allows concurrent execution of multiple threads within a single process, sharing the same memory space (code, data, and files) but having independent registers and stacks.

### Context Switching
Context switching is the process of storing the state (context) of the currently running process/thread so that it can be restored and execution resumed from the same point later. It is essential for multitasking but introduces overhead.

---

## 💡 4. Multiprocessing vs Multitasking

| Feature | Multiprocessing | Multitasking |
|---------|-----------------|--------------|
| **Definition** | Execution of multiple processes using multiple CPUs simultaneously. | Execution of multiple tasks/processes concurrently on a single CPU. |
| **Hardware** | Requires multiple processors/cores. | Can run on a single processor core. |
| **Execution** | True parallel execution. | Pseudo-parallel (concurrent) via rapid context switching. |
| **Throughput** | High throughput. | Moderate throughput (limited by single CPU speed). |
| **Complexity** | High (hardware and software synchronization). | Moderate (primarily software scheduling). |

---

## 5. Task Scheduling

Task scheduling is the mechanism by which the OS decides which process in the *Ready* queue should be executed next by the CPU.

### Preemptive vs Non-Preemptive
- **Preemptive Scheduling**: The OS can interrupt a running process and allocate the CPU to another process (usually of higher priority). Essential for RTOS.
- **Non-Preemptive (Cooperative) Scheduling**: A process retains the CPU until it voluntarily yields it or blocks for I/O. 

### Scheduling Algorithms
1. **First-Come, First-Served (FCFS)**: Non-preemptive. The process that arrives first is executed first. Simple but suffers from the *convoy effect*.
2. **Shortest Job First (SJF)**: Selects the process with the smallest execution time. Can be preemptive (Shortest Remaining Time First) or non-preemptive. Optimal for average waiting time.
3. **Priority Scheduling**: Each process is assigned a priority. The highest priority process is executed first. Can suffer from *starvation* (solved by aging).
4. **Round Robin (RR)**: Preemptive. Each process gets a small unit of CPU time (time quantum). After the quantum expires, the process is preempted and added to the end of the ready queue.

### Real-Time Scheduling Algorithms
Real-time systems require specific algorithms to meet hard deadlines.

1. **Rate Monotonic Scheduling (RMS)**:
   - Static priority scheduling.
   - Priority is inversely proportional to the task's period: shorter period = higher priority.
   - Utilization bound for schedulability of $n$ tasks: 

$$ U = \sum_{i=1}^n \frac{C_i}{T_i} \le n(2^{1/n} - 1) $$
     where $C_i$ is computation time and $T_i$ is the period.

2. **Earliest Deadline First (EDF)**:
   - Dynamic priority scheduling.
   - The task with the closest absolute deadline gets the highest priority.
   - Schedulable if total utilization is $\le 1$ ($100\%$).

---

## 6. Task Synchronization

In multitasking, tasks often share resources. Concurrent access to shared data can lead to data inconsistency.

> **Definition**: A **Race Condition** occurs when multiple processes access and manipulate shared data concurrently, and the final outcome depends on the particular order of execution.

### Critical Section
A section of code where shared resources (variables, memory, hardware) are accessed. To prevent race conditions, execution of critical sections must be mutually exclusive.

### Synchronization Primitives
1. **Mutex (Mutual Exclusion)**: A locking mechanism. Only the thread that acquired the mutex can release it. Used to protect critical sections.
2. **Semaphore**: A signaling mechanism. It is an integer variable used to control access to a common resource.
   - *Binary Semaphore*: Values 0 or 1. Similar to mutex but used for signaling.
   - *Counting Semaphore*: Values $> 1$. Used to manage a pool of identical resources.

### Priority Inversion
A problem in real-time systems where a high-priority task is indirectly preempted by a lower-priority task holding a shared resource (mutex).
- **Solution**: *Priority Inheritance Protocol*, where the low-priority task temporarily inherits the high priority of the task waiting for the resource.

---

## 7. Device Drivers

Device drivers are specialized software modules that allow the OS to interact with hardware devices.

- **Concept**: They act as a translator between the high-level OS commands and the low-level hardware-specific instructions.
- **Structure**: Typically consist of an initialization routine, interrupt service routines (ISRs), and standard interface functions (read, write, open, close).
- **Role in Embedded Systems**: In RTOS, drivers are crucial for managing peripherals like UART, SPI, I2C, and sensors. They must be highly optimized to ensure they do not violate real-time constraints.

---

## 8. Real-Time Systems

> **Definition**: A **Real-Time System** is one where the correctness of the system depends not only on the logical result of computation but also on the time at which the results are produced.

- **Hard Real-Time**: Missing a deadline results in total system failure (e.g., flight control systems, airbag deployment).
- **Soft Real-Time**: Missing a deadline degrades performance but is not catastrophic (e.g., video streaming, online gaming).

**RTOS Examples**:
- **FreeRTOS**: Open-source, highly portable, widely used in microcontrollers.
- **VxWorks**: Commercial, highly deterministic, used in aerospace and robotics (e.g., Mars rovers).

---

## 9. Control Systems Overview

A control system manages, commands, directs, or regulates the behavior of other devices or systems to achieve a desired output.

### Open-Loop vs Closed-Loop Control

| Feature | Open-Loop Control System | Closed-Loop Control System |
|---------|--------------------------|----------------------------|
| **Feedback** | No feedback mechanism. | Contains a feedback loop. |
| **Accuracy** | Less accurate, highly dependent on calibration. | Highly accurate, self-correcting. |
| **Complexity** | Simple design and easy to construct. | Complex design. |
| **Stability** | Generally stable. | Can become unstable if poorly tuned. |
| **Example** | Washing machine, toaster. | Cruise control, AC thermostat. |

### Block Diagram & Transfer Function
- **Transfer Function**: The ratio of the Laplace transform of the output to the Laplace transform of the input, assuming zero initial conditions.

$$ G(s) = \frac{Y(s)}{R(s)} $$

**Closed-Loop Transfer Function**:
```text
           +------+      +------+
R(s) ----->|  +   |----->| G(s) |-----> Y(s)
           |      |      +------+
           +--^---+         |
              |             |
           +------+         |
           | H(s) |<--------+
           +------+
```
For negative feedback:
$$ \frac{Y(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)} $$

### PID Controller Basics
The Proportional-Integral-Derivative (PID) controller is the most common control loop feedback mechanism.

$$ u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt} $$

- **Proportional (P)**: Output is proportional to the current error $e(t)$. Reduces rise time but leaves steady-state error.
- **Integral (I)**: Output is proportional to the accumulated error. Eliminates steady-state error but can cause overshoot and instability.
- **Derivative (D)**: Output is proportional to the rate of change of error. Reduces overshoot and improves transient response.

---

## 🔍 10. Worked Examples

**Example 1: Rate Monotonic Scheduling**
Given two tasks $T_1$ (computation $C_1=2$, period $T_1=5$) and $T_2$ (computation $C_2=4$, period $T_2=15$). Are they schedulable using RMS?

**Solution**:
1. Utilization $U = \frac{C_1}{T_1} + \frac{C_2}{T_2} = \frac{2}{5} + \frac{4}{15} = 0.4 + 0.267 = 0.667$.
2. RMS bound for $n=2$: $U_{bound} = 2(2^{1/2} - 1) = 2(1.414 - 1) = 0.828$.
3. Since $0.667 \le 0.828$, the tasks are schedulable.

**Example 2: PID Controller Transfer Function**
Find the transfer function $C(s)$ of an ideal PID controller.

**Solution**:
Taking the Laplace transform of the PID time-domain equation:
$$ U(s) = K_p E(s) + \frac{K_i}{s} E(s) + K_d s E(s) $$
$$ C(s) = \frac{U(s)}{E(s)} = K_p + \frac{K_i}{s} + K_d s = \frac{K_d s^2 + K_p s + K_i}{s} $$

---

## 💡 11. Common Mistakes / Exam Tips
> [!WARNING]
> **Priority Inversion vs Deadlock**: Do not confuse these. Priority inversion happens when a high-priority task waits on a low-priority task. Deadlock happens when two or more tasks are stuck waiting for each other indefinitely.
> 
> **Mutex vs Semaphore**: Mutex implies ownership (the thread that locks it must unlock it). Semaphores do not have ownership and can be signaled from an ISR.
>
> **RMS Priority Assignment**: In RMS, priority is determined by the **period**, not the computation time. Shortest period = highest priority.

---

## ✏️ 12. Practice Problems

**Q1.** Which scheduling algorithm suffers from the convoy effect?
A. Round Robin
B. FCFS
C. SJF
D. EDF

**Q2.** A system has 3 tasks with periods 10, 20, and 30, and execution times 2, 4, and 3 respectively. What is the CPU utilization?
A. 0.4
B. 0.5
C. 0.6
D. 0.7

**Q3.** Which mechanism is specifically designed to solve the priority inversion problem?
A. Priority Inheritance
B. Round Robin Scheduling
C. Binary Semaphore
D. Deadlock Avoidance

**Q4.** In a PID controller, which term is responsible for eliminating steady-state error?
A. Proportional
B. Integral
C. Derivative
D. Gain

**Answers:**
1. B (FCFS)
2. B (Utilization = 2/10 + 4/20 + 3/30 = 0.2 + 0.2 + 0.1 = 0.5)
3. A
4. B
