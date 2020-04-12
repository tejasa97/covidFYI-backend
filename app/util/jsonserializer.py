import json, datetime


class CustomClassEncoder(json.JSONEncoder):
    """
    Serialize custom classes into a JSON string. It is mandatory for the object
    to implement the toJson() method, which will be called from here.
    """

    def default(self, obj):
        """
        Call the toJson() method of the object to be serialized
        """
        if isinstance(obj,datetime.datetime):
            return obj.astimezone().isoformat()

        if isinstance(obj, None):
            return 'null'
        
        return obj.toJson()
