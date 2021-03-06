from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField()


    def __str__(self):
        return self.Title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title

class Text(Step):
    content = models.TextField(blank=True, default='') 
    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
               'course_pk': self.course_id,
               'step_pk': self.id
        })


class Quiz(Step):
    total_questions = models.IntegerField(default=4)
    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
               'course_pk': self.course_id,
               'step_pk': self.id
        })

    class Meta:
        verbose_name_plural = "Quizzes"  