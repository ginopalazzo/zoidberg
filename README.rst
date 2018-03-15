========
zoidberg
========


.. image:: https://img.shields.io/pypi/v/zoidberg.svg
        :target: https://pypi.python.org/pypi/dr-zoidberg

.. image:: https://img.shields.io/travis/ginopalazzo/zoidberg.svg
        :target: https://travis-ci.org/ginopalazzo/zoidberg

.. image:: https://readthedocs.org/projects/zoidberg/badge/?version=latest
        :target: https://zoidberg.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ginopalazzo/zoidberg/python-3-shield.svg
        :target: https://pyup.io/repos/github/ginopalazzo/zoidberg/
        :alt: Python 3

Are you ready to operate, Doctor? - I'd love to, but first I have to perform surgery.


.. figure:: https://upload.wikimedia.org/wikipedia/en/4/4a/Dr_John_Zoidberg.png
        :target: https://upload.wikimedia.org/wikipedia/en/4/4a/Dr_John_Zoidberg.png
        :alt: Dr. Zoidberg


* Free software: MIT license
* Documentation: https://zoidberg.readthedocs.io.

Features
--------

Zoidberg is a small lobster crawler that use Scrapy_ to get surgery doctor reviews from Internet message board.
Sometimes is hard to find real reviews of surgery doctors in Google.

For example (my case), I have Femoroacetabular Impingement in the hip and the only medical solution is surgery.
I thought Margalet was the best doctor who perform this operation but when I searched with Zoidberg, I realized that
López Carro was a much better choice.

By typing::

    python zoidberg.py -c es -d margalet -a traumatologia -i femoroacetabular -p test.csv -o csv

you get all the doctor Margalet comments for the femoroacetabular impingement in the test.csv file.

At this moment it only implement Femoroacetabular Impingement in Spain, but hopefully with some collaboration,
Zoidberg will extend his functionality

Install
--------

Just:

* pip install dr-zoidberg
* or clone this repository.

Usage
--------
To use zoidberg in a project::

    from zoidberg import zoidberg

    z = zoidberg.Zoidberg(country='es', doctor='margalet', area="traumatologia", illness="femoroacetabular", path='test.csv', output='csv')
    z.conf()
    z.run()

or clone from::

    git clone git@github.com:ginopalazzo/zoidberg.git

and use the Zoidberg CLI::

    python zoidberg.py -c es -d margalet -a traumatologia -i femoroacetabular -p test.csv -o csv


TODO
--------

* CLI: Change argparse to click.pocoo.org.
* Get list of countries available.
* Get list of areas available for a country.
* Get list of illness available for an area.
* Add keywords of illness for search.
* Search a doctor for every area or illness.

Credits
-------

* Gino Palazzo ginopalazzo@gmail.com
* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
* Zoidgber image from Wikipedia: https://en.wikipedia.org/w/index.php?curid=18173215

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Scrapy: https://scrapy.org/
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
