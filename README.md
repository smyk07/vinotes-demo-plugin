# vinotes-demo-plugin

This is a demo Vinotes 3rd Party Plugin. Just prints out some info...

## Usage

This plugin only has one command: that is `vn vinotes-demo-plugin`

## Release

Add the below to your `plugin.json` for installing `vinotes-demo-plugin` in your vault:

```json
{
  "smyk07/vinotes-demo-plugin": {
    "utils": ["vinotes-demo-plugin", "vinotes_demo_time_provider"],
    "opts": {
      "message": "Hello Vinotes! This is a message from the plugins config."
    }
  }
}
```

_Be sure to run `vn check-plugins` once added..._
