**step1** :

In this step your goal is to build your tool to accept a filename as input.
It should return an error if the file is not valid, otherwise your program should open it, 
read the text and determine the frequency of each character occurring within the text


**step-2** : Huffman Coding Trees:

process of creating huffman coading tree : 

 Initial Priority Queue:  [F(5), E(9), C(12), B(13), D(16), A(45)]

Step 1: Combine F(5) and E(9) into a node of weight 14.
New Queue:  [C(12), B(13), D(16), A(45), (F+E)(14)]

Step 2: Combine C(12) and B(13) into a node of weight 25.
New Queue:  [D(16), A(45), (F+E)(14), (C+B)(25)]

Step 3: Combine D(16) and (F+E)(14) into a node of weight 30.
New Queue:  [A(45), (C+B)(25), (D+(F+E))(30)]

Step 4: Combine (C+B)(25) and (D+(F+E))(30) into a node of weight 55.
New Queue:  [A(45), (C+B+D+F+E)(55)]

Step 5: Combine A(45) and (C+B+D+F+E)(55) into a root node with weight 100.
Final Tree: A full Huffman tree with root weight 100.

![image](https://github.com/user-attachments/assets/38518446-5663-4748-9ec4-44a08c08fdf1)


       

      
