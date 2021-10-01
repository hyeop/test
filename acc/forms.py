from django.forms import ModelForm
from .models import User
from django import forms
 
class FeedbackForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegistForm(forms.Form):
    email = forms.EmailField( label='이메일', widget=forms.EmailInput(attrs={'class':'form-control'}) )
    username = forms.CharField(label="이름", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField( label='비밀번호', widget=forms.PasswordInput(attrs={'class':'form-control'}) ) 
    re_password = forms.CharField( label='비밀번호 확인', widget=forms.PasswordInput(attrs={'class':'form-control'}) )

    def clean(self): 
        # 요청파라미터 값들 조회 
        print(super().clean())
        cleaned_data = super().clean() # dictionary 반환. 
        print(cleaned_data)
        username = cleaned_data.get('username') 
        password = cleaned_data.get('password') 
        re_password = cleaned_data.get('re_password') #password와 re_password가 같은지 체크 
        print(username, password, re_password)
        if password != re_password: 
            self.add_error('password', '비밀번호가 다릅니다.') 
            self.add_error('re_password', '비밀번호가 다릅니다') # 이메일(아이디) 중복 체크 
            try: 
                User.objects.get(pk=username) 
                self.add_error('email', '이미 가입된 이메일입니다.') 
            except: # # 조회 결과가 없다. 등록되지 않은 email 
                pass

# 출처: https://steminher.tistory.com/4 [so geek]