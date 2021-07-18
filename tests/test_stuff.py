import django
django.setup()


from hyke.api.jobs_system import scheduled_system


def test_schedule_systems():
    scheduled_system()
