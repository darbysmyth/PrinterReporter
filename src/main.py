import pandas as pd
import datetime
import html5lib
import bs4


cur_date = datetime.date.today()

for office in ["office1", "office2"]:

    report = pd.read_html(f"reports/{office}.xls")[0]
    # Filters the Cost type column to include only rows whose cost type is "Total"
    
    is_total = report["Cost type"] == "Total"
    
    report = report[is_total]
    col_to_delete = ["Job type", "Job source", "Job output", "Status", "Cost value", "Paper type", "Paper usage ft²",
                     "Scan length", "Mono category", "Ink used ml", "Print quality", "Scanned area"]
    
    # deletes all unnecessary columns

    for col in col_to_delete:
        report.drop(col, axis=1, inplace=True)
    # Converts all the entries in the Paper length column from string to floats and then rounds them to 0 decimal places
   
    report = report.astype({"Paper length": float})
    report = report.round({"Paper length": 0})

    # Drops any rows that show 0 copies and 0 Paper length (4)

    for row in report.itertuples():
        if row.Copies == 0 and row[4] == 0:
            report.drop(row[0], inplace=True)

    # Opens the last date text file for each branch and delees all rows before that date
    # All previous rows would have been included in the last report and are unnecessary

    
    with open(f"dates/{office}_last_date.txt", mode="r+") as txt:
        date = txt.read()
        for row in report.itertuples():
            if row[6] != date:
                report.drop(row[0], inplace=True)
            else:
                break
    # Grabs the new last date from the current doc and writes it to the last date text file
        last_date = report.iloc[-1]["Printing time"]
        txt.truncate(0)
        txt.seek(0)
        txt.write(last_date)
        txt.close()

    # Formats the output file so that its readable

    try:
        writer = pd.ExcelWriter(f"reports/{office}-Reports {cur_date.day} {cur_date.strftime('%B')} {cur_date.year}.xlsx", engine="xlsxwriter")
        report.to_excel(writer, index=False, sheet_name="report")

        workbook = writer.book
        worksheet = writer.sheets["report"]

        wrap_format = workbook.add_format({"text_wrap": True})

        worksheet.set_column("A:A", 45, wrap_format)
        worksheet.set_column("D:G", 15)
        worksheet.set_column("F:F", 20)
        worksheet.set_default_row(30)

        writer.save()
    except PermissionError:
        print("The output doc is open you gotta close it")



