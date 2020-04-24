from json import JSONEncoder
import six

from .models.base_model_ import Model


class CustomJSONEncoder(JSONEncoder):
    include_nulls = False

    def default(self, o):  # pylint: disable=method-hidden
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.openapi_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return JSONEncoder.default(self, o)
