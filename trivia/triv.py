import requests
import random

URL= "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium"

def main():
    data= requests.get(URL).json()
    for i in data["results"]:
        print("\033[36m\nQuestion:", i["question"], "\033[0m\n")
        
        # Combine correct and incorrect answers into one list
        answers = i["incorrect_answers"]
        correct_answer = i["correct_answer"]
        answers.append(correct_answer)
        
        # Randomize the order of answers
        random.shuffle(answers)
        
        # Print answers in A, B, C, D format
        options = ['A', 'B', 'C', 'D']
        for j in range(len(answers)):
            print(f"{options[j]}. {answers[j]}")
        
        # Ask for user input
        user_answer = input("\nPlease enter your answer (A, B, C, or D): ")
        
        # Check if the answer is correct
        if answers[options.index(user_answer.upper())] == correct_answer:
            print("\033[32mCorrect!\033[0m")
        else:
            print("\033[31mWrong! The correct answer was:", correct_answer, "\033[0m")
        
        print()

if __name__ == "__main__":
    main()