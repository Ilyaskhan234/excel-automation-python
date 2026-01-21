from openpyxl import Workbook


def save_report(data):
    wb=Workbook()
    ws=wb.active

    ws.append(["Metric", "Value"])

    ws.append(["Total", data['total']])
    ws.append(["Average", data['average']])
    ws.append(["Count", data['count']])

    wb.save('report.xlsx')