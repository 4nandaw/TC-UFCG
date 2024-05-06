from automata.tm.dtm import DTM

dtm1 = DTM(
    states={'start', 'done', 'convertA', 'convertB'},
    input_symbols={'a', 'b', 'A', 'B'},
    tape_symbols={'a', 'b', 'B', 'A', '.'},
    transitions={
        'start': {
            'A': ('convertA', 'a', 'R'),
            'B': ('convertB', 'b', 'R'),
            'a': ('start', 'a', 'R'),
            'b': ('start', 'b', 'R'),
            '.': ('done', '.', 'R')
        },
        'convertA': {
            'A': ('convertA', 'a', 'R'),
            'B': ('convertB', 'b', 'R'),
            'a': ('convertA', 'a', 'R'),
            'b': ('convertA', 'b', 'R'),
            '.': ('done', '.', 'R')
        },
        'convertB': {
            'A': ('convertA', 'a', 'R'),
            'B': ('convertB', 'b', 'R'),
            'a': ('convertB', 'a', 'R'),
            'b': ('convertB', 'b', 'R'),
            '.': ('done', '.', 'R')
        }
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)
    
