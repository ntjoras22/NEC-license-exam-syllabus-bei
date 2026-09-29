## Section Transaction Processing, Concurrency Control and Crash Recovery (AEiE0704)

## 📖 1. Introduction
Transaction processing, concurrency control, and crash recovery are fundamental concepts in Database Management Systems (DBMS) ensuring data integrity and consistency. A transaction is a logical unit of work that must be either entirely completed or entirely aborted. In modern systems where multiple users access data concurrently, concurrency control mechanisms are essential to prevent data inconsistencies, while crash recovery ensures that data is not lost during system failures. For the NEC exam, understanding the ACID properties, serializability, locking protocols, and log-based recovery is crucial.

## 💡 2. Basic Concept
A transaction represents a real-world event, such as transferring funds from one bank account to another. It involves a sequence of read and write operations on the database. 

> [!NOTE] Definition
> **Transaction**: A sequence of database operations that forms a single logical unit of work.
> **Concurrency Control**: The process of managing simultaneous operations on a database without having them interfere with one another.
> **Crash Recovery**: The process of restoring a database to a correct and consistent state after a system failure.

## 📋 3. ACID Properties
Every transaction must maintain the ACID properties to ensure database reliability.

- **Atomicity**: The "all or nothing" rule. A transaction is treated as a single indivisible unit. Either all its operations are executed, or none are.
- **Consistency**: The execution of a transaction must leave the database in a consistent state. If the database was consistent before the transaction, it must be consistent after.
- **Isolation**: Concurrent execution of transactions should result in a system state that is equivalent to a state achieved if these transactions were executed serially in some order.
- **Durability**: Once a transaction has been committed, its effects are permanent and will survive subsequent system failures.

### Example: Funds Transfer
Consider a transaction $T$ transferring $100 from account A to account B:
1. Read(A)
2. A = A - 100
3. Write(A)
4. Read(B)
5. B = B + 100
6. Write(B)

- **Atomicity** ensures both A is decremented and B is incremented, or neither happens.
- **Consistency** ensures the sum A + B remains the same before and after.
- **Isolation** ensures another transaction cannot see A decremented before B is incremented.
- **Durability** ensures the updated values of A and B are stored permanently.

## 4. Concurrent Executions and Serializability Concept
When multiple transactions execute concurrently, the database interleaves their operations. A **Schedule** (or history) is a chronological sequence of operations from multiple transactions.

> [!NOTE] Definition
> **Serial Schedule**: A schedule where the operations of each transaction are executed consecutively without any interleaving from other transactions.
> **Serializable Schedule**: A non-serial schedule that produces the same result as some serial execution of the same transactions.

### Conflict Serializability
Two operations conflict if they belong to different transactions, access the same data item, and at least one is a Write operation. The conflicts are:
- Read-Write (RW) conflict
- Write-Read (WR) conflict
- Write-Write (WW) conflict

A schedule is **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations.

**Testing for Conflict Serializability:**
Use a **Precedence Graph** (Serialization Graph):
1. Create a node for each transaction.
2. Add a directed edge $T_i \rightarrow T_j$ if $T_i$ executes an operation that conflicts with and precedes an operation of $T_j$.
3. If the graph has **no cycles**, the schedule is conflict serializable.

## 5. Lock-Based Protocols
Lock-based protocols restrict concurrent access to data items to ensure serializability.

- **Shared Lock (S-lock)**: Requested for reading. Multiple transactions can hold S-locks on the same data item.
- **Exclusive Lock (X-lock)**: Requested for writing (and reading). Only one transaction can hold an X-lock on a data item.

### Two-Phase Locking (2PL) Protocol
A transaction is said to follow the 2PL protocol if all locking operations precede the first unlock operation. It has two phases:
1. **Growing Phase**: Transaction may obtain locks but cannot release any lock.
2. **Shrinking Phase**: Transaction may release locks but cannot obtain any new lock.

> [!IMPORTANT] 
> 2PL guarantees serializability but does not prevent deadlocks.

**Strict 2PL**: A transaction holds all its exclusive locks until it commits or aborts. Prevents cascading rollbacks.
**Rigorous 2PL**: A transaction holds ALL locks (shared and exclusive) until it commits or aborts.

## 6. Deadlock Handling and Prevention
A deadlock occurs when two or more transactions are waiting for locks held by each other, forming a cycle of dependencies.

