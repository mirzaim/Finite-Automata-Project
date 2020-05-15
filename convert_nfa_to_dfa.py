# convert_nfa_to_dfa.py

from finite_state_machine import NFA


def load_nfa_from_file(filename):
    """Load an NFA from a file and return an NFA object."""
    with open(filename, encoding='utf-8') as f:
        lines = f.read().splitlines()

    nfa = NFA()
    try:
        # Initialize NFA components from the file data
        nfa.addAlphabet(set(lines.pop(0).split()))
        nfa.addStates(set(lines.pop(0).split()))
        nfa.initial_state = lines.pop(0)
        nfa.addFinalStates(set(lines.pop(0).split()))

        # Read the transition functions
        for line in lines:
            data = line.split()
            if len(data) != 3:
                raise ValueError(f"Invalid transition format: {line}")
            state_from, symbol, state_to = data
            nfa.addTransition(state_from, symbol, state_to)
    except IndexError:
        raise ValueError("Invalid NFA definition in the file.")

    return nfa


def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python convert_nfa_to_dfa.py <NFA_input_file>")
        sys.exit(1)

    nfa_input_file = sys.argv[1]
    try:
        nfa = load_nfa_from_file(nfa_input_file)
    except Exception as e:
        print(f"Error loading NFA: {e}")
        sys.exit(1)

    # Convert NFA to DFA
    dfa = nfa.convertToDFA()

    # Write DFA to output file
    dfa_output_file = 'DFA_Output.txt'
    with open(dfa_output_file, 'w', encoding='utf-8') as f:
        f.write(str(dfa))

    print(f"DFA has been successfully written to {dfa_output_file}")


if __name__ == '__main__':
    main()
