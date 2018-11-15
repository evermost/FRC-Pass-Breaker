# FRC-Pass-Breaker

A network of machines to brute force passwords on a locked pdf distributed by FRC for 2019 Competitions

From Linux packages, qpdf is required. It can be installed using the following line:

```
    Sudo apt install qpdf -y
```

The server will create intervals of strings for machines to test as password on the pdf. When a client is done with a task it will either inform the server that the password is found, or that it needs another interval to test.


The client receives a string from the server in file <to_be_made> which then activates client_attempts_inverval.py using the arguments "-start" to denote the first part of the password to be assumed and "-nums" for the number of characters to be added to the "start" string. If "-start" is not called, then it is assumed to be an empty string (or ""). Then passwords will be created until and tested on the pdf.
