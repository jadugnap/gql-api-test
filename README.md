# gql-api-test

A simple implementation of GraphQL API Test using pytest. Libraries [pytest-xdist](https://pypi.org/project/pytest-xdist/) and [sgqlc](https://sgqlc.readthedocs.io/en/latest/) are chosen for
- Quick API Testing in Python
- Easy-to-use GraphQL client
- Command line execution
- Parallel testing
- Compatibility across OS machines

## Project Structure:
- [library](https://github.com/jadugnap/gql-api-test/tree/main/lib) manage the main logic to query GraphQL API.
- [tests/csv](https://github.com/jadugnap/gql-api-test/tree/main/tests/csv) store the test cases table for lookup.
- [tests suites](https://github.com/jadugnap/gql-api-test/tree/main/tests/test_travel_product.py) contain the actual test functions to be executed.
- [parametrize decorator](https://docs.pytest.org/en/6.2.x/parametrize.html) enable single test function to receive arguments and validate multiple testing points at once, thus keeping it short and simple.
- **Future Work**: suppose the GraphQL schema introspection is granted, test cases implementation can be further improved on the other APIs beside `Query` operation and `Product` field.

## Test Scenario Spreadsheet:
https://docs.google.com/spreadsheets/d/17CtVE0aZCrCQXSteLKJfE_Ngpk1iVnOFuGxxjllGLhY/edit#gid=728841992

## Installation:
```
pip install -r requirements.txt
```

## Execution:
1. Pytest simple run (with cache disabled)
```
python3 -m pytest -p no:cacheprovider
```
2. Pytest print all test cases with duration
```
python3 -m pytest -p no:cacheprovider -v --durations 0
```
3. Pytest with parallel worker -n 4
```
python3 -m pytest -p no:cacheprovider -v --durations 0 -n 4
```

## Test Results
- Simple run (129 cases passed in 10+ seconds):

```
=================================================================== test session starts ====================================================================
platform darwin -- Python 3.8.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test
plugins: xdist-2.2.1, forked-1.3.0
collected 129 items                                                                                                                                        

tests/test_travel_product.py ....................................................................................................................... [ 92%]
..........                                                                                                                                           [100%]

=================================================================== 129 passed in 10.34s ===================================================================
```

- Parallel run with 4 workers (129 cases passed in 3+ seconds):
```
=================================================================== test session starts ====================================================================
platform darwin -- Python 3.8.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test/env-gql/bin/python3
rootdir: /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test
plugins: xdist-2.2.1, forked-1.3.0
[gw0] darwin Python 3.8.2 cwd: /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test
[gw1] darwin Python 3.8.2 cwd: /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test
[gw2] darwin Python 3.8.2 cwd: /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test
[gw3] darwin Python 3.8.2 cwd: /Users/jadug.parusa/go/src/github.com/jadugnap/gql-api-test
[gw0] Python 3.8.2 (default, Apr  8 2021, 23:19:18)  -- [Clang 12.0.5 (clang-1205.0.22.9)]
[gw1] Python 3.8.2 (default, Apr  8 2021, 23:19:18)  -- [Clang 12.0.5 (clang-1205.0.22.9)]
[gw2] Python 3.8.2 (default, Apr  8 2021, 23:19:18)  -- [Clang 12.0.5 (clang-1205.0.22.9)]
[gw3] Python 3.8.2 (default, Apr  8 2021, 23:19:18)  -- [Clang 12.0.5 (clang-1205.0.22.9)]
gw0 [129] / gw1 [129] / gw2 [129] / gw3 [129]
scheduling tests via LoadScheduling

tests/test_travel_product.py::test_typename_product_valid 
tests/test_travel_product.py::test_typename_product_invalid 
tests/test_travel_product.py::test_product_id_invalid 
tests/test_travel_product.py::test_product_id_valid_singapore[pbr9o] 
[gw0] [  0%] PASSED tests/test_travel_product.py::test_typename_product_invalid 
[gw1] [  1%] PASSED tests/test_travel_product.py::test_typename_product_valid 
tests/test_travel_product.py::test_product_id_valid_singapore[pgx9o] 
tests/test_travel_product.py::test_product_id_valid_singapore[p0ftx] 
[gw3] [  2%] PASSED tests/test_travel_product.py::test_product_id_valid_singapore[pbr9o] 
[gw2] [  3%] PASSED tests/test_travel_product.py::test_product_id_invalid 
...
[gw3] [ 97%] PASSED tests/test_travel_product.py::test_product_min_max_length_field[pr2q3-productName] 
tests/test_travel_product.py::test_product_min_max_length_field[pr2q3-address] 
[gw1] [ 98%] PASSED tests/test_travel_product.py::test_product_min_max_length_field[pr2q3-confirmationType] 
[gw0] [ 99%] PASSED tests/test_travel_product.py::test_product_min_max_length_field[pr2q3-voucherType] 
[gw2] [100%] PASSED tests/test_travel_product.py::test_product_min_max_length_field[pr2q3-address] 

==================================================================== slowest durations =====================================================================
1.16s call     tests/test_travel_product.py::test_product_id_invalid
1.16s call     tests/test_travel_product.py::test_product_id_valid_singapore[pbr9o]
1.12s call     tests/test_travel_product.py::test_typename_product_valid
1.12s call     tests/test_travel_product.py::test_typename_product_invalid
0.08s call     tests/test_travel_product.py::test_product_min_max_length_field[pgx9o-confirmationType]
0.08s call     tests/test_travel_product.py::test_product_min_max_length_field[pxv8r-address]
0.08s call     tests/test_travel_product.py::test_product_min_max_length_field[pbr9o-cancellationType]
...
0.05s call     tests/test_travel_product.py::test_product_min_max_numeric_field[pgx9o-priceRangeTo]
0.05s call     tests/test_travel_product.py::test_product_categorical_field[pt1x5-openDateTicket]
0.05s call     tests/test_travel_product.py::test_product_categorical_field[pr2q3-collectPhysicalTicket]

(258 durations < 0.005s hidden.  Use -vv to show these durations.)

=================================================================== 129 passed in 3.84s ====================================================================
```
