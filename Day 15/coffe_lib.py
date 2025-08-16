from statistics import quantiles

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": {
            "quant": 300,
            "unit": "ml"
            },
    "milk": {
            "quant": 200,
            "unit": "ml"
            },
    "coffee": {
            "quant": 100,
            "unit": "g"
            },
}
money = {
    "money": 125
}
