from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    new_project = Project(name="a")
    app.project.create(new_project)
    new_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    assert len(old_soap_project_list) + 1 == len(new_soap_project_list)
    old_soap_project_list.append(new_project)
    assert sorted(old_soap_project_list, key=Project.id_or_max) == sorted(new_soap_project_list, key=Project.id_or_max)


# def test_add_project_fv(app):
#     app.session.login("administrator", "root")
#     old_project_list = app.project.get_project_list()
#     new_project = Project(name="pre")
#     app.project.create(new_project)
#     new_project_list = app.project.get_project_list()
#     old_project_list.append(new_project)
#     assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
#     assert len(old_project_list) == len(new_project_list)