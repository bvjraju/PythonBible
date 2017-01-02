from random import choice
questions = ["what is your name","why is john snow white","where are the dinosours"]
question = choice(questions)
answer = input(question).lower()

while answer !="just because":
    answer = input("why? :").strip().lower()


print("Oh...okay")
    
