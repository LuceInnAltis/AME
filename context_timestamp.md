# 📂 프로젝트 히스토리 및 컨텍스트 요약 (Context Timestamp)
**기록 일시 (Timestamp):** 2026-03-01 00:50 KST

## 1. 프로젝트 개요 (Overview)
본 프로젝트는 **현대모비스 서비스부품BU 가격관리 직무 지원**을 목적으로 시작된 **"데이터 기반 선제적 부품 가격관리 및 손익 최적화 대시보드"** 구상 및 개발 과정의 총체입니다. 학부에서 이수한 **'응용계량거시경제학'** 지식을 기초로 하여, 단순 엑셀 기반 OLS나 사후 비용 정산의 실무적 한계를 극복하고 선제적으로 마진 압착(Margin Squeeze)을 헷징하는 솔루션을 증명하기 위해 기획되었습니다.

## 2. 주요 개발 내역 (Key Developments)

### 2.1. 3대 핵심 계량/통계 모델 엔진
1.  **Panel Fixed Effects (고정효과 모형)**: `linearmodels` 라이브러리를 사용, 국가 및 부품별 관측되지 않은 이질성(Unobserved Heterogeneity) 고유 노이즈를 식에서 소거(Demeaning)하여 OLS의 내생성(Endogeneity) 오류를 통제한 '순수 가격 탄력성' 도출 엔진 완성.
2.  **VAR & IRF (다변량 시계열 및 충격반응함수)**: 단위근 검정(ADF)을 통해 가짜 회귀(Spurious Regression)의 늪을 피하고, 환율 쇼크 시 조달 원가(철강 등)가 솟구치는 데까지 걸리는 시차(Lag=1~2개월)를 증명하는 골든타임 알람 엔진 완성.
3.  **K-Means Clustering & 잔차 회귀**: World Bank 오픈 API 연동을 통해 전 세계 국가의 1인당 GDP 및 물가 지표를 수집하고, 경제 체급 대비 부품 단가가 과소평가된 '마진 방어용 인상 타겟(Underpriced)' 국가군을 자동 추출해 내는 머신러닝/방정식 융합 엔진 완성.

### 2.2. Streamlit 통합 BI 개발 (Project 4)
- 백엔드에서 돌아가는 위의 통계/계량 엔진을 비전공 현업 부서도 마우스 클릭과 슬라이더 드래그만으로 조작할 수 있는 **Full-Stack 대시보드 웹 어플리케이션** 런칭 완료.
- 고급 CSS(Glassmorphism) 및 Tooltip 가이드 텍스트를 통해 UX 완성도 극대화.

## 3. SCI-Level 산출물 세트 (V2 Documents)
초기 문서를 완벽하게 심화 고도화(Version 2)하여 아래의 문서들을 산출했습니다.
-   `Project_Report_v2.md`: 5종의 차트가 삽입된 이론 및 실증분석 종합 결과 보고서.
-   `Presentation_Script_v2.md`: PPT 발표 흐름을 위한 12장 분량의 화법 스크립트.
-   `interview_prep_v2.md`: 경제학 논문 인용 및 트러블슈팅(보안 프록시 우회 대신 Synthetic Data 직접 구현, 위장회귀 타파 등) 면접 방어 가이드.
-   `Streamlit_BI_Dashboard_Narrative.md`: 화면별 기획 의도와 Frontend-Backend 분리 렌더링 최적화 스토리를 담은 개발 내러티브 로그.
-   `generate_report_charts.py` 및 `images/` 폴더: OLS vs FE 에러바 차트, 거시 이중축 차트, 다변량 히트맵 등 학술적 퀄리티의 고해상도 시각화 자료 5종.

## 4. Git 형상 관리 (Version Control)
-   방대해진 4개의 프로젝트별 폴더 트리를 포괄하여 `.gitignore`를 세팅하고 체계적인 Git Repository를 초기화했습니다.
-   2026-03-01 자정 무렵, 사용자의 로컬 인증을 통해 `https://github.com/LuceInnAltis/AME.git` 원격 저장소(Remote Repository)의 `main` 브랜치에 초기 모든 기능(Initial Commit)을 성공적으로 Push 완료했습니다.
-   본 `context_timestamp.md` 문서 작성을 끝으로 현재 시점까지의 완전한 아카이빙을 선언합니다.
