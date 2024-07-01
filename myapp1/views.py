from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    age= 24
    for i in range(0,4):
     
     age=age+6
     context={
     'name':'raghav',
     'age': age,
     'chatmate':'jonny'

     }
    return render(request,'index.html',context)

def count(request):
   words= request.GET['text']
   word2=words+" wlcome ji"
   print(word2)
   
   return render(request,'count.html',{'word2':word2})