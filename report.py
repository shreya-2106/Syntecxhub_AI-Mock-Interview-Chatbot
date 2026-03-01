def generate_report(history, total_questions):

    print("\n INTERVIEW REPORT")

    total_marks = 0

    for item in history:
        total_marks += item["marks"]

  
    tech_questions = min(total_questions, 15)
    hr_questions = max(0, total_questions - 15)

    max_marks = (tech_questions * 4) + (hr_questions * 10)

    percentage = (total_marks / max_marks) * 100

    print("Total Questions Attempted:", total_questions)
    print("Total Marks Scored:", total_marks, "/", max_marks)
    print("Percentage:", round(percentage, 2), "%")

   
    if percentage >= 80:
        performance = "Excellent"
    elif percentage >= 60:
        performance = "Good"
    elif percentage >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    print("Performance Level:", performance)

    
    if percentage >= 60:
        result = "Selected"
    else:
        result = "Rejected"

    print("Final Result:", result)

    
    file = open("history.txt", "a")

    file.write("\n===== New Interview =====\n")
    file.write("Total Questions: " + str(total_questions) + "\n")
    file.write("Total Marks: " + str(total_marks) + "/" + str(max_marks) + "\n")
    file.write("Percentage: " + str(round(percentage, 2)) + "%\n")
    file.write("Performance: " + performance + "\n")
    file.write("Result: " + result + "\n")

    file.close()