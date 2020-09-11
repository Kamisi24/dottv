#class Movies:
    #def __init__(self, name, genre1, genre2):
        #self.name = name
        #self.genre1 = genre1
        #self.genre2 = genre2

#Avengers = Movies('Avengers', 'Superhero', 'Action')
#Darknight = Movies('The Dark knight', 'Superhero', 'Action')
#Soundofmus = Movies('Sound of Music', 'Musical', 'Romance')
#Grease = Movies('Grease', 'Musical', 'Romance')
#Edgeoftomo = Movies('Edge of tomorrow', 'Action', 'Sci-fi')
#Starwars = Movies('Star Wars: The Last Jedi','Sci-fi', 'Action')

import json


filename = 'Actionmovies.json'
#if __name__ == '__main__':
    #Moviename = input('Action movie name: ')
    #Act_q1= input("how much graffic do you like your films on a scale from 1 to 10? ")
    #Act_q2= input("Do you enjoy science in the films? ")
    #Act_q3= input("How important is the story to you? ")
    #Act_q4= input("Are the films more likely have big name actors? ")
    #Act_q5= input("How much do you enjoy explosions? ")
    #movielist = (Moviename, Act_q1,Act_q2, Act_q3, Act_q4, Act_q5)

    #with open(filename, 'a') as f_obj:
        #json.dump(movielist, f_obj)

with open(filename, 'r') as f_obj:
    movielist = list(f_obj)
    for movie in movielist:
        print(type(movie[1]))