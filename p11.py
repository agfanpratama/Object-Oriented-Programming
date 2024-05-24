def honirific(cls):
    class HonirificCls(cls):
        def full_name(self):
            return "Mr." + super(HonirificCls, self).full_name()

    return HonirificCls


@honirific
class Name(object):
    def __init__(self, first_name, last_name, nim):
        self.first_name = first_name
        self.last_name = last_name
        self.nim = nim

    def full_name(self):
        return " ".join([self.first_name, self.last_name, self.nim])


result = Name("Agfan", "Hendarsin", "064002100043").full_name()
print("Full name: {0}".format(result))
