from flask import Flask, render_template
from store import PostStore, Post

app = Flask(__name__)

dummy_posts = [
    Post(id=1,
         photo_url='https://images.pexels.com/photos/91227/pexels-photo-91227.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
         name='Karl',
         body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
    Post(id=2,
         photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
         name='John',
         body='Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]
post_store = PostStore([])
post_store.add(dummy_posts[0])
post_store.add(dummy_posts[1])



@app.route('/')
def home():
    return render_template('index.html', posts=post_store.get_all())


app.run()
