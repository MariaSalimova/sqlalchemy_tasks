from data.__all_models import User
from data.db_session import global_init, create_session
import sqlalchemy


database_name = input()
global_init(database_name)
session = create_session()
print(*session.query(User).filter(User.address == "module_1").all(), sep='\n')
