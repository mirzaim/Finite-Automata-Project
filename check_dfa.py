# check_dfa.py

from finite_state_machine import DFA

def load_dfa_from_file(filename):
    """Load a DFA from a file and return a DFA object."""
    with open(filename, encoding='utf-8') as f:
        lines = f.read().splitlines()

    dfa = DFA()
    try:
        # Initialize DFA components from the file data
        dfa.alphabet = set(lines.pop(0).split())
        dfa.states = set(lines.pop(0).split())
        dfa.initial_state = lines.pop(0)
        dfa.final_states = set(lines.pop(0).split())

        # Read the transition functions
        for line in lines:
            data = line.split()
            if len(data) != 3:
                raise ValueError(f"Invalid transition format: {line}")
            state_from, symbol, state_to = data
            if symbol not in dfa.alphabet:
                raise ValueError(f"Symbol '{symbol}' not in DFA alphabet.")
            dfa.transition_function[(state_from, symbol)] = state_to
    except IndexError:
        raise ValueError("Invalid DFA definition in the file.")

    return dfa

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python check_dfa.py <DFA_input_file>")
        sys.exit(1)

    dfa_input_file = sys.argv[1]
    try:
        dfa = load_dfa_from_file(dfa_input_file)
    except Exception as e:
        print(f"Error loading DFA: {e}")
        sys.exit(1)

    # Display DFA information
    print("DFA loaded successfully.")
    print(f"Alphabet: {dfa.alphabet}")
    print(f"States: {dfa.states}")
    print(f"Initial State: {dfa.initial_state}")
    print(f"Final States: {dfa.final_states}")
    print("Transition Function:")
    for (state, symbol), next_state in dfa.transition_function.items():
        print(f"  δ({state}, {symbol}) -> {next_state}")

    # Get input string from the user
    input_string = input('Enter input string: ')

    # Validate input string
    for char in input_string:
        if char not in dfa.alphabet:
            print(f"Invalid input symbol '{char}' not in DFA's alphabet.")
            sys.exit(1)

    # Check if the string is accepted by the DFA
    if dfa.check(input_string):
        print(f'The string "{input_string}" is accepted by the DFA.')
    else:
        print(f'The string "{input_string}" is rejected by the DFA.')

if __name__ == '__main__':
    main()
