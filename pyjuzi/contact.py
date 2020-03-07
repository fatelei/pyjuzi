from .transport import Transport


class ContactApi(object):

    def __init__(self, endpoint: str, token: str):
        self.transport = Transport(endpoint=endpoint, token=token)

    def list_contact(self, page_num: int, page_size: int, wxid: str = ""):
        param = {
            "current": page_num,
            "pageSize": page_size
        }
        if wxid:
            param["wxid"] = wxid
        return self.transport.get("/contact/list", param)
