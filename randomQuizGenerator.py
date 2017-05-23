import random
import os

quizQuestionAnswer = {'The Great Britain': 'London', 'Russia': 'Moscow', 'USA': 'Vashington', 'China': 'Tokio'}
dir='C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\quizGenerator'
if not os.path.exists(dir):
    os.makedirs(dir)
countries=list(quizQuestionAnswer.keys())
for quizNum in range(3):
    quizFile=open('C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\quizGenerator\\ticket_N%s.txt' %(str(quizNum+1)),'w')
    answerFile=open('C:\\Users\\nata\\PycharmProjects\\ProjectPythonExample\\filesPrj\\quizGenerator\\ticket_answer_N%s.txt' %(str(quizNum+1)),'w')
    correctAnswers = []
    for i in range(0,len(countries)):
        correctAnswers.append(quizQuestionAnswer[countries[i]])
        wrongAnswers = list(quizQuestionAnswer.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers[i])]
        wrongAnswers=random.sample(wrongAnswers,3)
        answers=wrongAnswers+[correctAnswers[i]]
        random.shuffle(answers)

    quizFile.write('%s. Choice capital of the country %s:\n' % (quizNum+1, countries[quizNum]))
    for j in range(4):
        quizFile.write(' %s. %s\n' %('ABCD'[j],answers[j]))
    quizFile.write('\n')
    answerFile.write('%s. %s\n' % (quizNum + 1, 'ABCD'[answers.index(correctAnswers[quizNum])]))
quizFile.close()
answerFile.close()
