import json
from pydantic import BaseModel


class Configure:
    def __init__(
        self,
        room_name="",
        ip_address="",
        net_mask="",
        gate_way="",
        server_ip="",
        common_odl="",
        sip=0,
    ):
        self.room_name: str = room_name
        self.ip_address: str = ip_address
        self.net_mask: str = net_mask
        self.gate_way: str = gate_way
        self.server_ip: str = server_ip
        self.common_odl: str = common_odl
        self.sip: int = sip

    def to_dict(self):
        return vars(self)

    def to_json(self):
        result = vars(self)
        json_string = json.dumps(result, indent=4)
        return json_string

    def from_json(self, path):
        with open(path, "r") as file:
            data = json.load(file)
        return Configure(**data)


class ConfigureRequest(BaseModel):
    room_name: str
    ip_address: str
    net_mask: str
    gate_way: str
    server_ip: str
    common_odl: str
    sip: int
