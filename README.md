## 2019.03 ~ 2019.06 CapstoneDesign Project
# **Python Flask 기반** 머신러닝 구인/구직 양방향 매칭 플랫폼

## Contents
1. Outline
2. Directions for Use
3. Technology Stack
4. Complement

## 1. Outline
- ### 4차 산업시대가 다가옴에따라 기존 정규직의 직장구조가 아닌 프리랜서 및 아르바이트 형태의 직장구조로 변화하는 움직임을 보임. 그에 따라 효과적인 구인/구직 매칭 플랫폼을 만들고자하여 구인/구직자 데이터 기반의 양방향 매칭플랫폼을 제작하고자 한다.

- ### 양방향 매칭 플랫폼이라 함은 구인/구직자가 서비스를 이용한 뒤 상호간 평점부여 시스템을 통해 차후 서비스 이용시 타 이용자의 참고안이 되는 것으로 AirB&B, Uber 등 양방향 매칭 플랫폼의 주요 기능이다.

- ### 구인/구직자 데이터는 자체 데이터베이스 모델링을 통한 임의의 데이터를 사용한다.

- ### 임의의 데이터셋을 사용하기 때문에 정확한 측정, 객관적 판단은 불가능하다.

## 2. Directions for Use
- ### LogIn/SignIn 및 Sesseion/Cookie 기능
- ### LogIn/SignIn 기능은 SignIn 시 데이터 베이스에 등록, LogIn 시 데이터 베이스와 대조 후 해당 회원이 존재하면 LogIn 존재하지 않으면 Redirect의 구조를 가진다.

## LogIn Page
<div>
<img width="1440" alt="login" src="https://user-images.githubusercontent.com/47404600/70523862-3dd31500-1b87-11ea-8366-22a5771f77d7.png">
</div>

- ### SignIn 시 사용자의 ID/PW/Filter 값을 함께 입력하고 데이터 베이스에 저장한다.
- ### 데이터 베이스 모델링 시 고려 했던 구인/구직자의 Filter 종류는 이러하다.
* ### 직종
* ### 기업구분
* ### 근무지역
* ### 급여
* ### 근무시간
* ### 근무날짜
* ### 최종학력

## SignIn Page
<div>
<img width="1440" alt="스크린샷 2019-12-10 오후 7 58 40" src="https://user-images.githubusercontent.com/47404600/70523964-8094ed00-1b87-11ea-8e8a-56febfbf463b.png">
</div>
<div>
<img width="1440" alt="main" src="https://user-images.githubusercontent.com/47404600/70523766-0f553a00-1b87-11ea-8305-a681853e9e59.png">
</div>




