def rank(results):

    valid = [
        r for r in results
        if r is not None
    ]

    return sorted(
        valid,
        key=lambda x: (
            x["score"],
            x["confidence"],
        ),
        reverse=True,
    )