# Finite Automata Project

This project implements finite automata concepts in Python, including classes for Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA), along with functionality to convert an NFA to an equivalent DFA. It also provides scripts to check if a given string is accepted by a DFA and to perform the NFA to DFA conversion using input files.

## Project Structure

```
project/
├── check_dfa.py
├── convert_nfa_to_dfa.py
├── finite_state_machine.py
├── graph.py
├── DFA_Input_1.txt
└── NFA_Input.txt
```

- **check_dfa.py**: Script to check if a given string is accepted by a DFA.
- **convert_nfa_to_dfa.py**: Script to convert an NFA to an equivalent DFA.
- **finite_state_machine.py**: Module containing the `DFA` and `NFA` classes.
- **graph.py**: Module containing the `Graph`, `Node`, and `Edge` classes.
- **DFA_Input_1.txt**: Sample input file defining a DFA.
- **NFA_Input.txt**: Sample input file defining an NFA.

## Usage

### Checking if a String is Accepted by a DFA

1. **Prepare the DFA Input File**: Define your DFA in a text file (e.g., `DFA_Input_1.txt`) following the specified format (see [DFA Input File Format](#dfa-input-file-format)).

2. **Run the Script**:

   ```bash
   python check_dfa.py DFA_Input_1.txt
   ```

3. **Enter the Input String**: When prompted, enter the string you want to check.

4. **View the Result**: The script will output whether the string is accepted or rejected by the DFA.

### Converting an NFA to a DFA

1. **Prepare the NFA Input File**: Define your NFA in a text file (e.g., `NFA_Input.txt`) following the specified format (see [NFA Input File Format](#nfa-input-file-format)).

2. **Run the Script**:

   ```bash
   python convert_nfa_to_dfa.py NFA_Input.txt
   ```

3. **Output**: The script will convert the NFA to a DFA and write the result to `DFA_Output.txt`.

## Input File Formats

### DFA Input File Format

The DFA input file should have the following structure:

```
<alphabet symbols separated by spaces>
<states separated by spaces>
<initial state>
<final states separated by spaces>
<transition function entries>
```

- **Alphabet Symbols**: List all symbols in the DFA's alphabet.
- **States**: List all states in the DFA.
- **Initial State**: Specify the initial state.
- **Final States**: List all accepting (final) states.
- **Transition Function Entries**: Each entry defines a transition in the format:
  ```
  <current_state> <input_symbol> <next_state>
  ```

### NFA Input File Format

The NFA input file should have the following structure:

```
<alphabet symbols separated by spaces>
<states separated by spaces>
<initial state>
<final states separated by spaces>
<transition function entries>
```

- **Alphabet Symbols**: List all symbols in the NFA's alphabet (include 'λ' for lambda transitions if any).
- **States**: List all states in the NFA.
- **Initial State**: Specify the initial state.
- **Final States**: List all accepting (final) states.
- **Transition Function Entries**: Each entry defines a transition in the format:
  ```
  <current_state> <input_symbol> <next_state>
  ```

## Examples

### Example DFA Input

**File**: `DFA_Input_1.txt`

```
a b
Q0 Q1 Q2
Q0
Q1
Q0 a Q1
Q0 b Q1
Q1 a Q2
Q1 b Q2
Q2 a Q2
Q2 b Q2
```

### Example NFA Input

**File**: `NFA_Input.txt`

```
0 1
A B C
A
C
A 1 A
A 0 B
A λ B
A 0 C
B 1 B
B λ C
C 0 C
C 1 C
```

## Modules

### graph.py

Contains the following classes:

- **Graph**: Represents a directed graph, used to model the transitions in NFAs and DFAs.
- **Node**: Represents a state in the automaton.
- **Edge**: Represents a transition between states with a specific label (input symbol).

### finite_state_machine.py

Contains the following classes:

- **DFA**: Represents a Deterministic Finite Automaton.

  **Methods**:
  - `check(string)`: Checks if the given string is accepted by the DFA.
  - `__str__()`: Returns a string representation of the DFA.

- **NFA**: Represents a Nondeterministic Finite Automaton.

  **Methods**:
  - `addAlphabet(alphabet)`: Adds symbols to the NFA's alphabet.
  - `addStates(states)`: Adds states to the NFA.
  - `addFinalStates(final_states)`: Defines the NFA's final states.
  - `addTransition(begin, label, end)`: Adds a transition to the NFA.
  - `lambda_closure(states)`: Computes the lambda closure of a set of states.
  - `delta(states, symbol)`: Computes the set of states reachable from the given states on the given input symbol.
  - `convertToDFA()`: Converts the NFA to an equivalent DFA.
