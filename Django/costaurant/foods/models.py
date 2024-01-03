from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)   # CharField는 최대길이 필수 입력
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=25)

    def __stf__(self):
        # __str__ 함수는 이 클래스를 하나의 문자열로 표현하는 것을 지정해주는 함수
        # print(className을 했을 때 결과로 나오는 문자열을 넣어주는 것)
        # toString 처럼 쓸수도 있을 듯
        return self.name    