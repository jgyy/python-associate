# python -m packages.using_packages
# Defined `random_words` and `random_word` but we're only importing one directly
from words.generator import random_word

# *Only* provides `random_words` when the package is imported directly
from words import random_words

print(f"Random word generated: {random_word()}")
print(f"Random list of words: {random_words(5)}")
