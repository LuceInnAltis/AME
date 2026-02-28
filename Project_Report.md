# 📊 현대모비스 서비스부품 가격관리 최적화 프로젝트 결과 보고서

---

## 1. 목차 (Table of Contents)
1. 문제 정의 (Problem Definition)
2. 프로젝트 목적 및 설명 (Project Objective & Description)
3. 데이터에 대한 설명 (Data Description)
4. 내 역할 (My Role)
5. 주요 전략 및 구체적인 실행 과정과 결과 (Key Strategies, Execution & Results)
6. 결과 해석 (Interpretation of Results)
7. 의의 (Significance)

---

## 2. 문제 정의 (Problem Definition)
- **거시경제 변동성 위험 증가**: 수입 원자재(철강, 알루미늄 등) 가격과 환율(KRW/USD)의 급격한 변동은 A/S 부품의 조달 원가에 직격타를 주나, 과거의 원가 모니터링은 사후 정산(Post-mortem)에 머물러 있어 선제적 가격 방어가 불가능했습니다.
- **기존 가격 결정 모형의 한계(내생성)**: 가격과 수요가 동시에 결정되는 실무 환경에서 단순 선형회귀(OLS)로 가격 탄력성을 계산할 경우, 관측되지 않은 국가별 특성(Unobserved Heterogeneity)이 오차항에 포함되어 탄력성 계수가 왜곡되는 **내생성(Endogeneity)** 문제가 발생합니다.
- **글로벌 가격 차별화 부재**: 50개 이상의 다양한 글로벌 시장(Developed, Emerging)에 대해 거시 경제력(GDP, 물가수준)을 고려하지 않고 일괄적인 가격 인상을 단행할 경우, 저항(이탈) 리스크가 존재합니다.

## 3. 프로젝트 목적 및 설명
**[목적]**
학부 과정에서 이수한 **'응용계량거시경제학'** 지식과 데이터 분석 역량을 결합하여, 거시 지표 변화에 선제적으로 대응하고 국가별 맞춤 프라이싱(Pricing)이 가능한 **"글로벌 서비스부품 손익 최적화 대시보드"**를 구축하는 것입니다.

**[설명]**
가상의 A/S 부품 판매 데이터에 실제(Real) 거시 경제 API(World Bank 등) 데이터를 접목하여 파이프라인을 구축했습니다. 패널 데이터 분석(Panel Data Analysis), 다변량 시계열 모형(VAR), K-Means 군집 분석이라는 3가지 핵심 계량/통계 모델을 융합하여 실무에 즉각 적용 가능한 대시보드 솔루션을 개발한 통합 데이터 프로젝트입니다.

## 4. 데이터에 대한 설명
모델의 현실성을 높이기 위해 실제 API와 가상 데이터를 융합(Semi-Real Data)하여 사용했습니다.
1. **패널 데이터(Panel Data)**: 5개국 3개 주요 부품에 대한 26개월 치 월간 판매량, 판매가 추이. (거시 경제 쇼크와 내생적 수요 충격 수학적 시뮬레이션 결합)
2. **거시지표 다변량 시계열 데이터**: 2018~2024년 월간 KRW/USD 환율, 철강 수입 물가 지수, 알루미늄 원자재 지수. (자기회귀 AR 과정을 따르도록 생성)
3. **World Bank API 국가 지표**: `wbgapi` 라이브러리를 통해 실시간으로 수집한 전 세계 50개국의 최근 1인당 GDP(Current US$) 및 인플레이션(%) 지표.

## 5. 내 역할 (My Role)
- **Project Manager & Data Scientist**
- **Data Engineering**: Python(pandas) 및 OpenAPI(World Bank)를 활용한 실시간 거시 경제 지표 데이터 크롤링 및 파이프라인(ETL) 구축.
- **Econometric Modeling**: `statsmodels`, `linearmodels`, `scikit-learn`을 활용하여 패널 고정효과(Fixed Effects) 모형, VAR 시계열 모형, K-Means 알고리즘 수학적 설계 및 코딩.
- **Frontend Development**: 분석 엔진의 결과물(계수, IRF 차트, 클러스터링)을 현업 부서가 쉽게 모니터링할 수 있도록 `Streamlit` 과 `Plotly`를 이용해 인터랙티브 대시보드 웹 어플리케이션 풀스택 개발.

## 6. 주요 전략 및 구체적인 실행 과정과 결과

