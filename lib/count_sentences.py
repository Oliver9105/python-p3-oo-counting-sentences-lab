#!/usr/bin/env python3

import re
import sys

class MyString:
    def __init__(self, value=''):
        """
        Initializes the MyString instance with a default empty string value.
        """
        self._value = ''
        self.value = value

    @property
    def value(self):
        """
        Returns the value of the MyString instance.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Sets the value of the MyString instance, ensuring it is a string.
        Prints an error message if it's not a string.
        """
        if not isinstance(new_value, str):
            print("The value must be a string.", file=sys.stdout)
        else:
            self._value = new_value

    def count_sentences(self):
        """
        Counts the number of sentences in the value.
        Considers '.', '!', and '?' as sentence delimiters.
        """
        # Replace sequences of punctuation with a single period
        sanitized_value = re.sub(r'[.!?]+', '.', self.value)
        # Split the string into potential sentences
        sentences = sanitized_value.split('.')
        # Filter out empty strings and count the non-empty segments
        return len([s for s in sentences if s.strip()])

    def is_sentence(self):
        """
        Returns True if the value ends with a period, otherwise False.
        """
        return self.value.endswith('.')

    def is_question(self):
        """
        Returns True if the value ends with a question mark, otherwise False.
        """
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark, otherwise False."""
        return self.value.endswith('!')



# Example usage
if __name__ == "__main__":
    string = MyString("Is anybody there?")
    print(f"Is it a question? {string.is_question()}")
