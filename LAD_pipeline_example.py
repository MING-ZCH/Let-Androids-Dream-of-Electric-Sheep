# This is a python-like pseudocode example of the LAD pipeline.

def Perception(image):
    image_dep = Perception_image_dep(prompt1_image_dep, image)
    keywords = Perception_keywords(prompt1_keywords, image_dep)
    return image_dep, keywords

def Search(image_dep, keywords):
    search_questions_all = Search_construct_search_questions(prompt2_search_questions, keywords)
    search_questions = Search_split_search_questions(search_questions_all)
    search_result_all = ""
    for i, search_question in enumerate(search_questions):
        score = Search_self_judge(prompt2_self_judge, search_question)
        search_strategy = extract_score(score)
        if search_strategy == "web_search":
            search_result = web_search(search_question)
        elif search_strategy == "model_search":
            search_result = model_search(search_question)
        search_result_single = f'Question {i}: {search_question}\n Answer: """{search_result}"""\n'
        search_result_all += search_result_single

    rank_search_result = Search_rank(prompt2_rank, image_dep, search_result_all)
    search_result_top3 = Search_rank_top3_en(rank_search_result, search_result_all)
    search_summary = Search_summary(prompt2_summary, rank_search_result, search_result_top3)
    return search_summary

def Reasoning(image, image_dep, keywords, search_summary, MCQ, OSQ):
    MCQ_answer = Reasoning_MCQ(image, prompt3_explicit_reasoning_mcq, image_dep, keywords, search_summary, MCQ)
    OSQ_answer = Reasoning_OSQ(image, prompt3_explicit_reasoning_osq, image_dep, keywords, search_summary, OSQ)
    return MCQ_answer, OSQ_answer
