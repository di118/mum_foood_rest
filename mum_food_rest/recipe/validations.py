import six

from filters.schema import base_query_params_schema
from filters.validations import (
    CSVofIntegers,
    IntegerLike,
    DatetimeWithTZ
)

# make a validation schema for players filter query params
recipe_query_schema = base_query_params_schema.extend(
    {
        # "owner": six.text_type,
        # "title": six.text_type,  # Depends on python version
        # "description": six.text_type,  # Depends on python version
        # "created": DatetimeWithTZ(),
    }
)