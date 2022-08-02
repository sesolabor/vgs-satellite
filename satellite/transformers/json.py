import json
import sys
from typing import Callable

from jsonpath_ng import parse

from . import Transformer


class JsonTransformer(Transformer):
    def transform(self, payload: str, operation: Callable) -> str:
        payload_json = json.loads(payload)
        for expression in self.config.array:
            json_expr = parse(expression)
            transformed_values = []
            for match in json_expr.find(payload_json):
                transformed_value = operation(match.value)
                transformed_values.append(transformed_value)

                json_expr.update(payload_json, transformed_value)

            # Hack to handle revealing arrays of multiple tokens
            if str(json_expr) == "$.revealTokens.[*]":
                whole_array_expr = parse("$.revealTokens")
                whole_array_expr.update(payload_json, transformed_values)
        return json.dumps(payload_json)
