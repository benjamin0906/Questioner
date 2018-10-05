from tkinter import *
import tkinter
from random import randint
import codecs

root = tkinter.Tk()
QuestionArray = []
TestIterator = 0
TestNumber = 2
PrevTestNum = []
QuestionNumber = 0
GlobalCorrectAnswered = 0

NumberOfQuestions = Label(root)
NumberOfQuestions.place(x=5, y=50)
NumberOfQuestions.config(text='Click to load file')

LoadError = Label(root)

HelperLabel = Label(root, text='Number of training questions')
HelperLabel.place(x=240, y=5)

HelperLabel2 = Label(root, text='Give the path of file of question')
HelperLabel2.place(x=0, y=5)

ResultLabel = Label(root, text='Result:\n../..')
ResultLabel.place(x=400, y=130)

def ReadInFile(FileName):
    global QuestionNumber
    global LoadError
    global QuestionArray
    QuestionArray = []
    LoadError.destroy()
    LoadError = Label(root)
    LoadError.place(x=5, y=70)
    LoadError.config(text='')
    f = open(FileName, 'r')
    # f = codecs.open(FileName,encoding='utf-8',mode='r')
    s = 'asd'
    QuestionStartString = '<question>\n'
    QuestionEndString = '</question>'
    QuestionSign = '\t<q> '
    AnswerSign = '\t<a> '
    CorrectAnswerSign = '\t<ac> '
    a = 1
    b = 0
    c = 1
    QuestionNumber = 0
    s = f.readlines(0)
    for looper in range(0, len(s) - 1):
        s[looper] = bytes(s[looper + 1], "ansi").decode("utf-8")
    array = [[], []]
    meta = []
    array.append(meta)
    WrongFormat = 0
    LoopEn = 0
    # This looper discover the file of questions, and read the strings of: question, correct answer and possible answers
    # It puts into a list according to:
    #   1.  String of question
    #   2.  String of correct answer
    #   3.. String of the possible answers

    for looper in range(0, len(s)):
        if (s[looper] == QuestionStartString):
            looper = looper + 1
            if (s[looper][0:5] == QuestionSign and ('\n' != s[looper][5:len(s)])):
                meta = []
                ####here the string will be encode to utf-16
                # meta.append((s[looper][4:len(s[looper])-1]).encode('utf-8'))
                meta.append((s[looper][4:len(s[looper]) - 1]))
                # print((s[looper][4:len(s[looper])-1]))
                # print(str("éí").encode("utf-8"))
                QuestionNumber = QuestionNumber + 1
                corr = 0
                wrong = 0
                looper = looper + 1
                CAnswerNumber = 0
                temp = []
                while (looper < len(s)) and (s[looper][0:11] != QuestionEndString):
                    if (s[looper][0:6] == CorrectAnswerSign and ('\n' != s[looper][6:len(s)])):
                        if (corr == 0):
                            meta.append(temp)
                            meta[1].append(s[looper][5:len(s[looper]) - 1])
                            corr = 1
                        else:
                            if (CAnswerNumber != 0):
                                try:
                                    meta[1].append(s[looper][5:len(s[looper]) - 1])
                                except:
                                    LoopEn = 1
                                    LoadError.config(text=('Critical error in line ' + str(looper + 1)))
                            # meta[1]=s[looper][5:len(s[looper])-1]

                        CAnswerNumber = CAnswerNumber + 1
                    elif s[looper][0:5] == AnswerSign and ('\n' != s[looper][5:len(s)]):
                        if (corr == 0):
                            meta.append('valasz')
                            corr = 1
                        meta.append(s[looper][4:len(s[looper]) - 1])
                    elif s[looper][0:11] != QuestionEndString:
                        if (WrongFormat == 0):
                            LoadError.config(text=('Wrong format in line: ' + str(looper + 1)))
                        else:
                            LoadError.config(text=(LoadError.cget('text') + str(looper + 1)))
                        # print('Wrong format in line:',looper+1)
                        wrong = 1
                    looper = looper + 1
                    if (LoopEn != 0):
                        break;
                if (wrong == 0):
                    QuestionArray.append(meta)
            else:
                if (WrongFormat == 0):
                    LoadError.config(text=('Wrong format in line: ' + str(looper + 1)))
                else:
                    LoadError.config(text=(LoadError.cget('text') + str(looper + 1)))
                # print('Wrong format in line:',looper+1)
        if (LoopEn != 0):
            break;
    f.close()
    NumberOfQuestions.config(text='Number of questions: ' + str(len(QuestionArray)))

