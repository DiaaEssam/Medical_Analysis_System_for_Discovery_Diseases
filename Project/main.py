import sys
import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import *

# The following command points your notebook to the location of a folder outside your working directory that you want to import.
sys.path.append('..\project')


if(os.path.exists('C:/Users/Diaa Essam/PycharmProjects/pythonProject8/__pycache__')):
    shutil.rmtree('C:/Users/Diaa Essam/PycharmProjects/pythonProject8/__pycache__')
if(os.path.exists('C:/Users/Diaa Essam/PycharmProjects/pythonProject8/compiled_krb')):
    shutil.rmtree('C:/Users/Diaa Essam/PycharmProjects/pythonProject8/compiled_krb')

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

root = tk.Tk()
root.title('Medical analysis system for discovery diseases')
canvas1 = tk.Canvas(root, width=50, height=25)
canvas1.pack()
canvas2 = tk.Canvas(root, width=50, height=25)
canvas2.pack()
canvas3 = tk.Canvas(root, width=50, height=25)
canvas3.pack()
canvas4 = tk.Canvas(root, width=50, height=25)
canvas4.pack()
canvas5 = tk.Canvas(root, width=50, height=25)
canvas5.pack()
canvas6 = tk.Canvas(root, width=50, height=25)
canvas6.pack()
canvas7 = tk.Canvas(root, width=50, height=25)
canvas7.pack()
canvas8 = tk.Canvas(root, width=50, height=25)
canvas8.pack()
canvas9 = tk.Canvas(root, width=50, height=25)
canvas9.pack()
canvas10 = tk.Canvas(root, width=50, height=25)
canvas10.pack()
canvas11 = tk.Canvas(root, width=50, height=25)
canvas11.pack()
canvas12 = tk.Canvas(root, width=50, height=25)
canvas12.pack()
canvas13 = tk.Canvas(root, width=50, height=25)
canvas13.pack()
canvas14 = tk.Canvas(root, width=50, height=25)
canvas14.pack()
canvas15 = tk.Canvas(root, width=50, height=25)
canvas15.pack()
canvas16 = tk.Canvas(root, width=50, height=25)
canvas16.pack()
canvas17 = tk.Canvas(root, width=50, height=25)
canvas17.pack()



