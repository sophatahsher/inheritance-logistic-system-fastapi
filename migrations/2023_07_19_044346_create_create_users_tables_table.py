from orator.migrations import Migration


class CreateCreateUsersTablesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('create_users_tables') as table:
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('create_users_tables')
