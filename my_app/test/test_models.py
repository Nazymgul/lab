from django.test import TestCase

from my_app.models import test


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        test.objects.create(first_name='name', username='name')

    

    def test_false_is_false(self):
        
        self.assertFalse('BFASG'.islower())

    def test_false_is_true(self):
        
        self.assertTrue('asada'.islower())

    def test_one_plus_one_equals_two(self):
        author = test.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name 
        self.assertEqual(field_label,'first_name')