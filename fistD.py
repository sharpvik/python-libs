#
# ================================         BBBBBB      YY    YYY           MMMM    MMMM    RRRRRR              VV      VVV    RRRRRR
# =             THE              =         BBB   BB     YY  YYY            MMMMM  MMMMM    RRR   RR             VV    VVV     RRR   RR
# ===>       Fist class       <===         BBBBBB        YYYYY             MMM  MM  MMM    RRRRRR                VV  VVV      RRRRRR
# =         (10.05.2018)         =         BBB   BBB      YYY              MMM      MMM    RRR  R                 VVVVV       RRR  R
# ================================         BBBBBBBB       YYY              MMM      MMM    RRR   RR                VVV        RRR   RR
#
# My github --> https://www.github.com/sharpvik <--
#



class Fist:                                             # final state machine with binary-based input;
    def __init__(self):
        self.states = dict()
        self.state_current = int()
        self.state_final = int()

    def state_add(self, name, zero, one):               # name(int / str) -- name of current state;
                                                        # zero(int / str) and one(int / str) -- names of two other states;
                                                        # if your current state is name(int / str) and input is 0 -- current state changes to zero(int / str);
                                                        # if input is 1 -- current state changes to one(int / str);
                                                        # --> function returns name;
        if name in self.states:
            print("WARNING: You are changing parameters of an existing state!")
        self.states.update( {name : [zero, one]} )
        return name
    
    def state_init_set(self, name):                     # name(int / str) -- name of state you want to set as initial state;
                                                        # --> function returns name;
        self.state_current = name
        return name

    def state_final_set(self, name):                    # name(int / str) -- name of state you want to set as final state for validation;
                                                        # --> function returns name;
        self.state_final = name
        return name

    def validate(self, string):                         # string(str) -- string that consists of 0s and 1s (format: '010001');
                                                        # --> function retruns True if current state after all is equal to final state, otherwise returns False;
        for each in string:
            state = self.state_current
            each = int(each)
            self.state_current = self.states[state][each]  

        if self.state_current == self.state_final:
            return True
        else:
            return False

    def states_return(self):                            # --> funciton returns full dict of states;
        return self.states

    def in_states(self, name):                          # --> function returns True if state called name exists in states dict, otherwise returns False; 
        return name in self.states
