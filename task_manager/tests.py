from django.test import TestCase
from . import models
from django.utils import timezone
from users.models import BaseUser
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import authenticate, login

# Create your tests here.


class TagTest(TestCase):
    def setUp(self, name='name1', date_of_creation=timezone.now()):
        user = BaseUser.objects.create(username='new_one', password='Qwerty12345')
        models.Tag.objects.create(name=name, user=user, slug=name, date_of_creation=date_of_creation)

    def test_tag_creation(self, name='name2', date_of_creation=timezone.now()):
        user = BaseUser.objects.create(username='one_person', password='Qwerty12345')
        tag = models.Tag.objects.create(name=name, user=user, slug=name, date_of_creation=date_of_creation)

        self.assertTrue(isinstance(tag, models.Tag))
        self.assertEqual(tag.__str__(), tag.name)
        self.assertEqual(tag.user, BaseUser.objects.get(username='one_person'))

    def test_tag_getting(self):
        tag = models.Tag.objects.get(name='name1')
        self.assertTrue(isinstance(tag, models.Tag))
        self.assertEqual(tag.__str__(), tag.name)
        self.assertEqual(tag.user, BaseUser.objects.get(username='new_one'))

    def test_tag_updating(self):
        tag = models.Tag.objects.get(name='name1')
        tag.name = 'new_name'
        user = BaseUser.objects.create(username='dora', password='Qwerty12345')
        tag.user = user
        tag.save()
        self.assertTrue(isinstance(tag, models.Tag))
        self.assertEqual(tag.__str__(), tag.name)
        self.assertEqual(tag.user, user)

    def test_tag_deleting(self):
        tag = models.Tag.objects.get(name='name1')
        url = reverse('task_manager:tag_detail', args=[tag.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskTest(TestCase):
    def setUp(self, name='name1', date_of_creation=timezone.now(), start_time=timezone.now(), deadline=timezone.now()):
        user = BaseUser.objects.create(username='new_one', password='Qwerty12345')
        models.Task.objects.create(name=name, user=user, slug=name, date_of_creation=date_of_creation,
                                   start_time=start_time, deadline=deadline)

    def test_task_creation(self, name='name2', date_of_creation=timezone.now(), start_time=timezone.now(), deadline=timezone.now()):
        user = BaseUser.objects.create(username='one_person', password='Qwerty12345')
        task = models.Task.objects.create(name=name, user=user, slug=name, date_of_creation=date_of_creation,
                                          start_time=start_time, deadline=deadline)
        self.assertTrue(isinstance(task, models.Task))
        self.assertEqual(task.__str__(), task.name)
        self.assertEqual(task.user, BaseUser.objects.get(username='one_person'))

    def test_task_getting(self):
        task = models.Task.objects.get(name='name1')
        self.assertTrue(isinstance(task, models.Task))
        self.assertEqual(task.__str__(), task.name)
        self.assertEqual(task.user, BaseUser.objects.get(username='new_one'))

    def test_task_updating(self):
        task = models.Task.objects.get(name='name1')
        name = 'new_name'
        task.name = name
        user = BaseUser.objects.create(username='dora', password='Qwerty12345')
        task.user = user
        task.save()
        self.assertTrue(isinstance(task, models.Task))
        self.assertEqual(task.__str__(), name)
        self.assertEqual(task.user, user)