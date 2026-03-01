import json

with open('06_optimizationTimesteps.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if any('def data(time, features):' in line for line in source):
            new_source = []
            for line in source:
                if 'if features == 0:' in line:
                    # Insert new logic before this line
                    new_source.extend([
                        "    # Feature Engineering\n",
                        "    df = pd.DataFrame(data_strings, columns=['RSI', 'VWAP', 'HeikenResult', 'closeHeiken', 'CMF', 'Stochastic', 'OBV', 'QQE', 'TrendFilter'])\n",
                        "    \n",
                        "    # MACD\n",
                        "    ema12 = df['closeHeiken'].ewm(span=12, adjust=False).mean()\n",
                        "    ema26 = df['closeHeiken'].ewm(span=26, adjust=False).mean()\n",
                        "    df['MACD'] = ema12 - ema26\n",
                        "    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()\n",
                        "    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']\n",
                        "    \n",
                        "    # Bollinger Bands\n",
                        "    df['BB_Middle'] = df['closeHeiken'].rolling(window=20).mean()\n",
                        "    bb_std = df['closeHeiken'].rolling(window=20).std()\n",
                        "    df['BB_Upper'] = df['BB_Middle'] + (bb_std * 2)\n",
                        "    df['BB_Lower'] = df['BB_Middle'] - (bb_std * 2)\n",
                        "    df['BB_Width'] = df['BB_Upper'] - df['BB_Lower']\n",
                        "    \n",
                        "    # ATR proxy (14-period rolling standard deviation of closeHeiken)\n",
                        "    df['ATR_Proxy'] = df['closeHeiken'].rolling(window=14).std()\n",
                        "    \n",
                        "    # Feature Engineering\n",
                        "    df['RSI_overbought'] = (df['RSI'] > 70).astype(int)\n",
                        "    df['RSI_oversold'] = (df['RSI'] < 30).astype(int)\n",
                        "    \n",
                        "    # MACD bullish cross\n",
                        "    df['MACD_bullish_cross'] = 0\n",
                        "    df.loc[df['MACD'] > df['MACD_Signal'], 'MACD_bullish_cross'] = 1\n",
                        "    df.loc[df['MACD'] < df['MACD_Signal'], 'MACD_bullish_cross'] = -1\n",
                        "    \n",
                        "    # Price above EMA200\n",
                        "    ema200 = df['closeHeiken'].ewm(span=200, adjust=False).mean()\n",
                        "    df['Price_above_EMA200'] = (df['closeHeiken'] > ema200).astype(int)\n",
                        "    \n",
                        "    # ROC_10\n",
                        "    df['ROC_10'] = df['closeHeiken'] - df['closeHeiken'].shift(10)\n",
                        "    \n",
                        "    # Handle NaNs\n",
                        "    df.fillna(0, inplace=True)\n",
                        "    \n",
                        "    if features == 0:\n"
                    ])
                elif 'elif features == 2:' in line:
                    new_source.append(line)
                elif '        data_s = data_strings[:,:]' in line:
                    new_source.append(line)
                    new_source.append("    elif features == 3:\n")
                    new_source.append("        data_s = df.values\n")
                else:
                    new_source.append(line)
            cell['source'] = new_source

with open('06_optimizationTimesteps.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

