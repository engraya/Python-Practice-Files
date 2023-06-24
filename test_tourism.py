from http.client import responses
import unittest
from venv import create
from tourism import TravelTracker

class TestTravelTracker(unittest.TestCase):
    """Test for the traveltracker"""

    def test_store_single_response(self):
        question = "Which country did you visit during the summer holiday?"
        my_survey = TravelTracker(question)
        my_survey.store_response('Nigeria')
        self.assertIn('Nigeria', my_survey.responses)


    # def test_store_four_responses(self):
    #     """test that four responses are stored in ad records"""
    #     question = "which country did you visited during  your summer holiday?"
    #     my_survey = TravelTracker(question)
    #     responses = ['nigeria', 'niger', 'chad', 'gabon']
    #     for response in responses:
    #         my_survey.store_response(response)

    #         self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()


# class TestTravelTracker(unittest.TestCase):
#     """Test for the traveltracker"""

#     def setUp(self):
#         """create an isntance of survey and use in all methods"""
#         question = "which country did you visit during the summer holiday?"
#         self.my_survey = TravelTracker(question)
#         self.responses = ['italy', 'usa', 'lebanon', 'france']


#     def test_store_single_response(self):
#         question = "Which country did you visit during the summer holiday?"
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)
   

#     def test_store_four_responses(self):
#         """test that four responses are stored in ad records"""
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response, self.my_survey.responses)


# if __name__ == '__main__':
#     unittest.main()