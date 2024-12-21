from flask_jwt_extended import get_jwt_identity
from flask_smorest import abort
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from flaskr.db import db
from flaskr.models.task_model import TaskModel


class TaskController:
    @staticmethod
    def get_all():
        try:
            return (
                db.session.query(
                    TaskModel.id,
                    TaskModel.title,
                    TaskModel.created_at,
                )
                .all()
            )
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching tasks")

    @staticmethod
    def create(data):
        try:
            print(data)

            new_task = TaskModel(**data)

            db.session.add(new_task)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while creating task")

    @staticmethod
    def update(data, task_id):
        try:
            task = db.session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            ).scalar_one()

            task.title = data["title"]

            db.session.add(task)
            db.session.commit()
        except NoResultFound:
            abort(404, message="Task not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while updating task")

    @staticmethod
    def delete(task_id):
        try:
            task = db.session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            ).scalar_one()

            db.session.delete(task)
            db.session.commit()
        except NoResultFound:
            abort(404, message="Task not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while deleting task")
