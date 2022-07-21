import random

q1 = """Qus 1: Lali and Anju are a married couple. Tunu and Munu are brothers. 
Tunu is the brother of Lali. How is Munu related to Anju?

A. Brother
B. Brother-in-law
C. Sister-in-law
D. None of these"""

q2 = """Qus 2: Which alphabet will be 14th to the left of 8th alphabet from the 
right in the following series of letters?
A O B P C Q D R E S F T G U H V I W J X K Y L Z M N.

A. B
B. C
C. Y
D. P"""

q3 = """Qus 3: If orange is called blue, blue is called red, red is called yellow, yellow is called green, green is called black, black is called violet and violet is called orange, what would be the colour of blood?

A. Red
B. Green
C. Black
D. Yellow"""

q4 = """Qus 4: How many times can you subtract eight from eighty?

A. 1
B. 4
C. 6
D. 10"""

q5 = """Qus 5: Asha is older than Swati Mohtarma is older than Asha but younger 
than Kashish. Kashish is older than Swati. Swati is younger than Mohtarma. Gauri is the oldest.
Who is youngest?

A. Kashish
B. Asha
C. Mohtarma
D. Swati"""

q6 = """Qus 6: Pointing towards a lady, Neeraj said. “ She is the daughter of the only child of my grandmother.”
How is the lady related to Neeraj ?
A. Sister
B. Niece
C. Cousin
D. None of these
"""

q7 = """"Qus 7: What two keys can't open any door?
A. Pinkey and Minkey
B. Minkey and Dinkey
C. Dinkdy and Chinkey
D. Donkey and Monkey"""


q8 = """Qus 8: What is that thing that we cannot see even in the light of day?

A. Sun
B. Moon
C. Star
D. Darkness"""

questions = {q1:"B", q2:"B", q3:"D", q4:"A", q5:"D", q6:"A", q7:"D", q8:"D"}
wrong_ans = {q1: ["A. Brother", "C. Sister-in-law", "D. None of these"]}
name = input("Enter Your Name: ")
print()
print("Hello", name, "Welcome to the KBC !!")
score=0
for i in questions:
    print("======================================================")
    print(i)
    flag1 = input("Do you want to Life Line (Yes / No): ")
    if flag1=="Yes":
        eliminate = random.sample(wrong_ans[i], 2)
        for w in eliminate:
            j = i.replace(w, "")
        print(j)
    ans = input("===> Enter the your Answer (A / B / C / D): ")
    if ans==questions[i]:
        print()
        print("Correct Answer, You Got 50 Point")
        score = score+50
        print("Your Current Score is:", score)
    else:
        print("Wrong Anser, you lost 20 point")
        score = score-20
        print("Your Current Score is:", score)
    #flag2 = input("Do you want to quit (yes/no)")
    #if flag2 == "yes":
        #break

print("Final Score is:", score)


