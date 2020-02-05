import random
import time
from model.project import Project

class ProjectHelper():

    def __init__(self, app):
        self.app = app

    projects_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/mantisbt-1.2.20")):
            wd.get("http://localhost/mantisbt-1.2.20")

    def open_manage_proj_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/manage_proj_page.php')):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")
        time.sleep(1)

    def get_project_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_manage_proj_page()
            self.projects_cache = []
            for row in wd.find_elements_by_css_selector("tr.row-1"):
                cells = row.find_elements_by_css_selector("td")
                link = row.find_element_by_css_selector("a").get_attribute('href')
                id = link[link.find("=") + 1:]
                name = cells[0].text
                defined_project = Project(name=name, id=id)
                self.projects_cache.append(defined_project)
        return list(self.projects_cache)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        self.open_creation_form()
        self.fill_project_form(project)
        self.submit_addition()
        self.projects_cache = None
        time.sleep(2)

    def open_creation_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def submit_addition(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def choose_project_to_delete(self, project_name_to_delete):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'%s')]" % project_name_to_delete).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project(self, project_for_deletion):
        wd = self.app.wd
        self.open_manage_proj_page()
        print(project_for_deletion.id, project_for_deletion.name)
        pr_id = project_for_deletion.id
        wd.find_element_by_link_text(pr_id).click()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % pr_id).click()
        time.sleep(5)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.projects_cache = None
