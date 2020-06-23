# python -m using_modules.main
from using_modules.helpers import extract_lower as e_low, extract_upper as e_up

name = "Keith Thompson"
print(f"Lowercase letters: {e_low(name)}")
print(f"Uppercase letters: {e_up(name)}")
