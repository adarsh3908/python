import random
print(" Welcome To My Quiz Game \n Intresting Game to Play")
Player = input("Do you want to play the Game ?\n")
if Player.lower() == "yes":
    print("Let's Play")
else:
    print("Okay, Maybe Next Time")

name_p = input("Enter Your Name: ")
print("lets start the game : " , name_p)
score=0
questions = [
    ("Who was the first President of India?", "dr rajendra prasad"),
    ("What is the capital of India?", "new delhi"),
    ("In which year did India gain independence?", "1947"),
    ("Who wrote the national anthem of India?", "rabindranath tagore"),
    ("Who is known as the Iron Man of India?", "sardar vallabhbhai patel"),
    ("What is the national animal of India?", "tiger"),
    ("Who is the current Prime Minister of India (as of 2024)?", "narendra modi"),
    ("What is the official language of India?", ["hindi", "english"]),
    ("Which is the largest state in India by area?", "rajasthan"),
    ("Who is known as the Missile Man of India?", ["dr apj abdul kalam", "abdul kalam"]),
    ("Which is the national flower of India?", "lotus"),
    ("Who is the current President of India (as of 2024)?", "droupadi murmu"),
    ("What is the national sport of India?", "hockey"),
    ("What is the currency of India?", ["rupee", "indian rupee"]),
    ("Which river is known as the 'Ganga of the South'?", "godavari"),
    ("Who was the first woman Prime Minister of India?", "indira gandhi"),
    ("Who is the author of the book 'Discovery of India'?", "jawaharlal nehru"),
    ("Which Indian city is also known as the Silicon Valley of India?", ["bangalore", "bengaluru"]),
    ("Who was the first Indian to win a Nobel Prize?", "rabindranath tagore"),
    ("Which is the national bird of India?", "peacock")
] 
random_ques = random.sample(questions,5)
for question, answer in random_ques:
    
    ans  = input(question + "\n")
    if isinstance(answer,list):
        if ans.lower() in answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    else:
        if ans.lower() == answer: 
            print("Correct")
            score+=1
        else:
            print("Incorrect")

print("You got "+ str(score)+" correcr answers.")
print("Thanks for playing the game")

