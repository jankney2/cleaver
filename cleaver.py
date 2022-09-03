from app.app import create_app

# any middleware here?

app = create_app('DEV')
app.app_context().push()