QuestionLabel = Label(root)
QuestionLabel.place(x=10, y=90)
QuestionLabel.config(text='', wraplength=350, justify='left')

AnswerStringArray = []
AnswerArray = []
CorrectAnswers = []
CheckerVariable = []

def SetQuestion(QuestionIter):
    global AnswerStringArray
    global AnswerArray
    global CorrectAnswers
    global CheckerVariable
    AnswerStringArray = []
    CorrectAnswers = []
    CheckerVariable = []
    for i in range(len(AnswerArray)):
        AnswerArray[i].destroy()
    AnswerArray = []
    QuestionLabel.config(text=QuestionArray[QuestionIter][0])
    # QuestionLabel.config(text=(str("száéüíűóüör").encode("utf-8")).decode("utf-8"))
    x = 20
    y = 130
    looper = 1
    for looper in range(0, len(QuestionArray[QuestionIter][1])):
        AnswerStringArray.append(QuestionArray[QuestionIter][1][looper])
        # AnswerArray.append(Checkbutton (root, text = QuestionArray[QuestionIter][1][looper], command = asd))
        # AnswerArray[looper].place(x=x,y=y)
        CorrectAnswers.append(QuestionArray[QuestionIter][1][looper])
        # y=y+20
    looper = looper + 1
    for looper2 in range(0, len(QuestionArray[QuestionIter]) - 2):
        AnswerStringArray.append(QuestionArray[QuestionIter][2 + looper2])
        # AnswerArray.append(Checkbutton (root, text = QuestionArray[QuestionIter][2+looper2]))
        # AnswerArray[looper+looper2].place(x=x,y=y)
        # y=y+20
    iter = 0
    PrevRands = []

    for i in range(0, len(AnswerStringArray)):
        CheckerVariable.append(IntVar(value=0))
    while iter != len(AnswerStringArray):
        a = randint(0, len(AnswerStringArray) - 1)
        b = 0
        for i in range(0, len(PrevRands)):
            if a == PrevRands[i]:
                b = b + 1
        if (b == 0):
            # CheckerVariable
            AnswerArray.append(Checkbutton(root, text=AnswerStringArray[a], variable=CheckerVariable[iter], wraplength=320, justify='left'))
            AnswerArray[iter].place(x=x, y=y)
            if (len(AnswerStringArray[a]) >= 70):
                y = y + 60
            else:
                y = y + 30
            PrevRands.append(a)
            iter = iter + 1

def SetTheQuestion():
    ReadInFile(FileEntry.get())

AnswerButtonNumber = 0
AnsweredButton = Button(root)
# AnsweredButton.place(x=250,y=180)
qwe = ''

