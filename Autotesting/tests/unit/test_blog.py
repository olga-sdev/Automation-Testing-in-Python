from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test Author', blog.author)
        self.assertListEqual([], blog.posts)
        self.assertEqual(0, len(blog.posts))

    def test_repr(self):
        blog = Blog('Test', 'Test Author')
        another_blog = Blog('Blog', 'Blog Author')

        self.assertEqual(blog.__repr__(),
                         'Test by Test Author (0 posts)')
        self.assertEqual(another_blog.__repr__(),
                         'Blog by Blog Author (0 posts)')

    def test_repr_multiple_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.posts = ['test']

        another_blog = Blog('Blog', 'Blog Author')
        another_blog.posts = ['test', 'another']

        self.assertEqual(blog.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(another_blog.__repr__(), 'Blog by Blog Author (2 posts)')
