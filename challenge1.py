"""
This module loads an JSON file passed as a command line argument
and launches Docker instances specifed.
"""

import docker
import yaml as json
import argparse
import os


def main():
    parser = argparse.ArgumentParser("Read JSON to create Docker")
    parser.add_argument('jsonfile')
    args = parser.parse_args()
    startContainers(args.jsonfile)


def startContainers(inputJSON):
    cli = docker.from_env()
    with open(inputJSON) as file:
        dockerInstanceDescriptors = json.safe_load(file)
    print(dockerInstanceDescriptors)
    for el in dockerInstanceDescriptors:

        if 'cmd' in el:
            el['command'] = el.pop('cmd')
        if 'image' in el:
            el['image'] = "{0}:{1}".format(el.pop('image'), el.pop('tag'))
        elif 'dockerfile' in el:
            cli.images.build(path=os.path.dirname(
                el.pop('dockerfile')), tag=el['name'])
            el['image'] = tag = el['name']
        else:
            print("No image supplied")
            break

        cli.containers.run(detach=True, **el)


if __name__ == "__main__":
    main()
