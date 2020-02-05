from sys import maxsize


class Project:
    def __init__(self, id=None, name=None, status=None, view_status=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.view_status, self.description)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize