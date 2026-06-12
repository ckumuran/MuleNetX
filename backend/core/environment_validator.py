import os


REQUIRED = [
    "MULENETX_API_KEY",
    "MULENETX_SECRET"
]


def validate_environment():

    missing = []

    for item in REQUIRED:

        if not os.getenv(item):

            missing.append(
                item
            )

    if missing:

        raise RuntimeError(
            f"Missing: {missing}"
        )
