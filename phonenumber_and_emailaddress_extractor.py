
# this is python program to extract phonenumber(of any pattern) and email address(of any username and any domain name) 
# from any documents of any amount of pages

# firsty importing all module using in this program
import pyperclip
import re
# regular expression (regex) for phone number(phonenumber_regex)
phonenumber_regex=re.compile(r'''
(\d{3}|\(\d{3}\)|\<\d{3}\>|\[\d{3}\]|\{\d{3}\})        # area code
(-|.|\s|_|/)                                           # separator 
(\d{3})                                                # first 3 digits
(-|.|\s|_|/)                                           # separator
(\d{4})''',re.VERBOSE)                                 # last 4 digits

# regular expression (regex) for email address(emailadd_regex)
emailadd_regex=re.compile(r'''  
([a-zA-Z0-9%^&*_+-]+)                                  # username 
(@)                                                    # @ symbol
([a-zA-Z0-9%^&*_+-]+)                                  # domain name
(\.)                                                   # . symbol
([a-zA-Z]+)''',re.VERBOSE)                             # after dot symbol

# this is time to import or paste the document into program by using pyperclip.paste() method .

long_text=str(pyperclip.paste())
# phone number match object list
phonenumber_mo=phonenumber_regex.findall(long_text)
print("phone number list:")
for x in range(len(phonenumber_mo)):
    print("".join(list(phonenumber_mo[x])))
# email address match object list
emailadd_mo=emailadd_regex.findall(long_text)
print("\nemail address list:")
for x in range(len(emailadd_mo)):
    print("".join(list(emailadd_mo[x])))
