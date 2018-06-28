#Q1. Write a Python program to read last n lines of a file

n = int(input("Enter how many last lines are required: "))                                 #Read limit of iteration
with open("C:/Users/Intel/Desktop/Data.txt",'r') as f:                                     #Open File Data.txt
 lines = f.read().splitlines()                                                             #Seperate input line-wise
 for i in range(n):
  last_line = lines[-(i+1)]                                                                #Count last n lines one by one
  print(last_lines)

#Q2. Write a Python program to count the frequency of words in a file. 

import collections
import ast
with open("C:/Users/Intel/Desktop/Words.txt",'r') as f:                                    #Open File Words.txt
 string = ast.literal_eval(f.read())
 string = string.split()
counter = collections.Counter(string)                                                      #Count each letter in the file
dictionary = dict(counter)                                                                 #Create dictionary of word & it's frequency
print(dictionary)

#Q3. Write a Python program to copy the contents of a file to another file 

f2 = open("C:/Users/Intel/Desktop/Words.txt","r+")                                         #Open File Words.txt 
data = f2.read()                                             				   #Read the file					
f1 = open("C:/Users/Intel/Desktop/Words_duplicate.txt","w")                                #Open File Word_duplicate.txt
f1.write(data)                                                                             #Write the read data in new file
f2.close()
f1.close()

#Q4. Write a Python program to combine each line from first file with the corresponding line in second file. 

with open("C:/Users/Intel/Desktop/Data.txt",'r') as f:                                     #Open first file Data.txt
 p = f.readlines()                                                                         #Read each lines 
with open("C:/Users/Intel/Desktop/Data2.txt",'r') as g:                                    #Open second file Data2.txt
 q = g.readlines()                                                                         #Read each lines
for i in range(len(p)):
 for j in range(len(q)):
  if(i==j):                                                                                #If line number in both files match:
   s = str(p[i])+str(q[j])                                                                 #Then concatenate the strings from both files
   print(s)

#Q5. Generate 10 random numbers in a file & then sort it

file1=open("C:/Users/Intel/Desktop/Random.txt","r+")                                       #Open first file Random.txt 
for i in range(10): 
    file1.writelines(str(i))                                                               #Create file content by generating numbers
data=file1.read()
file1.close()
sorted_data=sorted(data)                                                                   #Sort the data 
file2=open("C:/Users/Intel/Desktop/Sorted.txt","r+")                                       #Open second file Sorted.txt 
file2.write(sorted_data)								   #Write the sorted data in the second file
file2.close()                  
