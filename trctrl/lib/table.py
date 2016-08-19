class Table(object):

    def __init__(self, *keys):
        self.rows = []
        self.keys = keys
        for k in keys:
            setattr(self, k, len(k) + 2)

    def append_row(self, **values):
        self.rows.append(values)

        for k, v in values.items():
            setattr(self, k, max(getattr(self, k), len(str(v)) + 2))

    def append_rows(self, rows):
        for r in rows:
            self.append_row(**r)

    def __str__(self):
        ret = [
            "".join(["{0:<{width}}".format(k, width=getattr(self, k))
            for k in self.keys])
        ]
        for r in self.rows:
            ret.append("".join([
                "{0:<{width}}".format(r[k], width=getattr(self, k))
                for k in self.keys
            ]))

        return "\n".join(ret)


if __name__ == '__main__':
    t = Table("id", "name", "value")
    t.append_row(id=1, name="test", value=42)

    print(t)
