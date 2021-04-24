import math

import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import *
import pickle
from datetime import date


window = Tk()
today = date.today()

# Global values for body composition
filename_body = '/Users/philipczarnecki/PycharmProjects/Daily_Food_Intake/HealthApp/BodyComposition.p'
gender = ""
age = 0
weight_kg = 0
height_cm = 0
height_m = 0
bmi = 0
bfpercent = 0
cneck = 0
cwaist = 0
chips = 0
fbm = 0
lbm = 0
bmr = 0
lfm = 0
alm = 0
alm_in = 0
cbpd = 0
goal = ""
cte = 0
BodyComp_Warning = False
bfpercent_b_press = False
firstfourinputs = [False, False, False, False]

#Global values for both
date = ""
cste = 0
past_bodycomposition = []

# Global values for food calculator
filename_food = '../HealthApp/cste.p'
breakfast = []
breakfast_cal_per_g = []
breakfast_percent = []
grams_of_breakfast = []
breakfast_more = ""
Foodsave = []

breakfasts = ['Oatmeal', 'Cereal', 'Scrambled Eggs', 'Omelet', 'Cheese Bagel', 'Waffle']
breakfasts_c = ['Calories per g', 'Fat per g', 'Sodium per g', 'Carbohydrates per g', 'Protein per g']
breakfasts_n = np.array([[3.58974359, 0.0641025641, 0, 0.7179487179, 0.1282051282],
                [4.237288136, 0.02542372881, 4.745762712, 0.9491525424, 0.186440678],
                [1.48, 0.11, 1.45, 0.016, 0.1], [1.54, 0.12, 1.55, 0.006, 0.11],
                [2.828358209, 0.08208955224, 3.985074627, 0.4253731343, 0.09701492537],
                [2.253521127, 0.05633802817, 2.957746479, 0.3943661972, 0.05633802817]])
breakfasts_n_r = np.around(breakfasts_n, 2)
df_breakfast = pd.DataFrame(breakfasts_n_r, index=breakfasts, columns=breakfasts_c)

# Basic Global Values
fonta = ("Courier", 23)
fontb = ("Courier", 15)
fontc = ("Courier", 10)
fontd = ("Courier", 45)

bg = 'black'
fg = 'white'

font_B = ("Courier", 10)
bg_b = 'white'
fg_b = 'white'
highlight_c_b = 'white'
width_b = '30'
height_b = '1'

# Get Screen Dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Save Data
def save(BodyComposition_data):
    with open(filename_body, 'wb') as filehandler:
        pickle.dump(BodyComposition_data, filehandler)

def savefood(Foodsave):
    with open(filename_food, 'wb') as filehandler:
        pickle.dump(Foodsave, filehandler)

# Numeric Value Error Message
def ValueError_M(x):
    global BodyComp_Warning
    if x == True and BodyComp_Warning==False:
        tryagain = Label(window, text='Please Input A Valid Value', bg=bg, fg=fg, font=fontb).pack(ipady=10)
        BodyComp_Warning=True
    elif x == False and BodyComp_Warning==True:
        windowchildren = window.winfo_children()
        windowchildren[len(windowchildren)-1].destroy()
        BodyComp_Warning = False

# Missing Value Error Message
def MissingValueError_M(x):
    global BodyComp_Warning
    if x == True and BodyComp_Warning == False:
        tryagain = Label(window, text='Please Input All Values', bg=bg, fg=fg, font=fontb).pack(
            ipady=10)
        BodyComp_Warning = True
    elif x == False and BodyComp_Warning == True:
        windowchildren = window.winfo_children()
        windowchildren[len(windowchildren) - 1].destroy()
        BodyComp_Warning = False


