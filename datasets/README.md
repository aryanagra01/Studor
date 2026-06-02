# OULAD datasets

Place the Open University Learning Analytics Dataset CSV files in this folder.

| File | In repo? | Notes |
|------|----------|-------|
| `studentInfo.csv` | Yes | Student profiles and outcomes |
| `studentVle.csv` | **No** | ~450 MB — exceeds GitHub limit; download separately |
| `vle.csv` | Yes | VLE site metadata |
| `studentAssessment.csv` | Yes | Assessment submissions |
| `assessments.csv` | Yes | Assessment due dates |
| `studentRegistration.csv` | Yes | Registration dates |
| `courses.csv` | Yes | Module lengths |

## Download

1. [OULAD on OpenML](https://www.openml.org/d/42712)
2. [OU open dataset page](https://analyse.kmi.open.ac.uk/open_dataset)

After cloning the repo, add `studentVle.csv` here before running Task 1 or Task 2 notebooks.

Verify setup:

```bash
python verify_setup.py
```
