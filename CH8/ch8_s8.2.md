## Section Context Free Language (AEiE0802)

## 📖 1. Introduction
Context-Free Languages (CFL) are a step above Regular Languages in the Chomsky Hierarchy. They can represent nested structures, such as balanced parentheses and block structures in programming languages. This makes them crucial for compiler design, specifically the syntax analysis (parsing) phase. 

## 💡 2. Basic Concept
A Context-Free Grammar (CFG) is a formal grammar which is used to generate all possible strings in a given formal language. 

> [!NOTE] Definition
> **Context-Free Grammar (CFG)**: A 4-tuple $G = (V, \Sigma, R, S)$ where:
> - $V$ is a finite set of variables (non-terminals).
> - $\Sigma$ is a finite set of terminals (alphabet).
> - $R$ is a finite set of production rules of the form $A \rightarrow \alpha$, where $A \in V$ and $\alpha \in (V \cup \Sigma)^*$.
> - $S \in V$ is the start symbol.

## 3. Derivation Trees and Parsing
A derivation shows how a string is generated from the start symbol by substituting non-terminals using production rules.

### Derivation Types
- **Leftmost Derivation (LMD)**: At each step, the leftmost non-terminal is replaced.
- **Rightmost Derivation (RMD)**: At each step, the rightmost non-terminal is replaced.

### Parse Trees
A parse tree (or derivation tree) is a graphical representation of a derivation. The root is the start symbol, inner nodes are non-terminals, and leaves are terminals.
- **Top-Down Approach**: Starts from the root (start symbol) and grows downwards to the leaves (the input string).
- **Bottom-Up Approach**: Starts from the leaves (the input string) and reduces upwards to the root (start symbol).

## 4. Ambiguous Grammar
A grammar is ambiguous if there exists at least one string in the language that has more than one distinct parse tree, or equivalently, more than one Leftmost Derivation (or Rightmost Derivation).

*Example:* $E \rightarrow E + E \mid E * E \mid id$
For the string `id + id * id`, there are two parse trees, making it ambiguous. Ambiguity is generally undesirable in compiler design because it leads to multiple interpretations of the same code.

## 5. Chomsky Normal Form (CNF)
A CFG is in Chomsky Normal Form if all production rules are of the form:
1. $A \rightarrow BC$ (where $B$ and $C$ are non-terminals)
2. $A \rightarrow a$ (where $a$ is a terminal)
3. $S \rightarrow \epsilon$ (only if $\epsilon$ is in the language, and $S$ does not appear on the right side of any rule).

Converting to CNF involves:
1. Eliminating $\epsilon$-productions.
2. Eliminating unit productions.
3. Eliminating useless symbols.
4. Restructuring remaining rules.

## 6. Push Down Automata (PDA)
A Push Down Automaton is a finite automaton equipped with a stack (LIFO memory). This allows it to recognize Context-Free Languages.

> [!NOTE] Definition
> **Push Down Automata (PDA)**: A 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$
> - $Q$: Finite set of states
> - $\Sigma$: Input alphabet
> - $\Gamma$: Stack alphabet
> - $\delta$: Transition function $Q \times (\Sigma \cup \{\epsilon\}) \times \Gamma \rightarrow 2^{Q \times \Gamma^*}$
> - $q_0$: Start state
> - $Z_0$: Initial stack symbol
> - $F$: Set of final states

A PDA can accept a string in two ways:
1. Acceptance by final state.
2. Acceptance by empty stack.

## 7. Equivalence of CFL and PDA
A language is context-free if and only if there is a Push Down Automaton that recognizes it. 
- For every CFG, we can construct a PDA that accepts the same language.
- For every PDA, we can construct a CFG that generates the same language.

## 📋 8. Properties of Context Free Languages
CFLs are closed under:
- Union
- Concatenation
- Kleene Star
- Reversal
- Homomorphism

CFLs are **NOT** closed under:
- Intersection
- Complementation

However, the intersection of a CFL and a Regular Language is always a CFL.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not assume CFLs are closed under intersection or complementation. This is a very common trick question in multiple-choice exams.

> [!TIP]
> - Ambiguity cannot be detected by a general algorithm (it is an undecidable problem).
> - Every regular language is a context-free language, but not vice versa.
> - A stack is the fundamental difference between an FA and a PDA.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - CFG: $G = (V, \Sigma, R, S)$
> - CNF: $A \rightarrow BC$ or $A \rightarrow a$
> - PDA: $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$
> - Closure Properties: CFLs closed under $\cup, \cdot, *$. Not closed under $\cap, '$.

## ✏️ Practice Problems
1. **Problem**: Construct a PDA for the language $L = \{a^n b^n \mid n \ge 1\}$.
   *Sketch*: Push 'a' onto the stack. When 'b' is read, pop 'a'. Accept if stack is empty after input is consumed.
2. **Problem**: Convert the grammar $S \rightarrow aSb \mid \epsilon$ to Chomsky Normal Form.
   *Sketch*: Remove $\epsilon$-production $S \rightarrow \epsilon$, yielding $S \rightarrow aSb \mid ab$. Then replace terminals with non-terminals to match $A \rightarrow BC$ and $A \rightarrow a$.
3. **Problem**: Show that $L = \{a^n b^n c^n \mid n \ge 1\}$ is not context-free.
   *Sketch*: Use the Pumping Lemma for Context-Free Languages.
</Section 8.2: Context Free Language (AEiE0802)>
