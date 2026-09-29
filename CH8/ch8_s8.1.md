## Section Finite Automata (AEiE0801)

## 📖 1. Introduction
Finite Automata (FA) is the simplest model of computation. It is a mathematical model of a system with discrete inputs and outputs. The system can be in any one of a finite number of internal configurations or "states". Finite Automata are fundamental in computer science, used in lexical analysis, text processing, pattern matching, and hardware design. For the NEC exam, understanding the mathematical definitions, conversions, and minimizations is crucial.

## 💡 2. Basic Concept
A finite automaton consists of a finite set of states, a start state, a set of accept states, and transition rules that dictate how the automaton moves from one state to another based on input symbols.

> [!NOTE] Definition
> **Finite Automaton**: A mathematical model of computation consisting of a set of states, a set of input symbols, and transitions between states. It does not have any auxiliary memory.

There are two primary types of Finite Automata without output:
1. **Deterministic Finite Automata (DFA)**: For every state and every input symbol, there is exactly one transition to a next state.
2. **Non-Deterministic Finite Automata (NFA / NDFA)**: For a given state and input symbol, there can be zero, one, or multiple transitions. It can also have $\epsilon$-transitions (transitions without input).

## 3. Deterministic Finite Automata (DFA)
A DFA is formally defined as a 5-tuple:
$$M = (Q, \Sigma, \delta, q_0, F)$$
Where:
- $Q$ is a finite set of states.
- $\Sigma$ is a finite set of input symbols (alphabet).
- $\delta: Q \times \Sigma \rightarrow Q$ is the transition function.
- $q_0 \in Q$ is the initial state.
- $F \subseteq Q$ is the set of final (accepting) states.

### Example
Construct a DFA that accepts all strings over $\{0,1\}$ ending with $11$.
- States $Q = \{q_0, q_1, q_2\}$
- $\Sigma = \{0, 1\}$
- Start state = $q_0$
- Final state = $\{q_2\}$

**Transition Table:**
| State | Input $0$ | Input $1$ |
|-------|-----------|-----------|
| $\rightarrow q_0$ | $q_0$ | $q_1$ |
| $q_1$ | $q_0$ | $q_2$ |
| $*q_2$ | $q_0$ | $q_2$ |

## 4. Non-Deterministic Finite Automata (NFA)
An NFA is formally defined as a 5-tuple $M = (Q, \Sigma, \delta, q_0, F)$, similar to DFA, but the transition function maps to a power set of states:
$$\delta: Q \times \Sigma \rightarrow 2^Q$$

## 5. Equivalence of DFA and NFA
Every language accepted by an NFA can also be accepted by a DFA. Thus, DFAs and NFAs are equivalent in power. The process of converting an NFA to a DFA is called the **Subset Construction Algorithm**.

### Subset Construction Algorithm
1. The start state of the DFA is the $\epsilon$-closure of the start state of the NFA.
2. For each state set in the DFA and each input symbol, compute the set of next states in the NFA and take their $\epsilon$-closure. This new set becomes a state in the DFA.
3. Repeat step 2 until no new sets of states are generated.
4. Any DFA state containing an NFA final state becomes a final state in the DFA.

## 6. Minimization of Finite State Machines
Minimization refers to finding a DFA with the minimum number of states that recognizes the same language. The standard algorithm used is the **Table Filling Algorithm** (or Myhill-Nerode theorem based approach).

### Steps for Minimization:
1. Remove unreachable states from the start state.
2. Divide states into two partitions: non-final states $Q \setminus F$ and final states $F$.
3. For each pair of states $(p, q)$, if for any input $a \in \Sigma$, $\delta(p,a)$ and $\delta(q,a)$ belong to different partitions, then $(p, q)$ are distinguishable. Move them into separate partitions.
4. Repeat step 3 until no more states can be separated.
5. Combine states in the same partition into a single state.

## 7. Regular Expressions
Regular expressions provide a declarative way to specify regular languages.

> [!NOTE] Definition
> **Regular Expression (RE)**: A sequence of characters that define a search pattern, representing a regular language algebraically.

Operations on Regular Expressions:
- **Union**: $R_1 + R_2$ (or $R_1 \cup R_2$)
- **Concatenation**: $R_1 \cdot R_2$
- **Kleene Star**: $R^*$ (zero or more occurrences)

### Arden's Theorem
If $P$ and $Q$ are two regular expressions over $\Sigma$, and if $P$ does not contain $\epsilon$, then the equation $R = Q + RP$ has a unique solution given by $R = QP^*$. This is extensively used in converting DFAs to Regular Expressions.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> A common mistake is forgetting to compute the $\epsilon$-closure when converting $\epsilon$-NFA to DFA. Always ensure you consider all states reachable without consuming input.

> [!TIP]
> - NFA and DFA have the same expressive power (Regular Languages).
> - Regular expression to DFA conversion usually involves finding the NFA first (Thompson's construction).
> - In minimization, don't forget to eliminate unreachable states BEFORE applying the equivalence partition algorithm.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - DFA transition: $\delta(q, a) = p$
> - NFA transition: $\delta(q, a) = \{p_1, p_2, \dots\}$
> - Equivalence: $L(NFA) = L(DFA)$
> - Arden's Theorem: $R = Q + RP \implies R = QP^*$

## ✏️ Practice Problems
1. **Problem**: Convert the regular expression $(0+1)^*10$ into an NFA.
   *Sketch*: Use Thompson's construction. Combine $(0+1)^*$ with a concatenation of $1$ and $0$.
2. **Problem**: Minimize the DFA defined by states $\{A, B, C, D, E, F\}$, where start is $A$, final is $\{C, D, E\}$, and transitions are provided.
   *Sketch*: Use partition method. Initial partitions: $\{A, B, F\}$ and $\{C, D, E\}$.
3. **Problem**: State and prove Arden's theorem.
   *Sketch*: Substitute $QP^*$ into $R = Q + RP$ and prove equivalence.
</Section 8.1: Finite Automata (AEiE0801)>
