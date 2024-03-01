import tarantool


class TarantoolSql:
    """example of message dialog schema beetween 2 users"""

    def __init__(self, url: str = "tarantool", port: int = 3301):
        self.conn = tarantool.connect(url, port)

    def insert_msg(self, u_id_1, u_id_2, msg):
        return self.conn.call("insert_msg", (u_id_1, u_id_2, msg))

    def get_from(self, u_id):
        d = self.conn.call("get_msg_from", (u_id))
        if d.data[0]:
            return d.data[0].get("rows")
        return []

    def get_to(self, u_id):
        d = self.conn.call("get_msg_to", (u_id))
        if d.data[0]:
            return d.data[0].get("rows")
        return []

    def select(self, id):
        d = self.conn.call("select", (id))
        if d.data[0]:
            return d.data[0].get("rows")[0]
        return []

    def select_all(self):
        d = self.conn.call("select_all")
        if d.data[0]:
            return d.data[0].get("rows")
        return []

    def del_msg_id(self, id):
        d = self.conn.call("del_msg_id", (id))
        return d
