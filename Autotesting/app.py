from blog import Blog
from post import Post

MENU_PROMPT = 'Enter: '\
              '"C" to create a blog; '\
              '"L" to list the blogs; '\
              '"R" to read the blog; '\
              '"P" to create a post; '\
              '"Q" to quit '
blogs = dict()


def menu():
    # Show the available blogs
    # Let make the choice
    # Interact with the choice
    # Exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "C":
            ask_create_blog()
        elif selection == "L":
            print_blogs()
        elif selection == "R":
            ask_read_blog()
        elif selection =="P":
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    # Print the available blogs
    for key, blog in blogs.items():
        print(f'- {blog}')


def ask_create_blog():
    title = input('Enter blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input('Enter the blog title you want to read')
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print(f'{post.title}, {post.content}')


def ask_create_post():
    blog_title = input('Enter the blog title to write a post in: ')
    post_title = input('Enter post title: ')
    post_content = input('Enter post content: ')

    blogs[blog_title].create_post(post_title, post_content)


