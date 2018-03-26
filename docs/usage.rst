=====
Usage
=====

To use Zoidberg from CLI just type zoidberg and follow the instructions.

To use zoidberg in a project::

    from zoidberg.zoidberg_main import Zoidberg

    z = Zoidberg(country='es', doctor='margalet', area="traumatologia", illness="femoroacetabular", path='test.csv', output='csv')
    z.conf()
    z.run()
