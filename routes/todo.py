from models.todo import Todo
from routes import *

main = Blueprint('todo', __name__)


@main.route('/')
def index():
    todos = Todo.objects.order_by('status', '-created_time')
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    Todo.new(form)
    return redirect(url_for('.index'))


@main.route('/done/<id>', methods=['POST'])
def done(id):
    Todo.done(id)
    return redirect(url_for('.index'))


@main.route('/reset/<id>', methods=['POST'])
def reset(id):
    Todo.reset(id)
    return redirect(url_for('.index'))


@main.route('/delete/<id>', methods=['POST'])
def delete(id):
    Todo.remove(id)
    return redirect(url_for('.index'))


@main.route('/clear', methods=['POST'])
def clear():
    Todo.clear()
    return redirect(url_for('.index'))


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
