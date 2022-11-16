# Write  a  function  that  removes  repeated  characters from a string. Sample Strings are:
# a. Hello: output shouldbe Helo
# b. Concatenate: output should be Conaten

def print_repeated_characters(string):
    not_repeated = ""
    for char in string:
        if char not in not_repeated:
            not_repeated += char
    print("The unrepeating characters are: ", not_repeated)


print_repeated_characters("Hello")
print_repeated_characters("Concatenate")
print_repeated_characters("Chevrolet")
print_repeated_characters("Mercedes")
print_repeated_characters("Aspirin")