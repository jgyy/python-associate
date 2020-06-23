# python -m using_modules.main
from using_modules import helpers

name = "Keith Thompson"
print(f"Lowercase letters: {helpers.extract_lower(name)}")
print(f"Uppercase letters: {helpers.extract_upper(name)}")