msgs=[]
def has_diabetes():
    msg_box1 = tk.messagebox.askquestion('have_polydipsia', 'Does he/she get thirsty more than usual?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'
    msg_box2 = tk.messagebox.askquestion('have_polyurea', 'Does he/she urinate more than usual in the day with an increase in the volume of urine excreted?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'
    msg_box3 = tk.messagebox.askquestion('have_polyphagia', 'Does he/she have Polyphagia?',
                                         icon='info')
    if (msg_box3 == "yes"):
        msg_box3 = 'True'
    else:
        msg_box3 = 'False'
    replace_line('medical_rules.krb', 5, '        $ans1=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 6, '        $ans3=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 13, '        $ans2=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 14, '        $ans3=' + msg_box3 + '\n')
    import diagnosis
    msgs.append(diagnosis.bc_has_diabetes())

button1 = tk.Button(root, text='Diabetes - Strong Sign', command=has_diabetes, bg='green', fg='white')
canvas1.create_window(25, 15, window=button1)
def maybe_diabetes():
    msg_box1 = tk.messagebox.askquestion('have_WeightLoss', 'Does he/she suffer from Weight Loss?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'
    msg_box2 = tk.messagebox.askquestion('have_weakImmunity', 'Does he/she get flu more often?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    replace_line('medical_rules.krb', 21, '        $ans4=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 22, '        $ans5=' + msg_box2 + '\n')
    import diagnosis
    msgs.append(diagnosis.bc_maybe_diabetes())

button2 = tk.Button(root, text='Diabetes - Weak Sign', command=maybe_diabetes, bg='green', fg='white')
canvas2.create_window(25, 15, window=button2)

def has1_cardio():
    msg_box1 = tk.messagebox.askquestion('have_atherosclerosis', 'Does he/she suspect having lesions?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    msg_box2 = tk.messagebox.askquestion('have_exhaust', 'Does he/she suffer from Exhaustion?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    msg_box3 = tk.messagebox.askquestion('have_shortBreath', 'Does he/she suffer from Shortness of Breath?',
                                         icon='info')
    if (msg_box3 == "yes"):
        msg_box3 = 'True'
    else:
        msg_box3 = 'False'

    msg_box4 = tk.messagebox.askquestion('have_anginaPectoris', 'Does he/she suffer from Chest Pain?',
                                         icon='info')
    if (msg_box4 == "yes"):
        msg_box4 = 'True'
    else:
        msg_box4 = 'False'

    msg_box5 = tk.messagebox.askquestion('have_legPain', 'Does he/she suffer from Leg Pain?',
                                         icon='info')
    if (msg_box5 == "yes"):
        msg_box5 = 'True'
    else:
        msg_box5 = 'False'

    replace_line('medical_rules.krb', 51, '        $ans6=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 52, '        $ans8=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 53, '        $ans7=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 54, '        $ans9=' + msg_box4 + '\n')
    replace_line('medical_rules.krb', 81, '        $ans9=' + msg_box4 + '\n')
    replace_line('medical_rules.krb', 82, '        $ans11=' + msg_box5 + '\n')


    import diagnosis
    msgs.append(diagnosis.bc_has1_cardio())

button3 = tk.Button(root, text='CardioVascular1', command=has1_cardio, bg='green', fg='white')
canvas3.create_window(25, 15, window=button3)

def has3_cardio():
    msg_box1 = tk.messagebox.askquestion('have_atherosclerosis', 'Does he/she suspect having lesions?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    msg_box2 = tk.messagebox.askquestion('have_shortBreath', 'Does he/she suffer from Shortness of Breath?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    msg_box3 = tk.messagebox.askquestion('have_exhaust', 'Does he/she suffer from Exhaustion?',
                                         icon='info')
    if (msg_box3 == "yes"):
        msg_box3 = 'True'
    else:
        msg_box3 = 'False'

    msg_box4 = tk.messagebox.askquestion('have_anginaPectoris', 'Does he/she suffer from Chest Pain?',
                                         icon='info')
    if (msg_box4 == "yes"):
        msg_box4 = 'True'
    else:
        msg_box4 = 'False'

    replace_line('medical_rules.krb', 29, '        $ans6=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 30, '        $ans7=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 31, '        $ans8=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 32, '        $ans9=' + msg_box4 + '\n')
    replace_line('medical_rules.krb', 40, '        $ans6=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 41, '        $ans7=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 42, '        $ans8=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 43, '        $ans9=' + msg_box4 + '\n')


    import diagnosis
    msgs.append(diagnosis.bc_has3_cardio())


button4 = tk.Button(root, text='CardioVascular2', command=has3_cardio, bg='green', fg='white')
canvas4.create_window(25, 15, window=button4)


def has1_hyper():
    msg_box1 = tk.messagebox.askquestion('have_headache', 'Does he/she get headaches more often?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    replace_line('medical_rules.krb', 65, '        $ans10=' + msg_box1 + '\n')

    import diagnosis
    msgs.append(diagnosis.bc_has1_hyper())

button5 = tk.Button(root, text='Hypertension - Most Common Sign', command=has1_hyper, bg='green', fg='white')
canvas5.create_window(25, 15, window=button5)


def has2_hyper():
    msg_box1 = tk.messagebox.askquestion('have_headache', 'Does he/she get headaches more often?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    def check():
        if(int(e1.get())>200 or int(e1.get())<1 or int(e2.get())>200 or int(e2.get())<1):
            messagebox.showwarning("warning",'you must enter numbers between 1 and 200')
            sys.exit(1)

    subroot = tk.Tk()
    Label(subroot, text='Enter SYSTOLIC mm Hg [1-200]').grid(row=0)
    Label(subroot, text='Enter DIASTOLIC mm Hg [1-200]').grid(row=1)
    e1 = Entry(subroot)
    e2 = Entry(subroot)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    tk.Button(subroot,
              text='Quit',
              command=subroot.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(subroot,
              text='Enter',command=check).grid(row=3,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
    subroot.mainloop()

    replace_line('medical_rules.krb', 71, '        $ans10=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 72, '        $ans19=' + e1.get() + '\n')
    replace_line('medical_rules.krb', 73, '        $ans20=' + e2.get() + '\n')

    import diagnosis
    msgs.append(diagnosis.bc_has2_hyper())



button6 = tk.Button(root, text='Hypertension - Most Accurate Sign', command=has2_hyper, bg='green', fg='white')
canvas6.create_window(25, 15, window=button6)


def has_dysli():
    msg_box1 = tk.messagebox.askquestion('have_anginaPectoris', 'Does he/she suffer from Chest Pain?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    msg_box2 = tk.messagebox.askquestion('have_legPain', 'Does he/she suffer from Leg Pain?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    replace_line('medical_rules.krb', 81, '        $ans9=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 82, '        $ans11=' + msg_box2 + '\n')

    import diagnosis
    msgs.append(diagnosis.bc_has_dysli())


button7 = tk.Button(root, text='Dyslipidemia - Strong Sign', command=has_dysli, bg='green', fg='white')
canvas7.create_window(25, 15, window=button7)


def maybe_dysli():
    msg_box1 = tk.messagebox.askquestion('have_shortBreath', 'Does he/she suffer from Shortness of Breath?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    replace_line('medical_rules.krb', 89, '        $ans22=' + msg_box1 + '\n')
    import diagnosis
    msgs.append(diagnosis.bc_maybe_dysli())



button8 = tk.Button(root, text='Dyslipidemia - Weak Sign', command=maybe_dysli, bg='green', fg='white')
canvas8.create_window(25, 15, window=button8)


def has1_obes():

    def check():
        if(int(e1.get())>200 or int(e1.get())<1):
            messagebox.showwarning("warning",'you must enter number between 1 and 200')
            sys.exit(1)

    subroot = tk.Tk()
    Label(subroot, text='Enter his/her BMI [1-200]').grid(row=0)
    e1 = Entry(subroot)
    e1.grid(row=0, column=1)
    tk.Button(subroot,
              text='Quit',
              command=subroot.quit).grid(row=2,
                                         column=0,
                                         sticky=tk.W,
                                         pady=4)
    tk.Button(subroot,
              text='Enter',command=check).grid(row=2,
                                 column=1,
                                 sticky=tk.W,
                                 pady=4)
    subroot.mainloop()

    replace_line('medical_rules.krb', 95, '        $ans21=' + e1.get() + '\n')

    import diagnosis
    msgs.append(diagnosis.bc_has1_obes())


button9 = tk.Button(root, text='Obesity1', command=has1_obes, bg='green', fg='white')
canvas9.create_window(25, 15, window=button9)

def has3_obes():

    import diagnosis
    has1_obes()
    msgs.append(diagnosis.bc_has3_obes())

button10 = tk.Button(root, text='Obesity2', command=has3_obes, bg='green', fg='white')
canvas10.create_window(25, 15, window=button10)

def has1_neuro():

    has_diabetes()
    msg_box1 = tk.messagebox.askquestion('have_strain', 'Does he/she have any muscle strain or Pain in foot?',
                                         icon='info')
    if (msg_box1 == "yes"):
        msg_box1 = 'True'
    else:
        msg_box1 = 'False'

    msg_box2 = tk.messagebox.askquestion('have_weak_muscles', 'Does he/she have weakness in peripheral muscles?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    msg_box3 = tk.messagebox.askquestion('have_delay_wound', 'Does he/she have any foot & toes gangrene or Delayed wound healing?',
                                         icon='info')
    if (msg_box3 == "yes"):
        msg_box3 = 'True'
    else:
        msg_box3 = 'False'



    replace_line('medical_rules.krb', 177, '        $ans16=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 178, '        $ans17=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 179, '        $ans18=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 186, '        $ans16=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 187, '        $ans17=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 188, '        $ans18=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 195, '        $ans16=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 196, '        $ans17=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 197, '        $ans18=' + msg_box3 + '\n')
    import diagnosis
    msgs.append(diagnosis.bc_has1_neuro())

button11 = tk.Button(root, text='Peripheral neuropathy1', command=has1_neuro, bg='green', fg='white')
canvas11.create_window(25, 15, window=button11)


def has2_neuro():
    msg_box1 = tk.messagebox.askquestion('have_numbness', 'Does he/she often feel numb?',
                                        icon='info')
    if(msg_box1=="yes"):
        msg_box1='True'
    else:
        msg_box1='False'

    msg_box2 = tk.messagebox.askquestion('have_tingle', 'Does he/she have any tingling in your feet or hands?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    msg_box3 = tk.messagebox.askquestion('have_burn_pain', 'Does he/she have any burning pain?',
                                         icon='info')
    if (msg_box3 == "yes"):
        msg_box3 = 'True'
    else:
        msg_box3 = 'False'

    msg_box4 = tk.messagebox.askquestion('have_redness', 'Does he/she have any redness?',
                                         icon='info')
    if (msg_box4 == "yes"):
        msg_box4 = 'True'
    else:
        msg_box4 = 'False'

    replace_line('medical_rules.krb', 106, '        $ans12=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 107, '        $ans13=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 108, '        $ans14=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 109, '        $ans15=' + msg_box4 + '\n')

    replace_line('medical_rules.krb', 115, '        $ans12=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 116, '        $ans13=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 117, '        $ans14=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 118, '        $ans15=' + msg_box4 + '\n')

    replace_line('medical_rules.krb', 125, '        $ans12=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 126, '        $ans13=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 127, '        $ans14=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 128, '        $ans15=' + msg_box4 + '\n')

    replace_line('medical_rules.krb', 135, '        $ans12=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 136, '        $ans13=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 137, '        $ans14=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 138, '        $ans15=' + msg_box4 + '\n')

    replace_line('medical_rules.krb', 145, '        $ans12=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 146, '        $ans13=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 147, '        $ans14=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 148, '        $ans15=' + msg_box4 + '\n')

    replace_line('medical_rules.krb', 155, '        $ans12=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 156, '        $ans13=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 157, '        $ans14=' + msg_box3 + '\n')
    replace_line('medical_rules.krb', 158, '        $ans15=' + msg_box4 + '\n')

    import diagnosis
    msgs.append(diagnosis.bc_has2_neuro())

button12 = tk.Button(root, text='Peripheral neuropathy2', command=has2_neuro, bg='green', fg='white')
canvas12.create_window(25, 15, window=button12)


def has_arterial():
    msg_box1 = tk.messagebox.askquestion('have_strain', 'Does he/she have any muscle strain or Pain in foot?',
                                         icon='info')
    if (msg_box1 == "yes"):
        msg_box1 = 'True'
    else:
        msg_box1 = 'False'

    msg_box2 = tk.messagebox.askquestion('have_weak_muscles', 'Does he/she have weakness in peripheral muscles?',
                                         icon='info')
    if (msg_box2 == "yes"):
        msg_box2 = 'True'
    else:
        msg_box2 = 'False'

    msg_box3 = tk.messagebox.askquestion('have_delay_wound',
                                         'Does he/she have any foot & toes gangrene or Delayed wound healing?',
                                         icon='info')
    if (msg_box3 == "yes"):
        msg_box3 = 'True'
    else:
        msg_box3 = 'False'


    replace_line('medical_rules.krb', 177, '        $ans16=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 178, '        $ans17=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 179, '        $ans18=' + msg_box3 + '\n')

    replace_line('medical_rules.krb', 186, '        $ans16=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 187, '        $ans17=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 188, '        $ans18=' + msg_box3 + '\n')

    replace_line('medical_rules.krb', 195, '        $ans16=' + msg_box1 + '\n')
    replace_line('medical_rules.krb', 196, '        $ans17=' + msg_box2 + '\n')
    replace_line('medical_rules.krb', 197, '        $ans18=' + msg_box3 + '\n')

    import diagnosis
    msgs.append(diagnosis.bc_has_arterial())

button13 = tk.Button(root, text='Peripheral Arterial', command=has_arterial, bg='green', fg='white')
canvas13.create_window(25, 15, window=button13)

def has_foot():
    has_arterial()
    has2_neuro()
    has_diabetes()
    import diagnosis
    msgs.append(diagnosis.bc_has_foot())

button14 = tk.Button(root, text='Diabetic Foot', command=has_foot, bg='green', fg='white')
canvas14.create_window(25, 15, window=button14)


def has_meta():
    has2_hyper()
    has1_obes()
    has_diabetes()
    has_dysli()
    import diagnosis
    msgs.append(diagnosis.bc_has_meta())

button15 = tk.Button(root, text='Metabolic Syndrome', command=has_meta, bg='green', fg='white')
canvas15.create_window(25, 15, window=button15)

def has_ather():
    has_meta()
    has_diabetes()
    import diagnosis
    msgs.append(diagnosis.bc_has_ather())

button16 = tk.Button(root, text='Atherolsclerosis', command=has_ather, bg='green', fg='white')
canvas16.create_window(25, 15, window=button16)
button17 = tk.Button(root, text='Show final result', command=root.quit, bg='red', fg='white')
canvas17.create_window(25, 15, window=button17)
root.mainloop()
messagebox.showinfo("Final Result",msgs[-1] )
