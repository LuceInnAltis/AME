# 📊 프리젠테이션 (PPT) 기획안 및 스크립트 가이드
본 문서는 작성된 `Project_Report.md`를 바탕으로 프레젠테이션용 슬라이드 덱을 구성하기 위한 기획안입니다. (총 10장 권장)

---

## [Slide 1] 표지 (Cover)
- **Title**: 데이터 기반 선제적 부품 가격관리 및 손익 최적화 대시보드 도입 기획안
- **Sub-Title**: 응용계량거시경제학 모델(Panel, VAR)과 실물 지표 연동을 중심으로
- **Name**: [지원자 이름] / 현대모비스 서비스부품BU AS부품 가격관리 직무 지원

---

## [Slide 2] 문제 정의: 왜 가격관리 방식이 변해야 하는가?
- **Headline**: 전통적 가격 관리의 한계 (사후 대응과 내생성의 늪)
- **Bullet View**:
  1. 환율/원자재 변동성 극대화 → 사후 가격 조정 시 **이미 총이익(Margin) 훼손 발생.**
  2. 단순 OLS 기반 탄력성의 오류 → 가격과 수요가 동시 결정되는 **내생성(Endogeneity)** 간과.
  3. 획일적 전략 → 50여 개 글로벌 시장의 체급(GDP)을 고려하지 않는 일괄적 프라이싱 위험성.

---

## [Slide 3] 솔루션 로드맵 및 나의 역할
- **Headline**: 3대 계량분석 모델을 융합한 실시간 의사결정 대시보드 구축
- **Architecture Flow**: 
  - [API Data Fetching] (FRED/World Bank API) ➔ [Econometric Engine] (Panel FE / VAR / K-Means) ➔ [Execution] (Streamlit 대시보드)
- **내 역할 (My Role)**: Data Pipeline 구축, 계량 모형 설계/최적화, 대시보드 풀스택 UI/UX 구현 (100% 단독 수행)

---

## [Slide 4] 전략 1. Panel Fixed Effects: 순수 가격 탄력성 규명
- **Headline**: 국가별 이질성을 통제하여 가격 인상의 정확한 근거 도출
- **Visual**: 
  ![OLS vs Panel FE 탄력성 비교](file:///c:/Users/GAG01/OneDrive/바탕 화면/안티그래비티연습/images/1_fe_vs_ols.png)
- **Script**: "각 시장마다 보이지 않는 특성, 예를 들어 브랜드 선호도나 인프라 환경이 다릅니다. 일반 선형회귀(OLS)는 이 노이즈를 방치해 계수가 왜곡됩니다. 저는 Panel Fixed Effects 모형을 가동하여 국가/시간 고정효과를 발라내고 타격 없는 **순수한 가격 탄력성**을 도출해냈습니다."

---

## [Slide 5] 전략 2. 다변량 시계열(VAR): 환율 쇼크와 원가 전이 시차
- **Headline**: 원가가 오르기 전 선제적 대응을 위한 골든타임 2개월 확보
- **Visual**: 
  ![VAR 충격반응함수(IRF)](file:///c:/Users/GAG01/OneDrive/바탕 화면/안티그래비티연습/images/2_var_irf.png)
- **Script**: "달러 강세가 뜨면 환차손과 원자재 구매단가 인상이 동반됩니다. VAR 모형 적합 후 IRF를 추출해본 결과, 환율 쇼크 시 조달 원가가 튀어 오르기까지 약 **1~2개월의 Lag(시차)**가 있음을 통계적으로 증명했습니다. 현업에서는 이 기간 내에 가격표를 수정해야만 Margin을 온전히 방어할 수 있습니다."

---

## [Slide 6] 전략 3. K-Means 글로벌 마켓 군집화 (World Bank 연동)
- **Headline**: 세계은행의 실물 지표(GDP) 대비 가격 Anomalies 자동 적발
- **Visual**: 
  ![글로벌 시장 군집 및 Pricing Anomaly](file:///c:/Users/GAG01/OneDrive/바탕 화면/안티그래비티연습/images/3_cluster_scatter.png)
- **Script**: "50개국 체급에 맞게 가격을 제대로 받고 있을까요? World Bank 실시간 GDP와 부품 가격을 매핑해 K-Means 분류 후 선형을 그어보았습니다. 저 경향선 한참 아래에 있는 국가들이 보이시나요? 바로 국민 소득 대비 부품을 너무 싸게 팔고 있는 **Target Market** 입니다."

---

## [Slide 7] Output: 글로벌 손익 최적화 통합 대시보드
- **Headline**: 복잡한 계량 모델 결과를 현업이 원클릭으로 통제하는 Streamlit App
- **Visual**: 구현한 4개의 대시보드 탭(KPI, 시뮬레이터, VAR, Scatter) 통합 스크린샷
- **Script**: "아무리 훌륭한 계량경제 모델도 실무자가 쓸 수 없으면 무용지물입니다. 파이썬 Streamlit으로 실시간 API 연동과 시뮬레이터가 탑재된 대시보드를 직접 개발하여 직무 배치 즉시 쓸 수 있는 툴로 구현했습니다."

---

## [Slide 8] 기대 효과 및 의의 (Business Value)
- **Headline**: 사후 정산 부서에서 **데이터 기반의 선제적 헷징(Hedging) 부서**로
- **Value Points**:
  - `Time-to-Action`: VAR-IRF를 통한 골든타임 사전 확정
  - `Maximized Margin`: 내생성을 배제한 탄력성 기반 정밀한 핀포인트 가격 인상 
  - `Targeted Promotion`: K-Means 기반 저항 리스크 국가 사전 식별

---

## [Slide 9] Conclusion & My Vision
- **Headline**: 거시경제를 아는 데이터 과학자, 모비스 수익성의 수호자가 되겠습니다.
- **Script**: "경제학 이론에 코딩이라는 무기를 달았습니다. 현대모비스 A/S 가격관리팀에서 외부적 충격(거시위기)을 내부 수익으로 방어해내는 실무형 데이터 전문가로 활약하겠습니다. 감사합니다."

---

## [Slide 10] Q&A (방어 전략)
*(발표자는 이 장을 띄우고 `interview_prep.md` 숙지 내용을 토대로 질의응답 대응)*
- Q. World Bank API는 왜 썼나? -> "시장 체급을 반영하지 않는 내부 데이터의 맹점을 깨기 위함입니다."
- Q. 단위근 검정(ADF)은 왜 했나? -> "최근 거시 지표는 가짜 회귀(Spurious Regression) 위험이 커서 시계열 안정성 확인이 학술적/실무적으로 필수이기 때문입니다."
