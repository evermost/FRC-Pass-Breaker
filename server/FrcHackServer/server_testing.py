import requests

if __name__ == '__main__':
    while True:
        action = input('a for add, g for get, s to submit password, r to reset, q to quit: ')

        if action == 'a':
            word = input("word to add: ")
            r = requests.post("http://127.0.0.1:8000/word/", params={'item': word})
            print(r.content.decode())
        elif action == 'g':
            r = requests.get("http://127.0.0.1:8000/word/")
            print(r.content.decode())
        elif action == 's':
            word = input("pass to submit: ")
            r = requests.post("http://127.0.0.1:8000/submit/", params={'item': word})
            print(r.content.decode())
        elif action == 'r':
            r = requests.post("http://127.0.0.1:8000/reset/")
            print(r.content.decode())
        elif action == 'q':
            break
