from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello():
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick':pick})

def name(request):
    my_name = '박누리'
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request):
    my_info=['박누리',25]
    name = '박누리'
    age = 25
    # dictionary
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'introduce.html', {'context':context})

def cus_introduce(request):
    context = {
        'name' : '박누리',
        'age' : 25,
        'favorite' : '../images/league.png',
        'img' : '../images/myham.png'
    }

    return render(request, 'cus_introduce.html', {'context': context})

def random_pick(request):
    data = ['12', '20', '31', '6', '22', '49', '58', '27', '24']
    pick = random.choice(data)
    context = {
        'pick' : pick
    }
    return render(request, 'random_pick.html', {'context':context})

def yourname(request, name):
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', {'context':context})


def search(request, name, age):
    context = {
        'name' : name,
        'age' :age
    }
    return render(request, 'search.html', {'context':context})

def multiple(request, num1, num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : num1*num2    
    }
    return render(request, 'multiple.html', {'context':context})

def gugu(request, num1, num2):
    list = []
    for data in range(1, num1):
        list.append(data*num2)
    context = {
        'list' : list
    }
    return render(request, 'gugu.html', {'context':context})


def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '가지튀김']
    empty_list = []
    my_string = 'Life is short, you need python'
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'today' : today,
        'empty_list' : empty_list,
        'my_string' : my_string
    }
    return render(request, 'dtl.html', context)

def forif(request):
    my_list = [100, 50, 20, 30, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b
    }
    return render(request, 'forif.html', context)