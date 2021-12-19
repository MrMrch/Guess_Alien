import random
from collections import Counter, namedtuple
# from application import culprit

class Alien(object):
    def __init__(self, name, skin, suit, hairlen, haircolor, glasses, hat, image, inplay=True):
        self.name = name
        self.skin = skin
        self.suit = suit
        self.hairlen = hairlen
        self.haircolor = haircolor
        self.glasses = glasses
        self.hat = hat
        self.inplay = inplay
        self.image = image

yes_no_attr = ["hat", "necklace", "mask", "glasses"]
multi_attr = ["skin", "suit", "hairlen", "haircolor"]
countable_attr = ("hat", "necklace", "mask")

#      --- , name,  skin,   suit,   len,   hcolor, glasses, hat, image, inplay=True):
axi = Alien("Axi", "blue", "grey", "short", "pink", True, False, "IMG-0927.jpg" )
bexi = Alien("Bexi", "orange", "grey", "short", "green", True, False, "IMG-0928.jpg")
cixi = Alien("Cixi", "blue", "grey", "long", "black", True, False, "IMG-0929.jpg")

#      --- , name,  skin,   suit,   len,   hcolor, glasses, hat, image, inplay=True):
dixi = Alien("Dixi", "pink", "red", "long", "green", True, False, "IMG-0930.jpg")
exi = Alien("Exi", "orange", "blue", "long", "yellow", True, False, "IMG-0931.jpg")
fixi = Alien("Fixi", "pink", "blue", "short", "yellow", True, False, "IMG-0932.jpg")

#      --- , name,  skin,   suit,      len,   hcolor, glasses, hat, image, inplay=True):
gixi = Alien("Gixi", "pink", "blue", "long", "black", True, False, "IMG-0933.jpg") ###
hexi = Alien("Hexi", "green", "red", "no", "pink", False, True, "IMG-0934.jpg")
ixi = Alien("Ixi", "orange", "blue", "no", "no", True, True, "IMG-0935.jpg")

#      --- , name,  skin,   suit,      len,   hcolor, glasses, hat, image, inplay=True):
lixi = Alien("Lixi", "green", "red", "long", "pink", True, True, "IMG-0936.jpg") ###
mixi = Alien("Mixi", "blue", "red", "short", "black", False, False, "IMG-0937.jpg") ###
nixi = Alien("Nixi", "green", "red", "short", "pink", False, False, "IMG-0938.jpg") ###
# #      --- , name,  skin,   suit,   len,   hcolor, glasses, hat, image, inplay=True):
# axi = Alien("Axi", "blue", "grey", "short", "pink", True, False, "IMG-0927.jpg", False)
# bexi = Alien("Bexi", "orange", "grey", "short", "green", True, False, "IMG-0928.jpg", False)
# cixi = Alien("Cixi", "blue", "grey", "long", "black", True, False, "IMG-0929.jpg", False)

# #      --- , name,  skin,   suit,   len,   hcolor, glasses, hat, image, inplay=True):
# dixi = Alien("Dixi", "pink", "red", "long", "green", True, False, "IMG-0930.jpg", False)
# exi = Alien("Exi", "orange", "blue", "long", "yellow", True, False, "IMG-0931.jpg", False)
# fixi = Alien("Fixi", "pink", "blue", "short", "yellow", True, False, "IMG-0932.jpg", False)

# #      --- , name,  skin,   suit,      len,   hcolor, glasses, hat, image, inplay=True):
# gixi = Alien("Gixi", "pink", "blue", "long", "black", True, False, "IMG-0933.jpg", False) ###
# hexi = Alien("Hexi", "green", "red", "no", "pink", False, True, "IMG-0934.jpg", False)
# ixi = Alien("Ixi", "orange", "blue", "no", "no", True, True, "IMG-0935.jpg", False)

# #      --- , name,  skin,   suit,      len,   hcolor, glasses, hat, image, inplay=True):
# lixi = Alien("Lixi", "green", "red", "long", "pink", True, True, "IMG-0936.jpg", False) ###
# mixi = Alien("Mixi", "blue", "red", "short", "black", False, False, "IMG-0937.jpg") ###
# nixi = Alien("Nixi", "green", "red", "short", "pink", False, False, "IMG-0938.jpg") ###

# aliens = [axi, bexi, cixi, dixi]
aliens = [axi, bexi, cixi, dixi, exi, fixi, gixi, hexi, ixi, lixi, mixi, nixi]
# aliens = [bexi, cixi, dixi, exi]

#print aliens in play
def print_aliens_in_play():
    for alien in aliens:
        if alien.inplay == True:
            print(alien.name)

