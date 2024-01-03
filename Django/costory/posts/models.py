from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.
class Post(models.Model):
    # 글의 제목 , 글의 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50, unique=True,  
                             error_messages={'unique':'이미 있는 제목이네요!'})
    # CharField(max_length=50)와 TextField()의 차이는 최대길이에 대해 정의가 필요한지 여부
    content = models.TextField(validators=[MinLengthValidator(10, '너무 짧군요! 10자 이상 적어주세요.'), 
                                           validate_symbols]) 
    # verbose_name은 사람이 읽기 좋은 필드명을 지정해주는 인자
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    # auto_now_add(처음 추가될 때 시간 저장), auto_now(마지막 수정 시간 저장)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title