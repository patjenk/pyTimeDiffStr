# pyTimeDiffStr

**pyTimeDiffStr** is a package that provides a str description of the difference between two dates. The str descriptions are entirely based on my preferences.

```python
>>> from pyTimeDiffStr.timediffstr import timediffstr
>>> from datetime import datetime
>>> datetime_one = datetime(year=2020, month=1, day=4, hour=5, minute=1)
>>> datetime_two = datetime(year=2020, month=1, day=1, hour=5, minute=1)
>>> timediffstr(datetime_one, datetime_two)
'3 days ago'
```

## Unit Tests
Don't forget to use "ipdb.sset_trace()" when using nosetests.

### Run all tests

```console
$ nosetests
```

### Run a specific test

```console
$ nosetests pyTimeDiffStr.tests.test_timediffstr:TestTimeDiffStr.test_1_year_2_weeks
```
