from django.shortcuts import render, redirect
import re
from django.http import HttpResponse
from .models import Record
from django.views.generic import TemplateView


def welcome(request):
    if request.POST:
        p, s = request.POST["regex"], request.POST["text"]
        result = bool(re.findall(p, s))
        record = Record(regex=p, text=s, result=result)
        record.save()
        print("THIS IS", record.pk)
        return redirect(f"result/{record.pk}/")
    return render(request=request, template_name='record/welcome.html')


class Result(TemplateView):
    def get(self, request, pk):
        template_name = 'record/result.html'
        data = Record.objects.get(id=pk)
        return render(request, template_name=template_name, context={'ob': data})


def history(request):
    data = Record.objects.all().order_by('-pk')
    return render(request, template_name="record/history.html", context={'data': data})