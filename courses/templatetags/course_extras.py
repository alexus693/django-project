from django import template

from django.utils.safestring import mark_safe

import markdown2

from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    ''' Gets the meost recent course that was added to the Library'''
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/courses_nav.html')
def nav_courses_list():
    '''returns a dictionary of courses to display a naviagation plane'''
    courses=Course.objects.all()
    return {'courses':courses}  

@register.filter('time_estimate')
def time_estimate(word_count):
    ''' estimates the N0 of minutes it will take to complete a step based on the passed in_wordcount.'''
    minutes=round(word_count/20)
    return minutes   

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    ''' Convert markdown text to html.'''
    html_body=markdown2.markdown(markdown_text)
    return mark_safe(html_body)

