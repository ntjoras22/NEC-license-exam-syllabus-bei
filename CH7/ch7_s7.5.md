## Section Operating System and Process Management (AEiE0705)

## 📖 1. Introduction
An Operating System (OS) is the fundamental software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between the user of a computer and the computer hardware. For the NEC exam, a deep understanding of process management, scheduling, threads, and concurrency mechanisms is vital.

## 💡 2. Basic Concept
The OS is essentially a resource manager. It allocates CPU time, memory, and I/O devices to various applications. A **process** is a program in execution, representing the fundamental unit of work in a system.

> [!NOTE] Definition
> **Operating System (OS)**: A program that acts as an intermediary between a user of a computer and the computer hardware.
> **Process**: A program in execution; an instance of a computer program that is being executed.
> **Thread**: A basic unit of CPU utilization, comprising a thread ID, a program counter, a register set, and a stack.

## 📚 3. Evolution and Types of Operating Systems
- **Batch Systems**: Jobs with similar needs are batched together and executed sequentially. No direct user interaction.
- **Multiprogramming Systems**: Keeps multiple jobs in memory to maximize CPU utilization by overlapping CPU and I/O operations.
- **Time-Sharing (Multitasking) Systems**: Logical extension of multiprogramming. CPU executes multiple jobs by switching among them frequently, providing interactive computing.
- **Real-Time Systems**: Used when rigid time requirements have been placed on the operation of a processor or the flow of data (Hard real-time vs. Soft real-time).
- **Distributed Systems**: Distribute computation among several physical processors loosely coupled.

## 📦 4. Operating System Components, Structure, and Services
**Components**: Process Management, Memory Management, File Management, I/O System Management, Secondary-Storage Management, Networking, Protection System, Command-Interpreter System.
**Structure**:
- Monolithic (e.g., MS-DOS, early Linux): All OS components run in a single memory space.
- Layered: OS is broken into a number of layers (levels), each built on top of lower layers.
- Microkernel: Moves as much from the kernel into user space as possible (e.g., Mach).
**Services**: Program execution, I/O operations, File-system manipulation, Communications, Error detection, Resource allocation, Accounting, Protection and security.

## 5. Process Description and States
A process is more than the program code (text section). It includes:
- **Program Counter (PC)** and processor registers.
- **Stack**: Contains temporary data (function parameters, return addresses, local variables).
- **Data Section**: Contains global variables.
- **Heap**: Memory dynamically allocated during run time.

### Process States
A process changes state as it executes:
- **New**: The process is being created.
- **Running**: Instructions are being executed.
- **Waiting (Blocked)**: The process is waiting for some event to occur (e.g., I/O completion).
- **Ready**: The process is waiting to be assigned to a processor.
- **Terminated**: The process has finished execution.

State transitions: New $\rightarrow$ Ready, Ready $\rightarrow$ Running, Running $\rightarrow$ Waiting, Running $\rightarrow$ Ready (Interrupt), Waiting $\rightarrow$ Ready, Running $\rightarrow$ Terminated.

## 6. Process Control and PCB
Each process is represented in the OS by a **Process Control Block (PCB)** or task control block. It contains:
- Process state, Program counter, CPU registers, CPU scheduling information, Memory-management information, Accounting information, I/O status information.

**Context Switch**: Saving the state (PCB) of the old process and loading the saved state for the new process when the CPU switches to another process.

## 7. Threads vs. Processes
A thread is a lightweight process.
- **Single-threaded process**: One path of execution.
- **Multi-threaded process**: Multiple paths of execution within the same process environment. Threads share the code section, data section, and OS resources (open files), but have their own registers and stack.

| Feature | Process | Thread |
| :--- | :--- | :--- |
| Resource Sharing | Do not share memory space | Share memory, data, and files within the process |
| Creation Overhead | High (heavyweight) | Low (lightweight) |
| Context Switching | High overhead | Low overhead |
| Independence | Independent entities | Interdependent |

## 📚 8. Types of Scheduling
The CPU scheduler selects a process from the ready queue to execute.
- **Preemptive Scheduling**: CPU can be taken away from a running process (e.g., on time quantum expiration).
- **Non-preemptive Scheduling**: A process keeps the CPU until it releases it by terminating or switching to the waiting state.

**Scheduling Algorithms:**
- **First-Come, First-Served (FCFS)**: Simple, non-preemptive. High average waiting time (Convoy effect).
- **Shortest-Job-First (SJF)**: Optimal for minimizing average waiting time. Difficult to know next CPU burst length.
- **Priority Scheduling**: CPU allocated to the highest priority process. Problem: Starvation (solution: Aging).
- **Round Robin (RR)**: Each process gets a small unit of CPU time (time quantum $q$). Preemptive.

## 9. Principles of Concurrency
Concurrency involves multiple processes executing at the same time, potentially sharing data.

### Race Condition
A situation where several processes access and manipulate the same data concurrently, and the outcome of the execution depends on the particular order in which the access takes place.

### Critical Region (Critical Section)
A segment of code in which the process may be changing common variables, updating a table, writing a file, etc.
**The Critical Section Problem** requires three conditions:
1. **Mutual Exclusion**: If process $P_i$ is executing in its critical section, then no other processes can be executing in their critical sections.
2. **Progress**: If no process is in its critical section and some processes wish to enter, only those not in their remainder section can participate in deciding who enters next, and this selection cannot be postponed indefinitely.
3. **Bounded Waiting**: A bound must exist on the number of times that other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted.

### Mutual Exclusion Mechanisms
- **Software solutions**: Peterson's Solution.
- **Hardware solutions**: TestAndSet, CompareAndSwap instructions.
- **Mutex Locks**: OS-provided tool with `acquire()` and `release()` functions.
- **Semaphores**: An integer variable $S$ accessed via two indivisible (atomic) operations: `wait()` and `signal()` (or P and V).

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Threads within the same process share the heap and data sections but NOT the stack or registers. A common trap is thinking threads share everything.

> [!TIP]
> For CPU scheduling calculations (turnaround time, waiting time), always draw a Gantt chart first. It makes visualizing the execution order much easier.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **Turnaround Time ($TAT$)** = Completion Time - Arrival Time
> - **Waiting Time ($WT$)** = Turnaround Time - Burst Time
> - **Little's Formula**: $L = \lambda W$ (Average queue length = Average arrival rate $\times$ Average waiting time in queue).

## ✏️ Practice Problems

1. Explain the difference between preemptive and non-preemptive scheduling. Give one example of each.
   *Answer sketch: Preemptive allows OS to interrupt a running process (Round Robin). Non-preemptive means a process runs until it finishes or blocks (FCFS).*

2. What is a race condition, and how is it prevented?
   *Answer sketch: A scenario where shared data outcome depends on execution order. Prevented by mutual exclusion mechanisms (mutexes, semaphores) ensuring only one process accesses the critical section at a time.*
</Section 7.5: Operating System and Process Management (AEiE0705)>
