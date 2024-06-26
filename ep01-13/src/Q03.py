from automata.fa.nfa import NFA

nfa01 = NFA(
        states={'q0','q1','q2', 'q3', 'q4'}, 
        input_symbols={'1','2', 'S','P','B'}, 
        transitions={
            'q0': {'1': {'q1'},'2':{'q2'}, 'S':{'q0'}, 'P': {'q0'}, 'B':{'q0'}},
            'q1': {'1':{'q2'},'2':{'q3'}, 'S':{'q1'}, 'P': {'q1'}, 'B':{'q1'}},
            'q2': {'1':{'q3'}, 'S':{'q2'}, 'P': {'q2'}, 'B':{'q2'}},
            'q3': {'S':{'q4'}, 'P': {'q4'}, 'B':{'q4'}}
        }, 
        initial_state='q0', 
        final_states={'q4'}
)
    
