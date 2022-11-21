# Write  a  Python  program  that  checks  if  a  string  is  a palindrome,
# Then  optionally  write  a  unit  test  to  check your program's correctness.

def check_for_palindrome(item):

    rev = reversed(item)
    if list(item) == list(rev):
        print ("Item is a Palindrome")
    else:
        print("item is not a Palindrome")


check_for_palindrome("DAD")
check_for_palindrome("Maid")
check_for_palindrome("34")

#Alternatively

def palindrome_status(string):
    if string == string[::-1]:
        print("String is a palindrome")
    else:
        print("String is not a Palindrome")

palindrome_status("Ahmed")
palindrome_status("SOS")
palindrome_status("pop")
palindrome_status("man")
palindrome_status("Tat")
palindrome_status("pap")

