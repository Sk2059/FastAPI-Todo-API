from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.current_user import get_current_user
from app.models.user import User
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

#creating task
@router.post(
    "",
    response_model=TaskResponse,
    status_code=201
)
def create_task(
    task: TaskCreate,
    db:Session=Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        owner_id=current_user.id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

#getting filtered task of login user
@router.get("",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
    return tasks

# #getting specific task
@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(task_id:int,db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    task = db.query(Task).filter(
        Task.id==task_id,
        Task.owner_id==current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="task you requested coluldn't be found"
        )
    return task

#updating task
@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id:int,
    task_update: TaskUpdate,
    db:Session=Depends(get_db),
    current_user :User=Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id==task_id,
        Task.owner_id==current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    
    update_data= task_update.model_dump(
        exclude_unset=True
    )

    for key,value in update_data.items():
        setattr(task,key ,value)

    db.commit()
    db.refresh(task)

    return task

#delete Task
@router.delete(
    "/{task_id}",
    status_code=201 
)
def delete_task(
    task_id:int,
    db:Session= Depends(get_db),
    current_user:User= Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id==task_id,
        Task.owner_id==current_user.id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="task doesn't exist"
        )
    db.delete(task)
    db.commit()

#mark complete
@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse
)
def complete_task(
    task_id:int,
    db:Session= Depends(get_db),
    current_user:User= Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    task.completed = True

    db.commit()
    db.refresh(task)

    return task

#getting tasks with pegination 
# @router.get(
#     "pegination",
#     response_model=list[TaskResponse]
# )
# def get_tasks_with_pagination(
#     skip: int = 0,
#     limit:int =10,
#     db:Session=Depends(get_db),
#     current_user:User=Depends(get_current_user)
# ):
#     task = (
#         db.query(Task)
#         .filter(Task.owner_id==current_user.id)
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )
#     return task

#filtering
# @router.get(
#     "/filtering",
#     response_model=list[TaskResponse]
# )
# def get_tasks(
#     completed: bool | None = None,
#     priority: str | None = None,
#     db:Session=Depends(get_db),
#     current_user:User=Depends(get_current_user)
# ):
#     query = db.query(Task).filter(
#     Task.owner_id == current_user.id
#     )

#     if completed is not None:
#         query = query.filter(
#             Task.completed == completed
#         )

#     if priority:
#         query = query.filter(
#             Task.priority == priority
#         )

#     tasks = query.all()

#     return tasks

