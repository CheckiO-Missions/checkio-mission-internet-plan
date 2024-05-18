"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [200, [150, 220]],
            "answer": 230,
        },
        {
            "input": [100, [50, 80, 30]],
            "answer": 240,
        },
        {
            "input": [150, [120]],
            "answer": 180,
        }
    ],
    "Extra": [
        {
            "input": [150, [150, 75, 125, 100]],
            "answer": 300,
        },
        {
            "input": [100, [100, 100, 100]],
            "answer": 100
        },
        {
            "input": [100, [71, 87, 89, 91, 65, 76, 100]],
            "answer": 221
        }
    ]
}
