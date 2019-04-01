
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
        # get all posts - الحصول على كل المنشورات
        for post in self.posts:
            print(post.name)
        return self.posts

    def add(self, post):
        # append post - إضافة منشور
        return self.posts.append(post)

    def get_by_id(self, id):
        # search for post by id - id البحث عن منشور بالمعرف
        print('hh')

    def update(self, id, fields):
        # update post data - id تعديل منشور بالمعرف
        print('hh')

    def delete(self, id):
        # delete post by id - id حذف منشور بالمعرف
        print('hh')