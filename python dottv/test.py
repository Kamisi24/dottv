import csv

def compare(user, movie):
    comp1 = abs(user[0]-int(movie[1]))
    comp2 = abs(user[1]-int(movie[2]))
    comp3 = abs(user[2]-int(movie[3]))
    comp4 = abs(user[3]-int(movie[4]))
    comp5 = abs(user[4]-int(movie[5]))
    return comp1+comp2+comp3+comp4+comp5



Act_q1= "how much graffic do you like your films on a scale from 1 to 10? "
Act_q2= "Do you enjoy science in the films? "
Act_q3= "How important is the story to you? "
Act_q4= "Are the films more likely have big name actors? "
Act_q5= "How much do you enjoy explosions? "

print(Act_q1)
Act1 = input("Please place the score: ")
print(Act_q2)
Act2 = input("Please place the score: ")
print(Act_q3)
Act3 = input("Please place the score: ")
print(Act_q4)
Act4 = input("Please place the score: ")
print(Act_q5)
Act5 = input("Please place the score: ")

def Action():
    actsc = [int(Act1),int(Act2),int(Act3),int(Act4),int(Act5)]
    # can use loop function eg for movies in action movies do the function

    with open('Action_movies.csv', 'r') as new_file:
        csv_movies = csv.reader(new_file)
        for films in csv_movies:
            print(films[0] + ' score is:')
            print(compare(actsc,films))


Action()