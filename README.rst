algorithm-logger
================

.. image:: https://travis-ci.org/mbodenhamer/algorithm-logger.svg?branch=master
    :target: https://travis-ci.org/mbodenhamer/algorithm-logger
    
.. image:: https://img.shields.io/coveralls/mbodenhamer/algorithm-logger.svg
    :target: https://coveralls.io/r/mbodenhamer/algorithm-logger

.. image:: https://readthedocs.org/projects/algorithm-logger/badge/?version=latest
    :target: http://algorithm-logger.readthedocs.org/en/latest/?badge=latest

A Python library for logging and debugging algorithm behavior.

Note that this project is in the very initial stages of development.  However, the idea behind it is to develop a set of tools for recording the execution state of an algorithm over the course of its execution on a particular problem instance.  The goal is to help the user to:

1. More easily debug a misbehaving algorithm,
2. Gain deeper insights into algorithm behavior, and
3. Easily produce visualizations of algorithm behavior for presentation purposes.

Moreover, the goal is to accomplish the preceding by providing tools that can be enabled/disabled in a single location (such as logger initialization) without having to make any changes to the code of the algorithm itself.
