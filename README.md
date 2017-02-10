# BitPermissions
[![Build Status](https://travis-ci.org/Brian-Williams/bitpermissions.svg?branch=master)](https://travis-ci.org/Brian-Williams/bitpermissions)
A simple bitwise permission system.

## Example use
```
>>> from bitpermissions import Permissions
>>> my_perms = Permissions(['execute', 'write', 'read'])
>>> my_perms
000b
>>> my_perms.read = True
>>> my_perms
100b
>>> int(my_perms.permissions)
4
```

## A bit of info
We represents the permissions as a set of bits.

Bit permissions is idempotent. So setting the permission to something it already is won't raise an error. You can also
set the entire set of permissions at once by using a number similar to how it would be done with POSIX file permissions.

