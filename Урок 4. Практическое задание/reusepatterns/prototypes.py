import copy


class PrototypeMixin:
    """Прототип"""
    def clone(self):
        """Clone a registered object and update inner attributes dictionary"""
        return copy.deepcopy(self)
