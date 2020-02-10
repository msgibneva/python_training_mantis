from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    new_project = Project(name="ddcnc")
    app.project.create(new_project)
    new_soap_project_list = app.soap.get_soap_project_list("administrator", "root")
    assert len(old_soap_project_list) + 1 == len(new_soap_project_list)
    sorted_new = sorted(new_soap_project_list, key=Project.id_or_max)
    old_soap_project_list.append(new_project)
    sorted_old = sorted(old_soap_project_list, key=Project.id_or_max)
    assert app.project.get_difference(sorted_old, sorted_new)