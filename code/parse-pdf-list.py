# %%
import camelot

pdf_path = 'data/raw/reestr-inostrannyih-agentov-17112023.pdf'

tables = camelot.read_pdf(pdf_path, flavor='lattice', pages='1-end')

for i, table in enumerate(tables):
    table.to_csv(f'data/interim/reestr-page/{i+1}.csv', index=False)
    print(f'write data/interim/reestr-page/{i+1}.csv')


