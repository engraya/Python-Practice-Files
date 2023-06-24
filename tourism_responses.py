from urllib import response
from tourism import TravelTracker

#define a question, and make some surveys.
question = "Which country did you visit during the summer holiday?"
my_survey = TravelTracker(question)


#show the questions and store response to the question.
my_survey.show_question()
print("Enter end to quit the program. \n")
while True:
    response = input("Country:  ")
    if response == 'end':
        break
    my_survey.store_response(response)

#show the survey results
print("\n Thank you for participating in this random survey, your responses are being handled by us, see you later!!!")
my_survey.show_results()