# HMLR Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/hmlr-frontend-jinja.svg)](https://pypi.org/project/hmlr-frontend-jinja/)
![hmlr-frontend 1.1.0](https://img.shields.io/badge/hmlr--frontend%20version-1.1.0-005EA5?logo=gov.uk&style=flat)
[![Python package](https://github.com/LandRegistry/hmlr-frontend-jinja/actions/workflows/python-package.yml/badge.svg)](https://github.com/LandRegistry/hmlr-frontend-jinja/actions/workflows/python-package.yml)

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macros that are kept up-to-date and 100% compliant with the original [HMLR Frontend](https://github.com/LandRegistry/hmlr-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine.

## Compatibility

The following table shows the version of HMLR Frontend Jinja that you should use for your targeted version of HMLR Frontend:

| HMLR Frontend Jinja Version | Target HMLR Frontend Version |
| --------------------------- | ---------------------------- |
| [2.0.0](https://github.com/LandRegistry/hmlr-frontend-jinja/releases/tag/2.0.0) | [2.0.0](https://github.com/LandRegistry/hmlr-frontend/releases/tag/v2.0.0) |
| [1.1.0](https://github.com/LandRegistry/hmlr-frontend-jinja/releases/tag/1.1.0) | [1.4.0](https://github.com/LandRegistry/hmlr-frontend/releases/tag/v1.4.0) |
| [1.0.0](https://github.com/LandRegistry/hmlr-frontend-jinja/releases/tag/1.0.0) | [1.1.0](https://github.com/LandRegistry/hmlr-frontend/releases/tag/v1.1.0) |
| [0.2.0](https://github.com/LandRegistry/hmlr-frontend-jinja/releases/tag/0.2.0) | [1.0.0-rc1](https://github.com/LandRegistry/hmlr-frontend/releases/tag/v1.0.0-rc1) |

Any other versions of HMLR Frontend not shown above _may_ still be compatible, but have not been specifically tested and verified.

## How to use

After running `pip install hmlr-frontend-jinja`, ensure that you tell Jinja where to load the templates from using the `PackageLoader` as follows:

```python
from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

app.jinja_loader = ChoiceLoader(
    [
        PackageLoader("app"),
        PrefixLoader({"hmlr_frontend_jinja": PackageLoader("hmlr_frontend_jinja")}),
    ]
)
```

### Calling a Macro in your template

To use a component in your project templates you must import and call the component macro and pass the relevant options, for example:

```html
{%- from 'hmlr_frontend_jinja/components/header/macro.html' import hmlrHeader -%}

{{ hmlrHeader({
  'serviceName': "Service name",
  'serviceUrl': "#"
}) }}
```

The options available to each component macro can be found in the original [HMLR Design System Components](https://hmlr-design-system.herokuapp.com/components/) documentation. Since this project is a like-for-like port, the only difference between the Nunjucks examples and their Jinja equivalents is having to quote key names, e.g. `'text'` instead of `text`.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/LandRegistry/hmlr-frontend-jinja/tags).

## How to contribute

We welcome contribution from the community. If you want to contribute to this project, please review the [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

## Contributors

- [Matt Shaw](https://github.com/matthew-shaw) (Author and primary maintainer)
