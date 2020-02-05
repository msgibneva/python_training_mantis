import random
from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    #old_project_list = app.project.get_project_list()
    #if len(app.project.get_project_list()) == 0:
    #    app.project.create(Project(name="testproject1"))
    old_project_list = app.project.get_project_list()
    project_for_deletion = random.choice(old_project_list)
    print(project_for_deletion)
    app.project.delete_project(project_for_deletion)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)

