import subprocess
import argparse


parser = argparse.ArgumentParser(description="hello?")

file_name = "file.pdf"


start = ""
nums = 3
l = []
s_char = 2
s_end = 128

for i in range(s_char, s_end):
    l.append(chr(i))


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
