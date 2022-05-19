# from faker import Faker
# from fastapi.encoders import jsonable_encoder

# from db.engine import session_local
# from models import UsersBase
# from services import user_services

# fake = Faker()

# def test_get_user():
#     user_dict = {
#         "role_id": fake.random_int(min=1,max=4),
#         "user_name": fake.pystr(min_chars= 4, max_chars=20),
#         "password": fake.password(length=10),
#         "name":fake.name(),
#         "gender":fake.random_int(min=0,max=1),
#         "date_of_birth":fake.date_of_birth(),
#         "email":fake.ascii_free_email(),
#         "address":fake.street_address(),
#         "phone_numbers":fake.phone_number()
#     }

#     user_in = UsersBase(**user_dict)

#     user_create=user_services.create_one(session_local(), obj=user_in)

#     user_get=user_services.get_one(session_local(), id=user_create.id)
    
#     assert user_create.user_name == user_get.user_name
#     assert jsonable_encoder(user_create)==jsonable_encoder(user_get)

