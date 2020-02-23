import subprocess
data = []
param1 = 0.01
param2 = 0.1
param3 = 0.01
test_cases = ['a', 'b', 'c', 'd', 'e', 'f']

class Library:
    def __init__(self, nb_books, signup_time, books_per_day):
        self.nb_books = nb_books
        self.signup_time = signup_time
        self.books_per_day = books_per_day

score = 0

def calculate_score():
    tmp_score = 0
    nb_books = 0
    nb_libraries = 0
    nb_days = 0
    books = []
    libraries = []
    for test_case in ['e']:
        with open(test_case + '.txt', 'r') as inputs:
            tmp = inputs.readline().strip("\n").split(" ")
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
        scanner = []
        scanned_days = 0
        for scanday in range(nb_days):
            scanner.append([])
        with open('./brute_force_files/' + test_case + '.out', 'r') as outputs:
            L = int(outputs.readline().strip("\n"))
            state = 0
            current_lib = -1
            nb_lib_books = 0
            books_to_send = []
            for line in outputs:
                if line.strip("\n").split(" ") == ['']:
                        continue
                if not state:
                    tmp = list(map(int, line.strip("\n").split(" ")))
                    current_lib = tmp[0]
                    nb_lib_books = tmp[1]
                    state = 1
                    scanned_days += libraries[current_lib].signup_time
                else:
                    tmp = list(map(int, line.strip("\n").split(" ")))
                    books_to_send = tmp
                    state = 0
                    counter = 0
                    for x in range(scanned_days, nb_days):
                        for _ in range(libraries[current_lib].books_per_day):
                            if counter < len(books_to_send):
                                scanner[x] += [books_to_send[counter]]
                                counter += 1
        print(test_case)
        print(len(scanner))
        bookset = set()
        for s in scanner:
            for ss in s:
                #print("sku")
                if ss in bookset:
                    continue
                else:
                    bookset.add(ss)
                    tmp_score += books[ss]





    return tmp_score

max_params=[0,0,0]
max_score=0
for k in range(1,31):
    i = 0.09
    j = 1
    k = round(param3*k, 2)
    #for j in range(10,11):
    #    j = round(param2*j,2)
    #    for k in range(1,11):
    #        k = round(param3*k,2)
    print(i, j, k)
    for test_case in ['e']:
        subprocess.run(["python3", "solution_brute.py", f"{i}", f"{j}", f"{k}", test_case])
    score = calculate_score()
    print(score)
    print("==============")
    if score > max_score:
        max_score = score
        max_params = [i, j, k]

print("========")
print("========")
print("MAX: ",max_score)
print(max_params)
print("========")
print("========")


                