from django.test import TestCase
from todos.models import Todo
from django.utils import timezone
from todos.forms import TodoForm


class TodoTestCase(TestCase):

    def setUp(self):
        self.todo_day = Todo.objects.create(
            headline="Test 1",
            description="Test 1",
            deadline=timezone.now(),
            recurring="d"
        )

        self.todo_week = Todo.objects.create(
            headline="Test 2",
            description="Test 2",
            deadline=timezone.now(),
            recurring="w"
        )

        self.todo_month = Todo.objects.create(
            headline="Test 3",
            description="Test 3",
            deadline=timezone.now(),
            recurring="m"
        )

        self.todo_year = Todo.objects.create(
            headline="Test 4",
            description="Test 4",
            deadline=timezone.now(),
            recurring="y"
        )

    def test_todo_headline_saved_correctly(self):
        self.assertEqual(self.todo_day.headline, 'Test 1')
        self.assertEqual(self.todo_week.headline, 'Test 2')
        self.assertEqual(self.todo_month.headline, 'Test 3')
        self.assertEqual(self.todo_year.headline, 'Test 4')

    def test_todo_description_saved_correctly(self):
        self.assertEqual(self.todo_day.description, 'Test 1')
        self.assertEqual(self.todo_week.description, 'Test 2')
        self.assertEqual(self.todo_month.description, 'Test 3')
        self.assertEqual(self.todo_year.description, 'Test 4')

    def test_todo_recurring_saved_correctly(self):
        self.assertEqual(self.todo_day.recurring, 'd')
        self.assertEqual(self.todo_week.recurring, 'w')
        self.assertEqual(self.todo_month.recurring, 'm')
        self.assertEqual(self.todo_year.recurring, 'y')

    def test_todo_form_valid_recurring_day(self):
        form = TodoForm(data={
            'headline': 'Test1',
            'description': "This is a Test",
            'deadline': timezone.now(),
            'recurring': 'd'
        })
        self.assertTrue(form.is_valid())

    def test_todo_form_valid_recurring_week(self):
        form = TodoForm(data={
            'headline': 'Test1',
            'description': "This is a Test",
            'deadline': timezone.now(),
            'recurring': 'w'
        })
        self.assertTrue(form.is_valid())

    def test_todo_form_valid_recurring_month(self):
        form = TodoForm(data={
            'headline': 'Test1',
            'description': "This is a Test",
            'deadline': timezone.now(),
            'recurring': 'm'
        })
        self.assertTrue(form.is_valid())

    def test_todo_form_valid_recurring_year(self):
        form = TodoForm(data={
            'headline': 'Test1',
            'description': "This is a Test",
            'deadline': timezone.now(),
            'recurring': 'y'
        })
        self.assertTrue(form.is_valid())

    def test_todo_form_unvalid_recurring(self):
        form = TodoForm(data={
            'headline': 'Test1',
            'description': "This is a Test",
            'deadline': timezone.now(),
            'recurring': 't'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
# Create your tests here.
