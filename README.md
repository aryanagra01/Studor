# StudorAI

Analytics project on the **Open University Learning Analytics Dataset (OULAD)**. Three tasks cover engagement scoring, early at-risk prediction, and course recommendations.

## Project structure

```
StudorAI/
├── datasets/                  # OULAD CSV files (see Data below)
├── task 1/                    # Dynamic engagement score
│   ├── eda.ipynb
│   └── task1_engagement_score.ipynb
├── task 2/                    # At-risk prediction
│   ├── task2_feature_engineering.ipynb
│   └── task2_model_comparison.ipynb
├── task 3/                    # Course recommender
│   └── task3_recommenders.ipynb
├── utils/
│   └── paths.py               # Shared data-path helper
├── archive/                   # Earlier notebook drafts
├── requirements.txt
└── README.md
```

## Setup

1. **Python 3.10+** recommended.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place OULAD CSV files in `datasets/`:

   | File | Description |
   |------|-------------|
   | `studentInfo.csv` | Student demographics and final results |
   | `studentVle.csv` | VLE clickstream |
   | `vle.csv` | VLE site metadata |
   | `studentAssessment.csv` | Assessment submissions |
   | `assessments.csv` | Assessment due dates and weights |
   | `studentRegistration.csv` | Registration dates |
   | `courses.csv` | Module presentation lengths |

   Download from [OULAD on OpenML](https://www.openml.org/d/42712) or the [OU repository](https://analyse.kmi.open.ac.uk/open_dataset).

   **Note:** `studentVle.csv` (~450 MB) is not stored in GitHub due to file-size limits. After cloning, download it separately and place it in `datasets/` (see `datasets/README.md`).

4. Launch Jupyter from the **project root**:

   ```bash
   jupyter notebook
   ```

   Notebooks auto-detect `datasets/` whether you run them from the root or from inside a `task N/` folder.

5. Optional — verify everything is in place:

   ```bash
   python verify_setup.py
   ```

## Task 1 — Dynamic engagement score

**Notebook:** `task 1/task1_engagement_score.ipynb`  
**EDA:** `task 1/eda.ipynb`

Builds a weekly **0–100 engagement score** from five equally weighted areas (20 points each):

| Area | Signal |
|------|--------|
| A1 Activity | Click volume + active days |
| A2 Breadth | Distinct VLE activity types |
| A3 Recency | Days since last click |
| A4 Relative standing | Cohort percentile within each week |
| A5 Assessment | Submission rate, timeliness, score rate |

**Course focus:** CCC 2014J (~2,500 students).

**Outputs** (written to `task 1/` when the notebook is run):

- `engagement_scores_v2_clean4.csv` — student-week scores
- `student_trajectory_summary_v2_clean4.csv` — per-student summary
- `validation_v2_clean4.csv` — mean score by outcome
- `archetype_trajectories_v2_clean4.png` — four report archetypes

**Archetypes:** Steady engager, Early fader, Late recoverer, High-effort struggler.

## Task 2 — At-risk prediction

**Notebooks:**

1. `task 2/task2_feature_engineering.ipynb` — build 19 features, correlation/relevance analysis, feature-set comparison
2. `task 2/task2_model_comparison.ipynb` — 3×3 model × feature-set grid, final evaluation

**Target:** `at_risk = 1` if final result is Withdrawn or Fail (~53% of students).

**Features** are computed from the **first 6 weeks only** (days 0–41) plus enrolment-time fields — no label leakage.

**Models:** Logistic Regression, Random Forest, XGBoost  
**Feature sets:** lean (9), balanced (11), full (19)

Run both notebooks top to bottom. The model comparison notebook evaluates the chosen winner on a held-out test set and saves calibration / threshold plots to `task 2/`.

## Task 3 — Course recommendation

**Notebook:** `task 3/task3_recommenders.ipynb`

Recommends the next course for a student using:

- **Method A — Content-based:** cosine similarity on course metadata + student academic profile
- **Method B — Collaborative filtering:** item-based CF on co-enrolment
- **Cold start:** content-based from profile only, or popularity fallback

**Evaluation:** leave-one-out hit-rate@3 and coverage vs a popularity baseline.

## Suggested run order

1. `task 1/eda.ipynb` (optional — informs scaling choices)
2. `task 1/task1_engagement_score.ipynb`
3. `task 2/task2_feature_engineering.ipynb`
4. `task 2/task2_model_comparison.ipynb`
5. `task 3/task3_recommenders.ipynb`

## Submission checklist

- [ ] `datasets/` contains all seven OULAD CSV files
- [ ] `pip install -r requirements.txt` succeeds
- [ ] Task 1 notebook runs and produces validation CSV + archetype plot
- [ ] Task 2 notebooks run and produce model comparison outputs
- [ ] Task 3 notebook runs and prints evaluation metrics
- [ ] Report write-ups reference outputs from each task

## Notes

- `studentVle.csv` is ~450 MB; allow time for loading in Task 1 and Task 2.
- Earlier notebook drafts are kept in `archive/` for reference.
- Large generated CSV `engagement_scores_v2_clean4.csv` is included as a pre-computed output; re-run Task 1 to regenerate.

## License & data attribution

Code in this repository is submitted coursework. OULAD is © The Open University; use and cite according to their [dataset terms](https://analyse.kmi.open.ac.uk/open_dataset).
