# BitPermissions

## Simple bit permissions
A simple bitwise permission system.

It represents the permissions as a set of bits.

Bit permissions is idempotent. So setting the permission to something it already is won't raise an error. You can also
set the entire set of permissions at once by using a number similar to how it would be done with POSIX file permissions.
