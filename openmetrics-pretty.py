#!/usr/bin/env python3
import sys, argparse, re

# Print to stderr - see https://stackoverflow.com/a/14981125/8545455
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_openmetrics(lines):
    metrics = {}
    for line in lines:
        if line.startswith("#"):
            # Group HELP, TYPE, UNIT information together for each metric
            for field in ['help', 'type', 'unit']:
                keyword = field.upper()
                if match := re.match(fr'^#\s*{keyword}\s+(?P<metric>\w+)\s*(?P<keyword>.*)$', line):
                    metric = match.group('metric')
                    if not metric in metrics:
                        metrics[metric] = {}
                    key_match = match.group('keyword')
                    if metric and key_match:
                        metrics[metric][field] = key_match
                    else:
                        eprint(f'Error in line: {line}')
        else:
            # Look for labels in metric values
            if match := re.match(r'(?P<metric>\w+){(?P<labels>.*)}\s+(?P<value>.*)', line):
                metric = match.group('metric')
                labels = match.group('labels')
                if not metric in metrics:
                    metrics[metric] = {}
                if labels:
                    metrics[metric]['labels'] = parse_metric_labels(labels)
    return metrics


# Return as simple comma-separated list of labels
def parse_metric_labels(labels):
    label_names = []
    for label in labels.split(","):
        key, _ = label.split("=")
        label_names.append(key.strip())
    return ",".join(label_names)


# Format for Halon help table in cli.rst
def format_help(metric, metric_field_len, attribute, attribute_list, attribute_names_length):
    res = f'{metric:{metric_field_len}} '
    for a_name in attribute_list:  # Build attributes in specific order
        a_value = attribute.get(a_name, '')
        res += f'{a_value:{attribute_names_length[a_name]}} '
    return res

# Dump metrics in a pretty format suitable for .RST docs
def dump_metrics(metrics):
    # pre-calculate the length of the longest string for each attribute
    attribute_names_length = {}
    attribute_list = ['help', 'type', 'unit', 'labels']
    table_heading = {
        'metric': 'Name',
        'help': 'Description',
        'type': 'Type',
        'unit': 'Unit',
        'labels': 'Labels'
    }
    for a in attribute_list:
        attribute_names_length[a] = len(a) # initial values
    # pre-calculate the length of the longest metric name
    metric_field_len = 0
    for metric, attribute in metrics.items():
        metric_field_len = max(metric_field_len, len(metric))
        for key, value in attribute.items():
            if key in attribute_names_length:
                attribute_names_length[key] = max(attribute_names_length[key], len(value))
    # Header rows
    header_rows = {key: '=' * length for key, length in attribute_names_length.items()}
    header_rows['metric'] = '=' * metric_field_len
    print(format_help(header_rows['metric'], metric_field_len, header_rows, attribute_list, attribute_names_length))
    print(format_help(table_heading['metric'], metric_field_len, table_heading, attribute_list, attribute_names_length))
    print(format_help(header_rows['metric'], metric_field_len, header_rows, attribute_list, attribute_names_length))
    # dump the metrics
    for metric, attribute in sorted(metrics.items()):
        print(format_help(metric, metric_field_len, attribute, attribute_list, attribute_names_length))


def main():
    parser = argparse.ArgumentParser(description="Pretty-print OpenMetrics output.")
    parser.add_argument("file", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="Input file (or stdin if omitted)")

    args = parser.parse_args()
    metrics_data = args.file.readlines()
    metrics = get_openmetrics(metrics_data)
    dump_metrics(metrics)

if __name__ == "__main__":
    main()
