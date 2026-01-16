from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.post import Post


class PostViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Cria posts publicados e rascunhos
        cls.published_post = Post.objects.create(
            title='Published Post',
            slug='published-post',
            author=cls.user,
            content='Published content',
            status=1
        )
        
        cls.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=cls.user,
            content='Draft content',
            status=0
        )

    def setUp(self):
        self.client = Client()

    def test_home_page_status_code(self):
        """Testa se a home page retorna status 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view(self):
        """Testa a listagem de posts"""
        # Você precisará criar esta view
        # response = self.client.get(reverse('post_list'))
        # self.assertEqual(response.status_code, 200)
        pass

    def test_post_detail_view(self):
        """Testa a visualização de detalhes de um post"""
        # response = self.client.get(reverse('post_detail', args=[self.published_post.slug]))
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Published Post')
        pass