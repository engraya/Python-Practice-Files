import unittest
from language_class import ProgrammingLanguage


class TestProgrammingLanguage(unittest.TestCase):
    """TEST FOR THE CLASS PROGRAMMING LANGUAGE"""


    def setUp(self):
        """CREATE A UNIVERSAL SURVEY TEST FOR ALL RESPONSES"""
        question = "Which programming language were u able to learn during the 2020 COVID-19 pandemic?  "
        my_survey = ProgrammingLanguage(question)
        responses = ['python', 'objective c', 'ruby']

    def test_store_single_response(self):
        """TEST THAT SINGLE RESPONSE IS STORED PROPERLY"""
        question = "Which programming language were u able to learn during the 2020 COVID-19 pandemic?  "
        my_survey = ProgrammingLanguage(question)
        my_survey.store_response('Python')
        self.assertIn('Python', my_survey.responses)

        
    def test_store_three_responses(self):
        """TEST FOR THREE INDIVIDUAL RESPONSES AND STORED THEM AS ACQUIRED RESPONSES PROPERLY"""
        question = "Which programming language were u able to learn during the 2020 COVID-19 pandemic?  "
        my_survey = ProgrammingLanguage(question)
        responses = ['python', 'objective c', 'ruby']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()


                    ##### SETUP METHOD#####
class TestProgrammingLanguage(unittest.TestCase):
    """TEST FOR THE CLASS PROGRAMMING LANGUAGE"""


    def setUp(self):
        """CREATE A UNIVERSAL SURVEY TEST FOR ALL RESPONSES"""
        question = "Which programming language were u able to learn during the 2020 COVID-19 pandemic?  "
        self.my_survey = ProgrammingLanguage(question)
        self.responses = ['python', 'objective c', 'ruby']

    def test_store_single_response(self):
        """TEST THAT SINGLE RESPONSE IS STORED PROPERLY"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

        
    def test_store_three_responses(self):
        """TEST FOR THREE INDIVIDUAL RESPONSES AND STORED THEM AS ACQUIRED RESPONSES PROPERLY"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
