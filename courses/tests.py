from django.test import TestCase

from django.utils import timezone

from .models import Course

class CourseModelTest(TestCase):
    def test_case_creation(self):
        course = Course.objects.create(
            Title ="Python Regular Expressions",
            Description ="Learn to write regular expressions in python"
        )
        now= timezone.now()
        self.assertLess(course.created_at, now)
