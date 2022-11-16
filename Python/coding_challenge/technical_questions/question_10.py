# Create a function that converts any string value to a Sentence  case,
# Then  write  a  unit  test  that  checks  the function's correctness

def convert_to_sentencecase(string):
    sentence_case = string.capitalize()
    print("Sentence case: ", sentence_case)



def convert_to_titlecase(string):
    title_case = string.title()
    print("Title case: ", title_case)


convert_to_sentencecase("are we happy?")
convert_to_sentencecase("it took Tayo a while to know the difference between mile 12 and mile 2. i also had that challenge")

convert_to_titlecase("are we happy?")
convert_to_titlecase("it took Tayo a while to know the difference between mile 12 and mile 2. i also had that challenge")
