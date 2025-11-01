import statistics

student_list = {}# {Student name1: { Subject1: (marks, max), Subject2: (marks, max) }  }
exit_flag = False
while True:
    
    student = input("Enter name of student (q to display): ")
    student_score = {} #Of the form {Subject: (Marks scored, Total possible)}
    if student == "q":
        break
    while True:
        sub = input("Enter name of subject evaluated ('m' to move on to next student or 'q' to display): ")
        if sub == "m":
            break
        elif sub == "q":
            exit_flag = True
            break
        else:
            marks = float(input(f"Enter marks scored in {sub} by {student}:"))
            tot = float(input(f"Enter maximum marks for {sub} exam: "))
            student_score[sub] = (marks, tot)   
    student_list[student] = student_score
    if exit_flag == True:
        break
##Individual Results
for key, value in student_list.items():
    
    print(f"---{str(key).upper()}'S SCORE---")

    for subj, score in (value).items():
        print(f"{subj}: {score[0]:.2f}/{score[1]:.2f}")

    
    percentages = [x/y * 100 for x, y in (value).values()]
    print(f"The mean %age of {key} are: {statistics.mean(percentages):.2f}%")
    print(f"Minimum %age of {key} is: {min(percentages):.2f}%")
    print(f"Maximum %age of {key} is: {max(percentages):.2f}%\n")
print("\n\n")

##Class result
print("=====CLASS RESULT=====\n")
class_subjects = {} # {subject1: [percentages]}
for student_scores in student_list.values():
    for subject, (marks, total) in student_scores.items():
        if subject in class_subjects.keys():
            class_subjects[subject].append(marks/total * 100)
        else:
            class_subjects[subject] = [marks/total * 100]
avg = {} # {subj1: avg}

for subj, percentages in class_subjects.items():
    subj_avg = statistics.mean(percentages)
    print(f"The class average in {subj} is {subj_avg:.2f}%.")
    avg[subj] = subj_avg
print()
best = max(avg, key = avg.get)
print(f"The best class performance is in {best} - {avg[best]:.2f}.")
worst = min(avg, key = avg.get)
print(f"The worst class performance is in {worst} - {avg[worst]:.2f}.")