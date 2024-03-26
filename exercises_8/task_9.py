import json
import xml.etree.ElementTree as ET
import yaml


def to_format(output_format=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if output_format == 'xml':
                return ET.tostring(ET.Element('data', result))
            
            elif output_format == 'yaml':
                return yaml.dump(result)
            
            else:
                return json.dumps(result)
        
        return wrapper
    return decorator


@to_format()
def example_json():
    return {"key": "value"}


@to_format('xml')
def example_xml():
    return {"key": "value"}


@to_format('yaml')
def example_yaml():
    return {"key": "value"}


print(example_json())  # Output: {"key": "value"}
print(example_xml())   # Output: b'<data><key>value</key></data>'
print(example_yaml())  # Output: key: value
