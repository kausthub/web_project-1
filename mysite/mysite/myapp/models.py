from django.db import models


class Subject(models.Model):
    subject_code = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.subject_code

class Question(models.Model):
    subject = models.ForeignKey(Subject)
    question_text = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

class ChoiceMain(models.Model):
    subject = models.ForeignKey(Subject)
    choice_text = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text


class result_final(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    q1 = models.CharField(max_length=10,null=True,blank=True)
    q2 = models.CharField(max_length=10,null=True,blank=True)
    q3 = models.CharField(max_length=10,null=True,blank=True)
    q4 = models.CharField(max_length=10,null=True,blank=True)
    q5 = models.CharField(max_length=10,null=True,blank=True)
    q6 = models.CharField(max_length=10,null=True,blank=True)
    q7 = models.CharField(max_length=10,null=True,blank=True)
    q8 = models.CharField(max_length=10,null=True,blank=True)
    q9 = models.CharField(max_length=10,null=True,blank=True)
    q10 = models.CharField(max_length=10,null=True,blank=True)
    q11 = models.CharField(max_length=10,null=True,blank=True)
    q12 = models.CharField(max_length=10,null=True,blank=True)
    q13 = models.CharField(max_length=10,null=True,blank=True)
    q14 = models.CharField(max_length=10,null=True,blank=True)
    q15 = models.CharField(max_length=10,null=True,blank=True)
    q16 = models.CharField(max_length=10,null=True,blank=True)
    q17 = models.CharField(max_length=10,null=True,blank=True)
    q18 = models.CharField(max_length=10,null=True,blank=True)
    q19 = models.CharField(max_length=10,null=True,blank=True)
    q20 = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

