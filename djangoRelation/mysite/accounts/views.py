from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # AuthenticationForm은 ModelForm이 
        # 아닌 Form 상속
        # 별도로 정의된 Model이 없다는 뜻
        # 그래서 넘겨주는 인자가 달라진다.
        if form.is_valid():
            # 로그인은 DB에 뭔가 작성하는 것은
            # 동일하지만, 연결된 모델이 있는건
            # 아닙니다.
            # 그럼 무엇을 확인해야 하는가?
            # 세션과 유저 정보
            auth_login(request, form.get_user())
#            return redirect(request.GET.get('next'), 'articles:index')
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('articles:index')        
    else:
        # auth_form = AuthenticationForm(request, request.POST)
        # if auth_form.is_valid():
        #     user =auth_form.get_user
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 이전 세션을 유지하면서 업데이트된 유저 정보로 갱신
            update_session_auth_hash(request, request.user)
            return redirect('articles:index')
    else :
        print(request.user)
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)