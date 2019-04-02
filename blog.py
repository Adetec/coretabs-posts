from store import PostStore, Post

class Blog:
    def __init__(self, title, photo, name, date, content):
        self.title = title
        self.photo =photo
        self.name = name
        self.date = date
        self.content = content


blog1 = Blog(title="Hello world",
             photo="https://media.licdn.com/dms/image/C4D03AQGuD6ly4LPekg/profile-displayphoto-shrink_200_200/0?e=1559779200&v=beta&t=DjYWqekHp5ITYCMJG8wHE8aycQAhwNVdBZFpfai6Tdo",
             name="Adel", date="4/1/2019", content="Hello amazing coretabs community!")

print(blog1.name)

post1 = Post(id=1,
             photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
             name='Sara',
             body='Lorem Ipsum')
post2 = Post(id=2,
             photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
             name='John',
             body='Lorem Ipsum')

updated_fields = {
    "name": "Adel",
    "photo_url": "https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100",
    "body": "coucou"
}


store = PostStore([])

store.get_all()
store.add(post1)
store.add(post2)
store.get_all()
print('Get by id')
store.get_by_id(2)
print("Update")
store.update(2, updated_fields)

