from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.post import Post


class AdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )
        self.client.login(username='admin', password='admin123')
        
        self.post = Post.objects.create(
            title='Admin Test Post',
            slug='admin-test-post',
            author=self.admin_user,
            content='Admin test content',
            status=1
        )

    def test_admin_post_list(self):
        """Testa se os posts aparecem no admin"""
        response = self.client.get('/admin/blog/post/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Post')

    def test_admin_post_change(self):
        """Testa se é possível acessar a página de edição"""
        response = self.client.get(f'/admin/blog/post/{self.post.id}/change/')
        self.assertEqual(response.status_code, 200)

    def test_admin_login_required(self):
        """Testa se o admin requer login"""
        self.client.logout()
        response = self.client.get('/admin/blog/post/')
        self.assertEqual(response.status_code, 302)  # Redirect to login