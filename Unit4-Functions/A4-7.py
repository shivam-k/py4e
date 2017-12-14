score = input("Enter Score: ")
try:
    score = float(score)
    score <= 1
except:
    print("Bad Score")
    exit()

def coumputegrade(score):
    if score < 0.6:
        grade = "F"
    elif score >= 0.6 and score < 0.7:
        grade = "D"
    elif score >= 0.7 and score < 0.8:
        grade = "C"
    elif score >= 0.8 and score < 0.9:
        grade = "B"
    elif score >= 0.9 and score < 1.0:
        grade = "A"
    elif score==1:
        grade = "Ex"
    else:
        print("Bad Score")
        exit()
    print(grade)

coumputegrade(score)
