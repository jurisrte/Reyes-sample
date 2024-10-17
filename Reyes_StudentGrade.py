# Input 
name = input("Enter your name: ")
section = input("Enter your section: ")
prelim = float(input("Enter  your prelim grade: "))

if prelim < 40 or prelim > 100:                                            

    print("Invalid grade input. Please enter a grade between 40 and 100.")  # Check if the grade input is within the range
    exit()
    
midterm = float(input("Enter your  midterm grade: "))   

if midterm < 40 or midterm > 100:
    print("Invalid grade input. Please enter a grade between 40 and 100.")   # Check if the grade input is within the range
    exit()
    
finals = float(input("Enter your finals grade: "))

if finals < 40 or finals > 100:
    print("Invalid grade input. Please enter a grade between 40 and 100.") # Check if the grade input is within the range
    exit()
    
final_grade = (prelim * 0.3333)  + (midterm * 0.3333) + (finals * 0.3333)    # Calculation for final grade
final_grade = round (final_grade)  #  Rounding the final grade to the nearest whole number
GPA = final_grade

print(f"Your final grade is: {final_grade}")
        
if GPA >= 99 and GPA <= 100:   
      print("Your GPA is: 1.00")
elif GPA >= 96 and GPA <= 98:
      print("Your GPA is: 1.25")
elif GPA >= 93 and GPA <= 95:
      print("Your GPA is: 1.50")
elif GPA >= 90 and GPA <= 92:
      print("Your GPA is: 1.75")
elif GPA >= 87 and GPA <= 89:
      print("Your GPA is: 2.00")
elif GPA >= 84 and GPA <= 86:
      print("Your GPA is: 2.25")
elif GPA >= 81 and GPA <= 83:
      print("Your GPA is: 2.50")
elif GPA >= 78 and GPA <= 80:
      print("Your GPA is: 2.75")
elif GPA >= 75 and GPA <= 77:
      print("Your GPA is: 3.00 ")
elif GPA >= 40 and  GPA < 75:
      print("Your GPA is: 5.0 ")
