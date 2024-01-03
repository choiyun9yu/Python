from .models import Page
import random

def validate_page():
    pages = Page.objects.all()
    for page in pages:
        if (page.score<0) or (page.score>10):
            page.score = random.randint(0,10)
            page.save()
            print(page.id, '번 게시글 감정 점수 조정')