import csv
from google.cloud import translate
translate_client = translate.Client()
def translateFunction(text,target):
        translation = translate_client.translate(text,target_language=target)
        return (translation['translatedText'])
output_file = open(r'C:\Users\akile\bancasella_complaints3.csv', 'wb')
reader = csv.reader(open(r'C:\Users\akile\bancasella_complaints.csv', 'rU'), dialect=csv.excel_tab,delimiter=',')
for row in reader:
    column1=translateFunction(translateFunction(row[1],'fr'),'en')
    column2=translateFunction(translateFunction(row[2],'fr'),'en')
    output_text = ','.join([row[0],column1,column2])
    output_file.write(output_text.encode('utf-8')+'\n')
output_file.close()
