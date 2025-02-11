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
def formatted_help(metric, metric_field_len, attribute, attribute_list, attribute_names_length):
    res = f'{metric:{metric_field_len}} '
    for a_name in attribute_list:  # Build attributes in specific order
        a_value = attribute.get(a_name, '')
        res += f'{a_value:{attribute_names_length[a_name]}} '
    return res.rstrip() # trim trailing spaces

# Dump metrics in a pretty format suitable for .RST docs
def dump_metrics(metrics):
    # pre-calculate the length of the longest string for each attribute, and set up published column headings
    attributes_col_width = {}
    attributes = ['help', 'type', 'unit', 'labels', 'reference']
    column_heading = {
        'metric': 'Name',
        'help': 'Description',
        'type': 'Type',
        'unit': 'Unit',
        'labels': 'Labels',
        'reference': 'Reference'
    }
    # pre-calculate the lengths for column formatting
    for a in attributes:
        attributes_col_width[a] = len(column_heading[a]) # Needs to be at least long enough for the column headings
    metric_col_width = 0
    for metric, attribute in metrics.items():
        metric_col_width = max(metric_col_width, len(metric))
        for key, value in attribute.items():
            if key in attributes_col_width:
                attributes_col_width[key] = max(attributes_col_width[key], len(value))
    # Show the table header rows
    header_row_symbol = '='
    header_rows = {key: header_row_symbol * length for key, length in attributes_col_width.items()}
    header_rows['metric'] = header_row_symbol * metric_col_width
    print(formatted_help(header_rows['metric'], metric_col_width, header_rows, attributes, attributes_col_width))
    print(formatted_help(column_heading['metric'], metric_col_width, column_heading, attributes, attributes_col_width))
    print(formatted_help(header_rows['metric'], metric_col_width, header_rows, attributes, attributes_col_width))

    # dump the metrics
    for metric, attribute in sorted(metrics.items()):
        print(formatted_help(metric, metric_col_width, attribute, attributes, attributes_col_width))

    # .rst needs a table footer
    print(formatted_help(header_rows['metric'], metric_col_width, header_rows, attributes, attributes_col_width))


# Decorate with documentation references. Update this as required
decorate_refs = {
'halon_process_pid':                       			'`smtpd`',
'halon_process_runtime':                   			'`smtpd`',
# 'halon_process_elapsed':                   			'`smtpd`', # Deprecated/not used?
'halon_resolver_running':                  			':confval:`resolver.concurrency`',
'halon_resolver_maxrunning':               			':confval:`resolver.concurrency`',
'halon_resolver_cache_size':               			':confval:`resolver.cache.size`',
'halon_resolver_cache_maxsize':            			':confval:`resolver.cache.size`',
'halon_resolver_cache_expires':            			':confval:`resolver.cache.ttl.min`',
'halon_servers_connections_concurrent':    			':confval:`servers[].concurrency.total`',
# 'halon_servers_serverid':                  			':confval:`servers[]`',
'halon_servers_connections_maxconcurrent': 			':confval:`servers[].concurrency.total`',
'halon_servers_scripts_connect_pending':   			':confval:`servers[].phases.connect.hook`',
'halon_servers_scripts_connect_running':   			':confval:`servers[].threads.script`',
'halon_queue_loader_count':                			':doc:`queue <queue>`',
'halon_queue_loader_maxactive':            			':confval:`queues.maxmessages`',
'halon_queue_scripts_predelivery_pending': 			':confval:`scripting.hooks.predelivery`',
'halon_queue_scripts_predelivery_running': 			':confval:`queues.threads.script`',
'halon_queue_queue_defer_size':            			':doc:`queue <queue>`',
'halon_queue_queue_active_size':           			':doc:`queue <queue>`',
'halon_queue_queue_active_priorities_size':			':doc:`queue <queue>`',
'halon_queue_freeze_update_size':          			':ref:`frozen for update <halonctl-queue-freeze>`',
'halon_queue_freeze_update_pending':       			':ref:`frozen for update <halonctl-queue-freeze>`',
'halon_queue_policy_concurrency_counters': 			':ref:`active queue policies <queue_policy>`',
'halon_queue_policy_concurrency_suspends': 			':ref:`Suspensions <queue_suspend>` created as a result of exceeded concurrency',
'halon_queue_policy_rate_buckets':         			':ref:`active queue policies <queue_policy>`',
'halon_queue_policy_rate_suspends':        			':ref:`Suspensions <queue_suspend>` created as a result of exceeded rate',
'halon_queue_policy_dynamic_suspends':     			'script_',
'halon_queue_policy_dynamic_conditions':   			'script_',
'halon_queue_connections_concurrent':      			':confval:`queues.concurrency.total`',
'halon_queue_connections_maxconcurrent':   			':confval:`queues.concurrency.total`',
'halon_queue_connections_pooling_size':    			':confval:`queues.pooling.size`',
'halon_queue_connections_pooling_maxsize': 			':confval:`queues.pooling.size`',
'halon_queue_connections_pooling_expires': 			':ref:`idle timeout <queue_delivery>`',
'halon_queue_connections_pooling_skips':   			':ref:`non-evictable <queue_delivery>`',
}

def add_references(metrics):
    reference_counts = {key: 0 for key in decorate_refs}
    for metric, attribute in metrics.items():
        if metric in decorate_refs:
            attribute['reference'] = decorate_refs[metric]
            reference_counts[metric] += 1 # we used this reference
    for metric,count in reference_counts.items():
        if count == 0:
            eprint(f'Warning: Reference not used: {metric}')


def main():
    parser = argparse.ArgumentParser(description="Pretty-print OpenMetrics output.")
    parser.add_argument("file", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="Input file (or stdin if omitted)")

    args = parser.parse_args()
    metrics_data = args.file.readlines()
    metrics = get_openmetrics(metrics_data)
    add_references(metrics)
    dump_metrics(metrics)

if __name__ == "__main__":
    main()
