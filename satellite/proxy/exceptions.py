class ProxyError(Exception):
    pass


class UnexistentFlowError(ProxyError):
    def __init__(self, flow_id: str):
        super().__init__(f'Unkillable flow: {flow_id}')


class UnkillableFlowError(ProxyError):
    def __init__(self, flow_id: str):
        super().__init__(f'Unkillable flow: {flow_id}')


class FlowUpdateError(ProxyError):
    pass
