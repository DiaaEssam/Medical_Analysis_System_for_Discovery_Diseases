
from tkinter import messagebox
from tkinter import *
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

# Here we prove if the patient has diabetes (Strong Symptoms)
def bc_has_diabetes():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_diabetes($a, $b)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg1="Unfortunately, He/She has strong symptoms of Diabetes"
        else:
            msg1 = "He/She is alright"

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg1

# Here we prove if the patient has diabetes (Weak Symptoms)
def bc_maybe_diabetes():

    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.maybe_diabetes($d, $e)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg2="Unfortunately, He/She has weak symptoms of Diabetes"
        else:
            msg2 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg2

# Here we prove if the patient has Cardiovascular Disease
def bc_has1_cardio():

    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_cardio($f)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg3="Unfortunately, He/She has strong symptoms of CardioVascular Disease"
        else:
            msg3 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg3

# Here we prove if the patient has Cardiovascular Disease
def bc_has3_cardio():

    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_cardio($f, $g, $h)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg4="Unfortunately, He/She has strong symptoms of CardioVascular Disease"
        else:
            msg4 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg4


# Here we prove if the patient has Hypertension (Common Symptoms)
def bc_has1_hyper():

    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_hyper($f)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg5="Unfortunately, He/She has strong symptoms of Hypertension"
        else:
            msg5 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg5


# Here we prove if the patient has Hypertension (Accurate Symptoms)
def bc_has2_hyper():

    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_hyper($f , $g)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg6="Unfortunately, He/She has strong symptoms of Hypertension"
        else:
            msg6 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg6


# Here we prove if the patient has Dyslipidemia Disease (Strong Symptoms)
def bc_has_dysli():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_dysli($a, $b)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg7="Unfortunately, He/She has strong symptoms of Dyslipidemia"
        else:
            msg7 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg7


# Here we prove if the patient has Dyslipidemia Disease (Weak Symptoms)
def bc_maybe_dysli():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.maybe_dysli($d)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg8="Unfortunately, He/She has weak symptoms of Dyslipidemia"
        else:
            msg8 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg8


# Here we prove if the patient has obesity
def bc_has1_obes():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_obes($d)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg9="Unfortunately, He/She is Overweight"
        else:
            msg9 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg9


# Here we prove if the patient has obesity
def bc_has3_obes():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_obes($d, $e, $f)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg10="since He/She is overweight Therefore He/She has high risk of complications of %s , %s ,%s " % (vars['d'], vars['e'], vars['f'])
        else:
            msg10 = "He/She is alright"

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg10


# Here we prove if the patient has Peripheral Neuropathy
def bc_has2_neuro():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_neuro($a, $b)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg11="since He/She has %s and %s therefore He/She has Peripheral neuropathy which can lead to blistering of the skin" % (vars['a'], vars['b'])
        else:
            msg11 = "He/She is alright"

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg11


# Here we prove if the patient has Peripheral Neuropathy
def bc_has1_neuro():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_neuro($a)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg12="since He/She has %s therefore He/She can suffer from Peripheral neuropathy as complication of disease" % (vars['a'])
        else:
            msg12 = "He/She is alright"



    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg12


# Here we prove if the patient has Peripheral Arterial
def bc_has_arterial():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_arty($a, $b)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg13="since He/She has %s and %s therefore He/She has Peripheral Arterial" % (vars['a'], vars['b'])
        else:
            msg13 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg13


# Here we prove if the patient has Diabetic Foot Disease
def bc_has_foot():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_foot($a, $b, $c)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg14="since He/She has %s , %s  and %s therefore He/She has Diabetic Foot Disease" % (vars['a'], vars['b'], vars['c'])
        else:
            msg14 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg14


# Here we prove if the patient has Metabolic Syndrome
def bc_has_meta():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_meta($a, $b)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg15="Unfortunately, He/She has Metabolic Syndrome"
        else:
            msg15 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg15


# Here we prove if the patient has Atherosclerosis
def bc_has_ather():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('medical_rules')

    flag = False

    try:
        with engine.prove_goal('medical_rules.has_ather($a, $b)') as gen:
            for vars, plan in gen:
                flag = True

        if flag == True:
            msg16="since He/She has %s , %s therefore u have Atherosclerosis" % (vars['a'], vars['b'])
        else:
            msg16 = "He/She is alright"


    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    return msg16
