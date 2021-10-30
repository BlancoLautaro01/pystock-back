from pystock.app.services.product_service import get_all_codes, get_by_cod
from pystock.app.services.movements_service import get_all_movements, get_all_movement_codes


def get_report():
    report = []
    codes = get_all_codes()

    for cod in get_all_movement_codes():
        if cod not in codes:
            codes.append(cod)

    for cod in codes:
        report.append(generate_report_of(cod))

    return report


def generate_report_of(cod):
    name = get_by_cod(cod)["name"]
    total_amount = 0
    for movement in get_all_movements():
        if movement["cod"] == cod:
            if movement["type"]:
                total_amount += int(movement["amount"])
            else:
                total_amount -= int(movement["amount"])

    return {
        "cod": cod,
        "name": name,
        "total": total_amount
    }
