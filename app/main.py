from unicodedata import name
from venv import create
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db.base import Base
from db.engine import engine, session_local
from services import medicine_services
from dbmodels import Medicines, Orders, Permissions, Roles, Users
from models import MedicinesBase, MedicinesCreate, MedicinesUpdate, OrdersBase, OrdersCreate, OrdersStatusUpdate, PermissionsBase, PermissionsCreate, PermissionsUpdate, RolesBase, RolesCreate, RolesUpdate, UsersBase, UsersCreate, UsersUpdate


app = FastAPI()

Base.metadata.create_all(engine)


def create_database():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# Đọc dữ liệu của tất cả các loại thuốc


@app.get("/medicines", response_model=list[MedicinesBase])
def get_all_medicines(skip: int = 0, limit: int = 200, session: Session = Depends(create_database)):
    read_all_medicines = medicine_services.get_all(
        session, skip=skip, limit=limit)
    return read_all_medicines


# Đọc dữ liệu của thuốc thông qua id
@app.get("/medicine/{id}", response_model=MedicinesBase)
def get_one_by_id(id: int, session: Session = Depends(create_database)):
    read_medicines = medicine_services.get_one(session,  id)
    return read_medicines


# Tạo thêm thuốc vào db
@app.post("/medicine", response_model=MedicinesCreate)
def create_one_medicine(medicine: MedicinesCreate, session: Session = Depends(create_database)):
    create_medicine = Medicines.create(medicine)
    session.add(create_medicine)
    session.commit()
    session.refresh(create_medicine)
    return create_medicine


# Cập nhật thuốc
@app.put("/medicine/{id}", response_model=MedicinesUpdate)
def update_medicine_by_id(medicine: MedicinesUpdate, session: Session = Depends(create_database)):
    update_mecdicine = medicine_services.get_one(session)
    if update_mecdicine:
        update_mecdicine.medicine = medicine
        session.commit()
    session.close()
    return update_mecdicine


# Xóa thuốc
@app.delete("/medicine/{id}", response_model=MedicinesBase)
def delete_medicine_by_id(id: int, session: Session = Depends(create_database)):
    delete_medicine = medicine_services.get_one(session, id)
    if delete_medicine:
        session.delete(delete_medicine)
        print(f"Đã xóa thành công thuốc với id là {id}")
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"medicine with id {id} not found"
        )

    return f"Đã xóa thành công id thuốc là {id}"


# Đọc dữ liệu của tất cả các loại order
@app.get("/orders", response_model=list[OrdersBase])
def get_all_orders(skip: int = 0, limit: int = 200, session: Session = Depends(create_database)):
    read_all_orders = medicine_services.get_all(
        session, skip=skip, limit=limit)
    return read_all_orders


# Đọc dữ liệu của order thông qua id
@app.get("/order/{id}", response_model=OrdersBase)
def get_order_by_id(id: int, session: Session = Depends(create_database)):
    read_order = medicine_services.get_one(session, id)
    return read_order


# Tạo thêm order vào db
@app.post("/order", response_model=OrdersCreate)
def create_one_order(order: OrdersCreate, session: Session = Depends(create_database)):
    create_order = Orders.create(order)
    session.add(create_order)
    session.commit()
    session.refresh(create_order)
    return create_order


# Cập nhật order
@app.put("/order/{id}", response_model=OrdersStatusUpdate)
def update_order_by_id(id: int, order: OrdersStatusUpdate, session: Session = Depends(create_database)):
    update_mecdicine = medicine_services.get_one(session,  id)
    if update_mecdicine:
        update_mecdicine.order = order
        session.commit()
    session.close()
    return update_mecdicine


# Xóa order
@app.delete("/order/{id}", response_model=OrdersBase)
def delete_order_by_id(id: int, session: Session = Depends(create_database)):
    delete_order = medicine_services.get_one(session, id)
    if delete_order:
        session.delete(delete_order)
        print(f"Đã xóa thành công order với id là {id}")
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"order with id {id} not found"
        )

    return f"Đã xóa thành công id order là {id}"


# Đọc dữ liệu của tất cả các loại thuốc
@app.get("/permissions", response_model=list[PermissionsBase])
def get_all_permissions(skip: int = 0, limit: int = 200, session: Session = Depends(create_database)):
    read_all_permissions = medicine_services.get_all(
        session, skip=skip, limit=limit)
    return read_all_permissions


