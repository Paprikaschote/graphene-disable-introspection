from django.conf import settings

DISABLED_INTROSPECTION_TYPES = getattr(
    settings, "DISABLED_INTROSPECTION_TYPES", ["__schema", "__type", "__typename"]
)

# check type of DISABLED_INTROSPECTION_TYPES
if not isinstance(DISABLED_INTROSPECTION_TYPES, list):
    raise ValueError("DISABLED_INTROSPECTION_TYPES must be a list")

# check if every element in DISABLED_INTROSPECTION_TYPES starts with "__"
if not all([t.startswith("__") for t in DISABLED_INTROSPECTION_TYPES]):
    raise ValueError(
        "Every element in DISABLED_INTROSPECTION_TYPES must start with '__'"
    )