def Evaluation():
    global AnswerButtonNumber
    global AnsweredButton
    global TestIterator
    global PrevTestNum
    global qwe
    global AnswerStringArray
    global AnswerArray
    global CorrectAnswers
    global CheckerVariable
    global GlobalCorrectAnswered
    CorrectVar = 0
    # print('AnswerButtonNumber')
    # print(AnswerButtonNumber)
    # print('TestIterator')
    # print(TestIterator)
    if (AnswerButtonNumber == 0):
        TestIterator = TestIterator + 1
        AnswerButtonNumber = 1
        AnsweredButton.config(text="Következő")
        for looper in range(0, len(AnswerArray)):
            looper2 = 0
            while looper2 < len(CorrectAnswers) and AnswerArray[looper].cget('text') != CorrectAnswers[looper2]:
                looper2 = looper2 + 1
            if (CheckerVariable[looper].get() != 0):
                if (looper2 == len(CorrectAnswers)):
                    AnswerArray[looper].config(foreground='red')
                else:
                    AnswerArray[looper].config(foreground='green')
                    CorrectVar = CorrectVar + 1
            else:
                if (looper2 == len(CorrectAnswers)):
                    AnswerArray[looper].config(foreground='gray')
                else:
                    AnswerArray[looper].config(foreground='blue')

        if (CorrectVar == len(CorrectAnswers)):
            GlobalCorrectAnswered = GlobalCorrectAnswered + 1
            ResultLabel.config(text='Result:\n' + str(GlobalCorrectAnswered) + '/' + str(TestIterator))
        else:
            ResultLabel.config(text='Result:\n' + str(GlobalCorrectAnswered) + '/' + str(TestIterator))
    else:
        if (TestNumber > TestIterator):
            if (TestIterator < len(QuestionArray)):
                b = 1
                while b != 0:
                    b = 0
                    a = randint(0, len(QuestionArray) - 1)
                    for looper in range(0, len(PrevTestNum)):
                        if (a == PrevTestNum[looper]):
                            b = b + 1
            else:
                a = randint(0, len(QuestionArray) - 1)
            PrevTestNum.append(a)
            SetQuestion(PrevTestNum[len(PrevTestNum) - 1])
            AnsweredButton.config(text="Ok")
        else:
            StartButton.config(text="Start")
            PrevTestNum = []
            AnswerStringArray = []
            CorrectAnswers = []
            CheckerVariable = []
            for i in range(len(AnswerArray)):
                AnswerArray[i].destroy()
            AnswerArray = []
            QuestionLabel.config(text='')
            StartButton.config(text="Start")
            AnsweredButton.destroy()
        AnswerButtonNumber = 0

FileName = 'asd'

def StartTest():
    global AnsweredButton
    global TestIterator
    global GlobalCorrectAnswered
    if (StartButton.cget('text') == 'Start'):
        global TestNumber
        TestNumber = (int(TestNumberEntry.get()))
        ResultLabel.config(text='Result:\n../' + str(TestNumber))
        StartButton.config(text="Stop")
        PrevTestNum.append(randint(0, len(QuestionArray) - 1))
        SetQuestion(PrevTestNum[len(PrevTestNum) - 1])
        # AnsweredButton.config(visible='yes')
        AnsweredButton = Button(root, width=8, text="Evaluate", command=Evaluation)
        AnsweredButton.place(x=400, y=100)
        TestIterator = 0
        GlobalCorrectAnswered = 0
        ResultLabel.config(text='Result\n' + str(GlobalCorrectAnswered) + '/' + str(TestIterator))
    else:
        global AnswerStringArray
        global AnswerArray
        global CorrectAnswers
        global CheckerVariable
        AnswerStringArray = []
        CorrectAnswers = []
        CheckerVariable = []
        for i in range(len(AnswerArray)):
            AnswerArray[i].destroy()
        AnswerArray = []
        QuestionLabel.config(text='')
        StartButton.config(text="Start")
        AnsweredButton.destroy()

FileEntry = Entry(root, textvariable=FileName)
FileEntry.place(x=5, y=30)
FileEntry.insert(0, 'questions.q')

FileEntryButton = Button(root, width=5, text="Load", command=SetTheQuestion)
FileEntryButton.place(x=150, y=27)

TestNumberEntry = Entry(root, textvariable=qwe)
TestNumberEntry.place(x=250, y=30)

StartButton = Button(root, width=5, text="Start", command=StartTest)
StartButton.place(x=400, y=25)

root.geometry("500x500")
root.mainloop()

