# 📊 [V2] 현대모비스 서비스부품 가격관리 최적화 프로젝트 심층 결과 보고서
**부제: 응용계량거시경제학 모델(Panel FE, VAR)과 실증 데이터를 융합한 선제적 마진 헷징 전략**

---

## 1. 목차 (Table of Contents)
1. 문제 정의 및 이론적 배경 (Problem Definition & Theoretical Background)
2. 프로젝트 목적 (Project Objective)
3. 데이터 파이프라인 및 변수 설명 (Data Pipeline & Variables)
4. 3대 핵심 분석 전략 및 실증 결과 (Key Analytical Strategies & Empirical Results)
   - 4.1. Panel Fixed Effects: 내생성 통제를 통한 순수 가격탄력성 도출
   - 4.2. VAR & IRF: 거시 충격 파급 경로와 Time Lag 분석
   - 4.3. K-Means Clustering & 잔차 분석: 글로벌 Pricing Anomaly 식별
   - 4.4. 이기종 변수 간 다중 상관관계 (Correlation Analysis)
5. 종합 결론 및 비즈니스 인플리케이션 (Conclusion & Business Implications)
6. 참고 문헌 (References)

---

## 2. 문제 정의 및 이론적 배경 (Problem Definition)

### 2.1. 글로벌 거시경제 변동성과 사후적 원가 관리의 한계
포스트 코로나 및 지정학적 리스크 심화로 인해, 국제 원자재 가격(철강, 알루미늄 등)의 슈퍼사이클과 환율(KRW/USD)의 급격한 변동성이 상시화되었습니다. 대외경제정책연구원(KIEP, 2023)의 *'글로벌 공급망 재편과 주요 광물자원 가격 변동'* 보고서에 따르면, 외부 조달 비중이 높은 제조업의 경우 원가 역전 현상이 영업이익률 훼손의 1차적 원인으로 지목됩니다. 하지만 기존 실무의 가격 관리는 원가가 인상된 후 가격표를 수정하는 **사후 정산(Post-mortem) 방식**에 머물러 있어, 수 개월간의 마진 압착(Margin Squeeze)을 방어하지 못하는 기회손실을 낳고 있습니다.

### 2.2. 통계적 한계: OLS의 내생성(Endogeneity) 오류 방치
수요(Q)와 가격(P)은 시장에서 동시에 결정되는 연립방정식적 성격을 띱니다. 그러나 기존 실무에서는 가격 탄력성을 계산할 때 엑셀 기반의 단순 선형회귀(OLS)를 사용합니다. 이 경우 시장마다 특수한 '브랜드 프리미엄'이나 '거시 인프라 수준' 같은 관측 불가한 요인(Unobserved Heterogeneity)이 오차항에 섞이며, 결국 가격 변수가 오차항과 독립이 아니게 되는 **내생성(Endogeneity)**이 발생합니다(Wooldridge, 2010). 이는 가격탄력성을 과소/과대 추정하게 만들어 치명적인 가격 의사결정 오류를 유발합니다.

---

## 3. 프로젝트 목적 및 데이터 파이프라인
**[목적]** 학부 과정에서 이수한 '응용계량거시경제학' 지식을 활용하여, 단순히 과거를 보여주는 BI를 넘어 **미래의 비용 충격을 예측하고 선제적으로 부품 단가를 인상/조정할 수 있는 '수익 방어용 계량경제 대시보드'**를 구축합니다.

**[데이터 설명 및 파이프라인]**
1. **패널 판매 데이터 (Panel Data)**: 글로벌 5개국의 3대 주요 부품(Brake Pad, Oil Filter, Spark Plug) 26개월 시계열 x 개체 데이터. 수요/공급 충격을 수학적 모델링으로 가미한 Synthetic Data.
2. **거시지표 (Macroeconomic Data)**: KRW/USD 환율, 글로벌 철강 지수(pt), 알루미늄 지수.
3. **World Bank 실물 지표 (API)**: `wbgapi`를 호출하여 수집한 50개국의 최근 1인당 GDP(Current US$) 및 소비자물가상승률(Inflation, %). 국가별 경제 체급(Capacity to Pay) 절대 평가 용도.

---

## 4. 3대 핵심 분석 전략 및 실증 결과 (Empirical Results)

본 프로젝트는 총 5가지의 정밀한 시각화와 통계 모델을 통해 결과를 도출했습니다.

