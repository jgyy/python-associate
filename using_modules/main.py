# python -m using_modules.main
from helpers.strings import extract_lower, extract_upper
from helpers import variables

print(f"Lowercase letters (from strings): {extract_lower(variables.name)}")
print(f"Uppercase letters (from package): {extract_upper(variables.name)}")
print(f"Off of helpers: {extract_lower(variables.name)}")
