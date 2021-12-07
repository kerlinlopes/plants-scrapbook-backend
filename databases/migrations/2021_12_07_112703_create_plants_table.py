"""CreatePlantsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePlantsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("plants") as table:
            table.increments("id")
            table.string("name")
            table.string("description")
            table.string("image")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("plants")
