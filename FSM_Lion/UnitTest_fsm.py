__author__ = 'PunkBASSter'

from fsm import cFsm
from unittest import TestCase
import unittest

class FsmTest(TestCase):
    def test_init(self):
        fsm = cFsm(1)
        self.assertEqual(1, fsm.state, 'Init Error State must be 1')

    def test_add_trans_get_list(self): #test of 2 methods: addTransition(...) and getList()
        fsm = cFsm(1)
        lst = list()
        lst = [0, 1, 2, 3]
        fsm.addTransition(0, 1, 2, 3)
        self.assertEqual(lst, fsm.getList()[0], 'addTransition Error')

    def test_set_state(self):
        fsm = cFsm(1)
        fsm.setState(2)
        self.assertEqual(2, fsm.state, 'setState() error')

    def test_get_state(self):
        fsm = cFsm(0)
        self.assertEqual(0, fsm.getState(), 'getState error')

    def test_exec_transition(self):
        fsm = cFsm(1)
        fsm.addTransition(0, 1, 2, 3)
        fsm.addTransition(3, 2, 1, 0)
        self.assertEqual(3, fsm.execTransition(0), 'execTransition() result must be 3')
        self.assertEqual(2, fsm.state, 'After execTransition() state must be 2')
        self.assertEqual(0, fsm.execTransition(3), 'execTransition() result must be 0')
        self.assertEqual(1, fsm.state, 'After execTransition() state must be 1')
        self.assertEqual('ERR: Undefined Input and CurrentState combination', fsm.execTransition(3), 'False positive result with 3,0')

if __name__ == '__main__':
    unittest.main()