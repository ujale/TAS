# Create  a  function  that  converts  any  string  value  to  uppercase,
# Then  write  a  unit  test  that  checks  the  function's correctness.


def convert_string_to_uppercase():
    items = ["Box", "Potato", "Lettuce", "Grain", "America"]
    for item in items:
        print(item.upper())

convert_string_to_uppercase()

# Alternately

def uppercase_converter(string):
    uppercase = string.upper()
    print(uppercase)

uppercase_converter("biscuit")
uppercase_converter("plasma")
uppercase_converter("Studio 47")
