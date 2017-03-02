 # Trivia Challenge
 # Trivia game that reads a plain text file

import sys

def open_file(trivia, mode):
    """Open a file."""
    try:
        the_file = open(trivia, mode)
    except IOError as e:
        print("Unable to open the file", trivia, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return trivia

def next_line(trivia):
    """Return next line from the trivia file, formatted."""
    line = trivia.readline()
    line = line.replace("/", "\n")
    return line

def next_block(trivia):
    """Return the next block of data from the trivia file."""
    category = next_line(trivia)
    
    question = next_line(trivia)
    
  
    answers = []
    for i in range(4):
        answers.append(next_line(trivia))
        
    correct = next_line(trivia)
    if correct:
        correct = correct[0]

    return category, question, answers, correct

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # 1
    category, question, answers, correct = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print("Score:", score, "\n\n")

	# 2
    category, question, answers, correct = next_block(trivia_file)
    while category:
		    print(category)
		    print(question)
		    for i in range(4):
			    print("\t", i + 1, "-", answer[i])
		
answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score:",score, "\n\n")
		
	# 3
category, question, answers, correct = next_block(trivia_file)
while category:
		    print(category)
		    print(question)
		    for i in range(4):
			    print("\t", i + 1, "-", answer[i])
			
answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score:",score, "\n\n")
		
	# 4
category, question, answers, correct = next_block(trivia_file)
while category:
		    print(category)
		    print(question)
		    for i in range(4):
			    print("\t", i + 1, "-", answer[i])
			
answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score:",score, "\n\n")
		
	# 5
category, question, answers, correct = next_block(trivia_file)
while category:
		    print(category)
		    print(question)
		    for i in range(4):
			    print("\t", i + 1, "-", answer[i])
			
answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")
		
	# 6
category, question, answers, correct = next_block(trivia_file)
while category:
		    print(category)
		    print(question)
		    for i in range(4):
			    print("\t", i + 1, "-",answer[i])
			
answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")
		
	# 7
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")
		
	# 8
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 9
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 10
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 11
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 12
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 13
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 14
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 15
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 16
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 17
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 18
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 19
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 20
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 21
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 22
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 23
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 24
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")

	# 25
category, question, answers, correct = next_block(trivia_file)
while category:
		print(category)
		print(question)
		for i in range(4):
			print("\t", i + 1, "-", answer[i])
			
		answer = input("What's your answer?: ")
		
if answer == correct:
			print("\nRight!", end=" ")
			score +=1
else:
			print("\nWrong.", end=" ")
print("Score: ",score, "\n\n")


trivia_file.close()

print("That was the last question!")
print("You're final score is", score)
 
main()  
input("\n\nPress the enter key to exit.")