import unittest
from script_states_profile import full_state_profile

class StateTestCase(unittest.TestCase):
    """test for state function """

    def test_state_capital(self):
        """Do states names and capital like : 'Yobe Damaturu' exist?"""
        complete_formatted_name = full_state_profile('JIGAWA', 'DUTSE', 'NORTH')
        self.assertEqual(complete_formatted_name, 'JIGAWA DUTSE NORTH')

if __name__ == '__main__':
    unittest.main()