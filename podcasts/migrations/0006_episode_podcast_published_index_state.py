"""Record the composite episode index in Django's migration state.

Migration 0005 creates this index with CREATE INDEX CONCURRENTLY, but its
RunSQL operation does not update Django's model state. This state-only
migration records the index without attempting to create it a second time.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0005_add_composite_indexes"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.AddIndex(
                    model_name="episode",
                    index=models.Index(
                        fields=["podcast", "-published"],
                        name="episode_podcast_published_idx",
                    ),
                ),
            ],
        ),
    ]
