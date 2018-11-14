import subprocess
import argparse

parser = argparse.ArgumentParser(description="Bruteforce values from \"start \" with \"nums\" many characters added")
parser.add_argument('-start', action="store", dest="start", default="")
parser.add_argument('-nums', action="store", dest="nums", type=int)

res = parser.parse_args()
start = res.start
nums = res.nums


file_name = "file.pdf"

l = []
s_char = 2
s_end = 128

print(start, nums)

for i in range(s_char, s_end):
    l.append(chr(i))

# THIS WHOLE "MAKING A LIST OF PASSWORDS" TO BE CHANGED TO A RECURSIVE FUNCTION

for k in range(nums - 1):
    new_list = []
    for i in range(len(l)):
        for j in range(s_char, s_end):
            new_list.append(l[i] + chr(j))
    l = new_list

for i in range(len(l)):
    command = "qpdf --decrypt --password=" + start + l[i] + " " + file_name + " output.pdf"
    command = command.split(" ")
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if res.stdout.decode("utf-8") == "":
        print("found pass: " + start + l[i])
        exit()
print(":|")
