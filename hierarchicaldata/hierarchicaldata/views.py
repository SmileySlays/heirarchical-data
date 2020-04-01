from django.shortcuts import render
from hierarchicaldata.models import File

def show_files(request):
    return render(request, "files.html", {'files': File.objects.all()})