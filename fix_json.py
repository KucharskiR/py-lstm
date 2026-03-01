import re

for filename in ['06_optimizationTimesteps.ipynb', '07_optimizationFeatures.ipynb']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the missing comma
    pattern = r'"        data_s = data_strings\[:, :\]\n"\s+"        \n",'
    replacement = r'"        data_s = data_strings[:, :]\n",\n    "        \n",'
    
    fixed_content = re.sub(pattern, replacement, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

print("Fix script executed")
