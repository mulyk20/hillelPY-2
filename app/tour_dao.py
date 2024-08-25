import uuid
from app.tour_database import Product, session, User, Visitor
from utils.utils_hashlib import get_password_hash

def create_product(name: str, description: str, price: float, quantity: int, cover_url: str) -> Product:
    product = Product(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        cover_url=cover_url
    )
    session.add(product)
    session.commit()
    return product

def get_all_products(limit: int = 100, skip: int = 0, name: str = '') -> list[Product]:
    products = session.query(Product).filter(Product.name.ilike(f'%{name}%')).offset(skip).limit(limit).all()
    return products

def search_products(name: str = '', limit: int = 100, skip: int = 0) -> list[Product]:
    query = session.query(Product)
    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))
    products = query.offset(skip).limit(limit).all()
    return products

def update_product(product_id: int, name: str, description: str, price: float, quantity: int, cover_url: str) -> Product:
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity
    product.cover_url = cover_url
    session.commit()
    session.refresh(product)
    return product

def delete_product(product_id: int) -> bool:
    product = session.query(Product).filter(Product.id == product_id).first()
    if not product:
        return False
    session.delete(product)
    session.commit()
    return True

def create_user(name: str, email: str, password: str) -> User:
    user = User(
        name=name,
        email=email,
        hashed_password=get_password_hash(password),
    )
    session.add(user)
    session.commit()
    return user

def get_user_by_email(email: str) -> User | None:
    user = session.query(User).filter(User.email == email).first()
    return user

def get_user_by_uuid(user_uuid: uuid.UUID) -> User | None:
    user = session.query(User).filter(User.user_uuid == user_uuid).first()
    return user

def activate_user_account(user: User) -> User:
    if user.is_verified:
        return user

    user.is_verified = True
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def create_visitor(name: str, email: str, password: str) -> Visitor:
    visitor = Visitor(
        name=name,
        email=email,
        hashed_password=get_password_hash(password),
    )
    session.add(visitor)
    session.commit()
    return visitor

def get_visitor_by_email(email: str) -> Visitor | None:
    visitor = session.query(Visitor).filter(Visitor.email == email).first()
    return visitor

def get_visitor_by_uuid(visitor_uuid: uuid.UUID) -> Visitor | None:
    visitor = session.query(Visitor).filter(Visitor.visitor_uuid == visitor_uuid).first()
    return visitor

def activate_visitor_account(visitor: Visitor) -> Visitor:
    if visitor.is_verified:
        return visitor

    visitor.is_verified = True
    session.add(visitor)
    session.commit()
    session.refresh(visitor)
    return visitor