# Đọc dữ liệu của thuốc thông qua id
@app.get("/permission/{id}", response_model=PermissionsBase)
def get_permission_by_id(id: int, session: Session = Depends(create_database)):
    read_permission = medicine_services.get_one(session,  id)
    return read_permission


# Tạo thêm thuốc vào db
@app.post("/permission", response_model=PermissionsCreate)
def create_one_permission(permission: PermissionsCreate, session: Session = Depends(create_database)):
    create_permission = Permissions.create(permission)
    session.add(create_permission)
    session.commit()
    session.refresh(create_permission)
    return create_permission


# Cập nhật thuốc
@app.put("/permission/{id}", response_model=PermissionsUpdate)
def update_permission_by_id(id: int, permission: PermissionsUpdate, session: Session = Depends(create_database)):
    update_permission = medicine_services.get_one(session,  id)
    if update_permission:
        update_permission.permission = permission
        session.commit()
    session.close()
    return update_permission


# Xóa thuốc
@app.delete("/permission/{id}", response_model=PermissionsBase)
def delete_permission_by_id(id: int, session: Session = Depends(create_database)):
    delete_permission = medicine_services.get_one(session, id)
    if delete_permission:
        session.delete(delete_permission)
        print(f"Đã xóa thành công thuốc với id là {id}")
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"medicine with id {id} not found"
        )

    return f"Đã xóa thành công id thuốc là {id}"


# Đọc dữ liệu của tất cả các loại thuốc
@app.get("/roles", response_model=list[RolesBase])
def get_all_roles(skip: int = 0, limit: int = 200, session: Session = Depends(create_database)):
    read_all_roles = medicine_services.get_all(session, skip=skip, limit=limit)
    return read_all_roles


# Đọc dữ liệu của thuốc thông qua id
@app.get("/role/{id}", response_model=RolesBase)
def get_role_by_id(id: int, session: Session = Depends(create_database)):
    read_role = medicine_services.get_one(session,  id)
    return read_role


# Tạo thêm thuốc vào db
@app.post("/role", response_model=RolesCreate)
def create_one_role(role: RolesCreate, session: Session = Depends(create_database)):
    create_role = Roles.create(role)
    session.add(create_role)
    session.commit()
    session.refresh(create_role)
    return create_role


# Cập nhật thuốc
@app.put("/role/{id}", response_model=RolesUpdate)
def update_role_by_id(id: int, role: RolesUpdate, session: Session = Depends(create_database)):
    update_role = medicine_services.get_one(session,  id)
    if update_role:
        update_role.role = role
        session.commit()
    session.close()
    return update_role


# Xóa thuốc
@app.delete("/role/{id}", response_model=RolesBase)
def delete_role_by_id(id: int, session: Session = Depends(create_database)):
    delete_role = medicine_services.get_one(session, id)
    if delete_role:
        session.delete(delete_role)
        print(f"Đã xóa thành công role với id là {id}")
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"role with id {id} not found"
        )

    return f"Đã xóa thành công id role là {id}"


# Đọc dữ liệu của tất cả các loại user
@app.get("/users", response_model=list[UsersBase])
def get_all_users(skip: int = 0, limit: int = 200, session: Session = Depends(create_database)):
    read_all_users = medicine_services.get_all(session, skip=skip, limit=limit)
    return read_all_users


# Đọc dữ liệu của thuốc thông qua id
@app.get("/user/{id}", response_model=UsersBase)
def get_one_by_id(id: int, session: Session = Depends(create_database)):
    read_user = medicine_services.get_one(session,  id)
    return read_user


# Tạo thêm thuốc vào db
@app.post("/read_user", response_model=UsersCreate)
def create_one_user(user: UsersCreate, session: Session = Depends(create_database)):
    create_user = Users.create(user)
    session.add(create_user)
    session.commit()
    session.refresh(create_user)
    return create_user


# Cập nhật thuốc
@app.put("/user/{id}", response_model=UsersUpdate)
def update_user_by_id(id: int, user: UsersUpdate, session: Session = Depends(create_database)):
    update_user = medicine_services.get_one(session,  id)
    if update_user:
        update_user.user = user
        session.commit()
    session.close()
    return update_user


# Xóa thuốc
@app.delete("/user/{id}", response_model=UsersBase)
def delete_user_by_id(id: int, session: Session = Depends(create_database)):
    delete_user = medicine_services.get_one(session, id)
    if delete_user:
        session.delete(delete_user)
        print(f"Đã xóa thành công user với id là {id}")
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"user with id {id} not found"
        )

    return f"Đã xóa thành công id user là {id}"
