# Myers-Briggs type quiz

# Welcome messages
print("Welcome to the Myers-Briggs personality test!")
print("Please rate statements from 1 (Strongly Disagree) to 5 (Strongly Agree)")
print("Would you like to know what personality type you are?")

# Confirm start
yes = input("Enter 'yes' to start the quiz: ")

if yes == "yes":
    print("Lets begin!")
else:
    print("Ok suit yourself.")
    quit()

# Set type statements

extrovert_statements = [
    "I am seen as outgoing or as a people person.",
    "I feel comfortable in groups and like working in them"
]
introvert_statements = [
    "I feel comfortable being alone and like things I can do on my own",
    "I prefer to know just a few people well"
]
intuition_statements = [
    "I remember events by what I read between the lines about their meaning",
    "I solve problems by leaping between different ideas and possibilities."
]
sensing_statements = [
    "I remember events as snapshots of what actually happened",
    "I solve problems by working through facts until I understand the problem."
]
thinking_statements = [
    "I enjoy technical and scientific fields where logic is important.",
    "I make decisions with my head and want to be fair."
]
feeling_statements = [
    "I am concerned with harmony and nervous when it is missing.",
    "I look for what is important to others and express concern for others."
]
judging_statements = [
    "I like to make lists of things to do.",
    "Sometimes I focus so much on the goal that I miss new information."
]
perceiving_statements = [
    "I like to stay open to respond to whatever happens.",
    "I work in bursts of energy."
]

# Set type variables
extrovert_score = 0
introvert_score = 0
intuition_score = 0
sensing_score = 0
thinking_score = 0
feeling_score = 0
judging_score = 0
perceiving_score = 0

# Run statements

for statement in extrovert_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    extrovert_score += rating
for statement in introvert_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    introvert_score += rating
for statement in intuition_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    intuition_score += rating
for statement in sensing_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    sensing_score += rating
for statement in thinking_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    thinking_score += rating
for statement in feeling_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    feeling_score += rating
for statement in judging_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    judging_score += rating
for statement in perceiving_statements:
    print(f"{statement}\n")

    rating = int(input("Enter your rating (1 to 5): "))

    perceiving_score += rating

# Calculate result
if extrovert_score >= introvert_score:
    extrovert_introvert = "E"
else:
    extrovert_introvert = "I"
if intuition_score >= sensing_score:
    intuition_sensing = "N"
else:
    intuition_sensing = "S"
if thinking_score >=  feeling_score:
    thinking_feeling = "T"
else:
    thinking_feeling = "F"
if judging_score >= perceiving_score:
    judging_perceiving = "J"
else:
    judging_perceiving = "P"
# Result
type_dict = {
    "ISTJ": "Inspector",
    "ISFJ": "Protector",
    "INFJ": "Counselor",
    "INTJ": "Mastermind",
    "ISTP": "Craftsman",
    "ISFP": "Composer",
    "INFP": "Healer",
    "INTP": "Architect",
    "ESTP": "Dynamo",
    "ESFP": "Performer",
    "ENFP": "Champion",
    "ENTP": "Inventor",
    "ESTJ": "Supervisor",
    "ESFJ": "Provider",
    "ENFJ": "Teacher",
    "ENTJ": "Commander"
}

type = str(extrovert_introvert+intuition_sensing+thinking_feeling+judging_perceiving)

# print("Your personality type is: ",extrovert_introvert,intuition_sensing,thinking_feeling,judging_perceiving)
print("Your personality type is " + type + " which is also known as The " + type_dict[type] + "!")
