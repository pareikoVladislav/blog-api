from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            email="test@email.com",
            password="secret",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="Test title",
            body="Test body content",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "test_user")
        self.assertEqual(self.post.title, "Test title")
        self.assertEqual(self.post.body, "Test body content")
        self.assertEqual(str(self.post), "Test title")
