from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test Post', 'Test Content')

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, 'Test Post')
        self.assertEqual(blog.posts[0].content, 'Test Content')
