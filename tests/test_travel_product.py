from __init__ import gql, raw, template
import csv, json, os
import pytest

url = "https://traveller-core.pelago.co/graphql"
dev_url = "https://traveller-core.dev.pelago.co/graphql"
dev_product_id = "p417p"
invalid_product_id = "xp417px"
typename_query = raw.query_product_typename
raw_query = raw.query_product_with_field

dir_path = os.path.dirname(os.path.realpath(__file__))
sg_product_id_path = '/csv/live_sg_product_id.csv'
categorical_path = '/csv/field_to_categorical.csv'
min_max_num_path = '/csv/field_to_min_max_num.csv'
min_max_len_path = '/csv/field_to_min_max_len.csv'


# beginning of init functions
def init_sg_product_id():
    with open(dir_path + sg_product_id_path, 'r') as file:
        product_ids = [','.join(row) for row in csv.reader(file)]
    return product_ids

all_product_ids = init_sg_product_id()


def init_categorical_field():
    cat_fields = []
    acceptable_values = {}
    with open(dir_path + categorical_path, 'r') as file:
        for row in csv.reader(file):
            field = row[0]
            cat_fields.append(field)
            for col in row[1:]:
                if field in acceptable_values:
                    acceptable_values[field].append(col)
                else:
                    acceptable_values[field] = [col]
    return cat_fields, acceptable_values

all_cat_fields, acceptable_values = init_categorical_field()


def init_numeric_field():
    numeric_fields = []
    min_value = {}
    max_value = {}
    with open(dir_path + min_max_num_path, 'r') as file:
        for row in csv.DictReader(file):
            # use csv header "num_field" as dict key
            numeric_fields.append(row["num_field"])
            min_value[row["num_field"]] = float(row["min_val"])
            max_value[row["num_field"]] = float(row["max_val"])
    return numeric_fields, min_value, max_value

all_numeric_fields, expected_min_value, expected_max_value = init_numeric_field()


def init_length_field():
    length_fields = []
    min_length = {}
    max_length = {}
    with open(dir_path + min_max_len_path, 'r') as file:
        for row in csv.DictReader(file):
            # use csv header "any_field" as dict key
            length_fields.append(row["any_field"])
            min_length[row["any_field"]] = int(row["min_len"])
            max_length[row["any_field"]] = int(row["max_len"])
    return length_fields, min_length, max_length

all_length_fields, expected_min_length, expected_max_length = init_length_field()
# end of init functions


# beginning of test functions
def test_typename_product_invalid():
    # 1. init precondition
    vars = {"productId": invalid_product_id}
    # 2. retrieve resp
    actual = json.dumps(gql.query(dev_url, vars, typename_query), indent=2)
    print(actual)
    # 3. assert resp validation
    expected = template.field_typename_only.safe_substitute({
        "typeField": "product",
        "typeName": "PelagoError"
    })
    assert actual == expected

def test_typename_product_valid():
    # 1. init precondition
    vars = {"productId": dev_product_id}
    # 2. retrieve resp
    actual = json.dumps(gql.query(dev_url, vars, typename_query), indent=2)
    print(actual)
    # 3. assert resp validation
    expected = template.field_typename_only.safe_substitute({
        "typeField": "product",
        "typeName": "Product"
    })
    assert actual == expected

def test_product_id_invalid():
    # 1. init precondition
    vars = {"productId": invalid_product_id}

    # 2. retrieve resp
    json_dict = gql.query(url, vars, raw_query)
    print(json.dumps(json_dict, indent=2))
    actual = json_dict["data"]["product"]

    # 3. assert resp validation
    expected_match = {
        "__typename": "PelagoError",
        "errorMessage": invalid_product_id + " product not found",
        "code": 404
    }
    for field in actual:
        assert actual[field] == expected_match[field]


@pytest.mark.parametrize("product_id", all_product_ids)
def test_product_id_valid_singapore(product_id):
    # 1. init precondition
    assert product_id is not None

    # 2. retrieve resp
    var = {"productId": product_id}
    json_dict = gql.query(url, var, raw_query)
    print(json.dumps(json_dict, indent=2))
    actual = json_dict["data"]["product"]

    # 3. assert resp validation
    expected_match = {
        "__typename": "Product",
        "productId": product_id,
        "destinationId": "singapore"
    }
    for field in expected_match:
        assert actual[field] == expected_match[field]


@pytest.mark.parametrize("field", all_cat_fields)
@pytest.mark.parametrize("product_id", all_product_ids)
def test_product_categorical_field(product_id, field):
    # 1. init precondition
    assert product_id is not None
    assert field is not None

    # 2. retrieve resp
    var = {"productId": product_id}
    json_dict = gql.query(url, var, raw_query)
    print(json.dumps(json_dict, indent=2))
    actual = json_dict["data"]["product"]    

    # 3. assert resp validation
    assert str(actual[field]) in acceptable_values[field]


@pytest.mark.parametrize("field", all_numeric_fields)
@pytest.mark.parametrize("product_id", all_product_ids)
def test_product_min_max_numeric_field(product_id, field):
    # 1. init precondition
    assert product_id is not None
    assert field is not None

    # 2. retrieve resp
    var = {"productId": product_id}
    json_dict = gql.query(url, var, raw_query)
    print(json.dumps(json_dict, indent=2))
    actual = json_dict["data"]["product"]

    # 3. assert resp validation
    actual_num = actual[field] if actual[field] else 0
    assert float(actual_num) >= expected_min_value[field]
    assert float(actual_num) <= expected_max_value[field]


@pytest.mark.parametrize("field", all_length_fields)
@pytest.mark.parametrize("product_id", all_product_ids)
def test_product_min_max_length_field(product_id, field):
    # 1. init precondition
    assert product_id is not None
    assert field is not None

    # 2. retrieve resp
    var = {"productId": product_id}
    json_dict = gql.query(url, var, raw_query)
    print(json.dumps(json_dict, indent=2))
    actual = json_dict["data"]["product"]

    # 3. assert resp validation
    assert len(actual[field]) >= expected_min_length[field]
    assert len(actual[field]) <= expected_max_length[field]
# end of test functions


if __name__ == "__main__":
    test_product_categorical_field("pbr9o", "cancellationType")
