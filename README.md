# 🚗 현대모비스 부품가격관리 직무 포트폴리오 (Advanced Econometrics)

이 리포지토리는 "현대모비스 A/S 부품가격관리" 직무를 위해 **응용계량거시경제학** 지식을 실무에 최적화하여 구현한 데이터 분석 포트폴리오입니다. 단순한 OLS나 EDA를 넘어, **실제 거시 데이터 API**와 **고급 계량경제 모형**을 결합하여 가격 정책의 탄탄한 통계적 근거를 도출하는 일련의 파이프라인을 보여줍니다.

## 🚀 Projects Overview

### Project 1: 가격 내생성을 고려한 패널 데이터 가격탄력성 분석 (`Project1_Price_Elasticity`)
- 단순 회귀분석 시 발생하는 가격과 수요 간의 **내생성(Endogeneity)** 문제를 지적하고 해결합니다.
- `linearmodels`의 **Panel Fixed Effects(고정효과)** 모델을 활용하여, 국가 및 시간 특유의 이질성(Unobserved Heterogeneity)을 통제한 순수한 부품별 가격 탄력성을 도출했습니다.

### Project 2: 환율/원자재 다변량 시계열 분석 (`Project2_TimeSeries_Forecast`)
- 환율(KRW/USD) 변동과 수입 원자재(철강, 알루미늄) 가격 지수 간의 선후 관계를 규명합니다.
- **VAR (Vector Autoregression) 모형**을 적합하고 시계열 안정성 검정(ADF)을 수행했습니다.
- **충격반응함수(IRF, Impulse Response Function)**를 시뮬레이션하여, 환율 쇼크 시 몇 개월 뒤에 원가 타격이 오는지를 정량화하고 "선제적 가격 인상"의 골든타임을 제언합니다.

### Project 3: World Bank API 글로벌 시장 군집화 (`Project3_Market_Clustering`)
- `wbgapi` (World Bank)를 활용하여 50개 주요 국가의 1인당 GDP, 인플레이션 등 **실제 경제 지표**를 수집했습니다.
- K-Means 알고리즘으로 체급별 시장을 군집화하고, 로그스케일 선형회귀를 통해 경제력 대비 극단적으로 과소평가(Underpriced) 혹은 과대평가(Overpriced)된 가격 징후(Anomaly)를 적발합니다.

### Project 4: 실시간 손익/거시 모니터링 대시보드 (`Project4_Profit_Dashboard`)
- 위 3가지 프로젝트의 핵심 분석 결과 엔진을 결합한 `Streamlit` 기반의 웹 대시보드입니다.
- 환율 쇼크, 원자재 동향, 군집별 가격 이탈 현황, 그리고 가격을 변경했을 때의 예상 손익 변화량을 원클릭으로 시뮬레이션 할 수 있습니다.

---

## 🛠 Tech Stack & Tools
- **Data & Modeling**: `pandas`, `numpy`, `statsmodels`, `scikit-learn`, `linearmodels`
- **Real-time API**: `yfinance` (Macro), `wbgapi` (World Bank)
- **App & Visualization**: `streamlit`, `plotly.express`, `matplotlib`, `seaborn`

## 💬 Interview & Resume Preparation
- 지원자가 본 프로젝트를 면접 및 자소서에서 어떻게 방어하고 '실무적 인사이트'로 포장할 수 있는지에 대한 디테일한 가이드는 프로젝트 폴더 외부에 위치한 `interview_prep.md` 문서에 정리되어 있습니다.
