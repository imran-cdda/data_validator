from errors import ValidationError, SchemaError
from fields import fields
from validations import validations

class validator:
    def __init__(self):
        self.schema = {k:v for k,v in self.__class__.__dict__.items() if not k.startswith("__")}

    def schema_data(self):
        return self.schema

    def load(self, data):
        error = {}
        result = {}
        for k in self.schema:
            type = self.schema[k]['type']
            val = data.get(k)
            if val is None:
                if self.schema[k]['missing'] is not None:
                    result[k] = self.schema[k]['missing']
                else:
                    if self.schema[k]['required']:
                        error[k] = "This field is required."
            else:
                if not isinstance(val, type):
                    error[k] = f"Not a valid {type.__name__}"
                else:
                    if not self.schema[k]['null'] and len(str(data.get(k))) == 0:
                        error[k] = "This field can't be null"
                    else:
                        if "validate" in self.schema[k] and self.schema[k]['validate']:
                            if isinstance(self.schema[k]['validate'], list):
                                for vald in self.schema[k]['validate']:
                                    try:
                                        error[k] = vald['error']
                                        break
                                    except:
                                        d = getattr(globals()['validations'](), vald['type'])(check = True, data = val, criteria = vald['criteria'], type = self.schema[k]['type'])
                                        if d:
                                            error[k] = d['error']
                                            break
                                        else:
                                            result[k] = data.get(k)
                            else:
                                try:
                                    error[k] = self.schema[k]['validate']['error']
                                except:
                                    d = getattr(globals()['validations'](), self.schema[k]['validate']['type'])(check = True, data = val, criteria = self.schema[k]['validate']['criteria'], type = self.schema[k]['type'])
                                    if d:
                                        error[k] = d['error']
                                    else:
                                        result[k] = data.get(k)
                        else:
                            result[k] = data.get(k)
        if error:
            raise ValidationError(error)
        return result

class user(validator):
    name = fields.string(required=True, null=False, validate = [validations.range(min = 6, max = 10), validations.length(min=5)])
    age = fields.integer(validate = [validations.range(min = 6, max = 10), validations.length(min=5)])

data = {
    "name": "wertg",
    "age": 6
}

try:
    vl = user().load(data)
    print(vl)
except ValidationError as e:
    print("error: ", e.message)
