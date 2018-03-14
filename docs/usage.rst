=====
Usage
=====

To use zoidberg in a project::

    from zoidberg import zoidberg

    z = zoidberg.Zoidberg(country='es', doctor='margalet', area="traumatologia", illness="femoroacetabular", path='test.csv', output='csv')
    print(z)
    z.conf()
    z.run()

or clone from git clone git@github.com:your_name_here/zoidberg.git and use the Zoidberg CL:
python zoidberg -country es -doctor margalet -area traumatologia -illness femoroacetabular -path test.csv -output csv
