# lib/query/template.py

import string

field_typename_only = string.Template("""{
  "data": {
    "$typeField": {
      "__typename": "$typeName"
    }
  }
}""")
