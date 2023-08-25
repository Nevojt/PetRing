
from database import get_db, SessionLocal
import models as models


# отримання всієї таблиці
def get_sesion():
    
    posts = next(get_db()).query(models.Post).all()
    return posts

result = get_sesion()

for post in result:
    print(post.surowiec, post.cena_za_kg)

#  Отримання конкретного елементу
def get_specific_post(surowiec: str = 'EURO'):
    db = SessionLocal()
    try:
        post = db.query(models.Post).filter(models.Post.surowiec == surowiec).first()
        return post
    finally:
        db.close()
specific_post = get_specific_post()




if specific_post:
    print("Title:", specific_post.surowiec)
    print("Cena:", specific_post.cena_za_kg)
    # Виведіть інші поля, які вас цікавлять
else:
    print("Рядок з таким ID не знайдений")
