from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list()
    print(old_project_list)
    new_project = Project(name="project")
    app.project.create(new_project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(new_project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)