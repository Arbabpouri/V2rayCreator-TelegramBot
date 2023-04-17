class InlineButtonsData:
    CUSTOM_CHARGE = "CUSTOM-CHARGE"

    @staticmethod
    def select_server(name: str) -> str:
        return "Server-{}".format(name)

    @staticmethod
    def select_plan(date, traffic) -> str:
        return "Plan-{}-{}".format(traffic, date)

    @staticmethod
    def select_config(name) -> str:
        return "Config-{}".format(name)

    @staticmethod
    def change_protocol(server_name: str, from_server: str, to_server: str) -> str:
        return "ChangeProtocol-{}-{}-{}".format(server_name, from_server, to_server)

    @staticmethod
    def change_server_from(from_server: str) -> str:
        return "ChangeServerFrom-{}".format(from_server)

    @staticmethod
    def change_server_to(to_server):
        return "ChangeServerTo-{}".format(to_server)
