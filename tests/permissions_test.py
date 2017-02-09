from bitpermissions import Permissions, PermissionException
import inspect


def get_props(object_):
    """
    :return: List of properties to test
    """
    # get properties
    prop_list = inspect.getmembers(object_, predicate=inspect.isdatadescriptor)
    # remove weakref and permissions
    remove_list = ['__weakref__', 'permissions']
    property_list = []
    for i, property in enumerate(prop_list):
        # compare property name not the object itself
        if property[0] in remove_list:
            pass
        else:
            property_list.append(property[0])
    return property_list


samurai = ['samurai', 'jack', 'back', 'to', 'the', 'past']


def test_negative_one_input():
        all_perms = Permissions(samurai, perm_rights=-1)
        assert all_perms.permissions == 2**all_perms._num_of_rights - 1


def test_remove_all():
    all_perms = Permissions(samurai, perm_rights=-1)
    for right_name in get_props(all_perms):
        right = getattr(all_perms, right_name)
        assert right
        right = False
        assert not right


def test_add_all():
    no_perms = Permissions(samurai, perm_rights=0)
    for right_name in get_props(no_perms):
        right = getattr(no_perms, right_name)
        assert not right
        right = True
        assert right


class TestMultipleInstances():

    def test_has_functions(self):
        self.a = Permissions(['a'], perm_rights=-1)
        self.b = Permissions(['b'], perm_rights=-1)

        try:
            self.a.has_a()
        except AttributeError:
            raise RuntimeError("Instance 'a' doesn't have method 'has_a'.")

        try:
            self.a.has_b()
        except AttributeError:
            print("Instance 'a' doesn't have method 'has_b'")
        else:
            raise RuntimeError("Instance 'a' has method 'has_b'")

    def test_properties(self):
        try:
            print(self.a.b)
        except AttributeError:
            print("'a' instance wasn't affected by 'b' instance")
        else:
            raise RuntimeError("'a' instance had 'b' instance's attribute!")


class TestPerms():

    def test_on_and_off_and_on_and_off_again(self):
        self.perms = Permissions(samurai, perm_rights=0)
        self.has_perm = self.perms.__getattribute__('has_' + samurai[0])

        self._on()
        self._off()
        self._on()
        self._off()
        self._on()
        self._on()
        self._off()
        self._off()

    def _on(self):
        setattr(self.perms, samurai[0], True)
        assert getattr(self.perms, samurai[0])
        self.has_perm()

    def _off(self):
        setattr(self.perms, samurai[0], False)
        assert not getattr(self.perms, samurai[0])
        try:
            self.has_perm()
        except PermissionException:
            print('Correct exception raised')
        else:
            raise RuntimeError("There was no PermissionException when there should have been!")
