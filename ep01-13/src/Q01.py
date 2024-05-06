from automata.fa.dfa import DFA

dfa01 = DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}, 
        input_symbols={'l','n','b','/','#'}, 
        transitions={
            'q0': {'l': 'q3', 'n': 'q3', 'b': 'q3', '/': 'q1', '#': 'q3', 'l': 'q3'},
            'q1': {'l': 'q3', 'n': 'q3', 'b': 'q3', '/': 'q3', '#': 'q2'},
            'q2': {'l': 'q2', 'n': 'q2', 'b': 'q2', '/': 'q3', '#': 'q4'},
            'q3': {'l': 'q3', 'n': 'q3', 'b': 'q3', '/': 'q3', '#': 'q3'},
            'q4': {'l': 'q3', 'n': 'q3', 'b': 'q3', '/': 'q5', '#': 'q3'},
            'q5': {'l': 'q3', 'n': 'q3', 'b': 'q3', '/': 'q3', '#': 'q3'}          
        }, 
        initial_state='q0', 
        final_states={'q5'}
)

    
