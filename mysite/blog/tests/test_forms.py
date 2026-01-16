from django.test import TestCase
from django.contrib.auth.models import User
from blog.post import Post


class PostFormTest(TestCase):
    """Testes para formulários de Post (quando criar)"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_valid_post_data(self):
        """Testa dados válidos para criar um post"""
        post_data = {
            'title': 'Form Test Post',
            'slug': 'form-test-post',
            'author': self.user,
            'content': 'Form test content',
            'status': 1
        }
        post = Post.objects.create(**post_data)
        self.assertTrue(post.id)
        self.assertEqual(post.title, 'Form Test Post')

    def test_blank_title_invalid(self):
        """Testa que título em branco é inválido"""
        with self.assertRaises(Exception):
            Post.objects.create(
                title='',
                slug='blank-title',
                author=self.user,
                content='Content'
            )