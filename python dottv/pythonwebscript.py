import csv
#can use a knn algorithem to recommend flims to people who might have similar scores after the tell you their fav films

#Action questions
Act_q1= "how much graffic do you like your films on a scale from 1 to 10? "
Act_q2= "Do you enjoy science in the films? "
Act_q3= "How important is the story to you? "
Act_q4= "Are the films more likely have big name actors? "
Act_q5= "How much do you enjoy explosions? "

#Adventure questions
Adv_q1 = "On a scale of 1 to 10 how much do u like treasure hunts? "
Adv_q2 = "On a scale of 1 to 10 how much do you like pirates? "
Adv_q3 = "On a scale of 1 to 10 how much do you like book adaptations? "
Adv_q4 = "On a scale of 1 to 10 how much do you enjoy films with big name actors? "
Adv_q5 = "On a scale of 1 to 10 how much do you enjoy a family friendly film?"

#Comedy questions
Com_q1= "On a scale of 1 to 10 how much do you like action in your films? "
Com_q2= "On a scale pf 1 to 10 how much do you like stupidity humour? "
Com_q3= "On a scale of 1 to 10 how much do you like offensive humour? "
Com_q4= "On a scale of 1 to 10 home much do you like adult humour? "
Com_q5= "On a scale of 1 to 10 how much do you like an actor you plays multiple roles? "

#Crime questions
Cri_q1= " "
Cri_q2= " "
Cri_q3= " "
Cri_q4= " "
Cri_q5= " "

#Drama questions
Dra_q1= " "
Dra_q2= " "
Dra_q3= " "
Dra_q4= " "
Dra_q5= " "

#Fantansy questions
Fan_q1= "On a scale of 1 to 10 how much do you enjoy films with magic? "
Fan_q2= "On a scale of 1 to 10 how do you enjoy films that are family friendly? "
Fan_q3= "On a scale of 1 to 10 how likely are you to enjoy a film with computer generated characters? "
Fan_q4= "On a scale of 1 to 10 how much do you like book adaptations? "
Fan_q5= "On a scale of 1 to 10 how much do you enjoy stand alone films? "

# Historical questions
His_q1= " "
His_q2= " "
His_q3= " "
His_q4= " "
His_q5= " "

#Horror questions
Hor_q1= "On a scale of 1 to 10 how graffic do you like your flims? "
Hor_q2= "On a scale of 1 to 10 how much do you like ghosts in your films? "
Hor_q3= "On a scale of 1 to 10 how much do you like jump scares? "
Hor_q4= "On a scale of 1 to 10 how much do you like supernatural creatures? "
Hor_q5= "On a scale of 1 to 10 how much do you like complex stories? "

#Mystery questions
Mys_q1= " "
Mys_q2= " "
Mys_q3= " "
Mys_q4= " "
Mys_q5= " "

#Satire questions
Sat_q1= " "
Sat_q2= " "
Sat_q3= " "
Sat_q4= " "
Sat_q5= " "

#Sci-fi questions
Sci_q1= "On a scale of 1 to 10 how much do you care about scientific accuracy? "
Sci_q2= "On a scale of 1 to 10 how much do like films that involve time travel? "
Sci_q3= "On a scale of 1 to 10 how much do you enjoy films that involve space travel? "
Sci_q4= "On a scale of 1 to 10 how much do you enjoy sci-fi classics? "
Sci_q5= "On a scale of 1 to 10 how much do you like big name actors? "

#Social questions
Soc_q1= " "
Soc_q2= " "
Soc_q3= " "
Soc_q4= " "
Soc_q5= " "

#Superhero questions
Sup_q1= "On a scale of 1 to 10 how much do you like contained stories? "
Sup_q2= "On a scale of 1 to 10 how much do you like graphic violence? "
Sup_q3= "On a scale of 1 to 10 how much do you like team up films? "
Sup_q4= "On a scale of 1 to 10 how much do you like realistic superhero films? "
Sup_q5= "On a scale of 1 to 10 how much do you enjoy comedy in your films? "

#Thriller questions
Thr_q1= "On a scale of 1 to 10 how much do you enjoy movies with complex storylines? "
Thr_q2= "On a scale of 1 to 10 how much do you enjoy films with horror? "
Thr_q3= "On a scale of 1 to 10 how much do you enjoy films with action? "
Thr_q4= "On a scale of 1 to 10 how much do you enjoy films with big name actors? "
Thr_q5= "On a scale of 1 to 10 how much do you enjoy stand alone films? "

#Tear-Jeak
Tea_q1= " "
Tea_q2= " "
Tea_q3= " "
Tea_q4= " "
Tea_q5= " "

#Urban questions
Urb_q1= " "
Urb_q2= " "
Urb_q3= " "
Urb_q4= " "
Urb_q5= " "

#Western questions
Wes_q1= " "
Wes_q2= " "
Wes_q3= " "
Wes_q4= " "
Wes_q5= " "

#Romance questions
Rom_q1 = 'On a scale of 1 to 10 how likely are you to enjoy a film with a famous actor? '
Rom_q2 = 'On a scale of 1 to 10 how much do you enjoy a film with a school setting? '
Rom_q3 = 'On a scale of 1 to 10 how much do you like tear jerkers? '
Rom_q4 = 'On a scale of 1 to 10 how important is nudity to you? '
Rom_q5 = 'On a scale of 1 to 10 how important is a happy ending? '

