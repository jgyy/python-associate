# python -m using_modules.main
from using_modules.helpers import extract_upper, extract_lower
import using_modules.extras as extras

print(f"__name__ in main.py: {__name__}")

print(f"Lowercase letters: {extract_lower(extras.name)}")
print(f"Uppercase letters: {extract_upper(extras.name)}")