### 4.1. Panel Fixed Effects: 내생성 통제를 통한 순수 가격탄력성 도출
*   **전략 원리**: 패널 고정효과(Fixed Effects) 모델 (Arellano, 1987)을 적용하여, 시간에 따라 변하지 않는 국가 고유의 이질성(Unobserved Individual Effects)을 수식적으로 차분(Demeaning)하여 완벽히 통제했습니다.
*   **그래프 해석**:
    *   **X축**: 주요 자동차 A/S 부품군 (Brake Pad, Oil Filter, Spark Plug)
    *   **Y축**: 가격 탄력성 계수 $\epsilon$ (가격 1% 인상 시, 수요가 변화하는 %). 단위: 무차원. 절대값이 작을수록 비탄력적.
    *   **막대 & 에러바(Error Bars) 의미**: 붉은색 막대는 통제되지 않은 일반 회귀(OLS), 푸른색 막대는 노이즈를 걷어낸 고정효과(FE) 모델의 결과입니다. 검은색 에러바(I)는 추정된 계수의 표준오차(Standard Error) 범위로 95% 신뢰구간을 뜻하며, 위에 표기된 `***`는 통계적 유의성(p-value < 0.01)을 지칭합니다.
    *   **인사이트**: OLS는 가격탄력성을 왜곡하게 만듭니다. OLS로는 브레이크 패드가 -0.6 수준으로 덜 탄력적인 줄 알았으나, 고유 특성을 분리한 FE 통계 검증 결과 실제로는 -0.85로 더 민감하게 수요가 반응함을 잡아냈습니다. 이는 OLS 맹신에 따른 **근거 없는 무리한 가격 인상 시도를 차단**하는 강력한 데이터 방어벽이 됩니다.

<p align="center">
  <img src="images\1_fe_vs_ols.png" width="700" alt="OLS vs Panel FE 탄력성 비교">
</p>

### 4.2. VAR & IRF: 거시 충격 파급 경로와 Time Lag 분석 (Sims, 1980)
*   **전략 원리**: 환율, 원자재 지수는 비정상 시계열(Non-stationary)이므로 단순 회귀 시 '가짜 회귀(Spurious Regression)'의 위험이 큽니다. ADF 단위근 검정을 거친 후 다변량 연립방정식 체계인 벡터자기회귀모형(VAR)을 수립하여 내생변수 간의 동태적 영향력을 분석했습니다. 특히 직교화된 충격반응함수(Orthogonalized IRF)를 통해 외생적 충격 스텝을 계산했습니다.
*   **그래프 해석**:
    *   **X축**: 환율 쇼크가 발생한 시점으로부터 경과한 달(Months, Lag). 단위: 월(Month)
    *   **Y축**: 반응 변수(철강, 알루미늄 지수)가 베이스라인 대비 몇 pt 솟구치는지 나타내는 인덱스 단위.
    *   **선(Line) 및 음영의 의미**: 실선은 추정된 점 추정치(Point Estimate), 연하게 깔린 음영은 95% 신뢰구간(Confidence Interval)입니다.
    *   **인사이트**: 달러가 1 표준편차 단위로 강세를 보일 때 (외생적 충격 발생), 철강 지수는 즉각 반응하지 않습니다. 그래프를 보면 **정확히 1개월~2개월 차에 피크(Peak)**를 찍고 하락합니다. 즉, 현장에서는 "환율이 급격히 올랐다는 뉴스랩을 받으면 당장이 아닌 1~2개월의 골든타임 이내에 딜러 네트워크 협의를 통해 공급 단가를 수정해야 수입 원가 역전 마진을 완벽히 방어"할 수 있는 액션 타임라인을 제공합니다.

<p align="center">
  <img src="images\2_var_irf.png" width="800" alt="VAR 충격반응함수(IRF)">
</p>

### 4.3. 거시경제 동태 추세 검증 (Macroeconomic Trend Overlay)
*   **그래프 해석**:
    *   VAR 모형의 직관을 뒷받침하기 위해 과거 시계열을 이중 축(Dual Axis)으로 전개한 플롯입니다.
    *   **왼쪽 Y축(적색)**: KRW/USD 환율 지표 (원화). **오른쪽 Y축(녹색)**: 글로벌 철강 인덱스(pt).
    *   **점선(Dash Line)**: 환율의 3개월 이동평균선(Moving Average)으로 단기 노이즈를 제거한 트렌드 진입 지점을 묘사합니다. 오른쪽 그래프의 강한 상승/하락 파동이 좌측 환율의 굵직한 스윙 주기를 시차를 두고 추종하고 있음이 시각적으로 입증됩니다.

<p align="center">
  <img src="images\4_macro_trends.png" width="700" alt="거시경제 트렌드 이중축 비교">
</p>