#Here I will add the attributes as I ask the questions
# question_built_profile = Alien(None, None, None,None, None, None, None)

q_built_prof_dict = {'name' : [], 'skin' : [], 'suit' : [], 'hairlen' : [],  'haircolor' : [], 'glasses' : [], 'hat' : [], 'image' : [], 'inplay' : []}



def create_attr_in_play():
    return {attribute:v for attribute in attr_names if len(v:=Counter([getattr(alien, attribute) for alien in aliens if alien.inplay]))>1}


attr_names = [x for x in dir(aliens[0]) if not x.startswith("__") and x not in ("name","inplay", "image")]

# attr_in_play  = {attribute:Counter([getattr(alien, attribute) for alien in aliens if alien.inplay]) for attribute in attr_names}
attr_in_play = create_attr_in_play()

#Find best attribute to ask about
def find_best_q(aliens):
    half = float(survivors) / 2
    tripletouple = []
    attr_in_play = create_attr_in_play()

    for attr, value in attr_in_play.items():
        for trait, count in value.items():
            tripletouple.append((attr, trait, count))

    def find_score(tripletouple):
        return abs(half-tripletouple[2])

    try:

        return min(tripletouple, key=find_score)
    except:
        print("error exception printed")
        pass

# THE MAIN QUESTION, FROM WHICH STEM ALL OTHERS. ONE QUESTION TO RULE THEM ALL.
# def master_question(aliens):
#     global attr_in_play
#     attr_to_ask = find_best_q(aliens, attr_in_play)
#     if attr_to_ask[0] in multi_attr:
#         gen_col_Q(attr_to_ask[1], attr_to_ask[0])
#     elif attr_to_ask[0] in yes_no_attr:
#         binary_question(attr_to_ask[1], attr_to_ask[0])
#     attr_in_play = create_attr_in_play()

# new main question to implement in application.py
def gen_master_question(aliens):
    # global attr_in_play
    attr_to_ask = find_best_q(aliens)
    print(attr_to_ask)
    if attr_to_ask == None:
        print("empty")
        q = "empty"
        return q, (0, 0)
    elif attr_to_ask[0] in multi_attr:
        q = gen_col_Q(*attr_to_ask[0:2])
    elif attr_to_ask[0] in yes_no_attr:
        q = binary_question(*attr_to_ask[0:2])
    else:
        q = None
    attr_in_play = create_attr_in_play()
    return q, attr_to_ask[0:2]

#This question works with hat, glasses (and future possible attributes necklace and mask)
def binary_question(attr, trait):
    trait = True
    text_attr = attr
    if attr in countable_attr:
        text_attr = "a" + attr
    # answer = input("Does your alien wear " + str(text_attr) + "? ")
    return "Does your alien wear " + str(text_attr) + "? "
    # yes_no_update(answer, attr, trait)
    if answer == "yes":
        for alien in aliens:
            if getattr(alien, attr) != trait:
                alien.inplay = False
        q_built_prof_dict[attr].append(True)

    elif answer == "no":
        for alien in aliens:
            if getattr(alien, attr) == trait:
                alien.inplay = False
        q_built_prof_dict[attr].append(False)

# This function generates a question that works well with attributes skin color, suit color, hair color and hair length
def gen_col_Q(attr, trait):
    text_attr = attr
    if attr in ("hairlen", "haircolor"):
        text_attr = "hair"
    # answer = input("Does your alien have " + str(trait) +" "+ str(text_attr) + "? ")
    return "Does your alien have " + str(trait) +" "+ str(text_attr) + "? "
    yes_no_update(answer, attr, trait)

#This function elaborates the answer and updates the list of aliens still in play
# AND adds attributes to question_built_profile
def yes_no_update(answer, attr, trait):
    #if alien has not that attribute  we remove all aliens with that attribute
    if answer == "yes":
        if attr in ("hairlen", "haircol") and trait == "no":
            for alien in aliens:
                if getattr(alien, "hairlen") != "no" or getattr(alien, "haircol"):
                    alien.inplay = False
        else:
            for alien in aliens:
                if getattr(alien, attr) != trait:
                    alien.inplay = False
        #here we add this answer to the question_built_profile that we are creating
            # setattr(question_built_profile, attr, trait)
        q_built_prof_dict[attr].append(trait)

    #if alien has that attribute we remove all aliens without that attribute
    elif answer == "no":
        for alien in aliens:
            if getattr(alien, attr) == trait:
                alien.inplay = False

    #here we add this answer to the question_built_profile that we are creating
        if attr in yes_no_attr: #for yes and no attributes like glasses etc
            # setattr(question_built_profile, attr, not trait)
            q_built_prof_dict[attr].append(not trait)

        elif attr in multi_attr and trait != "no": #for all multi option attributes except hair
            # setattr(question_built_profile, attr, "not " +trait)
            q_built_prof_dict[attr].append("not " + trait)

        elif trait == "no": #if the trait is something like "no hair"
            # setattr(question_built_profile, attr, trait)
            q_built_prof_dict[attr].append("some")


