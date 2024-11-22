from uuid import uuid4
from domain.user.user_entity import User
from domain.task.task_entity import Task

class TestUserWithTasks:
    
    #teste para adiconar tarefas ao usuário
    def test_user_with_tasks(self):
        
        user = User(id=uuid4(), name="Bta")
        task = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar mais sobre TDD e testes integração",
            description="Estudar mais sobre TDD e testes integração para melhorar a qualidade do código",
            completed=False
        )
        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar mais sobre TDD e testes unitários",
            description="Estudar mais sobre TDD e testes unitários para melhorar a qualidade do código",
            completed=False
        )
        user.collect_taks([task, task2])