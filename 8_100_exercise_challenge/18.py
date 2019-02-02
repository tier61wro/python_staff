#!/usr/bin/env python3
'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
import re
pass_in = input("insert some number\n")
pass_list = pass_in.split(",")
pass_list_out = []
for passw in pass_list:
    if not (re.search(r"[a-z]", passw) and re.search(r"[A-Z]", passw) and re.search(r"[0-9]", passw) and re.search(r"[$#@]", passw)):
        print ("{} is bad".format(passw))
    elif (len(passw) < 6 or len(passw) > 12):
        print ("bad password len = ", len(passw))
    else:
        pass_list_out.append(passw)
print (",".join(pass_list_out))