def ingameupdates(answer, attr, trait):

    if attr in yes_no_attr:
        trait = True

        if answer == "yes":
            for alien in aliens:
                if getattr(alien, attr) != trait:
                    alien.inplay = False
            q_built_prof_dict[attr].append(True)

        elif answer == "no":
            for alien in aliens:
                if getattr(alien, attr) == trait:
                    alien.inplay = False
            q_built_prof_dict[attr].append(False)

    elif attr in multi_attr:
        yes_no_update(answer, attr, trait)
        # return aliens





    # trait = True
    # text_attr = attr
    # if attr in countable_attr:
    #     text_attr = "a" + attr
    # # answer = input("Does your alien wear " + str(text_attr) + "? ")
    # return "Does your alien wear " + str(text_attr) + "? "
    # # yes_no_update(answer, attr, trait)
    # if answer == "yes":
    #     for alien in aliens:
    #         if getattr(alien, attr) != trait:
    #             alien.inplay = False
    #     q_built_prof_dict[attr].append(True)
#     = ["skin", "suit", "hairlen", "haircolor"]
# countable_attr = ("hat", "necklace", "mask")




############################
#      GAME BEGIN HERE

#The player is given a card
#culprit = random.choice(aliens)
# culprit = aliens[1]
# culprit = Alien("", "", "", "", "", True, True, "", False) ###

# print("your alien is " + culprit.name)

# for k, v in vars(culprit).items():
#     print(f"{k}: {v}")

survivors = 0

def survivors_count():
    global survivors
    survivors = 0
    for alien in aliens:
        if alien.inplay == True:
            survivors +=1
    return survivors

survivors_count()

def playgame():
    survivors_count()
    while survivors > 1:
        master_question(aliens)
        attr_in_play = create_attr_in_play()
        print("suspect:" + str(q_built_prof_dict))
        survivors_count()
        verdict()


def gameverdict_():
    guilty = [x for x in aliens if x.inplay == True]
    # print("my suspect is: " + str(guilty[0].name))
    return guilty, q_built_prof_dict

answers_list = []

def appeal_(culprit):
    global q_built_prof_dict
    global answers_list
    guilty = [x for x in aliens if x.inplay == True]
    print("my suspect is: " + str(guilty[0].name))
    # answers_list.append("Let's check. Your alien was " + culprit.name)
    answers_list.append("You gave me the wrong answers!")

    for (name, guesses), (_, value) in zip(sorted(q_built_prof_dict.items()), sorted(vars(culprit).items())):
        for guess in guesses:
            print(guess)
            #switch attributes with hair for readability (cosmetic)
            if name in ("hairlen", "haircolor"):
                name = "hair"

        #switch glasses/hat attributes for readability (cosmetic)
            # adds a for hat
            if name == "hat" and value == True:
                value = "a"
            elif name == "hat" and guess == True:
                guess = "a"

            # adds no for False statements and nothing for True, unless it was "hat"
            if guess == False:
                guess = "no"
            elif guess == True:
                guess = "" #used to be ___

            if value == False:
                value = "no"
            elif value == True:
                value = "" #ised to be ----

            guess_is_not = guess.startswith("not ")
            guess_content = guess.replace("not ", "")
            value_is_not = value.startswith("not ")
            value = value.replace("not ", "")

            if (guess_is_not and guess_content != value):
                continue

            elif ((not guess_is_not or guess=="no") and guess==value ):
                continue

            elif (guess=="some" and value!="no"):
                continue
            # answers_list.append("testpart")
            answers_list.append(f"You said it had {guess.upper()} {name.upper()} instead it has {value.upper()} {name.upper()}")
            # print(f"You said it had {guess.upper()} {name.upper()} instead it has {value.upper()} {name.upper()}")
            print("================================================")
            print(answers_list)

            continue
        
        print(answers_list)
    return guilty, answers_list

def restart_game():
    for alien in aliens:
        alien.inplay = True
    survivors = survivors_count()
    attr_in_play = create_attr_in_play()
    q_built_prof_dict = {'name' : [], 'skin' : [], 'suit' : [], 'hairlen' : [],  'haircolor' : [], 'glasses' : [], 'hat' : [], 'image' : [], 'inplay' : []}
