from django.contrib.auth import authenticate, login
import collections
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render,redirect
from .models import Question , Subject , ChoiceMain , result_final
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.views import logout

def form(request,subject_id):
    username = request.session['name']
    latest_question_list = Question.objects.filter(subject__subject_code=subject_id)
    latest_choice_list = ChoiceMain.objects.filter(subject__subject_code=subject_id)
    count = Question.objects.filter(subject__subject_code=subject_id).count()
    i_list = []
    num_questions = Question.objects.filter(subject__subject_code=subject_id).count()
    for i in range(1,count):
        i_list.append(i)
    list1 = zip(latest_question_list, i_list)
    context = {'name' : username , 'subject' : subject_id ,'num_question':num_questions,'latest_question_list':latest_question_list,'latest_choice_list':latest_choice_list,'i_list':i_list}
    return render(request, 'form.html',context)

def completed(request):
    return render(request, 'example.html')

def second(request):
    return render(request,'example_2.html')

def store(request):
    cursor = connection.cursor()
    count = Question.objects.filter(subject__subject_code=request.POST['subname']).count()
    data = []
    od = collections.OrderedDict(sorted(request.POST.items()))
    for key in od:
        if ( key != 'csrfmiddlewaretoken' and key !='submit'):
            data.append(request.POST[key])
    if( count == 1):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,name,subject) VALUES (%s, %s, %s)")
        cursor.execute(insert_stmt, data)

    elif( count == 2):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,name,subject) VALUES (%s, %s, %s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 3):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,name,subject) VALUES (%s, %s, %s, %s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 4):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,name,subject) VALUES (%s, %s, %s, %s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 5):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q5,name,subject,) VALUES (%s, %s, %s, %s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 6):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q5,q6,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 7):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 8):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 9):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 10):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 11):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 12):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 13):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 14):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 15):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 16):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 17):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q17,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 18):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q17,q18,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    elif( count == 19):
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q17,q18,q19,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)

    else:
        insert_stmt = ("INSERT INTO myapp_result_final(q1,q2,q3,q4,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q17,q18,q19,q20,name,subject) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(insert_stmt, data)



    return redirect('https://surabhi.pythonanywhere.com/sub')

def logout1(request):
    logout(request)
    return redirect("https://surabhi.pythonanywhere.com/")

def sub(request):
    latest_question_list = Question.objects.all()
    latest_choice_list = ChoiceMain.objects.all()
    latest_subject_list = Subject.objects.all()
    c = Subject.objects.count()
    done_list = result_final.objects.values_list('subject', flat=True).filter(name=request.session['name'])
    c2 = result_final.objects.filter(name=request.session['name']).count()
    if( c2 == c ):
        return render(request, 'end.html',{'name':request.session['name']})
    context = {'done_list':done_list,'latest_question_list': latest_question_list , 'name' : request.session['name'] , 'latest_choice_list' : latest_choice_list , 'latest_subject_list' : latest_subject_list}
    return render(request, 'subject.html',context)


def log(request):
    if( request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['name'] = username
                c = Subject.objects.count()
                c2 = result_final.objects.values_list('subject', flat=True).filter(name=username).count()
                if( c2 == c ):
                    return render(request, 'end.html',{'name':request.session['name']})

                latest_question_list = Question.objects.all()
                latest_choice_list = ChoiceMain.objects.all()
                latest_subject_list = Subject.objects.all()
                done_list = result_final.objects.values_list('subject', flat=True).filter(name=username)
                context = {'done_list':done_list,'latest_question_list': latest_question_list , 'name' : username , 'latest_choice_list' : latest_choice_list , 'latest_subject_list' : latest_subject_list}
                return render(request, 'subject.html',context)

        else:
            return redirect('http://surabhi.pythonanywhere.com/')
    else:
        return redirect('http://surabhi.pythonanywhere.com/')
def base(request):
    if "name" in request.session:
        del request.session['name']
    return render(request, 'base.html')










