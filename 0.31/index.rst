validators - Python Data Validation for Humans™
===============================================

|PyCQA| |SAST| |Docs| |Version| |Downloads|

.. raw:: html

   <!-- [![Package][package-badge]][package-link] -->

Python has all kinds of data validation tools, but every one of them
seems to require defining a schema or form. I wanted to create a simple
validation library where validating a simple value does not require
defining a form or a schema.

.. code:: python

   >>> import validators
   >>> 
   >>> validators.email('someone@example.com')
   True

Resources
---------

.. raw:: html

   <!-- Backup documentation URL :  https://yozachar.github.io/pyvalidators/ -->

.. raw:: html

   <!-- Original documentation URL :  https://python-validators.github.io/validators/ -->

-  `Documentation <https://yozachar.github.io/pyvalidators>`__
-  `Bugtracker <https://github.com/python-validators/validators/issues>`__
-  `Security <https://github.com/python-validators/validators/blob/master/SECURITY.md>`__
-  `Code <https://github.com/python-validators/validators/>`__

.. raw:: html

   <!-- Original docs URL will be restored, once properly versioned docs are ready. -->

--------------

   **Python 3.8** `reaches EOL in <https://endoflife.date/python>`__
   **October 2024.**

.. raw:: html

   <!-- Links -->

.. raw:: html

   <!-- [package-badge]: https://github.com/python-validators/validators/actions/workflows/package.yaml/badge.svg
   [package-link]: https://github.com/python-validators/validators/actions/workflows/package.yaml -->

.. |PyCQA| image:: https://github.com/python-validators/validators/actions/workflows/pycqa.yaml/badge.svg
   :target: https://github.com/python-validators/validators/actions/workflows/pycqa.yaml
.. |SAST| image:: https://github.com/python-validators/validators/actions/workflows/sast.yaml/badge.svg
   :target: https://github.com/python-validators/validators/actions/workflows/sast.yaml
.. |Docs| image:: https://github.com/yozachar/pyvalidators/actions/workflows/pages/pages-build-deployment/badge.svg
   :target: https://github.com/yozachar/pyvalidators/actions/workflows/pages/pages-build-deployment
.. |Version| image:: https://img.shields.io/pypi/v/validators?logo=pypi&logoColor=white&label=version&color=blue
   :target: https://pypi.python.org/pypi/validators/
.. |Downloads| image:: https://img.shields.io/pypi/dm/validators?logo=pypi&logoColor=white&color=blue
   :target: https://pypi.python.org/pypi/validators/


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Quick Start:
   :glob:

   install_and_use

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: API Reference:
   :glob:

   api/*
