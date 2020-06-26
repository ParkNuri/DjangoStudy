from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # username은 unique 해야하기때문에 수정 자제
        fields = ['email', 'first_name', 'last_name']