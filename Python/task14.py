sentence = " my name is Udeme and i am a software test engineer. nice to meet you ."
sentence2 = "My name is {} and I am a {}. Nice to meet you ."
sentence3 = "My name is {name} and I am a {job}. Nice to meet you ."


upper_case_value = sentence.upper()
print(upper_case_value)

lower_case_value = sentence.lower()
print(lower_case_value)

capitalized_value = sentence.capitalize()
print(capitalized_value)

leftstrip = sentence.lstrip()
print(leftstrip)

rightstrip = sentence.rstrip()
print(rightstrip)

split = sentence.split()
print(split)

split = sentence.split("and")
print(split)

unformatted = sentence2
unindexed_format = sentence2.format("Udeme", "Software Test Engineer")
print(unindexed_format)

unformatted = sentence3
named_format = sentence3.format(name="Udeme", job="Software Test Engineer")
print(named_format)
