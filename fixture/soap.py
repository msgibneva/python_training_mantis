from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        wd = self.app.wd
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_soap_project_list(self, username, password):
        wd = self.app.wd
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php" + "?wsdl")
        project_list = []
        try:
            soap_list = client.service.mc_projects_get_user_accessible(username, password)
            for i in range(len(soap_list)):
                extracted = Project(id=soap_list[i]['id'], name=soap_list[i]['name'])
                project_list.append(extracted)
            return project_list
        except WebFault:
            return False