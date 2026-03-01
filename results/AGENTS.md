# RESULTS KNOWLEDGE BASE

## OVERVIEW
Archive of sequential LSTM experiments containing notebook snapshots and performance plots.

## STRUCTURE
```text
results/
├── 01/                      # First experiment iteration
├── 02/                      # Second experiment iteration
├── ...                      # Sequential runs
└── 21/                      # Latest experiment iteration
    ├── *.ipynb              # Snapshot of the notebook used for this run
    ├── boxplot_*.png        # Summary boxplots comparing metrics
    ├── compare_models_*.jpg # Training curve plots for model comparison
    └── *_results.png        # Additional result visualizations
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Find latest run | `results/21/` | Highest number is the most recent experiment. |
| Check feature tests | `results/20/` | Contains `07_optimizationFeatures.ipynb` snapshots. |
| View metric spread | `boxplot_*.png` | Shows variance across multiple training repeats. |
| Analyze training | `compare_models_*.jpg` | Loss and accuracy curves over epochs. |
| Review early tests | `results/01/` | Contains initial baseline results and plots. |

## CONVENTIONS
- **Directory Naming**: Two-digit zero-padded numbers (`01` to `21`) representing sequential experiment runs.
- **Notebook Snapshots**: Exact copies of the Jupyter notebook executed for that specific run. This ensures reproducibility.
- **Plot Naming**: `boxplot_[param].png` for aggregate metric distributions. `compare_models_[index].jpg` for individual model training histories.
- **Immutability**: Treat these directories as read-only historical records. Don't modify past experiment data.
