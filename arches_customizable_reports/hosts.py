import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"arches_customizable_reports"), "arches_customizable_reports.urls", name="arches_customizable_reports"),
)