# Body Composition Func
def bodycompositionfunc():
    for child in window.winfo_children():
        child.destroy()
    # Male or Female text
    label_widget1 = Label(window, text="What is your biological gender? Male or Female?", bg=bg, fg = fg, font=fonta).pack()

    def Male():
        global gender
        gender="male"
        firstfourinputs[0] = True

    def Female():
        global gender
        global firstfourinputs
        gender="female"
        firstfourinputs[0] = True

    male_B = ttk.Button(window, text="Male", command = Male, width='30').pack()
    female_B = ttk.Button(window, text="Female", command = Female, width='30').pack()

    # Age text
    label_widget2 = Label(window, text='How old are you?', bg=bg, fg=fg, font=fonta).pack()
    t1=Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
    t1.pack()

    def valuea(t):
        x=t.get('1.0','end-1c')
        return x

    def submita():
        global age
        global firstfourinputs
        try:
            age=int(valuea(t1))
        except ValueError:
            ValueError_M(True)
        else:
            ValueError_M(False)
            firstfourinputs[1] = True
    ttk.Button(window, text='Submit', command=submita).pack()

    # Weight text
    label_widget3 = Label(window, text='How much do you weigh in kg?', bg=bg, fg=fg, font=fonta).pack()
    t2=Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
    t2.pack()
    def valueb(t):
        x=t.get('1.0','end-1c')
        return x
    def submitb():
        global weight_kg
        global firstfourinputs
        try:
            weight_kg = float(valueb(t2))
        except ValueError:
            ValueError_M(True)
        else:
            ValueError_M(False)
            height_m = float(height_cm / 100)
            # BMI calculation
            if height_m != 0:
                bmi = weight_kg / (height_m * height_m)
            firstfourinputs[2] = True
    ttk.Button(window, text='Submit', command=submitb).pack()


    # Height text
    label_widget4 = Label(window, text='How tall are you in cm?', bg=bg, fg=fg, font=fonta).pack()
    t3=Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
    t3.pack()
    def valuec(t):
        x=t.get('1.0','end-1c')
        return x
    def submitc():
        global height_cm
        global height_m
        global bmi
        global firstfourinputs
        try:
            height_cm=float(valuec(t3))
        except ValueError:
            ValueError_M(True)
        else:
            ValueError_M(False)
            height_m = float(height_cm / 100)
            # BMI calculation
            bmi = weight_kg / (height_m * height_m)
            if bmi == 0:
                MissingValueError_M(True)
            else:
                MissingValueError_M(False)
                firstfourinputs[3] = True
    ttk.Button(window, text='Submit', command=submitc).pack()

    # Do you know your body fat percentage?
    label_widget5 = Label(window, text="Do you know your body fat percentage?", bg=bg, fg = fg, font=fonta).pack()

    def yes():
        if bfpercent_b_press == False and firstfourinputs == [True, True, True, True]:
            askforbodyfatpercentage()
            MissingValueError_M(False)
        else:
            MissingValueError_M(True)

    def no():
        if bfpercent_b_press == False and firstfourinputs == [True, True, True, True]:
            calculatebfpercent()
            MissingValueError_M(False)
        else:
            MissingValueError_M(True)

    yes_b = ttk.Button(window, text="Yes", command = yes, width='30').pack()
    no_b = ttk.Button(window, text="No", command = no, width='30').pack()

    def calculatebfpercent():
        global bfpercent_b_press
        bfpercent_b_press = True
        if gender == "male":
            calculatebfpercentmale()
        elif gender == 'female':
            calculatebfpercentfemale()

    def calculatebfpercentmale():
        # CNeck
        label_widget6 = Label(window, text='What is the circumference of your neck in Cm?', bg=bg, fg=fg, font=fonta).pack()
        t4 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t4.pack()
        def valued(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submitd():
            global cneck
            try:
                cneck = float(valued(t4))
            except ValueError:
                ValueError_M(True)
            else:
                ValueError_M(False)
        ttk.Button(window, text='Submit', command=submitd).pack()

        # CWaist
        label_widget7 = Label(window, text='What is the circumference of your waist in Cm?', bg=bg, fg=fg,font=fonta).pack()
        t5 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t5.pack()
        def valuee(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submite():
            global cwaist
            global bfpercent
            try:
                cwaist = float(valuee(t5))
            except ValueError:
                ValueError_M(True)
            else:
                ValueError_M(False)
                bfpercent = float(495 / (1.0324 - 0.19077 * math.log10(cwaist - cneck) + 0.15456 * math.log10(height_cm)) - 450)
                afterbfcalc()
        ttk.Button(window, text='Submit', command=submite).pack()

    def calculatebfpercentfemale():
        # CNeck
        label_widget6 = Label(window, text='What is the circumference of your neck in Cm?', bg=bg, fg=fg,font=fonta).pack()
        t4 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t4.pack()
        def valued(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submitd():
            global cneck
            cneck = float(valued(t4))
        ttk.Button(window, text='Submit', command=submitd).pack()

        # CWaist
        label_widget7 = Label(window, text='What is the circumference of your waist in Cm?', bg=bg, fg=fg,font=fonta).pack()
        t5 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t5.pack()
        def valuee(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submite():
            global cwaist
            cwaist = float(valuee(t5))
        ttk.Button(window, text='Submit', command=submite).pack()

        # Chips
        label_widget8 = Label(window, text='What is the circumference of your hips in Cm?', bg=bg, fg=fg,font=fonta).pack()
        t6 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t6.pack()
        def valuef(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submitf():
            global chips
            global bfpercent
            chips = float(valuef(t6))
            bfpercent = 495 / (1.29579 - 0.35004 * math.log10(cwaist + chips - cneck) + 0.22100 * math.log10(height_cm)) - 450
            afterbfcalc()
        ttk.Button(window, text='Submit', command=submitf).pack()

    def askforbodyfatpercentage():
        global bfpercent_b_press
        bfpercent_b_press = True
    # Know bfpercent
        label_widget9 = Label(window, text='What is your body fat percentage?', bg=bg, fg=fg,font=fonta).pack()
        t7 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t7.pack()
        def valueg(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submitg():
            global bfpercent
            try:
                bfpercent = float(valueg(t7))
            except ValueError:
                ValueError_M(True)
            else:
                ValueError_M(False)
                afterbfcalc()
        ttk.Button(window, text='Submit', command=submitg).pack()

    def afterbfcalc():
        global fbm
        global lbm
        global lfm
        global bmr
        fbm = weight_kg * (bfpercent / 100)
        lbm = weight_kg - fbm
        if gender == "male":
            bfpercent_r = round(bfpercent)
            if bfpercent_r in range(10, 14, 1):
                lfm = 1
            elif bfpercent_r in range(15, 20, 1):
                lfm = .95
            elif bfpercent_r in range(21, 28, 1):
                lfm = .90
            elif bfpercent_r > 28:
                lfm = .85
        # ADD WOMEN LFM
        bmr = weight_kg * 24 * lfm
        Almcalc()

    def Almcalc():
        label_widget10 = Label(window, text='What would you consider your activity level?', bg=bg, fg=fg,font=fontb).pack()
        label_widget11 = Label(window, text='1) Very Light - Typical office job (sitting, studying, little walking throughout the day)', bg=bg, fg=fg,font=fontc).pack()
        label_widget12 = Label(window, text='2) Light - Any job where you mostly stand or walk (teaching, shop/lab work, some walking throughout the day)', bg=bg, fg=fg, font=fontc).pack()
        label_widget13 = Label(window, text='3) Moderate - Jobs requiring physical activity (landscaping, cleaning, maintenance, jogging/biking/working out 2 hours per day)', bg=bg, fg=fg, font=fontc).pack()
        label_widget14 = Label(window, text='4) Heavy - Heavy manual labour (construction, dancer, athlete, hard physical activity 4 hours per day)', bg=bg, fg=fg, font=fontc).pack()
        label_widget15 = Label(window, text='5) Very Heavy - Moderate to hard physical activity 8 hours per day', bg=bg, fg=fg, font=fontc).pack()
        t8 = Text(window, height=1, width=8)
        t8.pack()
        def valuee(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submite():
            global alm_in
            global alm
            global cbpd
            try:
                alm_in = float(valuee(t8))
            except ValueError:
                ValueError_M(True)
            else:
                ValueError_M(False)
                if alm_in == 1:
                    alm = 1.3
                if alm_in == 2:
                    alm = 1.55
                if alm_in == 3:
                    alm = 1.65
                if alm_in == 4:
                    alm = 1.80
                if alm_in == 5:
                    alm = 2.00
                cbpd = bmr * alm
                Goal()
        ttk.Button(window, text='Submit', command=submite).pack()

    def Goal():
        label_widget16 = Label(window, text='Do you want to lose, maintain or gain weight?', bg=bg, fg=fg,font=fontb).pack()
        t9 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
        t9.pack()
        def valueh(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submith():
            global goal
            global cste
            global cte
            goal = valueh(t9)
            goal = goal.lower()
            if goal == "maintain":
                ValueError_M(False)
                cte = cbpd
                complete()
            elif goal == "gain":
                ValueError_M(False)
                cte = cbpd + 500
                complete()
            elif goal == "lose":
                ValueError_M(False)
                cte = cbpd - 500
                complete()
            else:
                ValueError_M(True)

        ttk.Button(window, text='Submit', command=submith).pack()

    def complete():
        for child in window.winfo_children():
            child.destroy()
        ListBodyComp()

    def ListBodyComp():
        global BodyComposition_data
        global date
        date = today.strftime("%d/%m/%Y")
        label_widget1 = Label(window, text='Age: {}'.format(age), bg=bg, fg=fg,font=fontb).pack()
        label_widget2 = Label(window, text='Gender: {}'.format(gender), bg=bg, fg=fg,font=fontb).pack()
        label_widget3 = Label(window, text='Height: {} cm'.format(height_cm), bg=bg, fg=fg,font=fontb).pack()
        label_widget4 = Label(window, text='Weight: {} kg'.format(weight_kg), bg=bg, fg=fg,font=fontb).pack()
        label_widget5 = Label(window, text='Lean Body Mass: {} kg'.format(lbm), bg=bg, fg=fg,font=fontb).pack()
        label_widget6 = Label(window, text='Fat Body Mass: {} kg'.format(fbm), bg=bg, fg=fg,font=fontb).pack()
        label_widget7 = Label(window, text='BMI: {}'.format(bmi), bg=bg, fg=fg,font=fontb).pack()
        label_widget8 = Label(window, text='Body Fat Percentage: {}%'.format(bfpercent), bg=bg, fg=fg,font=fontb).pack()
        label_widget9 = Label(window, text='Basal Metabolic Rate: {} calories'.format(bmr), bg=bg, fg=fg,font=fontb).pack()
        label_widget10 = Label(window, text='Calories Burned Per Day with exercise: {} calories'.format(cbpd), bg=bg, fg=fg,font=fontb).pack()
        label_widget11 = Label(window, text='Goal: {}'.format(goal), bg=bg, fg=fg,font=fontb).pack()
        label_widget12 = Label(window, text='Calories To Eat Per Day: {} calories'.format(cte), bg=bg, fg=fg,font=fontb).pack()
        BodyComposition_data = [age, gender, height_cm, weight_kg, lbm, fbm, bmi, bfpercent, bmr, cbpd, goal, cte, date]
        save(BodyComposition_data)
        Button(window, text='Back To Menu', command=StartMenu, width=width_b, height=height_b,font=font_B, fg=fg_b, bg=bg_b, highlightcolor=highlight_c_b).pack()


def Before_dietfunc():
    for child in window.winfo_children():
        child.destroy()
    label_widget1 = Label(window, text='Would you like to use the last Body Composition Test or Input your Calories Per Day Manually?', bg=bg, fg=fg, font=fonta).pack()

    t9 = Text(window, height=1, width=8, borderwidth=2, relief=RIDGE)
    t9.pack()

    def valueh(t):
        x = t.get('1.0', 'end-1c')
        return x

    def submith():
        global cte
        try:
            cte = float(valueh(t9))
        except ValueError:
            ValueError_M(True)
        else:
            ValueError_M(False)
            dietfunc()

    ttk.Button(window, text='Submit', command=submith).pack()


    def submitg():
        global past_bodycomposition
        global cte
        global cste
        global Foodsave

        with open(filename_body, 'rb') as filehandler:
            past_bodycomposition = pickle.load(filehandler)
        cte = past_bodycomposition[11]
        try:
            with open(filename_food, 'rb') as filehandler:
                Foodsave = pickle.load(filehandler)
        except IOError:
            cste=cte

        try:
            cste = Foodsave[0]
            if today != Foodsave[1]:
                cste = cte
        except IndexError:
            cste = cte
        dietfunc()
    ttk.Button(window, text='Use Past Values', command=submitg).pack()


def dietfunc():
    for child in window.winfo_children():
        child.destroy()


    label_widget1 = Label(window, text='What would you like to eat for breakfast?', bg=bg, fg=fg, font=fonta).pack()

    # Options for breakfast
    label_widget2 = Label(window, text='{}: {} calories per gram'.format(breakfasts[1], round(breakfasts_n[0, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget3 = Label(window, text='{}: {} calories per gram'.format(breakfasts[2], round(breakfasts_n[1, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget4 = Label(window, text='{}: {} calories per gram'.format(breakfasts[3], round(breakfasts_n[2, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget5 = Label(window, text='{}: {} calories per gram'.format(breakfasts[4], round(breakfasts_n[3, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget6 = Label(window, text='{}: {} calories per gram'.format(breakfasts[5], round(breakfasts_n[4, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    # label_widget7 = Label(window, text='{}: {} calories per gram'.format(breakfasts[6], round(breakfasts_n[0, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    # label_widget8 = Label(window, text='{}: {} calories per gram'.format(breakfasts[7], round(breakfasts_n[0, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    # label_widget9 = Label(window, text='{}: {} calories per gram'.format(breakfasts[8], round(breakfasts_n[0, 0], 2)),bg=bg, fg=fg, font=fontb).pack()


    t = Text(window, height=1, width=20,borderwidth=2, relief=RIDGE)
    t.pack()
    def valueg(t):
        x = t.get('1.0', 'end-1c')
        return x
    def submitg():
        global breakfast
        global breakfast_cal_per_g
        breakfast = [(valueg(t))]
        breakfast1_row_array = df_breakfast.index == breakfast[(len(breakfast)-1)]
        breakfast1_row = df_breakfast.loc[breakfast1_row_array]
        try:
            breakfast_cal_per_g = [breakfast1_row.iloc[0]['Calories per g']]
        except IndexError:
            ValueError_M(True)
        else:
            ValueError_M(False)
            morebreakfest_check()

    ttk.Button(window, text='Submit', command=submitg).pack()


def morebreakfest_check():
    label_widgeta = Label(window, text='Would you like to have something else to eat for breakfast?',bg=bg, fg=fg, font=fontb).pack()
    t = Text(window, height=1, width=20,borderwidth=2, relief=RIDGE)
    t.pack()
    def valueg(t):
        x = t.get('1.0', 'end-1c')
        return x
    def submitg():
        global breakfast_more
        breakfast_more = valueg(t)
        breakfast_more = breakfast_more.lower()
        morebreakfast()
    ttk.Button(window, text='Submit', command=submitg).pack()

def morebreakfast():
    global breakfast_more
    if breakfast_more == "no":
        ValueError_M(False)
        label_widgeta = Label(window, text='How much of your daily calorie limit would you like to use for {}?'.format(breakfast[(len(breakfast)-1)]), bg=bg,fg=fg, font=fontb).pack()
        t = Text(window, height=1, width=20,borderwidth=2, relief=RIDGE)
        t.pack()
        def valueg(t):
            x = t.get('1.0', 'end-1c')
            return x
        def submitg():
            global breakfast_percent
            global grams_of_breakfast
            global cste
            emptyarray = []
            if breakfast_percent == emptyarray:
                try:
                    breakfast_percent = [float(valueg(t))]
                except ValueError:
                    ValueError_M(True)
                else:
                    ValueError_M(False)
                    grams_of_breakfast = [(float(cte) / float(100) * float(breakfast_percent[len(breakfast_percent)-1])) / float(breakfast_cal_per_g[len(breakfast_cal_per_g)-1])]
                    cste = cste - (grams_of_breakfast[len(grams_of_breakfast)-1] * breakfast_cal_per_g[len(breakfast_cal_per_g)-1])

                    for child in window.winfo_children():
                        child.destroy()
                    breakfastplan()

            else:
                breakfast_percent += [(valueg(t))]
                grams_of_breakfast += [(float(cte) / float(100) * float(breakfast_percent[len(breakfast_percent)-1])) / float(breakfast_cal_per_g[len(breakfast_cal_per_g)-1])]
                cste = cste - (grams_of_breakfast[len(grams_of_breakfast) - 1] * breakfast_cal_per_g[len(breakfast_cal_per_g) - 1])
                for child in window.winfo_children():
                    child.destroy()
                breakfastplan()
        ttk.Button(window, text='Submit', command=submitg).pack()

    elif breakfast_more == "yes":
        ValueError_M(False)
        label_widget = Label(window, text='How much of your daily calorie limit would you like to use for {}?'.format(breakfast[len(breakfast)-1]), bg=bg, fg=fg, font=fontb).pack()
        t = Text(window, height=1, width=20,borderwidth=2, relief=RIDGE)
        t.pack()

        def valueg(t):
            x = t.get('1.0', 'end-1c')
            return x

        def submitg():
            global breakfast_percent
            global grams_of_breakfast
            global cste
            emptyarray = []
            if breakfast_percent == emptyarray:
                breakfast_percent = [valueg(t)]
                grams_of_breakfast = [(float(cte) / float(100) * float(breakfast_percent[len(breakfast_percent) - 1])) / float(breakfast_cal_per_g[len(breakfast_cal_per_g) - 1])]
                cste = cste - (grams_of_breakfast[len(grams_of_breakfast) - 1] * breakfast_cal_per_g[len(breakfast_cal_per_g) - 1])
                morebreakfast_cont()
            else:
                breakfast_percent +=[(valueg(t))]
                grams_of_breakfast += [(float(cte) / float(100) * float(breakfast_percent[len(breakfast_percent) - 1])) / float(breakfast_cal_per_g[len(breakfast_cal_per_g) - 1])]
                cste = cste - (grams_of_breakfast[len(grams_of_breakfast) - 1] * breakfast_cal_per_g[
                    len(breakfast_cal_per_g) - 1])
                morebreakfast_cont()
        ttk.Button(window, text='Submit', command=submitg).pack()
    else:
        ValueError_M(True)

def morebreakfast_cont():
    for child in window.winfo_children():
        child.destroy()

    label_widget1 = Label(window,text='What else would you like to eat', bg=bg, fg=fg,font=fonta).pack()
    label_widget2 = Label(window,text='{}: {} calories per gram'.format(breakfasts[1], round(breakfasts_n[0, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget3 = Label(window,text='{}: {} calories per gram'.format(breakfasts[2], round(breakfasts_n[1, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget4 = Label(window,text='{}: {} calories per gram'.format(breakfasts[3], round(breakfasts_n[2, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget5 = Label(window,text='{}: {} calories per gram'.format(breakfasts[4], round(breakfasts_n[3, 0], 2)),bg=bg, fg=fg, font=fontb).pack()
    label_widget6 = Label(window,text='{}: {} calories per gram'.format(breakfasts[5], round(breakfasts_n[4, 0], 2)),bg=bg, fg=fg, font=fontb).pack()

    t = Text(window, height=1, width=20,borderwidth=2, relief=RIDGE)
    t.pack()
    def valueg(t):
        x = t.get('1.0', 'end-1c')
        return x

    def submitg():
        global breakfast
        global breakfast_cal_per_g
        breakfast += [(valueg(t))]
        breakfast_row_array = df_breakfast.index == breakfast[(len(breakfast) - 1)]
        breakfast_row = df_breakfast.loc[breakfast_row_array]
        breakfast_cal_per_g = [(breakfast_row.iloc[0]['Calories per g'])]
        morebreakfest_check()

    ttk.Button(window, text='Submit', command=submitg).pack()


def breakfastplan():
    global Foodsave
    Foodsave = [cste, today]
    savefood(Foodsave)
    label_widget = Label(window, text='Breakfast', bg=bg, fg=fg,font=fonta).pack()
    totalbreakfastpercent =100-(cste/cte*100)
    for i in range(len(breakfast)):
        label_widget1 = Label(window, text='{} - {}g'.format(breakfast[i], grams_of_breakfast[i]), bg=bg,fg=fg, font=fontb).pack()
    for z in range(len(breakfast_percent)):
        totalbreakfastpercent = totalbreakfastpercent+int(breakfast_percent[z])
    label_widget3 = Label(window, text='Total Percent Of Daily Calories Used: {}%'.format(totalbreakfastpercent), bg=bg, fg=fg, font=fontb).pack()
    label_widget4 = Label(window, text='Calories Still To Eat: {} calories'.format(cste),bg=bg, fg=fg, font=fontb).pack()
    ttk.Button(window, text='Back To Menu', command=StartMenu).pack()


# Past Body Composition Func
def pastbodycompositionfunc():
    global past_bodycomposition
    with open(filename_body, 'rb') as filehandler:
        past_bodycomposition = pickle.load(filehandler)

    for child in window.winfo_children():
        child.destroy()

    Title = Label(window, text='Past Body Composition', bg=bg, fg=fg,font=fonta).pack()
    label_widget = Label(window, text='Date: {}'.format(past_bodycomposition[12]), bg=bg, fg=fg,font=fontb).pack()
    label_widget1 = Label(window, text='Age: {}'.format(past_bodycomposition[0]), bg=bg, fg=fg, font=fontb).pack()
    label_widget2 = Label(window, text='Gender: {}'.format(past_bodycomposition[1]), bg=bg, fg=fg, font=fontb).pack()
    label_widget3 = Label(window, text='Height: {} cm'.format(past_bodycomposition[2]), bg=bg, fg=fg,font=fontb).pack()
    label_widget4 = Label(window, text='Weight: {} kg'.format(past_bodycomposition[3]), bg=bg, fg=fg,font=fontb).pack()
    label_widget5 = Label(window, text='Lean Body Mass: {} kg'.format(past_bodycomposition[4]), bg=bg, fg=fg,font=fontb).pack()
    label_widget6 = Label(window, text='Fat Body Mass: {} kg'.format(past_bodycomposition[5]), bg=bg, fg=fg,font=fontb).pack()
    label_widget7 = Label(window, text='BMI: {}'.format(past_bodycomposition[6]), bg=bg, fg=fg, font=fontb).pack()
    label_widget8 = Label(window, text='Body Fat Percentage: {}%'.format(past_bodycomposition[7]), bg=bg, fg=fg,font=fontb).pack()
    label_widget9 = Label(window, text='Basal Metabolic Rate: {} calories'.format(past_bodycomposition[8]), bg=bg, fg=fg,font=fontb).pack()
    label_widget10 = Label(window, text='Calories Burned Per Day with exercise: {} calories'.format(past_bodycomposition[9]), bg=bg,fg=fg, font=fontb).pack()
    label_widget11 = Label(window, text='Goal: {}'.format(past_bodycomposition[10]), bg=bg, fg=fg, font=fontb).pack()
    label_widget12 = Label(window, text='Calories To Eat Per Day: {} calories'.format(past_bodycomposition[11]), bg=bg, fg=fg,font=fontb).pack()
    ttk.Button(window, text='Back To Menu', command=StartMenu).pack()



# Starting Menu
def StartMenu():
    for child in window.winfo_children():
        child.destroy()
    Title = Label(window, text="Please select An Option?", bg=bg, fg=fg,font=fontd).pack(ipady=50)

    bodycompositionfunc_B = Button(window, text="Body Composition", command=bodycompositionfunc, width=width_b, height=height_b, font=font_B, fg=fg_b, bg=bg_b, highlightcolor=highlight_c_b).pack(ipady=10)
    diet_B = Button(window, text="Food Calculator", command=Before_dietfunc, width=width_b, height=height_b, font=font_B, fg=fg_b, bg=bg_b, highlightcolor=highlight_c_b).pack(ipady=10)
    past_bodycompositionfunc_B = Button(window, text="Past Body Composition", command=pastbodycompositionfunc, width=width_b, height=height_b, font=font_B, fg=fg_b, bg=bg_b, highlightcolor=highlight_c_b).pack(ipady=10)

window.title('Body Composition & Diet App')
window.geometry("{}x{}".format(screen_width, screen_height))
window.resizable(height = screen_height, width = screen_width)
window.configure(bg=bg)
StartMenu()
def Main():
    window.mainloop()

if __name__ == "__main__":
    Main()