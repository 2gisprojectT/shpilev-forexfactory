__author__ = 'PunkBASSter'
from fsm import cFsm

#+------------------------------------+
#| Lion FSM Class (Derived from cFsm) |
#+------------------------------------+
class cLion(cFsm):
    def __init__(self, ds):
        self.state = ds
        self.L = list()
        self.setMatrix()

    def setMatrix(self):
        #Assigning FSM's transition matrix.
        #addTransition(Input, CurrentState, NextState, Output)
        self.addTransition('Antelope', 'Hungry', 'Fed', 'Eat')
        self.addTransition('Antelope', 'Fed', 'Hungry', 'Sleep')
        self.addTransition('Hunter', 'Hungry', 'Hungry', 'Escape')
        self.addTransition('Hunter', 'Fed', 'Hungry', 'Escape')
        self.addTransition('Tree', 'Hungry', 'Hungry', 'Sleep')
        self.addTransition('Tree', 'Fed', 'Hungry', 'Look')
#+------------------------------------+

lion = cLion('Hungry')

print(lion.execTransition('Tree'))
print(lion.execTransition('Antelope'))
print(lion.execTransition('Tree'))
print(lion.execTransition('Hunter'))
print(lion.execTransition('Tree'))
print(lion.execTransition('Antelope'))
print(lion.execTransition('Zebra'))
print(lion.execTransition('Antelope'))
print(lion.execTransition('Antelope'))