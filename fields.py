class fields:
    def string(missing = None, required:bool = False, default = None, null:bool = False, validate = False):
        return {
            "missing": missing,
            "required": required,
            "default": default,
            "type": str,
            "null": null,
            "validate": validate
        }
    def integer(missing = None, required:bool = False, default = None, null:bool = False, validate = False):
        return {
            "missing": missing,
            "required": required,
            "default": default,
            "type": int,
            "null": null,
            "validate": validate
        }