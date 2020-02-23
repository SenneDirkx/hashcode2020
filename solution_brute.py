from operator import itemgetter
from math import inf, ceil
import sys
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
    

with open(sys.argv[4] + '.txt', 'r') as inputs:
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

lib_scores = []

scanned_books = {}

min_signup = inf
max_signup = 0
min_score = inf
max_score = 0
min_busy = inf
max_busy = 0

for i in range(len(libraries)):
    tmp_score = 0
    for book in libraries[i].books:
        tmp_score += books[book]
        if book in scanned_books:
            scanned_books[book] += (i,)
        else:
            scanned_books[book] = (i,)
    if libraries[i].signup_time > max_signup:
        max_signup = libraries[i].signup_time
    if libraries[i].signup_time < min_signup:
        min_signup = libraries[i].signup_time
    tmp_score = tmp_score/len(libraries[i].books)
    if tmp_score > max_score:
        max_score = tmp_score
    if tmp_score < min_score:
        min_score = tmp_score
    tmp_busy = ceil(libraries[i].nb_books/libraries[i].books_per_day)
    if tmp_busy > max_busy:
        max_busy = tmp_busy
    if tmp_busy < min_busy:
        min_busy = tmp_busy

for i in range(len(books)):
    if i in scanned_books:
        books[i] = books[i]//len(scanned_books[i])

    
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
    if max_busy == min_busy:
        tmp_busy = 0
    else:
        busy = ceil(libraries[i].nb_books/libraries[i].books_per_day)
        tmp_busy = (busy-min_busy)/(max_busy-min_busy)
    lib_scores.append([i,  float(sys.argv[1])*tmp_score+float(sys.argv[2])*tmp_signup+float(sys.argv[3])*tmp_busy])



lib_scores = sorted(lib_scores, key=itemgetter(1), reverse=True)

days_occupied = 0
i = 0
final_libs = []
while days_occupied < nb_days and i < len(lib_scores):
    final_libs.append(lib_scores[i][0])
    days_occupied += libraries[lib_scores[i][0]].signup_time
    i+=1

final_books = []
final_counts = []
scanned = set()
signup_counter = 0
for i in range(len(final_libs)):
    signup_counter += libraries[final_libs[i]].signup_time
    time_left = nb_days - signup_counter
    tmp_values = []
    tmp_books = libraries[final_libs[i]].books
    for j in range(len(tmp_books)):
        tmp_values.append([tmp_books[j], books[tmp_books[j]]])
    tmp_values = sorted(tmp_values, key=itemgetter(1), reverse=True)
    for j in range(len(tmp_values)):
        tmp_books[j] = tmp_values[j][0]
    #print(tmp_books)
    #no_double_books = []
    #day_count = 0
    #for book in tmp_books:
    #    if book in scanned:
    #        continue
    #    if day_count < time_left:
    #        no_double_books.append(book)
    #        scanned.add(book)
    #    day_count += 1/libraries[final_libs[i]].books_per_day
    #if no_double_books == []:
    #    no_double_books = tmp_books
    final_books.append(" ".join(list(map(str, tmp_books))))
    #final_counts.append(len(no_double_books))

result = [f"{len(final_libs)}\n"] + [(f"{final_libs[i]} {libraries[final_libs[i]].nb_books}\n"+final_books[i]+"\n") for i in range(len(final_libs))]

with open('./brute_force_files/' + sys.argv[4] + '.out', 'w') as output:
    output.writelines(result)