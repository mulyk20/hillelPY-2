from typing import List, Union

from sqlalchemy.orm.exc import NoResultFound

from app.tour_database import Tour, session


def create_tour(tour_data: dict) -> Tour:
    tour = Tour(**tour_data)
    session.add(tour)
    session.commit()
    return tour


def get_all_tours(limit: int = 10, skip: int = 0) -> List[Tour]:
    return session.query(Tour).offset(skip).limit(limit).all()


def get_tour_by_id(tour_id: int) -> Union[Tour, None]:
    try:
        return session.query(Tour).filter(Tour.id == tour_id).one()
    except NoResultFound:
        return None


def update_tour(tour_id: int, tour_data: dict) -> Union[Tour, None]:
    tour = get_tour_by_id(tour_id)
    if tour:
        for key, value in tour_data.items():
            setattr(tour, key, value)
        session.commit()
        return tour
    return None


def delete_tour(tour_id: int) -> bool:
    tour = get_tour_by_id(tour_id)
    if tour:
        session.delete(tour)
        session.commit()
        return True
    return False
