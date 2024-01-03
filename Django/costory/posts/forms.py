from django import forms
from .models import Post
# from .validators import validate_symbols
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    # 모델과 연관되지 않은 데이터 받을 때 추가적으로 폼필드 만들어서 받는다.
    # memo =  forms.CharField(max_length=80, validators=[validate_symbols])

    # PostForm을 만들 때 적용할 옵션을 명시하는 Meta클래스
    class Meta:
        # 참조할 모델 명시
        model = Post
        # 참조할 필드 명시
        fields = ['title', 'content']
        # 모든 필드 참조하고 싶으면
        # fields = '__all__'    
        # 위젯에 접근할 때 사용
        widgets = {'title': forms.TextInput(attrs={
                    'class':'title',
                    'placeholder': '제목을 입력하세요.'}),
                'content': forms.Textarea(attrs={
                    'placeholder': '내용을 입력하세요'}),
                }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
                raise ValidationError('*는 포함될 수 없습니다.')
        return title


# class PostForm(forms.Form):
#     # forms.CharField는 기본적으로 한 줄 입력을 위한 위젯을 가지고 있다.
#     title = forms.CharField(max_length=50, label='제목')
#     # 여러줄 입력을 위한 위젯으로 Textarea가 있다.
#     content = forms.CharField(label='내용', widget=forms.Textarea)

