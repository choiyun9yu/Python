from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()

    # 이 객체를 참조할 때 어떤 필드를 보여줄 것인지
    def __str__(self):
        return self.name  

class Review(models.Model):
    # Moive 모델 참조를 위해 ForeignKey 필드 사용
    # 필드 이름 재설정 related_name='reviews'
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=30)
    star = models.IntegerField()
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    # 이 객체를 참조할 때 어떤 필드를 보여줄 것인지
    def __str__(self):
        return self.comment

class Actor(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()