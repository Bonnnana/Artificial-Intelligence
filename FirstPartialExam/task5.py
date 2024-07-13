from constraint import *


def checkvalid_all(termin1, termin2):
    # moze i so split('_')

    day1 = termin1[:3]
    day2 = termin2[:3]

    hour1 = termin1[-2:]
    hour2 = termin2[-2:]
    if day1 == day2 and abs(int(hour1) - int(hour2)) < 2:
        return False

    return True

def func(*variables):
    time = []
    for var in variables:
        time.append(var[-2:])

    return len(time) == len(set(time))


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    variables = []
    variables_ml = []

    for i in range(casovi_AI):
        problem.addVariable(f"AI_cas_{i + 1}", AI_predavanja_domain)
        variables.append(f"AI_cas_{i + 1}")

    for i in range(casovi_ML):
        problem.addVariable(f"ML_cas_{i + 1}", ML_predavanja_domain)
        variables_ml.append(f"ML_cas_{i + 1}")
        variables.append(f"ML_cas_{i + 1}")

    for i in range(casovi_R):
        problem.addVariable(f"R_cas_{i + 1}", R_predavanja_domain)
        variables.append(f"R_cas_{i + 1}")

    for i in range(casovi_BI):
        problem.addVariable(f"BI_cas_{i + 1}", BI_predavanja_domain)
        variables.append(f"BI_cas_{i + 1}")

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    variables_ml.append("ML_vezbi")
    variables.append("AI_vezbi")
    variables.append("ML_vezbi")
    variables.append("BI_vezbi")
    # ---Tuka dodadete gi ogranichuvanjata----------------

    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            problem.addConstraint(checkvalid_all, (variables[i], variables[j]))
    problem.addConstraint(func, variables_ml)

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
