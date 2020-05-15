from graph import Graph


class DFA:

    def __init__(self):
        self.alphabet = set()
        self.states = set()
        self.initial_state = None
        self.final_states = set()
        # transition_function is dictionary that map (State, Alphabet) to (State).
        self.transition_function = {}

    def check(self, str):
        """Check that str String is accepted or not."""
        # Start from initial state.
        current_state = self.initial_state

        for char in str:
            # iterate on characters of string,
            # Change current state with transition funcion.
            current_state = self.transition_function[(current_state, char)]

        # Check that is reached state in final states.
        return current_state in self.final_states

    def __str__(self):
        """Retuen String that define DFA in specific format."""
        str = ''
        str += (' '.join(self.alphabet) + '\n')
        str += (' '.join(self.states) + '\n')
        str += (self.initial_state + '\n')
        str += (' '.join(self.final_states) + '\n')

        for (x, y) in self.transition_function:
            str += (f'{x} {y} {self.transition_function[(x,y)]}' + '\n')

        return str


class NFA:

    def __init__(self):
        self.alphabet = ['λ']
        self.states = []
        self.initial_state = None
        self.final_states = []
        # In NFA transition is handle by Graph()
        self.graph = Graph()

    def addAlphabet(self, alphabet):
        self.alphabet.extend(alphabet)

    def addStates(self, states):
        self.states.extend(states)
        self.graph.addNodes(states)

    def addFinalStates(self, finalStates):
        self.final_states.extend(finalStates)

    def addTransition(self, begin, label, end):
        self.graph.addEdge(begin, label, end)

    def delta(self, node, alphabet):
        """Transiton funcion with `node` as starting point and `alphabet` is current input.
        Return a set of nodes.
        It's not use lambda_moves.
        """
        nextNodeSet = set()
        for state in NFA.decodeState(node):
            nextNodeSet.update(self.graph.oneDepthTravel(state, alphabet))
        return nextNodeSet

    def lambda_moves(self, node):
        """Return a set of nodes that reachable from `node` with lambda moves."""
        nextNodeSet = set()
        for state in NFA.decodeState(node):
            nextNodeSet.update(self.graph.travelOnLabel(state, 'λ'))
        return nextNodeSet

    def delta_star(self, node, alphabet):
        """It's combination of delta and lambda_moves.
        Return all nodes that reachable from `node` with input `alphabet`.
        It's use lambda moves."""
        nextNodeSet = self.delta(node, alphabet)

        temp = set()
        for x in nextNodeSet:
            temp.update(self.lambda_moves(x))
        nextNodeSet.update(temp)
        return nextNodeSet

    def convertToDFA(self):
        """Conver nfa to dfa.
        return DFA object."""
        dfa = DFA()

        # copy all nfa alphabet to dfa exept λ.
        dfa.alphabet = self.alphabet.copy()
        if 'λ' in dfa.alphabet:
            dfa.alphabet.remove('λ')

        # add nfa's initial state and all state that reachable with λ moves from initial state,
        # as initial state of dfa
        dfa.initial_state = NFA.encodeState(self.lambda_moves(
            self.initial_state).union({self.initial_state}))
        dfa.states.add(dfa.initial_state)
        # if there is final state between initial-state's set of dfa make it final state
        if len(set(NFA.decodeState(dfa.initial_state)).intersection(self.final_states)) > 0:
            dfa.final_states.add(dfa.initial_state)
        
        temp = [dfa.initial_state]
        checked_states = []
        while temp:
            node = temp.pop(0)
            if node not in checked_states:
                for a in dfa.alphabet:
                    # nextNode is all reachable nodes in nfa with `a` as symbol
                    nextNodeSet = self.delta_star(node, a)
                    if len(nextNodeSet) == 0:
                        # if there is no reachable node then poin `nextNodeSet` to Nil
                        nextNodeSet = 'NIL'
                        NFA.addNilNodeToDFA(dfa)
                    else:
                        # if there is final node between reachable nodes make it final node for dfa
                        if len(set(self.final_states).intersection(nextNodeSet)) > 0:
                            dfa.final_states.add(
                                NFA.encodeState(nextNodeSet))
                        nextNodeSet = NFA.encodeState(nextNodeSet)
                    
                    # add `nextNodeSet` to dfa
                    if nextNodeSet not in dfa.states:
                        dfa.states.add(nextNodeSet)
                    # define transition for `nextNodeSet`
                    dfa.transition_function[(node, a)] = nextNodeSet
                    if nextNodeSet != 'NIL':
                        temp.append(nextNodeSet)
                checked_states.append(node)

        return dfa

    @classmethod
    def addNilNodeToDFA(cls, dfa):
        """Add Nil node to dfa"""
        if 'NIL' not in dfa.states:
            dfa.states.add('NIL')
            for a in dfa.alphabet:
                dfa.transition_function[('NIL', a)] = 'NIL'

    @classmethod
    def decodeState(cls, state):
        if '.' in state:
            return state.split('.')
        return (state,)

    @classmethod
    def encodeState(cls, states):
        return '.'.join(sorted(states))
