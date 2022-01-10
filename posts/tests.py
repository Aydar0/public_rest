from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create user
        testuser_1 = User.objects.create(username='testuser', password='absd1234')

        # Create a blog post
        test_post = Post.objects.create(author=testuser_1, title='Blog title', body='Body content ...')

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        body = f'{post.body}'
        title = f'{post.title}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content ...')


