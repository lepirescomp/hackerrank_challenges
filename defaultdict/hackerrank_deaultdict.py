# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import collections

def read_input():
    input_read = [] 
    for line in sys.stdin:
        input_read.append(line.rstrip())
    return input_read

def process_input(input_read):
    n,m = int(input_read[0].split(" ")[0]), int(input_read[0].split(" ")[1])
    return n,m

def construct_dict_of_letters(n,m,input_read):
    letters = collections.defaultdict(lambda: list())
    letters_a_indice = [(k, i) for i, k in enumerate(input_read[1:n+1],start=1)]
    for k, i in letters_a_indice:
        letters[k].append(i)
    return letters

def print_result(input_read, letters):
    printable_list = list(input_read[n+1:])

    for i in printable_list:
        if letters[i] == []:
            print(-1)
        else:
            for j in letters[i]:
                print(str(j)+str(" "),end="")
            print("")

input_read = read_input()
n,m = process_input(input_read)
letters = construct_dict_of_letters(n,m,input_read)
print_result(input_read, letters)