import re

def fix_numbers(text):
    text=text.replace("O","0").replace("l","1").replace("I","1")
    text=re.sub(r"[^0-9\.]","",text)
    return text