# -*- coding: utf-8 -*-

"""Console script for zoidberg."""
import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.append('..')
sys.path.append(HERE)

import click
import zoidberg_main

click.echo("Are you ready to operate, Doctor? - I'd love to, but first I have to perform surgery."
               "zoidberg.cli.main")
click.echo("See Zoidberg documentation at https://zoidberg.readthedocs.io/en/latest/readme.html")


@click.command()
def main():
    """Console script for zoidberg."""
    # z = Zoidberg()
    # check country
    # help = "ISO 3166-1 alfa-2 country code. i.e. 'es' for 'Spain'.")help="ISO 3166-1 alfa-2 country code. i.e. 'es' for 'Spain'.")
    country = cli_country()
    area = cli_area(country)
    illness = cli_illness(country, area)
    doctor = click.prompt('Your doctor to search', type=str)
    output = cli_output()
    path = click.prompt('Output file path', type=str, default='zoidberg_output.' + output)
    log = click.prompt('Level of logging', type=str, default='warning')
    import zoidberg
    zoidberg_runner = zoidberg_main.Zoidberg(country=country, doctor=doctor, area=area, illness=illness, path=path, output=output)
    zoidberg_runner.conf()
    zoidberg_runner.run()
    return 0


def cli_country():
    country = click.prompt('Your Country', type=str, default='es')
    if country.lower() == 'es':
        return country
    else:
        print("Only Spain available yet: choose 'es' or press 'enter'.")
        return cli_country()


def cli_area(country):
    areas = zoidberg_main.get_areas(country)
    text_area = 'Your medical area. Choices: ' + str(areas)
    area = click.prompt(text_area, type=str)
    if area in areas:
        return area
    else:
        print('Please, type a valid area:')
        print(str(areas))
        return cli_area(country)


def cli_illness(country, area):
    illnesses = zoidberg_main.get_illness(country, area)
    text_illness = 'Your medical illness for ' + area + '. Choices: ' + str(illnesses)
    illness = click.prompt(text_illness, type=str)
    if illness in illnesses:
        return illness
    else:
        print('Please, type a valid illness for ' + area + ':')
        print(str(illnesses))
        return cli_illness(country, area)


def cli_output():
    output = click.prompt('Output type, csv/json', type=str, default='csv')
    if output == 'csv' or output == 'json':
        return output
    else:
        print('Please, choose between csv or json output file type.')
        return cli_output()


if __name__ == "__main__":
    main()
    #sys.exit(main())  # pragma: no cover
