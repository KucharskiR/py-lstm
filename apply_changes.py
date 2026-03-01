import json

# Read both notebooks
with open('06_optimizationTimesteps.ipynb', 'r', encoding='utf-8') as f:
    nb6 = json.load(f)
    
with open('07_optimizationFeatures.ipynb', 'r', encoding='utf-8') as f:
    nb7 = json.load(f)

# Find the cells in nb6
imports_cell = None
data_cell = None
fit_cell = None

for cell in nb6['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'import numpy as np' in source and 'from keras.models import Sequential' in source:
            imports_cell = cell['source']
        elif 'def data(time, features):' in source:
            data_cell = cell['source']
        elif 'def fit_lstmModel(' in source:
            fit_cell = cell['source']

# Replace the cells in nb7
for cell in nb7['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'import numpy as np' in source and 'from keras.models import Sequential' in source:
            cell['source'] = imports_cell
        elif 'def data(time, features):' in source:
            # We need to keep the file paths from nb7
            # In nb7:
            # file_features = './data/8_150_1H/8_150_1H_f.csv'
            # file_labels = './data/8_150_1H/8_150_1H_l.csv'
            
            # Let's just replace the whole cell but fix the paths
            new_source = []
            for line in data_cell:
                if "file_features = './data/2_150x9/2_150x9f.csv'" in line:
                    new_source.append("    file_features = './data/8_150_1H/8_150_1H_f.csv'\n")
                elif "file_labels = './data/2_150x9/2_150x9l.csv'" in line:
                    new_source.append("    file_labels = './data/8_150_1H/8_150_1H_l.csv'\n")
                else:
                    new_source.append(line)
            cell['source'] = new_source
            
        elif 'def fit_lstmModel(' in source:
            cell['source'] = fit_cell

with open('07_optimizationFeatures.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb7, f, indent=1)

print("Changes applied to 07_optimizationFeatures.ipynb")
