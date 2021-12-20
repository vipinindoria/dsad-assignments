# dsad-assignments
data structure and algorithm design assignment in semester 1

## Problem Statement
Peter is playing a word jumble game. In this game, he is given two words beginWord and endWord and a word list Dict.
Peter has to find the shortest transformation sequence from beginWord to endWord and its length.The game rules are as below:
1. Adjacent words in the chain only differ by one character.
2. Each transformed word must exist in the word list. 
3. Note that beginWord is not a transformed word but endWord must be in the Dict.  

Example:  
    Input: beginWord = "cold", endWord = "warm",  
           Dict = ["warm",”code”,"card",”come”,"cord",”ward”,”wet”]  
    Output:  
           Length: 5  
           The shortest transformation is:"cold"->"cord"->"card"->"ward"->"warm"  

## Help to run the app
   - pyhton3 app.py -h

## Run the App:
  - pyhton3 app.py -i input.txt -o output.txt  
  or
  - pyhton3 app.py --inputfile input.txt --outputfile output.txt  
  or if output file name is not provided, then output file will be named as input file name with replacing input by output
  - pyhton3 app.py --inputfile input.txt  
  or
  - pyhton3 app.py -i input.txt  