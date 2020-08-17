#Course 2: Python Data Strcuture
#Week 1:

#exercise 1
text = "X-DSPAM-Confidence:    0.8475";
x=text.find('0.8475')
print(x)
y=float(text[x:])
print(y)


#Week 3: Chapter 7

#Exercise 1: Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Please input a valid file name: ')
    quit()
for line in fh:
    x=line.rstrip()
    y=x.upper()
    print(y)


# Exercise2:
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475.
#Count these lines and extract the floating point values from each of the line (use find to locate the starting point of float)
#and compute the average of those values and produce an output as shown below. Dont use the sum() function or variable named sum
# in your solution.

#Ask for file name
filename=input('Please enter the file name: ')

try:
    fh=open(filename)
except:
    print('Please enter a valid file name')
    quit()

num_location=fh.find('0.8475')
print(num_location)

