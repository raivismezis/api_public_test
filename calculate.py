import json

with open("metrics.json") as f:
    data = json.load(f)

values = data["values"]

result = {
    "sum": sum(values),
    "average": sum(values) / len(values),
    "min": min(values),
    "max": max(values),
    "count": len(values)
}

with open("result.json", "w") as f:
    json.dump(result, f, indent=2)

print("Done:", result)
