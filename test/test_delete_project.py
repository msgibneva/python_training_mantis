import random
from model.project import Project


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
    sorted_new = sorted(new_soap_project_list, key=Project.id_or_max)
    old_soap_project_list.remove(project_for_deletion)
    sorted_old = sorted(old_soap_project_list, key=Project.id_or_max)
    assert app.project.get_difference(sorted_old, sorted_new)