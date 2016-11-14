from .utils import AtlanticBase

class AtlanticPlan(AtlanticBase):
    def __init__(self, access_key, private_key):
        AtlanticBase.__init__(self, access_key, private_key)

    def describe(self, plan_name=None, platform=None):
        """
        List available cloud server plans, optionally narrow the list
        down by platform (windows/linux), or describe just one specific
        plan (e.g. L which represents the large plan)

        Link: https://www.atlantic.net/docs/api/?shell#describe-plans
        """
        params = {
            "Action": "describe-plan"
        }
        if plan_name:
            params.update({"plan_name": plan_name})
        if platform:
            params.update({"platform": platform})
        return self.request(params)
