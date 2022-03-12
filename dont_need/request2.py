from data.__all_models import User
from data.db_session import global_init, create_session


database_name = input()
global_init(database_name)
session = create_session()
res = session.query(User).filter(User.speciality == "module_1",
                                 User.speciality.notlike('%engineer%'),
                                 User.position.notlike('%engineer%')).all()

print(*map(lambda user: user.id, res), sep='\n')
session.close()
