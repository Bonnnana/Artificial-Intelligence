from constraint import *


# def func(*variables):
#     t1, t2, t3, t4 = 0, 0, 0, 0
#     for var in variables:
#         if var == "T1":
#             t1 += 1
#             if t1 > 4:
#                 return False
#         if var == "T2":
#             t2 += 1
#             if t2 > 4:
#                 return False
#         if var == "T3":
#             t3 += 1
#             if t3 > 4:
#                 return False
#         if var == "T4":
#             t4 += 1
#             if t4 > 4:
#                 return False
#     return True

def func(*variables):
    count = {}
    for arg in variables:
        if arg in count:
            count[arg] += 1
        else:
            count[arg] = 1
        if count[arg] > 4:
            return False
    return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []
    for title, topic in papers.items():
        var = f"{title} ({topic})"
        variables.append(var)

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata

    problem.addConstraint(func, variables)


    values_AI = [f"{title} ({topic})" for title, topic in papers.items() if topic=="AI"]
    values_ML = [f"{title} ({topic})" for title, topic in papers.items() if topic=="ML"]
    values_NLP = [f"{title} ({topic})" for title, topic in papers.items() if topic=="NLP"]

    if len(values_AI) <= 4:
        problem.addConstraint(AllEqualConstraint(), values_AI)
    if 0 < len(values_ML) <= 4:
        problem.addConstraint(AllEqualConstraint(), values_ML)
    if len(values_NLP) <= 4:
        problem.addConstraint(AllEqualConstraint(), values_NLP)


    # Tuka dodadete go kodot za pechatenje
    solution = problem.getSolution()
    for variable in variables:
        print(f"{variable}: {solution[variable]}")




