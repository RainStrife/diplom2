from django.core.urlresolvers import reverse
from django.test import TestCase
from core.models import Formation


class MainTestCase(TestCase):

    def test_note_list_view(self):
        url = reverse('formation_list_view')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        formation = Formation.objects.create(title='Тестовая Новость', leader='Тестовый руководитель')

        response = self.client.get(url)
        self.assertIn(formation, response.context_data['object_list'])

