## Section Turing Machine (AEiE0803)

## 📖 1. Introduction
The Turing Machine (TM) is the most powerful model of computation in formal language theory, capable of simulating any computer algorithm. Proposed by Alan Turing in 1936, it defines the theoretical limits of what can be computed (decidability). In the NEC exam, understanding the capabilities, variations, and complexities of TMs is essential.

## 💡 2. Basic Concept
A Turing Machine consists of a finite state control, an infinite tape divided into cells (each holding one symbol), and a read/write head that can move left or right along the tape.

> [!NOTE] Definition
> **Turing Machine**: A mathematical model of computation described by a 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$ where:
> - $Q$ is the finite set of states.
> - $\Sigma$ is the input alphabet (not containing the blank symbol).
> - $\Gamma$ is the tape alphabet ($\Sigma \subset \Gamma$).
> - $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$ is the transition function.
> - $q_0 \in Q$ is the start state.
> - $B \in \Gamma$ is the blank symbol.
> - $F \subseteq Q$ is the set of final (accepting) states.

## 3. Turing Machine as Different Models
### 3.1 As a Language Recognizer
A TM recognizes a language $L$ if it accepts every string in $L$ and either rejects or loops infinitely for strings not in $L$. If a TM halts on all inputs (accepts strings in $L$ and explicitly rejects strings not in $L$), it is called a **Decider**, and the language is **Recursive** (or Turing-decidable). If it only guarantees halting for strings in $L$, the language is **Recursively Enumerable** (Turing-recognizable).

### 3.2 As a Computing Function
A TM can compute mathematical functions. Given an input $x$ on the tape, if the TM halts with $f(x)$ on the tape, the TM computes the function $f(x)$. Such functions are called Turing-computable.

### 3.3 As an Enumerator
An enumerator is a TM with an attached printer. It systematically generates and prints all strings of a language, one by one. A language is Recursively Enumerable if and only if some enumerator enumerates it.

## 4. Variations of Turing Machines
All the following variations are equivalent in power to the standard single-tape deterministic Turing Machine.
- **TM with Multiple Tracks**: The single tape is divided into multiple tracks. The head reads an $n$-tuple of symbols at once.
- **TM with Multiple Tapes**: Consists of multiple tapes, each with its own independent read/write head. Useful for complex computations but does not increase the language recognition power.
- **Non-Deterministic Turing Machine (NTM)**: At each step, the NTM can choose from multiple possible actions. An NTM accepts an input if at least one computation branch leads to an accept state. NTMs and DTMs are equivalent in computational power.

## 5. Church-Turing Thesis
The Church-Turing Thesis is a fundamental hypothesis about the nature of computable functions.

> [!NOTE] Definition
> **Church-Turing Thesis**: Any intuitive, informal notion of a "computable algorithm" can be formally computed by a Turing Machine. 
It cannot be mathematically proven because "intuitive algorithm" is not a formal mathematical concept, but it is universally accepted.

## 6. Universal Turing Machine (UTM)
A Universal Turing Machine can simulate the behavior of any other Turing Machine. It takes as input the encoding (description) of a Turing Machine $M$ and an input string $w$, and simulates $M$ on $w$.
- Encoding involves representing the states, symbols, and transitions of $M$ as a string of 0s and 1s.
- This is the theoretical foundation for modern general-purpose computers (stored-program computers).

## 7. Time and Space Complexity
- **Time Complexity ($T(n)$)**: The maximum number of steps a TM makes on any input of length $n$.
- **Space Complexity ($S(n)$)**: The maximum number of tape cells scanned by a TM on any input of length $n$.
- Multi-tape TMs can sometimes solve problems faster than single-tape TMs, but space complexity remains roughly equivalent.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Remember that variations of Turing Machines (multi-tape, NTM) do NOT increase the class of languages they can recognize. They still only recognize Recursively Enumerable languages.

> [!TIP]
> - Halting Problem is undecidable.
> - Recursive languages are closed under complement, but Recursively Enumerable languages are not.
> - A TM has infinite memory, unlike PDA and FA.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - TM Transition: $\delta(q, X) = (p, Y, D)$ where $D \in \{L, R\}$
> - Class of Languages: FA (Regular) $\subset$ PDA (Context-Free) $\subset$ LBA (Context-Sensitive) $\subset$ TM (Recursively Enumerable).
> - Church-Turing Thesis connects informal algorithms with formal TM models.

## ✏️ Practice Problems
1. **Problem**: Design a TM to accept $L = \{0^n 1^n 2^n \mid n \ge 1\}$.
   *Sketch*: Replace '0' with 'X', move right to find first '1' and replace with 'Y', move right to find first '2' and replace with 'Z'. Return to left and repeat until all symbols are replaced.
2. **Problem**: Explain the difference between a Recursive language and a Recursively Enumerable language.
   *Sketch*: Recursive = TM halts on all inputs (accepts or rejects). RE = TM halts and accepts if string is in language, but may loop infinitely if not.
3. **Problem**: Briefly describe how a multi-tape TM can be simulated by a single-tape TM.
   *Sketch*: Use multiple tracks on the single tape. For $k$ tapes, use $2k$ tracks (one for content, one to mark head position for each tape).
</Section 8.3: Turing Machine (AEiE0803)>
