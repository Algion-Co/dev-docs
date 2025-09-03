## Handling Python Application Configurations

Often, you will need to define a config file for an application you are
developing.

For Python, we recommend using YAML files as config files files and parsing them
into class objects using Pydantic.

This has several advantages including the following:

- Handles default values better
- Can automatically extract values from environment variables, also allowing you
  to override them in config file
- Gives better errors messages
- Automatically converts certain values to the correct type e.g. if you give an
  `int` value to a parameter that is supposed to be a `str`
- Checks types and reports errors if you have incompatible types
- Allows you to access the items in a more natural dot syntax fashion
- The config or parts of it are serializable if you want to pass it over an API
  or create a dict so that you can pass keyword arguments into another function.

If you intend to extract values from environment variables, be sure to
understand and use
[BaseSettings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/).

The following is an example of config file handling with YAML (although it can
be easily modified to support JSON etc.) and Pydantic:

First install dependencies:

```python
pip install pydantic pydantic_settings PyYAML
```

Then:

```yaml
# config.yaml

db:
  url: abc.com
```

```python
# config.py

# Standard Library
from typing import Optional

# Third-Party Libraries
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DBConfig(BaseModel):
    url: str


class AppConfig(BaseSettings):
    secret_key: str = Field(alias="MY_SECRET_KEY")
    an_environment_variable_item: str = Field(alias="MY_ENVIRONMENT_VAR")
    an_item_with_a_default_value: Optional[int] = 123
    db: DBConfig
```

```python
# main.py

# Third-Party Libraries
import yaml

# Local Library
from config import AppConfig

def main():
    with open("config.yaml", "r") as f:
        config = AppConfig(**yaml.safe_load(f))

    print(config.secret_key)
    print(config.an_environment_variable_item)
    print(config.an_item_with_a_default_value)
    print(config.db.url)
    print(dict(config.db))

if __name__ == "__main__":
    main()
```

<!--
TODO:
- Tags: config file
-->
