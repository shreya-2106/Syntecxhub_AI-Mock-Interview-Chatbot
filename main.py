import random
import datetime

from questions import questions
from hr_questions import hr_questions
from evaluator import evaluate_answer
from report import generate_report
def technical_round():

    print("\n----- Technical Interview Round -----")

    score = 0
    interview_history = []

    # Combine all difficulty levels
    all_questions = questions["easy"] + questions["medium"] + questions["hard"]

    # Select 15 random questions
    selected_questions = random.sample(all_questions, 15)

    for i, q in enumerate(selected_questions, start=1):

        print("\nQuestion", i, "/ 15:", q["question"])

        answer = input("Your Answer: ")

        marks = evaluate_answer(answer, q["keywords"], 4)

        print("Marks for this question:", marks)

        score += marks

        interview_history.append({
            "question": q["question"],
            "answer": answer,
            "marks": marks
        })

    tech_percentage = (score / 60) * 100

    print("\nTechnical Score:", score, "/ 60")
    print("Technical Percentage:", round(tech_percentage, 2), "%")

    return tech_percentage, interview_history


def hr_round():

    print("\n----- HR Interview Round -----")

    score = 0
    hr_history = []

    # Select 7 random HR questions
    selected_hr = random.sample(hr_questions, 7)

    for i, q in enumerate(selected_hr, start=1):

        print("\nHR Question", i, "/ 7:", q["question"])

        answer = input("Your Answer: ")

        marks = evaluate_answer(answer, q["keywords"], 10)

        print("Marks for this question:", marks)

        score += marks

        hr_history.append({
            "question": q["question"],
            "answer": answer,
            "marks": marks
        })

    hr_percentage = (score / 70) * 100

    print("\nHR Score:", score, "/ 70")
    print("HR Percentage:", round(hr_percentage, 2), "%")

    return hr_percentage, hr_history


def main():

    print("================================")
    print(" AI MOCK INTERVIEW CHATBOT ")
    print(" TECH INTERVIEW BOT ")
    print("================================")

    candidate_name = input("Enter Candidate Name: ")

    interview_id = random.randint(1000, 9999)

    interview_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nCandidate Name:", candidate_name)
    print("Interview ID:", interview_id)
    print("Interview Date & Time:", interview_time)

    print("\nStarting Technical Interview...")

    tech_score, tech_history = technical_round()

    if tech_score >= 60:

        print("\nYou qualified for the HR Round.")

        hr_score, hr_history = hr_round()

        full_history = tech_history + hr_history

        print("\nInterview Completed for", candidate_name)

        generate_report(full_history, len(full_history))

    else:

        print("\nYou did not qualify for the HR Round.")

        print("\nInterview Completed for", candidate_name)

        generate_report(tech_history, len(tech_history))


if __name__ == "__main__":
    main()