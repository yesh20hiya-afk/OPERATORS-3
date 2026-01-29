print("Enter obtained marks in five subjects:")

marks1 = int(input("Subject 1: "))
marks2 = int(input("Subject 2: "))
marks3 = int(input("Subject 3: "))
marks4 = int(input("Subject 4: "))
marks5 = int(input("Subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
average = total_marks / 5

if average >= 91 and average <= 100:
   print ("A1")
    
elif average >= 81 and average < 91:
   print("A2")
    
elif average >= 71 and average < 81:
   print("B1")
    
elif average >= 61 and average < 71:
    print("B2")
    
