# 2022 동계 모각소 @ Ajou Univ

I'm Learning From.. 

1. https://docs.flutter.dev/ (Flutter 공식 Document)

2. https://firebase.google.com/docs?authuser=0&hl=ko (FireBase 공식 Document)

3. https://firebase.flutter.dev/ (Flutter-Firebase 연동 공식 Document)
 
4. https://nomadcoders.co/dart-for-beginners (노마드코더 Dart 기초 강의)

5. https://nomadcoders.co/flutter-for-beginners (노마드코더 Flutter 기초 강의)


## Introduce 
해당 레포지터리는 아주대학교에서 진행하는 2022 동계 모각소 학습을 위한 레포지터리입니다.

~(+ 1/24 Dart 언어 학습 및 Flutter 기본 학습에 대한 내용은 해당 레포에도 TIL로 작성했었으나.. merge를 잘못해서 날려버렸습니다...ㅠㅠ)~

1/24일 이전의 TIL 내용(Dart 기본, Flutter 기본)은 Tistory 팀블로그에 업로드 되어있습니다.

구글 GDSC에 참여하기 위한 앱 (VaryRecycle)을 개발하면서 배운 점들은 해당 레포지터리에서 기록해나갈 예정입니다.

## TIL

### January

- [23.01.07](https://flutter-winter.tistory.com/10)

Today I Learned :

1. MaterialApp 쓰는법

2. Scaffold를 이용해서 화면 나누기

3. Container의 child를 통해 공간을 분리하고 요소 구성하기

4. 텍스트, 이미지 등 위젯 활용법

---

- [23.01.10](https://flutter-winter.tistory.com/12)

Today I Learned :

1. Dart에서의 변수 선언, Null safety, final과 const형 변수의 차이점

2. Dart의 자료형, collection if & for, String interpolation

3. Dart는 모든 변수나 자료형, 함수도 Object로 관리되는 완전완전 객체지향 언어임 자바랑 비슷한게 많아서 쉽게 이해할수 있었음

---

- [23.01.11](https://flutter-winter.tistory.com/17)

Today I Learned :

1. positinal parameter와 named parameter의 차이

2. named parameter에 대한 null safety 방지법(초깃값 설정 or 선언시 required).

3. QQ Operator와 Typedef를 통한 자료형 관리

--- 

- [23.01.12](https://flutter-winter.tistory.com/18)

Today I Learned :

1. 생성자와 positional,named argument , 생성자 overloading

2. enum class와 mixin class

3. 부모 생성자에 변수값 넘기는 법 (Player(..) : super(name))

--- 

- [23.01.18](https://flutter-winter.tistory.com/24)

Today I Learned :

1. custermized widget 생성법, stateless widget에 여러 개 만들어보기

2. MainAxis, CrossAxis 생각하며 차곡차곡 화면 채우기

3. 각 위젯 안에 들어가는 값들이 named parameter로써 쓰인다는 것 (생성자에서 {required this.}로 처리)

---

- [23.01.19](https://flutter-winter.tistory.com/25)

Today I Learned :

1. Stateful Widget 구성 방법 및 상태변수를 관리하는 메소드들

2. MatreialApp에서 home 이전에 theme을 지정해서 쓸 색깔 등을 한군데 저장해두는 방법

3. Flexible 박스, Expanded 위젯

---

- [23.01.22](https://flutter-winter.tistory.com/28)

Today I Learned :

1. Firebase colabs의 firebase-get-to-know lab2 실습 (https://firebase.google.com/codelabs/firebase-get-to-know-flutter?hl=ko#0)

2. 예제 코드를 통한 어플리케이션 인증 기능, 데이터베이스 읽기,쓰기 기능 따라서 구현해보기

---

- [23.01.24](https://github.com/h-wi/flutter-webtoonapp-demo)
~TIL 레포를 날려먹은 원흉~

Today I Learned :

1. git 협업 관리 방법 (branch,merge 등) 

2. [VaryRecycle 앱 UI 구성 (모각소 3차 모임)](http://ovenapp.io/project/u5OHOgHQjLy5iWE6GTd27oWjdQiDbPVl)

2. 노마트코더 웹툰 앱에 이메일 인증 & 구글 인증 기능 추가

---

- [23.01.25](https://github.com/h-wi/2022-Winter-TIL/tree/main/0125)

Today I Learned :

1. Navigator를 통한 Page Routing 방법

2. firebase_storage package를 이용해서 Firebase 서버에 이미지 파일 업로드

3. await 호출과 네비게이터로 빌드 시에 if (!mounted) return; 추가해서 동기화하기

---

- [23.01.31](https://github.com/h-wi/2022-Winter-TIL/tree/main/0131)

Today I Learned : 

1. [TensorFlow Lite를 통한 커스텀 객체 감지 모델 배포 방법, 구글 클라우드 dataset 사용](https://developers.google.com/codelabs/tflite-object-detection-android?continue=https%3A%2F%2Fdevelopers.google.com%2Flearn%2Fpathways%2Fgoing-further-object-detection%3Fhl%3Den&hl=ko#0)

2. 플러터의 MainActivity.kt 파일을 수정해서 프로젝트에도 적용해볼려고 했지만 플러터는 안드로이드 파일만 수정이 불가능했다..

![image](https://user-images.githubusercontent.com/108285793/216071587-7b83b18d-20ae-4476-9120-10b63d9ee9fd.png)

## Febraury

- [23.02.01](https://github.com/h-wi/2022-Winter-TIL/tree/main/0201)

Today I Learned :

1. tflite_model_make API를 통해서 커스텀 객체 감지 모델 빌드(커스텀 dataset 사용)

2. epoch 조정 및 batch size 조정을 통한 모델 성능 개선

3. 코드랩 어플리케이션에 배포

![image](https://user-images.githubusercontent.com/108285793/216071419-7f8515b3-f0ef-4bc9-9829-d1657ed8acd5.png)

---

- [23.02.03](https://github.com/h-wi/2022-Winter-TIL/tree/main/0203)

Today I Learned :

1. [Roboflow에서 custom dataset(캔) 제작](https://app.roboflow.com/varyrecycle/can-cwf4o/overview)

<img width="881" alt="image" src="https://user-images.githubusercontent.com/108285793/216554771-3e4b6e98-77f9-481e-bc23-d25fc18550b2.png">

2. YOLOv5를 통해 object detection 모델(캔) 빌드

3. [Flask API에서 이미지 데이터 preprocessing](https://github.com/h-wi/vary-recycle-flask-server)

---

- [23.02.04](https://github.com/h-wi/2022-Winter-TIL/tree/main/0204)
Today I Learned :

1. Flask API에서 Tensorflow YOLO 모델 아웃풋 decoding하기 (https://github.com/OxAN0N/vary-recycle-flask-server/pull/3/commits/07a2371385a1d1051e5fd532abe6365e9d044ed2)

2. 플라스틱 재활용 감지 모델 4개의 class에 대해서 빌드하기 (뚜껑, 라벨, 내용물, 찌그러트림)

---

- [23.02.07](https://github.com/h-wi/2022-Winter-TIL/tree/main/0207)

Today I Learned :

1. 유리병, 종이 및 박스 Object Detect Model 빌드 -> https://app.roboflow.com/varyrecycle

2. 각 모델에 대한 Inference 결과 후처리 코드 작성

---