### 4.4. K-Means 군집 분석 & 다중 상관성: 글로벌 Pricing Anomaly 도출
*   **전략 원리**: 세계은행의 실시간 데이터를 통해 각국의 지불 여력(Capacity to pay)을 정량화하고, 머신러닝 K-Means 클러스터링 기반의 이상치(Anomaly) 검출 파이프라인을 구축해 일괄적 가격 인상의 위험을 헷징합니다.
*   **다중 상관관계(Heatmap) 의미**: 가격, 분량, 인플레이션, GDP 간의 이변량 상관계수(Pearson)입니다. 예를 들어 GDP와 가격 사이에는 매우 높은 긍정적 상관(+0.80 상회)이 나와야 정상적인 경제 궤도입니다.

<p align="center">
  <img src="images\5_correlation_heatmap.png" width="600" alt="차원별 상관관계 히트맵">
</p>

*   **산점도(Scatter) 군집 그래프 해석**:
    *   **X축**: 대상 국가의 1인당 GDP. (왜도/Skewness 해결을 위해 로그 변환(Log-scale) 진행)
    *   **Y축**: 해당 국가에 현대모비스가 공급 중인 부품의 '평균 판매가(USD)'.
    *   **마커 및 선 의미**: 버블의 크기는 부품 판매 물량(Volume)을 묘사하고, 버블의 색상(Color-map)은 국가별 물가상승률(인플레이션)입니다. 검은 점선은 GDP 수준에 맞추어 기대되는 '글로벌 적정 가격 회귀선(Trend line)'입니다.
    *   **인사이트 (U vs O)**: 회귀선 그래프 아래에 깊숙이 위치한 **'U (Underpriced)' 표적 국가**는 국가 단위의 경제력 대비 우리가 부품을 턱없이 싸게 주고 있는 시장입니다. 이 시장들은 다음 분기에 가장 공격적으로 3~5% 가격을 인상해도 시장 저항(물량 하락)이 현격히 적어 수익을 캐리(Carry)하는 캐시카우 시장으로 즉각 분류할 수 있습니다. 반면 위에 떠 있는 **'O (Overpriced)' 국가군**은 경제 체력 대비 가격 허들이 커서 프로모션이 우선 필요합니다.

<p align="center">
  <img src="images\3_cluster_scatter.png" width="800" alt="글로벌 시장 군집 및 Pricing Anomaly">
</p>

---

## 5. 종합 결론 및 비즈니스 인플리케이션

본 연구 및 시스템 구축 프로젝트는 단순히 멋진 통계 차트를 그리는 데 그치지 않고, "수익 창출(Profit Making)"이라는 비즈니스 관점에서 치명적으로 중요한 3가지 전환점을 제안합니다.

1. **사후 정산 부서에서 선제적 헷징 부서로의 진화**: VAR-IRF 모델의 시계열 시차(Lag) 증명을 통해, 부품 BU의 전략 기획단은 '환율 급등으로부터 조달 단가 상승까지의 2개월'이라는 뚜렷한 "Golden Time"을 정량적으로 입수하게 되었습니다.
2. **"감(Intuition)"이 배제된 진성 탄력성 획득**: 국가/시간 차원의 이질적 노이즈(내생성)를 발라낸 패널 고정효과 계수는, 영업 일선에서 체감하는 불필요한 공포를 제거하고 한 치 오차 없는 수학적 가격 인상 한계선(Threshold)을 제시합니다.
3. **World Bank API 융합을 통한 마진 저항 최적화 타겟팅**: 기업 내부 DB라는 우물 안에서 벗어나 외부의 실물 GDP/물가 API를 다이렉트로 결합함으로써, 가격 인상을 감내할 수 있는(Underpriced) 국가를 레이더망 켜듯 자동 추출하는 지능형 Pricing 맵을 세계 최초로 도출했습니다.

이 분석 파이프라인은 최종적으로 현무 부서 실무진들이 URL 접속 한 번으로 조작 가능한 **Streamlit 기반 인터랙티브 BI(Business Intelligence) 대시보드**로 통합/배포되어, 현대모비스 글로벌 서비스부품 사업 이익률 향상의 강력한 두뇌 역할을 수행할 역량을 입증합니다.

---

## 6. 참고 문헌 (References)
*   Arellano, M. (1987). "Computing robust standard errors for within-groups estimators", Oxford Bulletin of Economics and Statistics.
*   Sims, C. A. (1980). "Macroeconomics and Reality", Econometrica.
*   Wooldridge, J. M. (2010). "Econometric Analysis of Cross Section and Panel Data", MIT Press.
*   대외경제정책연구원(KIEP). (2023). "글로벌 공급망 재편과 주요 광물자원 가격 변동 분석".
*   World Bank Open Data Platform. "GDP per capita (Current US$)", "Inflation, target (Annual %)".
