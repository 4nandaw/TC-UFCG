from automata.fa.nfa import NFA

nfa02 = NFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'},
        input_symbols={'L', 'N', 'S', '@', 'P'}, 
        transitions={
            'q0': {'': {'q1'}},
            'q1': {'L': {'q1', 'q2'}},
            'q2': {'S': {'q2'}, 'N': {'q2'}, '@': {'q3'}},
            'q3': {'L': {'q3', 'q4'}, 'N': {'q3', 'q4'}},
            'q4': {'P': {'q5'}},
            'q5': {'L': {'q6'}},
            'q6': {'L': {'q7'}},
            'q7': {'L': {'q8'}},
            'q8': {'P': {'q9'}},
            'q9': {'L': {'q10'}},
            'q10': {'L': {'q11'}},
            'q11': {'' : {}},
        }, 
        initial_state='q0', 
        final_states={'q11'}
)
