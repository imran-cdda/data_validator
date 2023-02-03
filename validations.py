class validations:
    def length(min = False, max = False, **kwargs):
        if "check" in kwargs:
            if 'data' in kwargs:
                error = {}
                try:
                    len_val = len(kwargs['data'])
                except:
                    return {
                        "error": f"{kwargs['type'].__name__} type field have no length."
                    }
                if 'min' in kwargs['criteria'] and 'max' in kwargs['criteria'] and len_val < kwargs['criteria']['min'] and len_val > kwargs['criteria']['max']:
                    error = {
                        "error": f"Length must be between {kwargs['criteria']['min']} and {kwargs['criteria']['max']}."
                    }
                elif "max" in kwargs['criteria'] and len_val > kwargs['criteria']['max']:
                    error = {
                        "error": f"Length must be less than {kwargs['criteria']['max']+1}."
                    }
                elif "min" in kwargs['criteria'] and len_val < kwargs['criteria']['min']:
                    error = {
                        "error": f"Length must be greater than {kwargs['criteria']['min']-1}"
                    }
            else:
                error = {
                    "error": "Value is required."
                }
            if error:
                return error
            else:
                return {}

        else:
            if not min and not max:
                return  {
            "error": "min or max is required."
            }
            schema = {"type": "length", "criteria": {}}
            if min:
                schema['criteria']['min'] = min
            if max:
                schema['criteria']['max'] = max
            return  schema

    def range(min = False, max = False, **kwargs):
        if "check" in kwargs:
            if 'data' in kwargs:
                error = {}
                if not isinstance(kwargs['data'], int):
                    return {
                        "error": f"{kwargs['type'].__name__} have not range validation."
                    }
                if 'min' in kwargs['criteria'] and 'max' in kwargs['criteria'] and  kwargs['data'] < kwargs['criteria']['min'] and kwargs['data'] > kwargs['criteria']['max']:
                    error = {
                        "error": f"Value must be between {kwargs['criteria']['min']} and {kwargs['criteria']['max']}."
                    }
                elif "max" in kwargs['criteria'] and kwargs['data'] > kwargs['criteria']['max']:
                    error = {
                        "error": f"Value must be less than {kwargs['criteria']['max']+1}."
                    }
                elif "min" in kwargs['criteria'] and kwargs['data'] < kwargs['criteria']['min']:
                    error = {
                        "error": f"Value must be greater than {kwargs['criteria']['min']-1}"
                    }
            else:
                error = {
                    "error": "Value is required."
                }
            if error:
                return error
            else:
                return {}

        else:
            if not min and not max:
                return  {
            "error": "min or max is required."
            }
            schema = {"type": "range", "criteria": {}}
            if min:
                schema['criteria']['min'] = min
            if max:
                schema['criteria']['max'] = max
            return  schema