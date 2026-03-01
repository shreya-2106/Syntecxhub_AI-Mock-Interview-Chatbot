def evaluate_answer(answer, keywords, max_marks):

    answer = answer.lower()

    matched_keywords = 0

    for group in keywords:

        for word in group:

            if word.lower() in answer:
                matched_keywords += 1
                break

    total_groups = len(keywords)

    if matched_keywords == 0:
        return 0

    elif matched_keywords == 1:
        return max_marks * 0.25

    elif matched_keywords == 2:
        return max_marks * 0.5

    elif matched_keywords == 3:
        return max_marks * 0.75

    else:
        return max_marks