from orator.orm import has_many

from ..db_connection import Model


class Post(Model):
    @has_many
    def comments(self):
        from .comment import Comment

        return Comment