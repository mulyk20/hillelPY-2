import uuid
from fastapi import Query, Path, HTTPException, APIRouter, Request, BackgroundTasks
from starlette import status
import app.tour_dao as dao
from app.tour_schemas import RegisterVisitorRequest, BaseUserInfo
from background_tasks.confirm_registration_for_visitor import confirm_registration_for_visitor

api_router_visitors = APIRouter(
    prefix='/api/visitors',
    tags=['API', 'Visitors']
)

@api_router_visitors.post('/create/', status_code=status.HTTP_201_CREATED)
def create_visitor(
        request: Request,
        new_visitor: RegisterVisitorRequest,
        background_tasks: BackgroundTasks,
) -> BaseUserInfo:
    maybe_visitor = dao.get_visitor_by_email(new_visitor.email)
    if maybe_visitor:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Visitor with email {new_visitor.email} already exists'
        )

    created_visitor = dao.create_visitor(**new_visitor.dict())
    background_tasks.add_task(confirm_registration_for_visitor, created_visitor, request.base_url)
    return created_visitor

@api_router_visitors.get('/verify/{visitor_uuid}')
def verify_visitor_account(visitor_uuid: uuid.UUID):
    maybe_visitor = dao.get_visitor_by_uuid(visitor_uuid)
    if not maybe_visitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Wrong data'
        )
    dao.activate_visitor_account(maybe_visitor)
    return {'verified': True, 'visitor_email': maybe_visitor.email}
