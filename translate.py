from googletrans import Translator
import pandas as pd
import csv

headers = ['A','B','A_translation', 'B_translation']
output_file = open(r'C:\Users\akile\bancasella_complaints3.csv', 'wb')
data = pd.read_csv(r'C:\Users\akile\bancasella_complaints.csv',encoding='latin-1')
translator = Translator()
# Init empty dataframe with much rows as `data`
df = pd.DataFrame(index=range(0,len(data)), columns=headers)


def translate_row(row):
    ''' Translate elements A and B within `row`. '''
    a = translator.translate(row[0], dest='Fr')
    b = translator.translate(row[1], dest='en')
    return pd.Series([a.origin, b.origin, a.text, b.text], headers)


for i, row in enumerate(data.values):
    # Fill empty dataframe with given serie.
    df.loc[i] = translate_row(row)


#    output_file.write(translate_row(row)+'\n')
#output_file.close()


#    writer = csv.writer(open(r'C:\Users\akile\bancasella_complaints2.csv', 'w'))
#for row in data:
#    if counter[row[0]] >= 4:
#        writer.writerow(row)
#df.to_csv('r'C:\Users\akile\bancasella_complaints2.csv')
print(df)
