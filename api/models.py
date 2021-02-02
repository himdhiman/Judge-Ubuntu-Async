from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Problem(models.Model):
    choose = (
        ("E", "Easy"),
        ("M", "Medium"),
        ("H", "Hard"),
    )

    title = models.CharField(max_length = 100)
    description = models.TextField()
    note = models.TextField(blank = True, null = True)
    tags = models.ManyToManyField(Tag)
    level = models.CharField(max_length = 20, choices = choose)
    accuracy = models.IntegerField()
    totalSubmissions = models.IntegerField()
    sampleTc = models.IntegerField()
    totalTC = models.IntegerField()
    createdAt = models.DateField()
    memoryLimit = models.CharField(max_length = 20, null = True, blank = True)
    timeLimit = models.CharField(max_length = 20, null = True, blank = True)


    def __str__(self):
        return self.title


class UploadTC(models.Model):
    name = models.ForeignKey(to = "Problem", on_delete = models.CASCADE)
    testcases = models.FileField(upload_to = "tempTC/", blank = True, null = True)

class Submission(models.Model):
    LANGUAGE_CODE = (
        ('CP', 'CPP'),
        ('JV', 'JAVA'),
        ('P3', 'PYTHON 3'),
        ('P2', 'PYTHON 2'),
        ('JS', 'JAVASCRIPT')
    )
    STATUS_CODE = (
        ('Q', 'QUEUED'),
        ('R', 'RUNNING'),
        ('AC', 'ACCEPTED'),
        ('CE', 'COMPILATION ERROR'),
        ('WA', 'WRONG ANSWER'),
        ('RE', 'RUNTIME ERROR')
    )
    userId = models.IntegerField(blank = False)
    problemId = models.IntegerField(blank = False)
    language = models.CharField(max_length = 2, choices = LANGUAGE_CODE)
    code = models.TextField(blank = True)
    status = models.CharField(max_length = 2, choices = STATUS_CODE)
    error = models.TextField(blank = True)
    inputGiven = models.TextField(blank = True)
    outputGen = models.TextField(blank = True) 
    testCasesPassed = models.CharField(max_length = 15, blank = True)

    def __str__(self):
        return str(self.pk)
