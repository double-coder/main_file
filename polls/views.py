from django.shortcuts import render
from django.http import HttpResponse

def polls_req(request):
    return render(request,'polls/login.html')
def index(request):
    latest_question_list = LoginID.objects.order_by('-username')[:5]
    output = ', '.join([q.username for q in latest_question_list])
    return HttpResponse(output)


    

# Create your views here.
