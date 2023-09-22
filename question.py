class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def iscorrect(self, useranswer):
        return self.answer==useranswer
    