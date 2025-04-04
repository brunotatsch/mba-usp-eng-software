from uuid import UUID
 

class User:

    id: UUID
    name: str
 
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name 
        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("id must be an UUID")

        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("name is required")
        
    def collect_taks(self, tasks):
        self.tasks = tasks
        return self.tasks
 