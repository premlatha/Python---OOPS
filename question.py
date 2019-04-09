# Question class
class Question:

    # Init method
    def __init__(self,ques,ans,options=[]):
        self.question=ques
        self.answer=ans
        self.options=options

    def __str__(self):
        return print("Question {} has {} answer.".format(self.question,self.answer))
   


Q1=Question("Python is Object oriented?","True",["True","False"])
print(Q1.options)