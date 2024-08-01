Install, Configure and Use
==========================

Installation
------------

Execute the following command:

.. code:: console

   pip install validators

..

   It's preferable to use ``pip`` within a virtual environment.

--------------

Usage
-----

.. code:: python

   from validators import email
   print(email('someone@example.com'))

.. code:: python

   # Output
   # True

--------------

Configuration
-------------

``validators`` uses environment variables prefixed with ``PYVLD_`` for
it's configuration. You can set environment variables as:

.. code:: sh

   # bash/zsh/ksh
   export PYVLD_CONFIG=VALUE

   # fish
   set PYVLD_CONFIG VALUE

.. code:: pwsh

   # pwsh
   [Environment]::SetEnvironmentVariable("PYVLD_CONFIG", "VALUE", "Machine")

Currently, the following configuration options are available:

**``PYVLD_RAISE_ERROR``**
~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Reason**: Causes the library to raise
   ```ValidationError`` </pyvalidators/api/utils/#validators.utils.ValidationError>`__
   instead of returning it.
-  **Default**: Unset
-  **Possible values**: ``True``, ``False``

..

   Note:
   ```ValidationError`` </pyvalidators/api/utils/#validators.utils.ValidationError>`__
   can also be raised by passing ``r_ve=True`` to the caller function.

**``PYVLD_CACHE_TLD``**
~~~~~~~~~~~~~~~~~~~~~~~

-  **Reason**: Caches TLD list to speedup lookup.
-  **Default**: Unset
-  **Possible values**: ``True``, ``False``
