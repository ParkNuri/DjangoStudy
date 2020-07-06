Django																																			2020.06.10

---

# Django

## 1.설치하기

bash 창에서

```bash
 pip install django=={django version}
 
 ex)
 pip install django==2.1.15
```



## 2. 시작하기

#### 1) django 프로젝트 생성

```bash
django-admin startproject {project_name} {project_location}

 ex)
django-admin startproject mysite .
```



#### 2)

```bash
python manage.py startapp {app_name}

ex)
python manage.py startapp pages
```



#### 3) settings.py 수정하기

* Installed_apps 에 내가 설정한 애플리케이션 이름 추가하기

  (django에게 내 app 알리기)

```python
### settings.py ###

INSTALLED_APPS = [
    'pages',
    ...
    ]
```

* 언어/시간 설정

```python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



#### 4) 서버 실행

```bash
python manage.py runserver
```





#### 5) urls.py에 url 경로 설정

```python
urlpatterns = [
    path('{url_name}/', {view_file_name}.{function_name})
]
```

```python
### urls.py ###

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index)
]
```



#### 5-1+) 여러 경로 한 곳에 모아 등록하기

1. urls.py에 include import

```python
from django.urls import path, include
```



2. app_name으로 폴더를 생성한 후 urls.py 추가하기

#### 6) views.py 에 함수 추가

! django에서는 기본적으로 templates 폴더를 html 파일 위치로 인식하기 때문에 templates 내의 파일들을 별도의 import 없이 사용할 수 있다.

```python
def {function_name}(request):
    return render(request, '{html_file_name}', {'{key}':value})
```



```python
### views.py ###

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello():
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick':pick})
```



#### 7) 앱 폴더에 templates 폴더 생성 후 html 작성

```python
# view에서 넘겨준 인자를 html에서 사용하는법
{{ {key_name} }}
```



```python
### index.html ###

<h1>Hello, World!</h1>
```

```python
### hello.html ###

<h1>오늘 점심 메뉴는 {{ pick }}</h1>
```







https://docs.djangoproject.com/en/3.0/topics/http/urls/



## 3. 파일 설명

* __init__.py

:

* admin.py 

: DB내의 데이터들을 어떻게 꾸며서 보여줄지 설정

* apps.py

: app의 전체적인 정보를 담고있는 파일

* models.py

: 

* views.py

:

* tests.py

: model을 테스트하기 위해 사용하는 파일

* MTV 패턴 

  : django의 모델링 구조 Model, Template(view), View(controller)

* urls.py

:



# 4. 구조

![image-20200610100504872](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200610100504872.png)



## + 구구단

```python
def gugu(request, num1, num2):
    list = []
    for data in range(1, num1):
        list.append(data*num2)
    context = {
        'list' : list
    }
    return render(request, 'gugu.html', {'context':context})

```



```html
<h1>{{context.list}}</h1>
{# 이것도 주석 #}
{% comment %}
여기도 주석
여러줄 주석
{% endcomment %}
<!--django template language (DTL) %-->
<!-- for문 -->
{% for num in context.list %}
<p>{{num}}</p>
{% endfor %}
```



* result

  ![image-20200610150637919](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200610150637919.png)

# For문

```python
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
```



```html
<h1>for문</h1>
{% for food in my_list %}
<p>{{forloop.counter}}.{{food}}</p>
{% endfor %}
<hr>
<!-- empty 를 이용해 list가 비어있는지 확인 가능-->
{% for data in empty_list %}
<p>data</p>
{% empty %}
<p>비어있습니다.</p>
{% endfor %}

<h2>조건문</h2>
{% for food in my_list%}
{% if forloop.first %}
{{ forloop.first }}
{{ forloop.last }}
<p>짜장면엔 고춧가루지</p>
{% else %}
<p>{{food}}</p>
{% endif %}
{% endfor %}

<hr>
<h2>filter 활용</h2>
<p>{{ my_string|lower }}</p>
<p>{{ my_string|upper }}</p>
<p>{{ my_string|title }}</p>
<p>{{ my_string|length }}</p>
<p>{{ my_string|truncatewords:3 }}</p>
<!-- truncatechars: ... 까지 count에 포함-->
<p>{{ my_string|truncatechars:3 }}</p>
<hr>
<h2>lorem ipsum</h2>
<!-- dtl에 이미 lorem ipsum이 정의되어있음 -->
{% lorem %}
<!-- 3 w : 세 단어만 출력-->
<!-- 3 p : 세 문단만 출력-->
<hr>
{% lorem 3 w %}
{% lorem 3 p %}
```



* result

  ![image-20200610144951844](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200610144951844.png)



# For문, If문

```python
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
```

```html
<p>data a : {{data_a}}</p>
<p>data b : {{data_b}}</p>

<hr>

{% for data in my_list%}
<h4>{{ data }}</h4>
{% endfor %}

<hr>

{% for data in my_list %}
{% if data == 10 %}
<p>your got lowest score</p>
{% elif data == 100 %}
<p>your got highest score</p>
{% else %}
<p>your score : {{ data }}</p>
{% endif %}
{% endfor %}
<hr>

{% if 5 >= my_string|length %}
<p>short!</p>
{% elif my_string|length >= 10 %}
<p>long!</p>
{% else %}
<p>적당~</p>
{% endif %}

<hr>

{% for data in my_list %}
{% if data >= 90 %}
<p>A</p>
{% elif data >= 50 %}
<p>B</p>
{% else %}
<p>C</p>
{% endif %}
{% endfor %}
```



* result

![image-20200610144855178](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200610144855178.png)

# 