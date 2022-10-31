## Smelly Code

Refactored code and test cases exist in an_testing.py and test_refactored respectively. Image of passing test cases if found in refactored.png
Original code and test cases exist in original.py and test_original respectively. Image of passing test cases is found in og.png
Output.txt contains text output for each (they are the same)



The 'smelly code' exists in two sections. 

1) Where we aren't utlizing proper functionality within our code. I changed this so we use proper functions for code readability and so forth. This exists primarily in the create_family() function in the Family class of orginial.py. Here we don't abstract things to seperate functions.

2) The second section which is 'smelly' is in how we sort the keys at the very end. In the original we had an improper way of sorting the keys that it was doing it poorly on erroneous input (where it wasn't sorted on input). We initially thought this was fine but I realized I should test all edge cases and found the error. I then refactored the code to sort the keys at the very end correctly!