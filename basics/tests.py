import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionDummyTests(TestCase):

    def test_dummy(self):
        a = Question(title='Test', init_time=timezone.now(), status=False,
                     mod_time=timezone.now(), description='Dummy question')
        self.assertEqual(a.title, 'Test')
