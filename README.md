# Why?

There are few reasons. Basically:

- Just to discuss and try different approaches to maintain and load access instances (Permissions) to the system.
- Just to have some fun implementing loading data directly from txt.files.
- Stress testing whole process. Checking how time-consuming that would be with larger files.
- Checking dirrerences between django's `update_or_create` method versions.


# Access files (*.access)

The files that I decided to go with are really simple structures, JSON-like with comments:

<div align="center">
    <img src=".readme/access_txt.png" width=400/>
</div>



# Error handling

You cannot use a field that is not implemented in model.

<div align="center">
    <img src=".readme/weird_field.png" width=400/>
</div>

To be fair, I didn't even think I would implement something to this point :D
That was just small quick side-quest. Although, there are nice errors with
pinpoiting exactly where the problem is in our *.access file.

<div align="center">
    <img src=".readme/weird_field_error.png"/>
</div>



