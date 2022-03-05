from data.db_session import global_init, create_session
from data.__all_models import User, Jobs


global_init('database.db')
session = create_session()
"""user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)
session.commit()"""
"""job = Jobs()
job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False
session.add(job)
session.commit()"""
job = session.query(Jobs).first()
print(job, job.team_leader_instance)
