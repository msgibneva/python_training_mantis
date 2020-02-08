import random
from model.project import Project
import numpy as np


def test_delete_project(app):
    app.session.login("administrator", "root")
    old_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    if len(old_soap_project_list) == 0:
        app.project.create(Project(name="testproject1"))
    old_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    project_for_deletion = random.choice(old_soap_project_list)
    app.project.delete_project(project_for_deletion)
    new_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    assert len(old_soap_project_list) - 1 == len(new_soap_project_list)
    old_soap_project_list.remove(project_for_deletion)
    assert sorted(old_soap_project_list, key=Project.id_or_max) == sorted(new_soap_project_list, key=Project.id_or_max)
    #np.array_equal(old_soap_project_list, new_soap_project_list)


# def test_delete_project(app):
#     app.session.login("administrator", "root")
#     if len(app.project.get_project_list()) == 0:
#         app.project.create(Project(name="testproject1"))
#     old_project_list = app.project.get_project_list()
#     project_for_deletion = random.choice(old_project_list)
#     app.project.delete_project(project_for_deletion)
#     new_project_list = app.project.get_project_list()
#     assert len(old_project_list) - 1 == len(new_project_list)
#     old_project_list.remove(project_for_deletion)
#     assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
