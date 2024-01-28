# %%
import sys
import camelot

pdf_path = sys.argv[1]
print(f'parse {pdf_path}')

tables = camelot.read_pdf(pdf_path, flavor='lattice', pages='1-end')

for i, table in enumerate(tables):
    table.to_csv(f'data/interim/the-registry/{i+1}.csv', index=False)
    print(f'write data/interim/the-registry/{i+1}.csv')


