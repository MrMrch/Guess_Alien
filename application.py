from flask import Flask, render_template, request, redirect, Response, flash
import os
from engine import *
# del culprit

app = Flask(__name__)

@app.route('/home',methods=['GET', 'POST'])
@app.route("/")
def home():
    restart_game()
    print("================")
    attr_in_play = create_attr_in_play()
    for attr in attr_in_play:
        print(attr)
    q_built_prof_dict = {'name' : [], 'skin' : [], 'suit' : [], 'hairlen' : [],  'haircolor' : [], 'glasses' : [], 'hat' : [], 'image' : [], 'inplay' : []}
    print(q_built_prof_dict)
    # print(q_built_prof_dict)
    global answers_list
    answers_list.clear()
    print_aliens_in_play()
    print("@@@@@@@@@@@@@@@@ BEGIN @@@@@@@@@@@@@@")
    print(answers_list)
    if request.method == "GET":
        question = ""
        answer = request.form.get('answer')

        return render_template('home.html', aliens=aliens, question = "Ready to play?")

    elif request.method == "POST":
        answer = request.form.get('answer')
        question, (attr, trait) = gen_master_question(aliens)
        # ingameupdates(answer, attr, trait)


        attr_in_play = create_attr_in_play()

        # return render_template('ingame.html', aliens=aliens, question = question)
        return redirect("/ingame")

@app.route('/ingame', methods=['GET', 'POST'])
# @app.route("/")

def ingame():

    global q_built_prof_dict
    # if request.method == "GET":
    #     question, attr_in_play = gen_master_question(aliens)
    #     return render_template('ingame.html', aliens=aliens, question = question)

    # elif request.method == "POST":
    if request.method == "POST":

        answer = request.form.get('answer')
        attr_in_play = create_attr_in_play()
        print("===================== ingame =============")
        question, (attr, trait) = gen_master_question(aliens)

        ingameupdates(answer, attr, trait)
        attr_in_play = create_attr_in_play()



        # print(q_built_prof_dict)
        print("answer is: " + answer)
        print(question)
        # # print("attribute: " + attr)
        # print("trait: " + str(trait))
        # print("still in play: " + str(attr_in_play))

        survivors = survivors_count()
        print_aliens_in_play()
                # survivors = survivors_count()
        if survivors == 1:
            print("VERDICT")
            guilty, q_built_prof_dict = gameverdict_()
            # return render_template('gameverdict.html', guilty = guilty)
            return redirect('gameverdict')

            # return redirect(f"/gameverdict?answer={request.form.get('answer')}")

        else:
            question, (attr, trait) = gen_master_question(aliens)
            print(q_built_prof_dict)

            return render_template('ingame.html', aliens=aliens, question = question)
    else:
        question, (attr, trait) = gen_master_question(aliens)

        print("GET in ingame")
        attr_in_play = create_attr_in_play()
        survivors = survivors_count()
        print_aliens_in_play()

        print("still in play: " + str(attr_in_play))

        return render_template('ingame.html', aliens=aliens, question = question)

@app.route('/gameverdict', methods=['GET', 'POST'])
def gameverdict():
    if request.method == "POST":
        guilty, q_built_prof_dict = gameverdict_()
        print("#################### POST #########################")

        answer = request.form.get('answer')
        # if answer == "yes":
        #     return render_template('endgame.html', aliens=aliens, resolution = "I won!", guilty = guilty)
        # else:
        return render_template('endgame.html', aliens=aliens, resolution = "so Did I guess?", guilty = guilty)

        # return render_template('gameverdict.html', aliens=aliens, question = question, guilty = guilty)
    else:
        print("#################### GET #########################")
        guilty, q_built_prof_dict = gameverdict_()
        return render_template('gameverdict.html', guilty = guilty)

# @app.route('/gameverdict', methods=['GET', 'POST'])
# def gameverdict():
#     if True:
#         guilty = gameverdict_()
#         print("#################### POST #########################")

#         answer = request.form.get('answer')
#         if answer == "yes":
#             return render_template('endgame.html', aliens=aliens, resolution = "I won!", guilty = guilty)
#         else:
#             return render_template('endgame.html', aliens=aliens, resolution = "I lose", guilty = guilty)

#         # return render_template('gameverdict.html', aliens=aliens, question = question, guilty = guilty)
#     else:
#         print("#################### GET #########################")
#         guilty = gameverdict_()
#         return render_template('gameverdict.html', guilty = guilty)



@app.route('/endgame', methods=['GET', 'POST'])
def endgame():
    # if request.method == "POST":
    print("endgame")
    # guilty = gameverdict_()
    guilty, q_built_prof_dict = gameverdict_()

    return render_template('endgame.html', aliens=aliens, resolution = "WINNER WINNER CHICKEN DINNER", guilty = guilty)

@app.route('/pick_alien', methods=['GET', 'POST'])
def pick_alien():
    # if request.method == "POST":
    print("pick_alien")
    # guilty = gameverdict_()
    # culprit = request.args.get('picked')
    value = request.form.get('picked')
    culprit = ""
    for alien in aliens:
        if alien.name == value:
            culprit = alien
    # print(str(culprit.name))
    return render_template('pick_alien.html', aliens=aliens, culprit=culprit)

@app.route('/appeal', methods=['GET', 'POST'])
def appeal():
    # if request.method == "POST":
    print("appeal")
    guilty, q_built_prof_dict = gameverdict_()
    answers_list = []
    # answers_list.clear()
    print(guilty, q_built_prof_dict)

    # print(guilty, answers_list)
    global culprit
    value = request.form.get('picked')
    for alien in aliens:
        if alien.name == value:
            culprit = alien
    print(culprit.name)
    # print(str(culprit.name))
    # culprit = request.args.get('picked')
    # guilty, answers_list = appeal_()
    # culprit = aliens[1]

    guilty, answers_list = appeal_(culprit)
    # guilty ="dwight"
    # answers_list = ("baba", "tata")
    print(culprit.name)
    print("@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@")
    print(answers_list)
    # for attr, val in culprit:
    #     print(attr, val)

    # q_built_prof_dictitems = q_built_prof_dictitems
    return render_template('appeal.html', aliens=aliens, resolution = "You are lying!", guilty = guilty, culprit = culprit, answers_list = answers_list, q_built_prof_dict = q_built_prof_dict)


if __name__ == "__main__":
    app.run(debug=True)
