# Analiza Wyników Optymalizacji Modelu LSTM

Data analizy: 2025-09-01

## Cel Analizy

Celem było zidentyfikowanie najlepiej działających hiperparametrów dla modelu LSTM na podstawie wyników eksperymentów zapisanych w katalogu `results`. Analiza opierała się na interpretacji kodu z notebooków oraz na wizualnej inspekcji wygenerowanych wykresów (plików `.png`), ze szczególnym uwzględnieniem metryki **Profit**.

---

## 1. Wnioski z Analizy Architektury Modelu

- **Folder z wynikami:** `results/17/`
- **Plik z wykresem:** `boxplot_Model.png`

**Wniosek:** Najlepsze wyniki pod względem zysku osiągnął **Model 2 (`modelVar = 2`)**. Charakteryzował się on najwyższą medianą oraz najwyższym maksymalnym zanotowanym zyskiem.

- **Zwycięska Architektura:** 2 warstwy LSTM (150 neuronów) + 1 warstwa Dense (75 neuronów).

---

## 2. Wnioski z Analizy Kroku Czasowego (Timestep)

- **Folder z wynikami:** `results/19/`
- **Plik z wykresem:** `boxplot_Timestep.png`

**Wniosek:** W tym eksperymencie wszystkie warianty przyniosły stratę. Najlepszym ustawieniem (minimalizującym stratę) był **Timestep = 10**. Dłuższe kroki czasowe prowadziły do systematycznego pogarszania wyniku.

- **Zwycięski Timestep:** `10`.

---

## 3. Wnioski z Analizy Zestawu Cech (Features)

- **Folder z wynikami:** `results/20/`
- **Plik z wykresem:** `boxplot_Features.png`

**Wniosek:** Podobnie jak w teście kroków czasowych, ten eksperyment również zanotował ujemny zysk. Najlepsze i najbardziej stabilne wyniki (najmniejsza strata, niska wariancja) zapewnił **Zestaw 1**.

- **Zwycięski Zestaw Cech:** `features = 1` (6 cech: RSI, VWAP, CMF, Stochastic, OBV, TrendFilter).

---

## Podsumowanie i Rekomendowana Konfiguracja do Dalszych Testów

Na podstawie powyższej analizy, rekomendowana konfiguracja dla nowej, potencjalnie najlepszej wersji modelu, to połączenie zwycięskich parametrów ze wszystkich testów:

*   **Architektura:** Model 2 (2x LSTM 150 neuronów + Dense 75).
*   **Krok Czasowy (Timestep):** 10.
*   **Zestaw Cech:** Zestaw 1 (6 wybranych cech).

**Ważna obserwacja:** Należy odnotować, że nowsze eksperymenty (dot. Timestep i Features) przyniosły stratę, podczas gdy starszy test (dot. Architektury) był zyskowny. Może to wynikać z użycia innych danych lub modyfikacji w funkcji obliczającej zysk w późniejszych notebookach. Ten aspekt należy wziąć pod uwagę przy dalszych pracach.
