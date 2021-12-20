#!/usr/bin/env python3
"""
Example cijoe extractor showing the required signature of a cijoe extractor:

```python
def extract_metrics(_: TestCase) -> List[dict]
```

The example also shows how some utility functions help to make unit conversions
(`to_base_unit()`) and dumping of metrics (`dump_metrics_to_file()`) to yaml
files easy.

`to_base_unit()` takes as arguments the measured value and the unit of this
value, which can then be converted to cijoe's base unit.

`dump_metrics_to_file()` takes as argument the metrics in base units and the
path to the testcase auxiliary directory, where the properly formatted output
will be placed.
"""

import os
from typing import List

from cij.runner import TestCase
from cij.analyser import to_base_unit
from cij.extractors.util import dump_metrics_to_file

_MY_NAME = os.path.splitext(os.path.basename(__file__))[0]


def extract_metrics(tcase: TestCase) -> List[dict]:
    metrics = [
        {
            # context for the test that was run, likely taken from tcase
            'ctx': {
                'extractor': _MY_NAME,
                'some other extractor defined context': 1,
            },

            # iops was 100,000 io/sec, which is translated to cijoe's base unit
            "iops": to_base_unit(100_000, ""),

            # bwps was 4500 KiB/s, which is translated to cijoe's base unit
            "bwps": to_base_unit(4500, "KiB"),

            # latency was 4500usec, which is translated to cijoe's base unit
            "lat": to_base_unit(4500, "usec"),
        }
    ]
    if metrics:  # Only dump non-empty metrics
        dump_metrics_to_file(metrics, tcase.aux_root)

    return metrics
