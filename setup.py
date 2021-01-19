# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['formchen']

package_data = \
{'': ['*'], 'formchen': ['tests/*']}

install_requires = \
['gridchen>=0.1.3,<0.2.0']

setup_kwargs = {
    'name': 'formchen',
    'version': '0.1.6beta1',
    'description': 'Generate HTML forms and bind hierarchical and tabular data.',
    'long_description': 'Generate HTML forms and bind hierarchical and tabular data with the help of [JSON Schema](https://json-schema.org).\n\nForm-Chen supports master-detail relationships and undo/redo transaction management.\n\nIt uses [gridchen](https://github.com/decatur/gridchen) to produce Excel-like web-components for\ntabular (aka table/grid/matrix) data. \n\nEdits on the original object are emitted as standard [JSON Patch](https://tools.ietf.org/html/rfc6902),\nwhich can be directly passed to the back end.\n\nOptionally, object properties can be specified by [JSON Pointers](https://tools.ietf.org/html/rfc6901) to be bound to given HTML-elements.\n\nFormchen is written in plain EcmaScript 2017 modules and can be directly imported as such with any modern browser.\n\n# Installation\n\nEither\n* Use a CDN such as\n    * https://unpkg.com/formchen@0.1.3/webcomponent.js?module\n    * or https://cdn.skypack.dev/formchen (a bit involved)\n    * or https://decatur.github.io/formchen/formchen\n* or git-clone a release\n* or copy the formchen module folder\n* or `pip install formchen`\n* or `npm install formchen`\n\nNote: cdn.jsdelivr.net currently does not support bare module specifiers.\n\n# Usage\n\nThis is a basic form which runs standalone or can be loaded from https://decatur.github.io/formchen/usage.html.\n![usage](usage.png)\n\n\n```html\n<!DOCTYPE html>\n<div class="form-chen">\n    <div id="/person"></div>\n    <span style="font-size: x-large" id="/person/vip"></span>\n</div>\n<script type="module">\n    import {createFormChen} from "https://decatur.github.io/formchen/formchen/webcomponent.js"\n\n    const schema = {\n        title: \'Person\',\n        pathPrefix: \'/person\',\n        type: \'object\',\n        properties: {\n            name: {\n                title: \'Full Name of Person\', type: \'string\'\n            },\n            dateOfBirth: {\n                title: \'Date of Birth\', type: \'string\', format: \'full-date\'\n            },\n            vip: {\n                type: \'boolean\'\n            }\n        }\n    };\n\n    const data = {\n        name: \'Frida Krum\',\n        dateOfBirth: \'2019-01-01T00:00Z\',\n        vip: true\n    };\n\n    createFormChen(schema, data);\n</script>\n\n```\n\n# Demos\n\nSee https://decatur.github.io/formchen\n\n# Hosting Form-Chen\n\nDeploy both [formchen](https://github.com/decatur/formchen/tree/master/formchen) and \n[gridchen](https://github.com/decatur/gridchen/tree/master/gridchen) directories from the respective git repositories. \nformchen depends on gridchen to be at the bare URL ``gridchen``, i.e. ``import "gridchen/webcomponent.js"``\nSo be sure you bundle or inplace your imports.\n\n## NPM Install\n\n⚠ Currently formchen is not registered with npmjs!\n\n## Python PyPI Install\nUsing Python you can install the [formchen package](https://pypi.org/project/formchen/).\nA Python routing example can be found in the provided dev server.\n\n## Note on module resolving\n\nThe old way of module resolution is via \n[bare import specifiers](https://html.spec.whatwg.org/multipage/webappapis.html#resolve-a-module-specifier) \nsuch as ``import "gridchen/webcomponent.js"``. Note the missing slash at the beginning. \nThis is usually handled by bundlers, which replace the bare import specifier with a relative path to the routed module location.\nAs we do not want to rely on any bundler, and because currently there is no Web browser standard for module resolution of bare import\nspecifiers, we opted for the relative URL approach.  \n\n\n# Read Only\n\nAt any level, the schema can be marked `readOnly:true|false`, the default value being `false`.\nThe `readOnly` property is inherited by sub-schemas. \n\n# DOM Api and CSS Styling\n\nThe form is generated as a flat list of paired elements. The input elements are generated with the document ID corresponding to the JSON Pointer to its value.\n\nPairs           | Semantic\n----------------|-----------\n&lt;label/&gt; &lt;input&gt;     | For all scalar fields\n&lt;label/&gt; &lt;select&gt;    | For all scalar fields having an enum type\n&lt;label/&gt; &lt;checkbox&gt;  | For all scalar boolean fields\n&lt;label&gt; &lt;grid-chen/&gt; &lt;/label&gt;| For all grid fields\n&lt;label class=error/&gt;                   | For errors\n\nIn case a field has a unit, then the label will have a nested &lt;span class=unit/&gt; element.\n\nNo direct element style is applied.\n\nBased on this flat list of paired elements, the layout can be tweaked using CSS Column Layout, CSS Grid Layout or CSS Flex Layout, or whatever. See the demos for examples.\n\n# JavaScript Api\n\nPlease see the source code of the demos or [formchen TypeScript Definitions](formchen/formchen.d.ts) for the public JavaScript Api.\n\n# Contribute\n\nForm-Chen is written in plain EcmaScript 2017 modules with JSDocs type hinting.\nThere is no overhead related to transpiling or packing.\nAs tool I recommend either vscode or one of JetBrains IDEs (WebStorm, PyCharm).\n\n## Dev Server\n\nThere is a FastAPI-based dev server in the dev_server directory.\n\n## Unit Testing\n\nAfter starting the dev server, navigate to\nhttp://localhost:8000/gridchen/testing/suiterunner.html?testpath=/formchen/tests/\n\n## Project Website\n\nFormchen can be deployed to a static web server. We use Github Pages and serve from /docs of the master branch. \nThe /docs folder is generated from project root by running\n````bash\npython build.py\n````\nThis will substitute the bare import specifier `gridchen/` with `https://decatur.github.io/gridchen/gridchen/`.\n\nSteps:\n1. `python build.py`\n2. Test web site locally by opening `./docs/index.html` (PyCharm: Open in browser) and navigating the site.\n3. `git push`\n4. Test web site on [Formchen Github Pages](https://decatur.github.io/formchen/index.html) \n\n## Python Package\n\n````shell script\nvi pyproject.toml\ngit add pyproject.toml\ngit commit -m\'bumped version\'\ngit tag x.y.z\npoetry build\n````\n\n## Python Publish\n\n````shell script\npoetry publish\n````\n\n## Publish as npm Package\n\nBump version in `fromchen/package.json` and `git tag`.\n\n````bash\ncd fromchen & npm publish\n````\n\n\n',
    'author': 'Wolfgang Kühn',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/decatur/formchen',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)