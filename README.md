# DSAD-Assignments
Data Structure and Algorithm Design Assignments in Semester 1

## Assignment 1
## Problem Statement
Peter is playing a word jumble game. In this game, he is given two words beginWord and endWord and a word list Dict.
Peter has to find the shortest transformation sequence from beginWord to endWord and its length.The game rules are as below:
1. Adjacent words in the chain only differ by one character.
2. Each transformed word must exist in the word list. 
3. Note that beginWord is not a transformed word but endWord must be in the Dict.  

Example:  
    Input:  
           beginWord = "cold", endWord = "warm",  
           Dict = ["warm",”code”,"card",”come”,"cord",”ward”,”wet”]  
    Output:  
           Length: 5  
           The shortest transformation is:"cold"->"cord"->"card"->"ward"->"warm"  

## Help to run the app
   - pyhton3 app.py -h

## Run the App:
  - cd assignment1
  - pyhton3 app.py -i input.txt -o output.txt  

  or  
  
  - pyhton3 app.py --inputfile input.txt --outputfile output.txt  
  
  or if output file name is not provided, then output file will be named as input file name with replacing input by output  
  
  - pyhton3 app.py --inputfile input.txt  
  
  or  
  
  - pyhton3 app.py -i input.txt


## Assignment 2
## Problem Statement
There are dedicated teams in the state roadways department, which handles the task of preparation of tables indicating 
distances between all pairs of major cities and towns in road maps of states. Assume that you are part of such a team 
for State X. Your task is to find the shortest distances between all pairs of major cities and towns within the state X.
The aim should be to find the highly efficient method for obtaining these shortest paths. The following graph contains 
five nodes, and various directed and weighted edges. Consider this as the representation of the cities and the paths 
between them.

Requirements
1. Formulate an efficient algorithm to perform the above task using Dynamic programming
2. Provide a description about the design strategy used
3. Analyse the time complexity of the algorithm and show that it is an “efficient” one.
4. Implement the above problem statement using Python 3.7

Example:  
    Input:  
           start_node/end_node/distance  
           0/1/2  
           1/2/7  
           2/1/6  
           2/3/1  
           3/5/3  
           5/0/1  
           5/1/4   
    Output:  
              n1,n2,n3,n4,n5  
           n1 0,2,9,10,13  
           n2 12,0,7,8,11  
           n3 5,6,0,1,4  
           n4 4,6,13,0,3  
           n5 1,3,10,11,0  

## Help to run the app
   - pyhton3 app.py -h

## Run the App:
  - cd assignment2
  - pyhton3 app.py -i input.txt -o output.txt  

  or  
  
  - pyhton3 app.py --inputfile inputPS14.txt --outputfile outputPS14.txt  
  
  or if output file name is not provided, then output file will be named as input file name with replacing input by output  
  
  - pyhton3 app.py --inputfile inputPS14.txt  
  
  or  
  
  - pyhton3 app.py -i inputPS14.txt