from copy import deepcopy


class Original:
    pass


original = Original()
prototype = deepcopy(original)


prototype.name = 2
