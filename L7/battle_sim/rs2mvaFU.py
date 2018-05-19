#!/usr/bin/env python3

import argparse
import json
import random
import sys


def generate_soldiers(prefix, soldiers_mn, soldiers_mx):
    assert 0 < soldiers_mn <= soldiers_mx
    for i in range(random.randint(soldiers_mn, soldiers_mx)):
        yield {
            "health": 50,
            "name": "%s, soldier #%d" % (prefix, i + 1),
            "unit_type": "soldier",
        }


def generate_vehicles(prefix, vehicles_mn, vehicles_mx):
    assert 0 < vehicles_mn <= vehicles_mx
    for i in range(random.randint(vehicles_mn, vehicles_mx)):
        name = "%s, vehicle #%d" % (prefix, i + 1)
        yield {
            "health": 50,
            "name": name,
            "unit_type": "vehicle",
            "operators": list(generate_soldiers(name, 1, 3)),
        }


def generate_squads(
        prefix,
        squads_mn, squads_mx,
        vehicles_mn, vehicles_mx,
        soldiers_mn, soldiers_mx,
):
    assert 0 < squads_mn <= squads_mx
    for i in range(random.randint(squads_mn, squads_mx)):
        name = "%s squad #%d" % (prefix, i + 1)
        yield {
            "name": name,
            "units": [
                *generate_vehicles(name, vehicles_mn, vehicles_mx),
                *generate_soldiers(name, soldiers_mn, soldiers_mx),
            ]
        }


def generate_armies(
        army_names,
        squads_mn, squads_mx,
        vehicles_mn, vehicles_mx,
        soldiers_mn, soldiers_mx,
):
    for army_name in army_names:
        yield {
            "name": army_name,
            "squads": list(generate_squads(
                army_name,
                squads_mn, squads_mx,
                vehicles_mn, vehicles_mx,
                soldiers_mn, soldiers_mx,
            )),
        }


def generate_config(
        army_names,
        squads_mn, squads_mx,
        vehicles_mn, vehicles_mx,
        soldiers_mn, soldiers_mx,
):
    return {
        "armies": list(generate_armies(
            army_names,
            squads_mn, squads_mx,
            vehicles_mn, vehicles_mx,
            soldiers_mn, soldiers_mx,
        ))
    }


def main():
    parser = argparse.ArgumentParser(
        description='Generate battle simulator config',
    )
    parser.add_argument(
        'armies',
        metavar='NAME',
        nargs='+',
        help='Army names',
    )
    parser.add_argument(
        '--min-squads',
        metavar='N',
        type=int,
        required=True,
        help="Min. number of squads per army",
    )
    parser.add_argument(
        '--max-squads',
        metavar='N',
        type=int,
        required=True,
        help="Max. number of squads per army",
    )
    parser.add_argument(
        '--min-soldiers',
        metavar='N',
        type=int,
        required=True,
        help="Min. number of soldiers per squad",
    )
    parser.add_argument(
        '--max-soldiers',
        metavar='N',
        type=int,
        required=True,
        help="Max. number of soldiers per squad",
    )
    parser.add_argument(
        '--min-vehicles',
        metavar='N',
        type=int,
        required=True,
        help="Min. number of vehicles per squad",
    )
    parser.add_argument(
        '--max-vehicles',
        metavar='N',
        type=int,
        required=True,
        help="Max. number of vehicles per squad",
    )
    parser.add_argument(
        '--pprint',
        action='store_true',
        help="Produce human-readable json",
    )

    args = parser.parse_args()
    config = generate_config(
        args.armies,
        args.min_squads, args.max_squads,
        args.min_vehicles, args.max_vehicles,
        args.min_soldiers, args.max_soldiers,
    )

    json.dump(
        config, sys.stdout,
        sort_keys=True, indent=2 if args.pprint else None,
    )

    return 0


if __name__ == '__main__':
    sys.exit(main())