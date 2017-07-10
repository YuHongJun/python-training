class Dict(dict):
    def __int__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


with open('mydict2.py', 'r') as f:
    print(f.read())

# with open('test1.jpg', 'rb') as f:
#     print(f.read())
#
# with open('mydict2.py', 'w') as f:
#     f.write('hhheeelllooo')
