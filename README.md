# jonsible.ulist

[![Build Status](https://travis-ci.com/jonsible/ulist.svg?branch=master)](https://travis-ci.org/jonsible/ulist)
[![Galaxy](https://img.shields.io/badge/galaxy-jonsible.ulist-blue.svg)](https://galaxy.ansible.com/jonsible/ulist/)

This role has 2 task files

- `set_ulist.yml`
- `process_ulist.yml`

The first one allows you to extract system users with an UID between `UID_MIN` and `UID_MAX`  
The second one allows you to strip and filter keys of ulist by using regex keys
## Requirements

None.

## Role Variables

### Default usage

```yaml
# This will set the fact `ulist` containing a list with
# all the users with a UID between UID_MIN and UID_MAX
- include_role:
    name: jonsible.ulist
    tasks_from: set_ulist.yml

# { 
#   <user>: { 
#      "uid": item.value[1],
#      "gid": item.value[2],
#      "home": item.value[4],
#      "shell": item.value[5] 
#   }
# }

# This will filter THEN strip using the specified strip and filter lists
- include_role:
    name: jonsible.ulist
      tasks_from: process_ulist.yml
    vars:
      filter: ['svc_.*2']
      strip: ['user1', 'user2']
```
If you want to adapt this to your needs look at the [Advanced usage](#advanced-usage) section.

### Advanced usage

For more advanced usage the following variables are available:
```yaml
# These variables are only used by filter_users.yml
filter: [] # Select users matching this filter list (regex)
strip: [] # Strip users matching this strip list (regex)
```

You can also use the custom filter plugin in your other roles by putting this role as a dependency
```yaml
- set_fact:
    # Keys matching at least one of the filter regex will be selected
    ulist: "{{ ulist | dict_filter_keys(filter) }}"
    # Keys matching at least one of the strip regex will be stripped
    ulist: "{{ ulist | dict_strip_keys(strip) }}"
```

## Dependencies

None

## Example Playbook

Use jonsible.ulist with the default settings
```yaml
- hosts: all
  roles:
     - role: jonsible.ulist
```

## License

GPL-3.0-or-later

## Author Information

This role was created in 2020 by [Jonathan Scherrer].