### Deadlock Prevention
Protocols that ensure the system never enters a deadlock state.
- **Wait-Die scheme (Non-preemptive)**: If older $T_i$ requests a lock held by younger $T_j$, $T_i$ waits. If younger $T_j$ requests a lock held by older $T_i$, $T_j$ dies (rolls back).
- **Wound-Wait scheme (Preemptive)**: If older $T_i$ requests a lock held by younger $T_j$, $T_i$ wounds (forces to roll back) $T_j$. If younger $T_j$ requests a lock held by older $T_i$, $T_j$ waits.

### Deadlock Detection and Recovery
Allow deadlocks to occur, periodically check for them using a **Wait-For Graph**, and recover by aborting a transaction (victim selection).

## 🏷️ 7. Failure Classification
- **Transaction failure**: Logical errors (bad input) or system errors (deadlock).
- **System crash**: Hardware malfunction or OS bug causing loss of volatile storage (RAM) but non-volatile storage (disk) remains intact. Fail-stop assumption is usually made.
- **Disk failure**: Loss of non-volatile storage (head crash). Handled using backups and RAID.

## 8. Recovery and Atomicity
Recovery algorithms have two parts:
1. Actions taken during normal transaction processing to ensure enough info exists to recover.
2. Actions taken after a failure to recover the database contents.

- **Redo**: Reapplying modifications of committed transactions.
- **Undo**: Reversing modifications of uncommitted/aborted transactions.

## 9. Log-Based Recovery
The log is a sequence of records maintaining information about update activities on the database. It is kept on stable storage.

**Log Records:**
- $<T_i, \text{start}>$: Transaction $T_i$ has started.
- $<T_i, X, V_{old}, V_{new}>$: Transaction $T_i$ modified data item $X$ from $V_{old}$ to $V_{new}$.
- $<T_i, \text{commit}>$: Transaction $T_i$ has committed.
- $<T_i, \text{abort}>$: Transaction $T_i$ has aborted.

### Deferred Database Modification
- All updates are deferred until the transaction partially commits.
- Uses only REDO. Log record needs only new value: $<T_i, X, V_{new}>$.
- If crash occurs before commit, no undo is needed (database wasn't modified).

### Immediate Database Modification
- Updates are applied to the database while the transaction is still active.
- Requires both UNDO and REDO. Log record needs both old and new values.
- **Undo**: If log has $<T_i, \text{start}>$ but no $<T_i, \text{commit}>$.
- **Redo**: If log has both $<T_i, \text{start}>$ and $<T_i, \text{commit}>$.

### Checkpoints
Reading the entire log for recovery is expensive. A checkpoint periodically saves the DBMS state to disk.
- Output all log records to stable storage.
- Output all modified buffer blocks to disk.
- Write a log record $<checkpoint, L>$ where $L$ is a list of active transactions.
- During recovery, the system scans backwards to the most recent checkpoint.

## Comparison Table: Concurrency Control

| Feature | Two-Phase Locking | Timestamp Ordering |
| :--- | :--- | :--- |
| **Approach** | Pessimistic (prevents conflicts via locks) | Optimistic (checks timestamps for conflicts) |
| **Deadlock Possibility** | High (needs handling) | None (transactions aborted/restarted) |
| **Overhead** | Locking/unlocking, deadlock detection | Timestamp maintenance |
| **Best suited for** | High conflict environments | Low conflict environments |

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse Strict 2PL with Rigorous 2PL. Strict holds only Exclusive locks until commit, Rigorous holds ALL locks until commit.

> [!TIP]
> In precedence graph questions, remember: Cycle = Not Conflict Serializable. No Cycle = Conflict Serializable. For Wait-For graphs: Cycle = Deadlock.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - **ACID**: Atomicity, Consistency, Isolation, Durability.
> - **Conflict operations**: RW, WR, WW on the same data item by different transactions.
> - **Wait-Die**: Older waits for younger, younger dies.
> - **Wound-Wait**: Older wounds (kills) younger, younger waits.
> - **Recovery**: Undo uncommitted, Redo committed.

## ✏️ Practice Problems

1. Given the schedule $S = R_1(X), W_2(X), R_2(Y), W_1(Y)$, draw the precedence graph and determine if it is conflict serializable.
   *Answer sketch: $T_1$ reads $X$ before $T_2$ writes $X$ $\rightarrow T_1 \rightarrow T_2$. $T_2$ reads $Y$ before $T_1$ writes $Y$ $\rightarrow T_2 \rightarrow T_1$. The graph has a cycle. Not conflict serializable.*

2. Explain the difference between deferred and immediate database modification.
   *Answer sketch: Deferred applies updates only after commit (needs REDO only). Immediate applies updates before commit (needs both UNDO and REDO).*
</Section 7.4: Transaction Processing, Concurrency Control and Crash Recovery (AEiE0704)>
