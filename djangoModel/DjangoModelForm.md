django day10																							2020.06.17

---

# Model 생성

DB 스키마 생성



app_folder > models.py 에 스키마 정의

```python
from django.db import models

# Create your models here.
# 객체 생성 (클래스 생성) -> 테이블 명
class Musician(models.Model):
    # 멤버 변수
    # name = '이름이란 사람이 가지는 공통 특성'
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # 인스턴스 호출 시 출력 내용 덮어쓰기
    def __str__(self):
        return f'{self.name} : {self.age}'
```



```bash
python manage.py makemigrations

python manage.py migrate
```



! vscode DOCTYPE html 자동완성 단축키

`!` +` tab`

# ModelForm

# Bootstrap4

## 1. install

https://django-bootstrap4.readthedocs.io/en/latest/installation.html

```bash
pip install django-bootstrap4
```



## 2. setting

`{project_name}>settings.py`의 `INSTALLED_APPS`에 `bootstrap4` 추가

```python
INSTALLED_APPS = [
    'bootstrap4',
]
```

`base.html`파일에 library 추가

```html
{% load bootstrap4 %}

{# Load CSS and JavaScript #}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
```



