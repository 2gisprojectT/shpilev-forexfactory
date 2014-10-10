__author__ = 'PunkBASSter'

from lion import cLion
from unittest import TestCase
import unittest

class LionTest(TestCase):
    def test_init(self):
        lion1 = cLion('Hungry')
        self.assertEqual('Hungry', lion1.state, 'Init Error State must be Hungry')
        lion2 = cLion('Fed')
        self.assertEqual('Fed', lion2.state, 'Init Error State must be Fed')

    def test_ante_hng(self):
        lion = cLion('Hungry')
        self.assertEqual('Eat', lion.execTransition('Antelope'), 'Antelope+Hungry WRONG Output')
        self.assertEqual('Fed', lion.state, 'Antelope+Hungry WRONG State')

    def test_ante_fed(self):
        lion = cLion('Fed')
        self.assertEqual('Sleep', lion.execTransition('Antelope'), 'Antelope+Fed WRONG Output')
        self.assertEqual('Hungry', lion.state, 'Antelope+Fed WRONG State')

    def test_hunt_hng(self):
        lion = cLion('Hungry')
        self.assertEqual('Escape', lion.execTransition('Hunter'), 'Hunter+Hungry WRONG Output')
        self.assertEqual('Hungry', lion.state, 'Hunter+Hungry WRONG State')

    def test_hunt_fed(self):
        lion = cLion('Fed')
        self.assertEqual('Escape', lion.execTransition('Hunter'), 'Hunter+Fed WRONG Output')
        self.assertEqual('Hungry', lion.state, 'Hunter+Fed WRONG State')

    def test_tree_hng(self):
        lion = cLion('Hungry')
        self.assertEqual('Sleep', lion.execTransition('Tree'), 'Tree+Hungry WRONG Output')
        self.assertEqual('Hungry', lion.state, 'Tree+Hungry WRONG State')

    def test_tree_fed(self):
        lion = cLion('Fed')
        self.assertEqual('Look', lion.execTransition('Tree'), 'Tree+Fed WRONG Output')
        self.assertEqual('Hungry', lion.state, 'Tree+Fed WRONG State')

    def test_tree_negative_state(self):
        lion = cLion('Tired')
        self.assertEqual('ERR: Undefined Input and CurrentState combination', lion.execTransition('Tree'), 'Tree+Tired WRONG Output')

    def test_tree_negative_input(self):
        lion = cLion('Fed')
        self.assertEqual('ERR: Undefined Input and CurrentState combination', lion.execTransition('Zebra'), 'Zebra+Fed WRONG Output')

if __name__ == '__main__':
    unittest.main()