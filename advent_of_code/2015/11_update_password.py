#  11th day of advent of code 2015
from utils.inputs import get_data_set
import re

input_string = "cqjxjnds"


class Letter:
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   def __init__(self, letter):
      self.letter = letter
      self.position = self.alphabet.index(letter)
   def increment(self, num):
      if (self.position + num)>(len(self.alphabet)-1): 
         return Letter(self.alphabet[num - (len(self.alphabet) - self.position)]), True
      else:
         return Letter(self.alphabet[num + self.position]), False
   def __str__(self):
         return self.letter
   def __repr__(self):
         return f"Letter('{self.letter}')"
   
class Password:
   def __init__(self, letters):
      self.password = letters
      self.positions = [letter.position for letter in letters]
   def __str__(self):
      return "".join([letter.letter for letter in self.password])
   
   def update_password(self):
      is_password_valid = False
      while not is_password_valid:
         it = 0
         carryover = True
         while carryover:
            self.password[-1-it], carryover = self.password[-1-it].increment(1)
            self.positions[-1-it] = self.password[-1-it].position
            it+=1
         is_password_valid = self.self_validation()
         # print(self.password)

   
   def self_validation(self):
      increasing_requirement = False
      letter_requirement = False
      double_requirement = False
      for i1, i2, i3 in zip(self.positions[0:-2], self.positions[1:-1], self.positions[2:]):
         if (i1+1 == i2) and (i2+1 == i3): 
            increasing_requirement = True
            break

      if not(8 in self.positions or 14 in self.positions or 11 in self.positions):
         letter_requirement = True

      double_count = 0
      if (self.positions[0] == self.positions[1]) and not (self.positions[1] == self.positions[2]):
         double_count+=1
      if (self.positions[-1] == self.positions[-2]) and not (self.positions[-2] == self.positions[-3]):
         double_count+=1
      for i1, i2, i3, i4 in zip(self.positions[0:-3], self.positions[1:-2], self.positions[2:-1], self.positions[3:]):
         if double_count == 2:
            double_requirement = True
            break 
         if (i2 == i3) and not (i1 == i2) and not (i3 == i4): 
            double_count +=1
      return increasing_requirement and letter_requirement and double_requirement

letters = []
for letter in input_string:
   letters.append(Letter(letter))

pwd = Password(letters)
print(pwd)
pwd.update_password()
print(pwd)
pwd.update_password()
print(pwd)
