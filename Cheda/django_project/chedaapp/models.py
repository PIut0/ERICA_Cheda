from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100) #강좌명
    for_whom = models.CharField(max_length=50) #교육대상

    L_FIELD_CHOICES = [
        ('CF','문화예술/가정'), #Culture and Family
        ('SP', '생활체육/건강'), #Sports
        ('HS','인문/사회'), #Humanities and Social
        ('IT','IT관련'), #IT
        ('LC', '자격증과정'), #License
        ('GN', '일반') #General
    ]

    l_field = models.CharField(max_length=2, choices=L_FIELD_CHOICES) #강좌분야

    fee = models.IntegerField() #수강료
    st_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_시작
    fin_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_끝

    date = models.TextField(max_length=200) #수강요일
    where = models.CharField(max_length=100) #교육장소

    to_st_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_시작
    
    to_fin_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_끝
    
    people=models.IntegerField() #수강정원

    how_apply = models.CharField(max_length = 50) #접수방법
    ask=models.CharField(max_length=50) #문의전화

    etc=models.TextField(max_length=300) #비고

    def __str__(self):
        return self.name

class Nak(models.Model):
    name = models.CharField(max_length=100) #강좌명
    for_whom = models.CharField(max_length=50) #교육대상
    L_FIELD_CHOICES = [
        ('문화예술/가정','문화예술/가정'), #Culture and Family
        ('생활체육/건강', '생활체육/건강'), #Sports
        ('인문/사회','인문/사회'), #Humanities and Social
        ('IT관련','IT관련'), #IT
        ('자격증과정', '자격증과정'), #License
        ('일반', '일반') #General
    ]
    l_field = models.CharField(max_length=10, choices=L_FIELD_CHOICES) #강좌분야
    fee = models.IntegerField() #수강료
    st_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_시작
    fin_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_끝
    date = models.TextField(max_length=200) #수강요일
    where = models.CharField(max_length=100) #교육장소
    to_st_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_시작
    to_fin_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_끝
    people=models.IntegerField() #수강정원
    how_apply = models.CharField(max_length = 50) #접수방법
    ask=models.CharField(max_length=50) #문의전화
    etc=models.TextField(null=True, blank=True) #비고

    def __str__(self):
        return self.name

class Snu(models.Model):
    name = models.CharField(max_length=100) #강좌명
    for_whom = models.CharField(max_length=50) #교육대상
    L_FIELD_CHOICES = [
        ('문화예술/가정','문화예술/가정'), #Culture and Family
        ('생활체육/건강', '생활체육/건강'), #Sports
        ('인문/사회','인문/사회'), #Humanities and Social
        ('IT관련','IT관련'), #IT
        ('자격증과정', '자격증과정'), #License
        ('일반', '일반') #General
    ]
    l_field = models.CharField(max_length=10, choices=L_FIELD_CHOICES) #강좌분야
    fee = models.IntegerField() #수강료
    st_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_시작
    fin_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_끝
    date = models.TextField(max_length=200) #수강요일
    where = models.CharField(max_length=100) #교육장소
    to_st_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_시작
    to_fin_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_끝
    people=models.IntegerField() #수강정원
    how_apply = models.CharField(max_length = 50) #접수방법
    ask=models.CharField(max_length=50) #문의전화
    etc=models.TextField(null=True, blank=True) #비고

    def __str__(self):
        return self.name

class Mirim(models.Model):
    name = models.CharField(max_length=100) #강좌명
    for_whom = models.CharField(max_length=50) #교육대상
    L_FIELD_CHOICES = [
        ('문화예술/가정','문화예술/가정'), #Culture and Family
        ('생활체육/건강', '생활체육/건강'), #Sports
        ('인문/사회','인문/사회'), #Humanities and Social
        ('IT관련','IT관련'), #IT
        ('자격증과정', '자격증과정'), #License
        ('일반', '일반') #General
    ]
    l_field = models.CharField(max_length=10, choices=L_FIELD_CHOICES) #강좌분야
    fee = models.IntegerField() #수강료
    st_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_시작
    fin_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_끝
    date = models.TextField(max_length=200) #수강요일
    where = models.CharField(max_length=100) #교육장소
    to_st_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_시작
    to_fin_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_끝
    people=models.IntegerField() #수강정원
    how_apply = models.CharField(max_length = 50) #접수방법
    ask=models.CharField(max_length=50) #문의전화
    etc=models.TextField(null=True, blank=True) #비고

    def __str__(self):
        return self.name

class Forever(models.Model):
    name = models.CharField(max_length=100) #강좌명
    for_whom = models.CharField(max_length=50) #교육대상
    L_FIELD_CHOICES = [
        ('문화예술/가정','문화예술/가정'), #Culture and Family
        ('생활체육/건강', '생활체육/건강'), #Sports
        ('인문/사회','인문/사회'), #Humanities and Social
        ('IT관련','IT관련'), #IT
        ('자격증과정', '자격증과정'), #License
        ('일반', '일반') #General
    ]
    l_field = models.CharField(max_length=10, choices=L_FIELD_CHOICES) #강좌분야
    fee = models.IntegerField() #수강료
    st_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_시작
    fin_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_끝
    date = models.TextField(max_length=200) #수강요일
    where = models.CharField(max_length=100) #교육장소
    to_st_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_시작
    to_fin_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_끝
    people=models.IntegerField() #수강정원
    how_apply = models.CharField(max_length = 50) #접수방법
    ask=models.CharField(max_length=50) #문의전화
    etc=models.TextField(null=True, blank=True) #비고

    def __str__(self):
        return self.name

class Gumin(models.Model):
    name = models.CharField(max_length=100) #강좌명
    for_whom = models.CharField(max_length=50) #교육대상
    L_FIELD_CHOICES = [
        ('문화예술/가정','문화예술/가정'), #Culture and Family
        ('생활체육/건강', '생활체육/건강'), #Sports
        ('인문/사회','인문/사회'), #Humanities and Social
        ('IT관련','IT관련'), #IT
        ('자격증과정', '자격증과정'), #License
        ('일반', '일반') #General
    ]
    l_field = models.CharField(max_length=10, choices=L_FIELD_CHOICES) #강좌분야
    fee = models.IntegerField() #수강료
    st_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_시작
    fin_period = models.DateField(auto_now=False, auto_now_add=False) #교육기간_끝
    date = models.TextField(max_length=200) #수강요일
    where = models.CharField(max_length=100) #교육장소
    to_st_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_시작
    to_fin_date = models.DateTimeField(auto_now=False, auto_now_add=False) #접수기간_끝
    people=models.IntegerField() #수강정원
    how_apply = models.CharField(max_length = 50) #접수방법
    ask=models.CharField(max_length=50) #문의전화
    etc=models.TextField(null=True, blank=True) #비고

    def __str__(self):
        return self.name