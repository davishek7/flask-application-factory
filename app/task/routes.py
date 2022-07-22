from . import task


@task.route('/', methods=(['GET']))
def get_tasks():
    return {'tasks':'All Tasks'}