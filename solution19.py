from operator import itemgetter
from math import inf
data = []
nb_books = 0
nb_libraries = 0
nb_days = 0
books = []
libraries = []

class Library:
    def __init__(self, nb_books, signup_time, books_per_day):
        self.nb_books = nb_books
        self.signup_time = signup_time
        self.books_per_day = books_per_day
    

with open('f_libraries_of_the_world.txt', 'r') as inputs:
    tmp = inputs.readline().strip("\n").split(" ")
    nb_books = int(tmp[0])
    nb_libraries = int(tmp[1])
    nb_days = int(tmp[2])
    
    books = list(map(int, inputs.readline().strip("\n").split(" ")))

    state = 0
    for line in inputs:
        if line.strip("\n").split(" ") == ['']:
                continue
        if not state:
            tmp = list(map(int, line.strip("\n").split(" ")))
            libraries.append(Library(tmp[0], tmp[1], tmp[2]))
            state = 1
        else:
            tmp = list(map(int, line.strip("\n").split(" ")))
            libraries[-1].books = tmp
            state = 0

#print(books)
#print(libraries)

lib_scores = []

scanned_books = {}
# Meer boeken POSITIEF
# Lager aantal dagen POSTIEF
min_signup = inf
max_signup = 0
min_score = inf
max_score = 0

for i in range(len(libraries)):
    tmp_score = 0
    for book in libraries[i].books:
        tmp_score += books[book]
        if book in scanned_books:
            scanned_books[book] += (i)
        else:
            scanned_books[book] = (i)
    if libraries[i].signup_time > max_signup:
        max_signup = libraries[i].signup_time
    if libraries[i].signup_time < min_signup:
        min_signup = libraries[i].signup_time
    tmp_score = tmp_score/len(libraries[i].books)
    if tmp_score > max_score:
        max_score = tmp_score
    if tmp_score < min_score:
        min_score = tmp_score

    
for i in range(len(libraries)):
    tmp_score = 0
    for book in libraries[i].books:
        tmp_score += books[book]
    tmp_score = tmp_score/len(libraries[i].books)
    if max_score == min_score:
        tmp_score = 0
    else:
        tmp_score = (tmp_score - min_score)/(max_score-min_score)
    if  max_signup == min_signup:
        tmp_signup = 0
    else:
        tmp_signup = 1 - (libraries[i].signup_time - min_signup)/(max_signup-min_signup)
    lib_scores.append([i,  tmp_score+tmp_signup])



lib_scores = sorted(lib_scores, key=itemgetter(1), reverse=True)
print(lib_scores)
days_occupied = 0
i = 0
final_libs = []
while days_occupied < nb_days and i < len(lib_scores):
    final_libs.append(lib_scores[i][0])
    days_occupied += libraries[lib_scores[i][0]].signup_time
    i+=1

final_books = []
for i in range(len(final_libs)):
    final_books.append(" ".join(list(map(str, libraries[final_libs[i]].books))))

result = [f"{len(final_libs)}\n"] + [(f"{final_libs[i]} {libraries[final_libs[i]].nb_books}\n"+final_books[i]+"\n") for i in range(len(final_libs))]
#print(result)
with open('f2.out', 'w') as output:
    output.writelines(result)