def doc_to_text(doc: dict) -> str:
    return f"다음 지문을 읽고, 질문에 대한 정답으로 알맞은 것을 보기 A, B, C 중에 고르시오. 설명 없이 알파벳 하나만으로 대답하시오.\n\n지문: {doc['context']}\n질문: {doc['question']}\nA: {eval(doc['choices'])[0]}\nB: {eval(doc['choices'])[1]}\nC: {eval(doc['choices'])[2]}\n정답:"

def answer_to_target(doc: dict) -> str:
    if doc['answer'] == eval(doc['choices'])[0]:
        answer = "A"
    elif doc['answer'] == eval(doc['choices'])[1]:
        answer = "B"
    elif doc['answer'] == eval(doc['choices'])[2]:
        answer = "C"
    return answer