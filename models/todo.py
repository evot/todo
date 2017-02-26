import time
from . import db


class Todo(db.Document):
    content = db.StringField()
    created_time = db.IntField(default=int(time.time()))
    status = db.IntField(default=0)

    @classmethod
    def new(cls, form):
        content = form.get('content', '')
        m = cls(content=content)
        m.save()
        return m

    @classmethod
    def done(cls, todo_id):
        m = cls.objects.get_or_404(id=todo_id)
        m.status = 1
        m.save()
        return m

    @classmethod
    def reset(cls, todo_id):
        m = cls.objects.get_or_404(id=todo_id)
        m.status = 0
        m.save()
        return m

    @classmethod
    def remove(cls, todo_id):
        m = cls.objects.get_or_404(id=todo_id)
        print(m.content)
        m.delete()

    @classmethod
    def clear(cls):
        ms = cls.objects.all()
        for m in ms:
            m.delete()
