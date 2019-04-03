
class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body


class PostStore:

    def __init__(self, posts):
        self.posts = posts

    def get_all(self):
        for post in self.posts:
            print(post.name)
        return self.posts

    def add(self, post):
        return self.posts.append(post)

    def get_by_id(self, id):
        result = 'No post with this id'

        for post in self.posts:
            if post.id == id:
                result = post
                break

        print(result.name, result.body)
        return result

    def update(self, id, fields):
        post = self.get_by_id(id)
        post.name = fields['name']
        post.photo_url = fields['photo_url']
        post.body = fields['body']
        print(post.name, post.body)
        return post

    def delete(self, id):
        post = self.get_by_id(id)
        self.posts.remove(post)
        return self.posts
