import django
django.setup()


from hyke.api.jobs_system import scheduled_system


def test_schedule_systems():
    scheduled_system()




# Write a test for each happy path StatusEngine that matched the if criteria in scheduled_systems