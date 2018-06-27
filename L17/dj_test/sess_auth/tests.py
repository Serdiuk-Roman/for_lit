from django.test import TestCase

# Create your tests here.


class TaskViewTest(TestCase):

    def test_create_article():
        art_num1 = Articles.objects.count()
        # create_new
        art_num2 = Articles.objects.count()
        # testcase good if art2 - art1 == 1