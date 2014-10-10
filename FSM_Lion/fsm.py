__author__ = 'PunkBASSter'

#+-----------------------------------------------------------+
#| General-purpose Finite State Machine class based on lists |
#+-----------------------------------------------------------+
class cFsm:
    def __init__(self, ds):
        self.state = ds
        self.L = list()

    def addTransition(self, inp, cstate, nstate, out):
        self.L.append([inp, cstate, nstate, out])

    def setState(self, s):
        self.state = s

    def getState(self):
        return self.state

    def getList(self):
        return self.L

    def execTransition(self, inp):
        n=0
        while n < len(self.L):
            if inp == self.L[n][0]:
                if self.state == self.L[n][1]:
                    self.state = self.L[n][2]
                    return self.L[n][3]
            n += 1
        return 'ERR: Undefined Input and CurrentState combination'
#+-----------------------------------------------------------+