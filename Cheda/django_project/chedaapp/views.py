from django.shortcuts import render
# Display View import
from django.views.generic import ListView, DetailView
# Generic Date View import
# from django.views.generic.dates import ArchiveIndexView, YearArchiveView,MonthArchiveView
# from django.views.generic.dates import DayArchiveView, TodayArchiveView

# model import 해오기
from .models import Item, Nak, Snu, Mirim, Forever, Gumin, Sb

# Create your views here.
class ItemLV(ListView):
    # 기본적으로 모든 view를 짤 때, model=Item으로 지정해주어서 어떤 테이블에서 긁어오는지 지정해주어야한다.
    model = Item
    template_name = 'info.html'

class NakLV(ListView):
    model = Nak
    template_name = 'nak.html'

class SnuLV(ListView):
    model = Snu
    template_name = 'snu.html'

class MirimLV(ListView):
    model=Mirim
    template_name = 'mirim.html'

class ForeverLV(ListView):
    model=Forever
    template_name = 'forever.html'

class GuminLV(ListView):
    model=Gumin
    template_name = 'gumin.html'

class SbLV(ListView):
    model=Sb
    template_name = 'sb.html'