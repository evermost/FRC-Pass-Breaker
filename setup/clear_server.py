"""
Clears all the words from the server and resets found password if any.
"""

import requests

if __name__ == '__main__':
    r = requests.post("http://127.0.0.1:8000/reset/")
    if r.content.decode() == 'success':
        item = '-'
        while item != '':
            item = requests.get("http://127.0.0.1:8000/word/").content.decode()
            print("Cleared " + item)
    else:
        raise ConnectionError("Could not connect to server / Error when processing reset request")

    print("Server Cleared")
