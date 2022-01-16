from copy import deepcopy


class PrototypeMixin:
    # прототип

    def clone(self):
        return deepcopy(self)


class Original(PrototypeMixin):
    pass


class OriginalClass(PrototypeMixin):
    pass


original = Original()
original.clone()

original_2 = OriginalClass()
original_2.clone()


class ModernPrototypeMixin(PrototypeMixin):

    def clone(self):
        print('что то еще')
        return deepcopy(self)


class Original(ModernPrototypeMixin):
    pass


original = Original()
original.clone()