#Romcom questions
Romcom_q1 = 'On a scale of 1 to 10 how likely are you to enjoy a film with a famous actor? '
Romcom_q2 = 'On a scale of 1 to 10 how much do you enjoy a film with a school setting? '
Romcom_q3 = 'On a scale of 1 to 10 how important is the comedy element? '
Romcom_q4 = 'On a scale of 1 to 10 how much do you enjoy awkward or cringe worthy moments? '
Romcom_q5 = 'On a scale of 1 to 10 how important is a happy ending? '

#Musicals questions
Mus_q1 = 'On a scale of 1 to 10 how likely are you to enjoy a film with a famous actor? '
Mus_q2 = 'On a scale of 1 to 10 how much do you enjoy a film with a school setting? '
Mus_q3 = 'On a scale of 1 to 10 how much do you like classics? '
Mus_q4 = 'On a scale of 1 to 10 how important are the upbeat songs? '
Mus_q5 = 'On a scale of 1 to 10 how much do you enjoy a high ratio of song to story? '


#comparison function
def compare(user, movie):
    comp1 = abs(user[0]-int(movie[1]))
    comp2 = abs(user[1]-int(movie[2]))
    comp3 = abs(user[2]-int(movie[3]))
    comp4 = abs(user[3]-int(movie[4]))
    comp5 = abs(user[4]-int(movie[5]))
    return comp1+comp2+comp3+comp4+comp5

#genre function
def genre_function(genre,a,b,c,d,e):
    questions = [int(a),int(b),int(c),int(d),int(e)]

    with open(f'{genre}_movies.csv', 'r') as new_file:
        csv_movies2 = csv.reader(new_file)
        for films in csv_movies2:
            print(films[0] + ' score is:')
            print(compare(questions,films))
    
print('What are your favourite 5 genres out of action, adventure, comedy, crime, drama, fantasy, historical, horror, musical, mystery, romance, romcom, satire, sci-fi, social, superhero, tear-jeak, thriller, urban and western?')
genreyoulike1 = input("First: ")
genreyoulike2 = input("Second: ")
genreyoulike3 = input("Third: ")
genreyoulike4 = input("Fourth: ")
genreyoulike5 = input("Fifth: ")

genreyoulike = [genreyoulike1.title(),genreyoulike2.title(),genreyoulike3.title(),genreyoulike4.title(),genreyoulike5.title()]
if "Action" in genreyoulike:
    genre = 'Action'
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
   # Then call a new function
    genre_function(genre,Act1,Act2,Act3,Act4,Act5)

if "Adventure" in genreyoulike:
    genre2 = 'Adventure'
    print(Adv_q1)
    Adv1 = input("Please place the score: ")
    print(Adv_q2)
    Adv2 = input("Please place the score: ")
    print(Adv_q3)
    Adv3 = input("Please place the score: ")
    print(Adv_q4)
    Adv4 = input("Please place the score: ")
    print(Adv_q5)
    Adv5 = input("Please place the score: ")
    #run func
    genre_function(genre2,Adv1, Adv2,Adv3, Adv4, Adv5)

if "Comedy" in genreyoulike:
    genre3 = 'Comedy'
    print(Com_q1)
    Com1 = input("Please place the score: ")
    print(Com_q2)
    Com2 = input("Please place the score: ")
    print(Com_q3)
    Com3 = input("Please place the score: ")
    print(Com_q4)
    Com4 = input("Please place the score: ")
    print(Com_q5)
    Com5 = input("Please place the score: ")
    genre_function(genre3,Com1, Com2,Com3, Com4, Com5)

if "Romance" in genreyoulike:
    genre4 = 'Romance'
    print(Rom_q1)
    Rom1 = input("Please place the score")
    print(Rom_q2)
    Rom2 = input("Please place the score")
    print(Rom_q3)
    Rom3 = input("Please place the score")
    print(Rom_q4)
    Rom4 = input("Please place the score")
    print(Rom_q5)
    Rom5 = input("Please place the score")
    genre_function(genre4,Rom1, Rom2,Rom3, Rom4, Rom5)

if "Romcom" in genreyoulike:
    genre5 = 'Romcom'
    print(Romcom_q1)
    Romcom1 = input("Please place the score")
    print(Romcom_q2)
    Romcom2 = input("Please place the score")
    print(Romcom_q3)
    Romcom3 = input("Please place the score")
    print(Romcom_q4)
    Romcom4 = input("Please place the score")
    print(Romcom_q5)
    Romcom5 = input("Please place the score")
    genre_function(genre5,Romcom1, Romcom2,Romcom3, Romcom4, Romcom5)


if "Crime" in genreyoulike:
    genre6 = 'Crime'
    print(Cri_q1)
    Cri1 = input("Please place the score")
    print(Cri_q2)
    Cri2 = input("Please place the score")
    print(Cri_q3)
    Cri3 = input("Please place the score")
    print(Cri_q4)
    Cri4 = input("Please place the score")
    print(Cri_q5)
    Cri5 = input("Please place the score")
    genre_function(genre6,Cri1, Cri2,Cri3, Cri4, Cri5)

