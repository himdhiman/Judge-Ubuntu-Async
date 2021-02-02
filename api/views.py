from django.shortcuts import render, redirect
from django.http import JsonResponse
from api import models, forms
import os, shutil, json, requests
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import serializers
from api.models import Submission
from api.models import Problem
import asyncio
from api import tasks

BASE_DIR = Path(__file__).resolve().parent.parent


def upload_tc(request):
    if request.method == "POST":
        form = forms.TcUpload(request.POST, request.FILES)
        files = request.FILES.getlist("testcases")
        ProbId = request.POST['name']
        if form.is_valid():
            for f in files:
                file_instance = models.UploadTC(name = models.Problem.objects.get(pk = int(ProbId)), testcases=f)
                file_instance.save()
        files_list = os.listdir(os.path.join(BASE_DIR, 'media/tempTC'))
        if(os.path.isdir(os.path.join(BASE_DIR, "media", "TestCases", ProbId))):
            shutil.rmtree(os.path.join(BASE_DIR, "media", "TestCases", ProbId))
        os.mkdir(os.path.join(BASE_DIR, "media", "TestCases", ProbId))
        for f in files_list:
            shutil.move(os.path.join(BASE_DIR, "media", "tempTC", f), os.path.join(BASE_DIR, "media", "TestCases", ProbId))

    else:
        form = forms.TcUpload()
    return render(request, "uploadtc.html", {"form": form})




@api_view(["GET", "POST"])
def getData(request):
    body = json.loads(request.body)
    if(body['type'] == "list"):
        s = set()
        for i in body['tags']:
            tagId = models.Tag.objects.get(name=i)
            c = models.Problem.objects.filter(tags=tagId.id).values_list('id', flat=True)
            for i in c:
                qs = models.Problem.objects.get(pk=i)
                s.add(qs.id)
        final_qs = models.Problem.objects.filter(id__in = s);
        res = serializers.ProblemSerializer(final_qs, many = True)
        return Response(res.data)
    else:
        probId = body["id"]
        q = models.Problem.objects.get(id = probId)
        res = serializers.ProblemSerializer(q)
        return Response(res.data)





@api_view(['POST'])
def runCode(request, uid):
    body = json.loads(request.body)
    tasks.runCode.delay(body, uid)
    return Response()