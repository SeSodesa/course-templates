Hello programming
-----------------

This chapter includes three exercises on one page. Questionnaires and
submission forms can exist anywhere and as many on one page as required.
The automatic assessment of a submission is defined in the referenced
YAML file.

This is the configuration file ``docker-compose.yml``:  

.. include:: ../docker-compose.yml
  :code: yaml

Note: acos is an optional component used for interactive exercises.

.. submit:: mathcheck 10
  :config: exercises/mathcheck-example/config.yaml

.. submit:: geogebra2 10
  :config: exercises/geogebra-example/config.yaml


.. submit:: python 10
  :config: exercises/hello_python/config.yaml

.. submit:: scala 10
  :config: exercises/hello_scala/config.yaml

.. submit:: javascript 10
  :config: exercises/hello_javascript/config.yaml



Be careful with the RST and YAML syntaxes. They are too easy to break
with blank space and indentations.

