# bookbot

**bookbot** is a Python-based tool that analyzes text files (such as books) and provides detailed statistics about word and character usage. This project was created as part of the [Boot.dev](https://boot.dev) curriculum to practice working with files, loops, and dictionaries in Python.

## What It Does

bookbot takes a `.txt` file (like a novel), analyzes its contents, and outputs:

- The total number of words in the book.
- The frequency of each character (including punctuation and special characters).
- A nicely formatted report in the terminal.

---

### Example Output

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============


---

## Technologies Used

- Python 3.x
- Standard Library only (no external dependencies)

---

## Getting Started

1. **Clone the Repo**
    
Open your terminal and run:

git clone https://github.com/Dima-72/bookbot.git 
cd bookbot


2. **Add a `.txt` File** 

Place your desired `.txt` file inside the `books/` directory.  
You can use `books/frankenstein.txt` as an example.

3. **Run the Script**

Make sure you have Python 3 installed, then run:

python main.py





