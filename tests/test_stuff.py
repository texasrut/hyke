import django

from hyke.api.models import StatusEngine

django.setup()


from hyke.api.jobs_system import scheduled_system


def test_schedule_systems():
    scheduled_system()

# we've refactored scheduled_system() so that it is decoupled from the items query and now we can
# individually test each item.  So we need to write a test FOR EACH happy path branch of the
# original implementation scheduled_systems.
# I've included a sample of one of how to test part of one of those branches.
def test_annual_report_uploaded_assigns_outcome():

    #arrange the annual report process
    annual_report_status_engine = StatusEngine()
    annual_report_status_engine.process = "Annual Report Uploaded"

    # act - process the sttus
    scheduled_system([annual_report_status_engine])

    # assert that the process completed
    assert annual_report_status_engine.outcome == StatusEngine.COMPLETED
    assert annual_report_status_engine.executed is not None


