from django.test import TestCase
from django.contrib.auth.models import User
from blog.post import Post
from django.utils.text import slugify


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Cria um usuário de teste
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Cria um post de teste
        cls.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=cls.user,
            content='This is test content',
            status=1
        )

    def test_post_creation(self):
        """Testa se o post foi criado corretamente"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.content, 'This is test content')
        self.assertEqual(self.post.status, 1)

    def test_post_str_method(self):
        """Testa o método __str__ do modelo"""
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_ordering(self):
        """Testa se os posts são ordenados por data de criação (mais recente primeiro)"""
        post2 = Post.objects.create(
            title='Second Post',
            slug='second-post',
            author=self.user,
            content='Second content',
            status=1
        )
        posts = Post.objects.all()
        self.assertEqual(posts[0], post2)
        self.assertEqual(posts[1], self.post)

    def test_title_max_length(self):
        """Testa o tamanho máximo do título"""
        max_length = self.post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_is_unique(self):
        """Testa se o slug é único"""
        with self.assertRaises(Exception):
            Post.objects.create(
                title='Another Post',
                slug='test-post',  # Slug duplicado
                author=self.user,
                content='Content'
            )

    def test_post_default_status(self):
        """Testa se o status padrão é Draft (0)"""
        post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='Draft content'
        )
        self.assertEqual(post.status, 0)

    def test_author_relationship(self):
        """Testa o relacionamento com User"""
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertIn(self.post, self.user.blog_post.all())