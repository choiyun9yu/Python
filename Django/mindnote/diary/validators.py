from django.core.exceptions import ValidationError

def validate_no_hash(value):
    if ('#' in value) or ('@' in value):
        raise ValidationError("제목'과 '내용'에는 '#'이 들어갈 수 없습니다.", code='symbol-err')
    
def validate_no_number(value):
    if value.isdigit() :
        raise ValidationError("'감정 상태' 에는 숫자가 들어갈 수 없습니다.", code='symbol-err')
    
def validate_no_above10(value):
    if (value>10) or (value<0):
        raise ValidationError(" '감정 점수'는 0부터 10사이의 숫자만 들어갈 수 있습니다.", code='symbol-err')