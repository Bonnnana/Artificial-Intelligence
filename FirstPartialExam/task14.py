from constraint import *

def func(v1,v2,v3,v4):
    vreme_simona = [13, 14, 16, 19]
    vreme_marija = [14, 15, 18]
    vreme_petar = [12, 13, 16, 17, 18, 19]

    if v1 == 0:
        return False
    else:
        if v2 == 1 and v3 == 0:
            for vreme in vreme_marija:
                if vreme in vreme_simona:
                    if vreme == v4:
                        return True
        elif v2==0 and v3==1:
            for vreme in vreme_petar:
                if vreme in vreme_simona:
                    if vreme == v4:
                        return True






if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())


    vreme_sostanok = list(range(12, 20))

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", vreme_sostanok)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(InSetConstraint([1]),  ["Simona_prisustvo"])
    problem.addConstraint(SomeInSetConstraint([1]), ["Marija_prisustvo", "Petar_prisustvo"])

    problem.addConstraint(func, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    # ----------------------------------------------------

    solutions = problem.getSolutions()
    for solution in solutions:
        reordered_solution = {'Simona_prisustvo': solution['Simona_prisustvo'],
                              'Marija_prisustvo': solution['Marija_prisustvo'],
                              'Petar_prisustvo': solution['Petar_prisustvo'],
                              'vreme_sostanok': solution['vreme_sostanok']}
        print(reordered_solution)