### 전략 1: 국가별 이질성을 통제한 패널 가격탄력성 도출 (Panel Fixed Effects)
- **과정**: 국가별 소득 수준이나 브랜드 충성도 등 보이지 않는 특성이 오차항에 섞이는 내생성을 통제하고자, `PanelOLS` 고정효과 모델을 적용.
- **결과**: 단순 OLS 수행 시 양(+)으로 편향(Bias)되거나 낮게 측정되던 가격탄력성을 정밀하게 교정함. (예: Brake Pad 탄력성 OLS -0.6 -> FE -0.85로 교정)

<p align="center">
  <img src="file:///c:/Users/GAG01/OneDrive/바탕 화면/안티그래비티연습/images/1_fe_vs_ols.png" width="700" alt="OLS vs Panel FE 탄력성 비교">
</p>

### 전략 2: 다변량 시계열(VAR)과 충격반응함수(IRF)를 통한 Time Lag 분석
- **과정**: 환율(KRW/USD)과 철강/알루미늄 지수가 서로 영향을 주고받는 다이나믹스를 포착하기 위해 ADF(단위근 검정)로 안정성을 확인한 후, 최적 시차(Lag=1~2)를 갖는 VAR 모형을 적합.
- **결과**: 충격반응함수(IRF) 도출 결과, 환율 상승(달러 강세) 쇼크가 발생했을 때 철강 수입 원가 지수는 1~2개월 뒤에 가장 크게 상승한다는 인과적 통계 결과를 시각적으로 증명함.

<p align="center">
  <img src="file:///c:/Users/GAG01/OneDrive/바탕 화면/안티그래비티연습/images/2_var_irf.png" width="700" alt="VAR 충격반응함수(IRF)">
</p>

### 전략 3: World Bank 데이터 기반 K-Means 글로벌 마켓 군집화
- **과정**: 가격 최적화 시장을 찾기 위해 World Bank의 1인당 GDP를 Log 스케일 변환하고, 정규화(StandardScaler) 후 K-Means(K=3) 군집 분석 알고리즘 적용. GDP 대비 부품 단가의 선형 회귀 경향선을 그림.
- **결과**: 경제력 대비 부품 가격이 이례적으로 낮게 책정된(Underpriced) 국가들과 높게 책정된(Overpriced) 국가들의 리스트를 자동 색출함.

<p align="center">
  <img src="file:///c:/Users/GAG01/OneDrive/바탕 화면/안티그래비티연습/images/3_cluster_scatter.png" width="800" alt="글로벌 시장 군집 및 Pricing Anomaly">
</p>

## 7. 결과 해석 (Interpretation of Results)
- **골든타임(Golden Time) 확보**: VAR 모형의 결과에 따르면 외환 위기/원자재 값 폭등 시 당장 원가가 오르는 것이 아닙니다. 조달 원가 인상 전 **약 2개월의 시차(Time Lag)** 동안 선제적으로 해외 법인/대리점의 부품 판매가를 인상함으로써 총이익산(Margin) 훼손을 100% 방어할 수 있습니다.
- **타겟팅된 가격 인상 가능**: K-Means와 회귀 잔차(Residual) 분석을 통해 찾아낸 'Underpriced 국가군(GDP가 높음에도 가격이 쌈)'을 타겟으로 가격 인상을 단행할 경우, 판매량 감소(Quantity drop) 저항을 최소화하면서 손익을 극대화할 수 있습니다. 반면 Overpriced 국가군은 가격 저항 이탈(Churn) 방지를 위해 프로모션이 우선되어야 합니다.

## 8. 의의 (Significance)
본 프로젝트는 현대모비스 서비스부품BU의 수익성을 관리하는 '가격관리' 직무에 응용계량거시경제학이라는 **정통 통계/경제학적 접근법을 소프트웨어 기술로 융합**했다는 데 큰 의의가 있습니다.
감이나 과거 경험치, 혹은 엑셀에 의존하던 수동적 사후 원가 정산 방식에서 벗어나, **"데이터 기반의 인과적 추론(Causal Inference) 모형을 통해 선제적 헷징(Hedging) 전략을 제안할 수 있는 데이터 어플리케이션(Streamlit 대시보드)"**을 직접 구현함으로써, 글로벌 서비스부품 사업의 이익경쟁력을 강화할 수 있는 실무적 데이터 역량을 입증했습니다.
