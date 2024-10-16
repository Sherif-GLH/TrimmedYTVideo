import re

def remove_special_characters(input_string):
    # Use regular expression to remove any character that is not a letter or number
    clean_string = re.sub(r'[^A-Za-z0-9 ]+', '', input_string)
    return clean_string

original_string = "Hello, World! .?[Th_is] (is) a {test} #123."
cleaned_string = remove_special_characters(original_string)
print(cleaned_string)  # Output: "Hello World This is a test 123"

