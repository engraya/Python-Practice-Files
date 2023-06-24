import unittest
from script_states_profile import full_state_profile

class StateTestCase(unittest.TestCase):
    """test for state function """

    def test_state_capital(self):
        """Do states names and capital like : 'Yobe Damaturu' exist?"""
        complete_formatted_name = full_state_profile('JIGAWA', 'DUTSE')
        self.assertEqual(complete_formatted_name, 'JIGAWA DUTSE')

if __name__ == '__main__':
    unittest.main()


def test_state_capital_region(self):
            """Do states names and capital like : 'Yobe Damaturu' exist?"""
            complete_formatted_name = full_state_profile('LAGOS', 'IKEJA', 'SOUTH')
            self.assertEqual(complete_formatted_name, 'lagos ikeja south')

if __name__ == '__main__':
    unittest.main()
