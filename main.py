from processor import process_file
from reporter import save_report

if __name__=='__main__':
    file='sample.xlsx'
    data=process_file(file)
    save_report(data)
