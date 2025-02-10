#!/usr/bin/env python3
import sys, argparse, re

# Print to stderr - see https://stackoverflow.com/a/14981125/8545455
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_openmetrics(lines):
    metrics = {}
    for line in lines:
        if line.startswith("#"):
            # Format comments (metadata)
            if match := re.match(r'^#\s*HELP\s+(?P<metric>\w+)\s*(?P<help>.*)$', line):
                metric = match.group('metric')
                help = match.group('help')
                if metric and help:
                    metrics[metric] = {'help': help}
                else:
                    eprint(f'Error in line: {line}')
            else:
                pass # ignore the type info for now
        else:
            # A metric value
            if match := re.match(r'^\s*(?P<metric>\w+)(?P<labels>{.*})*\s+(?P<val>\w+)', line):
                metric = match.group('metric')
                val = match.group('val')
                if metric not in metrics:
                    metrics[metric] = {} # ensure it's defined
                if labels := match.group('labels'):
                    labs = parse_metric_labels(labels)
                    if labs:
                        metrics[metric]['labels'] = labs
                    else:
                        eprint(f'Labels not recognized in: {line}')
            else:
                    eprint(f'Error in line: {line}')
    return metrics


def parse_metric_labels(metric):
    match = re.search(r"\{([^{}]+)\}", metric)
    if match:
        labels = match.group(1)  # Extract content inside {}
        return dict(item.split("=") for item in labels.split(","))
    return {}


# How these labels should appear in the help text
label_map = {
    'priority': ('priorities', 'priorities[]'),
    'threadid': None, # Ignored in help text?
    'id': None, # Ignored in help text?
    'serverid': ('servers', 'servers[]'),
}

# Format for Halon help table in cli.rst
def format_help(key, value):
    # Strip off the halon_ prefix
    halon_prefix = 'halon_'
    if key.startswith(halon_prefix):
        key = key.removeprefix(halon_prefix)
        helptext = value['help']

        # Fix up any specific labels into the format used in the help text
        if 'labels' in value:
            for l in value['labels']:
                if l in label_map:
                    if replace := label_map[l]:
                        key = key.replace(replace[0], replace[1])
                else:
                    eprint(f'Unknown label {l}')
        # Underscore separators become periods
        key = key.replace('_', '.')
        return(f'{key:43}{helptext}')
    else:
        eprint(f'Key did not start with {halon_prefix}: {key}')


def dump_metrics(metrics):
    for key, value in sorted(metrics.items()):
        print(format_help(key, value))


def main():
    parser = argparse.ArgumentParser(description="Pretty-print OpenMetrics output.")
    parser.add_argument("file", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="Input file (or stdin if omitted)")

    args = parser.parse_args()
    metrics_data = args.file.readlines()
    metrics = get_openmetrics(metrics_data)
    dump_metrics(metrics)

if __name__ == "__main__":
    main()
