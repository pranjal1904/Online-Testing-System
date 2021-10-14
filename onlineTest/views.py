from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from onlineTest.models import *
from django.contrib.auth import authenticate,login,logout
import random
@csrf_exempt
def test(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/test/login/")
    res=render(request,'onlineTest/test_paper.html')
    return HttpResponse(res)

@csrf_exempt
def newQuestion(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/test/login/")
    res=render(request,'onlineTest/add_questions.html')
    return res

@csrf_exempt
def saveQuestion(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/test/login/")
    if(request.method=='POST'):
        formData=request.POST
        que=Questions()
        que.queno=formData['Question Number']
        que.que=formData['Question']
        que.ans=formData['Answer']
        que.marks=formData['Marks']
        que.save()
    s="http://localhost:8000/test/new-question/"
    return HttpResponseRedirect(s)

def question_info(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/test/login/")
    questions=Questions.objects.all()
    data={'que':questions}
    res=render(request,'onlineTest/show_questions.html',data)
    return res

@csrf_exempt
def userLogin(request):
    data={}
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect("http://localhost:8000/test/online-test/")
        else:
            data['error']="Username or Password is incorrect"
            return render(request,'onlineTest/user_login.html',data)
    else:
        return render(request,'onlineTest/user_login.html',data)



@csrf_exempt
def calculateResult(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/test/login/")
    if(request.method=='POST'):
        formData=request.POST
        totalMarks=0
        CorrectAnswered=[]
        WrongAnswered=[]
        NumberOfQuestions=0
        s=Questions.objects.get(que=formData['que0'])       
        if(s.ans == formData['ans0']):
            totalMarks+=4
            CorrectAnswered.append(0)
        else:
            WrongAnswered.append(0)
        NumberOfQuestions+=1

        s=Questions.objects.get(que=formData['que1'])       
        if(s.ans == formData['ans1']):
            totalMarks+=4
            CorrectAnswered.append(1)
        else:
            WrongAnswered.append(1)
        NumberOfQuestions+=1

        s=Questions.objects.get(que=formData['que2'])       
        if(s.ans == formData['ans2']):
            totalMarks+=4
            CorrectAnswered.append(2)
        else:
            WrongAnswered.append(2)
        NumberOfQuestions+=1

        s=Questions.objects.get(que=formData['que3'])       
        if(s.ans == formData['ans3']):
            totalMarks+=4
            CorrectAnswered.append(3)
        else:
            WrongAnswered.append(3)
        NumberOfQuestions+=1
    
    data={'totalMarks':totalMarks,'CorrectAnswered':CorrectAnswered,'WrongAnswered':WrongAnswered,'NumberOfQuestions':NumberOfQuestions}
    return render(request,'onlineTest/result.html',data)
    

            

def userLogout(request):
    logout(request)
    return HttpResponseRedirect("http://localhost:8000/test/login/")

def startTest(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/test/login/")
    s=set()
    while(len(s)<5):
        s.add(random.randint(0,7))
    q=[]
    for index in s:
        # q.append(Questions.objects.get(queno = index))
        q.append(Questions.objects.all()[index])
    data={}
    data["question"]=q
    res=render(request,'onlineTest/question_paper.html',data)
    return res