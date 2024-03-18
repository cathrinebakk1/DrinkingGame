import random

# Define the questions and answers with all provided questions
questions_answers = {
    "In a website browser address bar, what does “www” stand for?": "World Wide Web",
    "In what country did the first Starbucks open outside of North America?": "Japan",
    "Who was the first televised President?": ["Franklin D. Roosevelt", "Roosevelt"],
    "Who painted the Mona Lisa?": "Leonardo Da Vinci",
    "Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "What does SPF in sunscreen stand for?": "Sun Protection Factor",
    "When did Facebook first launch?": "2004",
    "Who won the 2010 World Cup?": "Spain",
    "Who provided the voice of Groot in the Guardians of the Galaxy movies?": "Vin Diesel",
    "In which city is Studio 54 located?": "New York",
    "How many Harry Potter books are there?": "7",
    "What day is known as Star Wars Day?": "May 4th",
    "What singer holds the most Grammy nominations?": "Beyonce",
    "How many years have passed between the release of Avatar and its sequel, Avatar: The Way of Water?": "13",
    "Which country has won the most medals in the winter olympics?": "Norway",
    "What is the signature food dish served at Wimbledon?": "Strawberries and cream",
    "What occasion corresponds to the longest day of the year?": "Summer solstice",
    "Which country is the largest in the world?": "Russia",
    "According to Guinness World Records, what's the best-selling book of all time?": "The Bible",
    "What is the only food that can never go bad?": "Honey",
    "Who is considered the 'Father of Relativity?'": "Albert Einstein",
    "Actor Steve Carell plays what memorable character in the popular TV series 'The Office?'": "Michael Scott",
    "What name is singer-actor Stefani Germanotta better known by?": "Lady Gaga",
    "What 1994 Quentin Tarantino movie stars John Travolta and Samuel L. Jackson as hitmen?": "Pulp Fiction",
    "Which soft drink once contained cocaine as one of its original ingredients?": ["Coca-Cola", "Coca Cola"],
    "What country uses approximately four billion miles of toilet paper each year?": "China",
    "The Da Vinci Code opens with a murder in which famous museum?": "The Louvre",
    "Which US president was a licensed bartender?": "Abraham Lincoln",
    "When was the first iPod released?": "2001",
    "Which Italian town is the setting for Shakespeare’s Romeo and Juliet?": "Verona",
    "Which travels faster: Sound or light?": "Light",
    "What is the largest bone in the human body?": "Femur",
    "Which singer’s real name is Robyn Fenty?": "Rihanna",
    "Who was the first Disney princess?": "Snow White",
    "What species of fish is Nemo?": "Clown Fish",
    "Who was the highest-paid athlete in 2022?": ["Lionel Messi", "Messi"],
    "What is the meaning of 'fn' on your computer keyboard?": "Function",
    "What is the longest river in the world?": ["The Nile", "Nile"],
    "Which desert is the largest in the world?": ["The Sahara Desert", "Sahara"],
    "What is the capital city of Australia?": "Canberra",
    "In which year did the Titanic sink?": "1912",
    "Who wrote the Declaration of Independence?": "Thomas Jefferson",
    "Which famous leader was assassinated by his friend Brutus?": "Julius Caesar",
    "Who was the first human to journey into space?": "Yuri Gagarin",
    "Which country won the first ever FIFA World Cup in 1930?": "Uruguay",
    "What is the term used when a golfer scores one under par on a hole?": "Birdie",
    "What is the only sport to be played on the moon?": "Golf",
    "What is the title of the 2021 James Bond film, Daniel Craig's last appearance as Bond?": ["No Time to Die", "No time to die"],
    "Who played the lead role in the 2021 film 'The Batman'?": "Robert Pattinson",
    "What new variant of COVID-19 emerged in late 2021, causing global concern?": "Omicron",
}


def play_trivia_game(questions_answers):
    print("Choose your difficulty: Easy, Normal, or Norwegian.")
    print("Note: These difficulties do not regard the questions but the drinking.")
    difficulty = input("Your difficulty: ").strip().capitalize()

    # Select 20 random questions from the pool
    selected_questions = random.sample(list(questions_answers.keys()), 20)
    round_number = 1
    lives = 3  # Player starts with 3 lives for all difficulties

    for question in selected_questions:
        if lives <= 0:
            break  # End the game if the player has run out of lives

        print(f"Round {round_number}: {question}")
        user_answer = input("Your answer: ").strip()

        # Check if the answer is correct
        correct_answer = questions_answers[question]
        if isinstance(correct_answer, list):  # If there are multiple correct answers
            is_correct = user_answer in correct_answer
        else:
            is_correct = user_answer.lower() == correct_answer.lower()

        # Difficulty-based drinking rules
        if is_correct:
            if difficulty == "Easy":
                print("Correct! You can give away 1 sip.")
            elif difficulty == "Normal":
                print("Correct! You can give away 2 sips.")
            elif difficulty == "Norwegian":
                print("Correct! You can give away 10 sips.")
        else:
            lives -= 1
            if difficulty == "Easy":
                print("Wrong! You have to take 2 sips. Lives remaining: ", lives)
            elif difficulty == "Normal":
                print("Wrong! You have to take 5 sips. Lives remaining: ", lives)
            elif difficulty == "Norwegian":
                print(f"Wrong! You have to drink {round_number * 2} sips. Lives remaining: ", lives)

        round_number += 1
        if lives > 0 and round_number < 21:
            print("\nNext round!\n")
        else:
            break

    # Post-game outcomes based on difficulty
    if lives > 0:
        if difficulty == "Easy":
            print("\nYou've won! Choose 1 person to finish their drink.\n")
        elif difficulty == "Normal":
            print("\nYou've won! Choose 3 people to finish their drink.\n")
        elif difficulty == "Norwegian":
            print("\nYou've won! Everyone else has to finish their drink.\n")
    else:
        if difficulty == "Easy":
            print("\nGame Over. You have to finish your drink.\n")
        elif difficulty == "Normal":
            print("\nGame Over. You have to finish two drinks.\n")
        elif difficulty == "Norwegian":
            print("\nGame Over. You have to finish 5 drinks.\n")


# Start the game
play_trivia_game(questions_answers)