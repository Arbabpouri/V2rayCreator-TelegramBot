class InlineButtonsData:
    CUSTOM_SHARJ = "CUSTOM-SHARJ"
    select_server = lambda name: "Server-{}".format(name)
    select_plan = lambda date, traffic: "Plan-{}-{}".format(traffic, date)
    select_config = lambda name: "Config-{}".format(name)
    change_protocol = lambda ServerName, From, To: "ChangeProtocol-{}-{}-{}".format(ServerName, From, To)
    change_server_from = lambda From: "ChangeServerFrom-{}".format(From)
    change_server_to = lambda To: "ChangeServerTo-{}".format(To)