import html


def triv():

    trivia= {
            "category": "Entertainment: Film",
            "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
                ]
            }


    question = trivia["question"]
    correct = html.unescape(trivia["correct_answer"])
    incorrect1 = html.unescape(trivia["incorrect_answers"][0])
    incorrect2 = html.unescape(trivia["incorrect_answers"][1])
    incorrect3 = html.unescape(trivia["incorrect_answers"][2])

    print(question)
    print(f"A. {correct}")
    print(f"B. {incorrect1}")
    print(f"C. {incorrect2}")
    print(f"D. {incorrect3}")

    user_answer = input("\nAnswer: ").lower

    if user_answer == "a":
        print("Correct!")
    else:
        print("Incorrect, try next time!")

triv()