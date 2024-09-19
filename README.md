# Graphene Middleware to Disable Introspection
[![PyPI version](https://badge.fury.io/py/graphene-disable-introspection.svg)](https://badge.fury.io/py/graphene-disable-introspection)
![Static Badge](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)


This middleware for Python's Graphene library disables introspection queries, enhancing the security of your GraphQL API by preventing clients from discovering the schema.

## Installation

To install the middleware, you can use pip:

```bash
pip install graphene-disable-introspection
```

## Configuration
### DISABLED_INTROSPECTION_TYPES
(default : `["__schema", "__type", "__typename"]`)

The middleware will disable introspection queries for the types listed in the `DISABLED_INTROSPECTION_TYPES` list. You can customize this list by overriding this variable in your settings. The values in the list have to start with `__` and are case-sensitive.

e.g.
```python
DISABLED_INTROSPECTION_TYPES = ["__schema", "__directive"]
```


## Usage
To use the middleware in your Graphene project, you need to add it to your GraphQL schema.

### Django Usage
Add the middleware to your Django settings. I recommend to add it to the top of the middleware list.
```python
GRAPHENE = {
    ...
    "MIDDLEWARE": [
        "graphene_disable_introspection.DisableIntrospectionMiddleware",
        ...
    ],
}
```

Alternatively, you can deactivate Graphene introspection for the production system only.
```python
if os.environ.get("APP_SETTINGS") == "production":
    GRAPHENE["MIDDLEWARE"].insert(0, "graphene_disable_introspection.DisableIntrospectionMiddleware")
```

### Python Usage
Import the middleware and add it to your schema.
```python
from graphene_disable_introspection import DisableIntrospectionMiddleware

GraphqlView.as_view(middleware=[DisableIntrospectionMiddleware()])
```


## License
This project is licensed under the GPL-3.0 License.

