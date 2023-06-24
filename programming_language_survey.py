from traceback import print_tb
from urllib import response
from language_class import ProgrammingLanguage

#1. Define a question and make a survey from the imported class
question = "Which programming language were u able to learn during the 2020 COVID-19 pandemic?  "
my_survey = ProgrammingLanguage(question)


#2. Show the question and prepare to store response to the question
my_survey.show_question()
print("Enter 'q' any to quit the program \n")
while True:
    response = input("Programming language: ")
    if response == 'q':
        break
    my_survey.store_response(response)


#3. Show the result of the survey
print("\nYou have used much of your time effectively during the pandemic.")
print("Thank you for participating in this survey, hope you enjoy it!")
my_survey.show_results()
