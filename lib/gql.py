from sgqlc.endpoint.http import HTTPEndpoint
import json, os

def query(url: str, vars:dict, query_raw:str) -> dict:
    headers = {'Content-Type': 'application/json'}

    endpoint = HTTPEndpoint(url, headers)
    json_dict = endpoint(query_raw, vars)

    return json_dict
