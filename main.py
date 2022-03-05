from data.db_session import global_init, create_session
from data.__all_models import User, Jobs


global_init('database.db')
session = create_session()
user = User()
"""user.surname = "Boris"
user.name = "Olegov"
user.age = 10
user.position = "child"
user.speciality = "unemployed"
user.address = "module_2"
user.email = "boris_olegov@mars.org"
user.hashed_password = "mars_is_cool"
session.add(user)
session.commit()
session.close()"""

job = Jobs()
job.team_leader = 1
job.job = 'biologist'
job.work_size = 20
job.collaborators = '2'
job.is_finished = False
session.add(job)
session.commit()
session.close()
job = session.query(Jobs).first()
print(job, job.team_leader_instance)
