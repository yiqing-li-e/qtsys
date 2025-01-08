from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from .models import OTProcess


@frontend.register
class OTFlow(Flow):
    process_class = OTProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["start_time", "end_time", "text"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["start_time", "end_time", "text", "approved"]
        ).Permission(
            auto_create=True
        ).Next(this.end)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_ot_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_ot_request(self, activation):
        print(activation.process.approved)