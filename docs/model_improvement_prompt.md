# Prompt Ulepszenia Modelu LSTM do Predykcji Sygnałów Kupna/Sprzedaży

## Kontekst Projektu

Tworzysz model predykcyjny LSTM do identyfikowania sygnałów kupna/sprzedaży na rynkach finansowych. Obecny model wykorzystuje dane techniczne z 9 różnych wskaźników (RSI, VWAP, HeikenResult, closeHeiken, CMF, Stochastic, OBV, QQE, TrendFilter) i przewiduje 2 wyjścia (kupno/sprzedaż). Projekt zawiera już implementację z wieloma alternatywnymi architekturami modelu LSTM i mechanizmami treningowymi.

## Cel

Twoim celem jest ulepszenie obecnego modelu LSTM zgodnie z załączonymi sugestiami, aby poprawić jego skuteczność w przewidywaniu sygnałów kupna/sprzedaży. Musisz wdrożyć konkretną implementację tych ulepszeń w istniejącym kodzie.

## Obecna Architektura

Z badania kodu wynika, że obecny model:
- Wykorzystuje dane wejściowe o 4, 6 lub 9 cechach (w zależności od parametru `features`)
- Posiada różne architektury (model 0-4) z warstwami LSTM, Dropout i Dense
- Przetwarza sekwencje o długości 150 kroków czasowych
- Ma 2 wyjścia (prawdopodobieństwo sygnału kupna i sprzedaży)
- Wykorzystuje funkcję straty `binary_crossentropy` i optymalizator `Adam`
- Zawiera mechanizmy Early Stopping i zapis modelu najlepszego

## Zadania do Wdrożenia

Wdrożenie wszystkich poniższych ulepszeń w kodzie projektu:

### 1. Dodanie Nowych Wskaźników Technicznych

Rozszerz zestaw cech o nowe wskaźniki techniczne na podstawie danych wejściowych:
- **MACD (Moving Average Convergence Divergence)**: Dodaj trzy osobne cechy - linię MACD, linię sygnału i histogram MACD
- **Bollinger Bands (Wstęgi Bollingera)**: Dodaj trzy cechy - górną wstęgę, dolną wstęgę i szerokość wstęg (różnica między górną i dolną)
- **ATR (Average True Range)**: Dodaj jako pojedynczą cechę jako miarę zmienności

### 2. Inżynieria Cech (Feature Engineering)

Stwórz dodatkowe cechy, które wyraźnie informują o sygnałach transakcyjnych:
- `RSI_overbought`: 1 gdy RSI > 70, 0 w przeciwnym wypadku
- `RSI_oversold`: 1 gdy RSI < 30, 0 w przeciwnym wypadku
- `MACD_bullish_cross`: 1 dla byczego przecięcia (MACD powyżej linii sygnału), -1 dla niedźwiedziego, 0 w pozostałych przypadkach
- `Price_above_EMA200`: 1 gdy cena jest powyżej 200-okresowej średniej kroczącej, 0 w przeciwnym wypadku
- Tempo zmian wskaźników: Oblicz różnicę między aktualną wartością wskaźnika a jego wartością sprzed N kroków (np. 5 lub 10)

### 3. Ulepszenia Architektury Modelu

- **Mechanizm Uwagi (Attention Mechanism)**: Zaimplementuj warstwę Attention po warstwach LSTM, aby model mógł skupić się na najważniejszych krokach czasowych podczas predykcji
- **Alternatywa GRU**: Zaimplementuj alternatywną architekturę z GRU zamiast LSTM i przeprowadź eksperymenty porównujące skuteczność

### 4. Opcjonalne Ulepszenia (jeśli czas pozwoli)

- **Analiza Sentymentu**: Jeśli możliwe, zintegruj dane o sentymencie z mediów finansowych jako dodatkową cechę
- **Ulepszenia Callbacków**: Dodaj dodatkowe callbacki do monitorowania i zapisywania modeli na podstawie metryk profitu
- **Ulepszenia Optymalizatora**: Eksperymentuj z innymi optymalizatorami i harmonogramami zmiany Learning Rate

## Kryteria Sukcesu

- Wdrożenie co najmniej 5 nowych wskaźników technicznych wraz z dodatkowymi cechami inżynieryjnymi
- Implementacja mechanizmu Attention w architekturze modelu
- Przetestowanie architektury GRU jako alternatywy dla LSTM
- Zmierzenie wpływu ulepszeń na:
  - Dokładność predykcji (accuracy)
  - Zyskowność strategii opartej na modelu (profit)
  - Stabilność i zdolność do generalizacji modelu

## Wskazówki Implementacyjne

- Rozszerz funkcję `data()` w notebookach, aby obliczać nowe wskaźniki
- Zmodyfikuj architektury modelu w funkcji `fit_lstmModel()` w celu wdrożenia Attention i GRU
- Użyj TensorFlow/Keras Attention lub zaimplementuj własnoręcznie mechanizm Attention
- Dostosuj funkcję `experiment()` do testowania nowych architektur
- Upewnij się, że nowe cechy są odpowiednio normalizowane przed przekazaniem do modelu
- Przetestuj różne konfiguracje nowych cech, aby znaleźć optymalną kombinację