### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #to check if the card.value is 1, operator must be '=='
      return True
    else #put a colon here
      return False
   

  dif highest_card(self, card1 card2): # use def instead of 'dif', put a comma bewtween the two parameter
  if card1.value > card2.value: # the whole if-else statement should be indented here
    return card #card1 should be returned
  else:
    return card2
  


def cards_total(self, cards): 
  #the function's indentation is incorrect. The definition should be aligning with the previouse two functions
  total
  # total should be initialised with a value, like 'total = 0'
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # return is now in the loop, it should be indented to the left to take it out and show correct result
    # We are not able to concatenate the total variable with a string. We should use type conversion or a formatted string
    # Should also add a space at the end of the sting to make it look nicer
  
```
