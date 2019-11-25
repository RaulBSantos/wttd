from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Raul Santos',
                    cpf='12345678901',
                    email='raul@santos.net',
                    phone='21-99618-6180')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'raul@santos.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Raul Santos',
            '12345678901',
            'raul@santos.net',
            '21-99618-6180',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        # self.assertIn('Raul Santos', self.email.body)
        # self.assertIn('12345678901', self.email.body)
        # self.assertIn('raul@santos.net', self.email.body)
        # self.assertIn('21-99618-6180', self.email.body)
