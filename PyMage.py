
import inspect


class EnchantedClasses:

    def __init__(self):
        self.left = None
        self.right = None

    def __rlshift__(self, other):
        self.left = other
        return self

    def __rshift__(self, other):
        self.right = other
        return self.__enchant()

    def __enchant(self):
        left_fields = [field[0] for field in inspect.getmembers(self.left)]
        right_fields = inspect.getmembers(self.right)

        for field in right_fields:
            if field[0] not in left_fields:
                self.left.__setattr__(field[0], field[1])

        return self.left


class SummonedClasses:

    def __init__(self):
        self.right = None
        self._globals_dict = None

    def __rshift__(self, other):
        if isinstance(other, str):
            print(inspect.getmembers(self.__summon()))
            self._globals_dict[other] = self.__summon()
            self._globals_dict["all_summons"]._add_summon(other)
        else:
            self.right = other
            return self

    def __unsummon(self):
        del self

    def _reference(self, globals_dict: dict):
        self._globals_dict = globals_dict
        return self

    def __summon(self):
        self.right.__setattr__("_unsummon()", self.__unsummon)
        return self.right


class UnsummonedClasses:

    def __init__(self):
        self.right = None
        self._globals_dict = None

    def __rshift__(self, other):
        if isinstance(other, GlobalSummonStorage):
            other._unsummon()
        elif isinstance(other, str):
            del self._globals_dict[other]
        else:
            del other

    def _reference(self, globals_dict: dict):
        self._globals_dict = globals_dict
        return self


class GlobalSummonStorage:

    def __init__(self):
        self.summons_array = []
        self._globals_dict = None

    def _add_summon(self, summon):
        self.summons_array.append(summon)

    def _unsummon(self):
        for summon in self.summons_array:
            if summon in self._globals_dict:
                del self._globals_dict[summon]
                self.summons_array.remove(summon)

    def _reference(self, globals_dict: dict):
        self._globals_dict = globals_dict
        return self


class PyMage:

    @staticmethod
    def become_mage(globals_dict: dict):
        globals_dict["enchanted_with"] = EnchantedClasses()
        globals_dict["summon"] = SummonedClasses()._reference(globals_dict)
        globals_dict["unsummon"] = UnsummonedClasses()._reference(globals_dict)
        globals_dict["all_summons"] = GlobalSummonStorage()._reference(globals_dict)