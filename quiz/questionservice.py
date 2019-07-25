from question import Question
class QuestionService:

    questions = []
    @classmethod
    def loadQuestions(cls):
        with open("quest.txt") as file:
            data = file.readlines()
            for line in data:
                q = line.split(",")
                cls.questions.append(Question(*q))

    @classmethod
    def begin_quiz(cls):
        cls.loadQuestions()
        print(f"Total questions found:{len(cls.questions)}")
        n_correct = 0
        n_wrong = 0
        for i,question in enumerate(cls.questions):
            print(f"{i+1}. {question}")
            ch = input("enterb your choice [A,B,C,D] only...")
            if ch == question.canswer.strip():
                n_correct += 1
            else:
                n_wrong += 1
        cls.show_result(n_correct,n_wrong)
    @classmethod
    def show_result(cls,n_correct,n_wrong):
        print("*"*50)
        total_q = len(cls.questions)
        print(f"total questions :{total_q}")
        print(F"no of questions correct:{n_correct}")
        print(f"no of questions wrong: {n_wrong} ")
        percen = ((n_correct)/total_q) * 100
        print(f"percentage: {percen}")
        if percen >=65:
            print("congo u r an army")
        else:
            print("its ok try next time")
