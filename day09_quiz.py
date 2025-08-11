#quiz using collection
quiz  = (("num of planets"),("how many oceans"),("how many continents"))

options = (("A.8","B.23","C.78"),("A.34","B.5","C.90"),("A.12","B.34","C.7"))
answer = (("a"),("b"),("c"))
score = 0
qus_num = 0

for quizz in quiz:
    print("---------------")
    print(quizz)
    for option in options[qus_num]:
        print(option)

    result = input("enter a,b,c:  ").lower()
    if result == answer[qus_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
    qus_num += 1  

print("---------------")
print(f"your score is {score}")
print("---------------")

for answers in answer:
    print(answers,end = " ")
print( )

print("---------------")