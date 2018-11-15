"""
Load words into the server from .txt file.
Words are to be in .txt file with following format:
<Start of File>
word1
word2
word3
<End of File>
"""

import os.path
import requests

if __name__ == '__main__':
    file_name = input("File containing words: ")
    failure_limit = int(input("How many failed additions should be tolerated: " ))
    failure_count = 0

    if os.path.isfile(file_name):
        file = open(file_name,'r')
        lines = file.readlines()

        for line in lines:
            line.replace(' ','')
            line.replace('\n','')

            r = requests.post("http://127.0.0.1:8000/word/", params={'item': line})

            if r.content.decode() == 'failure':
                print("failure to add word: " + line)
                failure_count += 1

            if failure_count >= failure_limit:
                print("Failure limit exceeded. Check for server connection / proper file format")
                break
    else:
        print("File not found.")