import json

import click
import uvicorn

from . import app


def write_schema():
    schema = app.openapi()
    filename = "./openapi.json"
    print(f"Writing schema to {filename}")

    with open(filename, "wt") as f:
        json.dump(schema, f, indent=4)


@click.command()
@click.option("--schema", default=False)
def main(schema):
    if schema:
        write_schema()
        return

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
