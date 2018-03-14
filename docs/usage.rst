=====
Usage
=====

To use zoidberg in a project::

    from zoidberg import zoidberg

    z = zoidberg.Zoidberg(country='es', doctor='margalet', area="traumatologia", illness="femoroacetabular", path='test.csv', output='csv')
    z.conf()
    z.run()

or clone from::

    git clone git@github.com:ginopalazzo/zoidberg.git

and use the Zoidberg CLI::

    python zoidberg -country es -doctor margalet -area traumatologia -illness femoroacetabular -path test.csv -output csv
