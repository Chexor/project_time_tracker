# main.py

from models.project import Project
#from models.worksession import Worksession

project1 = Project("Test Project 1", [])
project2 = Project("Test Project 2", [])
project3 = Project("Test Project 3", [])


print(project1.__str__())
print(project2.__str__())

