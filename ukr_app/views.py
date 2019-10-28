import json
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_celery_beat.models import PeriodicTask, IntervalSchedule
# Create your views here.
from django_celery_beat.models import IntervalSchedule

from .models import Links


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


class LinkForm(ModelForm):
    class Meta:
        model = Links
        fields = ['url', 'interval']


def link_list(request, template_name='ukr_app/links_list.html'):
    link = Links.objects.all()
    data = {}
    data['object_list'] = link
    return render(request, template_name, data)


def link_view(request, pk, template_name='ukr_app/links_detail.html'):
    link = get_object_or_404(Links, pk=pk)
    return render(request, template_name, {'object': link})


def link_create(request, template_name='ukr_app/links_form.html'):
    form = LinkForm(request.POST or None)
    if form.is_valid():
        form.save()
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=form.cleaned_data.get("interval"),
            period=IntervalSchedule.SECONDS, )
        PeriodicTask.objects.create(interval=schedule, name=form.cleaned_data.get("url"), task='ukr_app.tasks.test', args=json.dumps([form.instance.id]))
        return redirect('link_list')
    return render(request, template_name, {'form': form})


def link_update(request, pk, template_name='ukr_app/links_form.html'):
    link = get_object_or_404(Links, pk=pk)
    form = LinkForm(request.POST or None, instance=link)
    if form.is_valid():
        form.save()
        return redirect('link_list')
    return render(request, template_name, {'form': form})


def link_delete(request, pk, template_name='ukr_app/links_confirm_delete.html'):
    link = get_object_or_404(Links, pk=pk)
    if request.method == 'POST':
        link.delete()
        return redirect('link_list')
    return render(request, template_name, {'object': link})
