from question import Question
from random import shuffle
import time

class Quiz:
    def __init__(self, questions, timelimit=5):
        self.questions=[Question(q["text"], q["answer"]) for q in questions]
        self.score=0
        self.index=0
        self.timelimit=timelimit
        self.shuffleques()
        self.starttime=None

    def nextques(self):
        if self.index<len(self.questions):
            self.starttime=time.time()
            question=self.questions[self.index]
            self.index+=1
            return question
        else:
            return None
   
    def checkanswer(self, useranswer):
        if self.index>0:
            currentques=self.questions[self.index-1]
            if not self.istimeup():
                if currentques.iscorrect(useranswer):
                    self.score+=2
                else:
                    self.score-=1
    
    def questionremain(self):
        return self.index<len(self.questions)
   
    def shuffleques(self):
        shuffle(self.questions)
    
    def istimeup(self):
        if self.starttime is not None:
            elapsedtime=time.time()-self.starttime
            return elapsedtime>=self.timelimit
        return False

