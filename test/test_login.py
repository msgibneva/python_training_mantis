

def test_login(app):
    app.session.login("administrator", "root")
    app.session.is_logged_in_as("administrator")