from pydantic import BaseModel


class Fisherman(BaseModel):
    # TODO: it would be nice to have this use a uuid rather than an int for id
    # this goes for all tables in the db
    # This would require updating the DDL file, which might be super annoying
    # str(uuid.uuid4())
    fisherman_id: int
    name: str
