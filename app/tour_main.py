from fastapi import FastAPI, HTTPException, Query, Path, status
from app.tour_database import create_tables
from app.tour_schemas import TourCreate, Tour
import app.tour_dao as dao

app = FastAPI(on_startup=[create_tables])

@app.post('/api/tours/', response_model=Tour, status_code=status.HTTP_201_CREATED)
def create_tour(tour: TourCreate):
    return dao.create_tour(tour.dict())

@app.get('/api/tours/', response_model=list[Tour])
def get_tours(limit: int = Query(10, gt=0), skip: int = Query(0, ge=0)):
    return dao.get_all_tours(limit=limit, skip=skip)

@app.get('/api/tours/{tour_id}', response_model=Tour)
def get_tour(tour_id: int = Path(..., gt=0)):
    tour = dao.get_tour_by_id(tour_id)
    if tour is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tour not found")
    return tour

@app.put('/api/tours/{tour_id}', response_model=Tour)
def update_tour(tour_id: int, tour: TourCreate):
    updated_tour = dao.update_tour(tour_id, tour.dict())
    if updated_tour is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tour not found")
    return updated_tour

@app.delete('/api/tours/{tour_id}', response_model=dict)
def delete_tour(tour_id: int):
    success = dao.delete_tour(tour_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tour not found")
    return {"status": "success", "tour_id": tour_id}
