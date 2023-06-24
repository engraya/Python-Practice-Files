from urllib import response

class TravelTracker:
    """ a survey to shoe how many countries visited"""

    def __init__(self, question):
        """store a question and go prepare to store the response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses inserted"""
        print("Survey results: ")
        for response in self.responses:
            print(f"{response}")
