# 라즈베리를 활용한 미니 프로젝트

## 제목: 안전지킴이

## 작품개요
이 작품은 소리 센서, 초음파 센서를 사용하여 거리가 멀어질 때 소리가 나는 장치를 만드는 것을 목표로 합니다. 
이 작품은 물체와의 거리를 감지하기 위해 초음파센서를 사용합니다. 또한 초음파 센서로부터 얻은 값을 기준으로 부저를 제어하여 소리를 동작시킵니다.
코드 실행 중에는 버튼을 사용하여 작품의 동작을 제어할 수 있습니다. 버튼을 한 번 누르면 모든 정지되고, 버튼을 다시 누르면 코드가 동작합니다.
이 작품을 이용하여 범죄 예방과 안전에 주의할 수 있습니다.

## 작품 제작에 사용한 센서와 엑추에이터와 역활
-초음파센서 : 거리를 측정하여 거리에 따라 동작하게 합니다.
-LED: 초음파센서와 같이 동작합니다.
-부저:거리가 가까우면 소리(경고음)가 납니다.
-버튼:작동 중에 동작을 멈출 수 있습니다.
-mqtt:작동 중에 동작을 멈출 때 mqtt화면에서 작동 상황을 알 수 있습니다.
## 완성 작품

### 작품 회로도
![회로](https://github.com/hsy0125/safe/assets/131340824/d43fa3f6-4009-4558-bc62-25755ed0c5bc)

### 작품사진


![완성사진](https://github.com/hsy0125/safe/assets/131340824/0ae14b36-6f34-4f76-9407-0bccb321add0)

## 동작 시나리오 및 예시
거리가 가까우면 소리와 불빛이 나고, 거리가 멀어지면 소리와 불빛이 멈춥니다.
또한 임의로 동작을 제어할 수 있도록 버튼을 사용하여 동작을 제어할 수 있습니다.

방범용을 예시로 하면, 창가에 '안전지킴이'를 설치하여 창가를 통해 외부에서 누군가 집안으로 들어오려는 상황에서 일정 거리 안에 사람이 들어오면 
경고음과 불빛이 같이 작동하여 주변 사람들에게 현재 상황을 알릴 수 있고, 침입자로 부터 자신을 지킬 수 있습니다.
또한 상황이 종료되거나 경고음을 꺼야하는 경우, 버튼을 눌러 임의로 동작을 제어할 수 있습니다. 이 과정이 mqtt에 작품의 동작 상황이 업데이트 됩니다.
## 기대 효과
거리에 따라 소리와 불빛이 나는 것을 모티프로 하여 방범,안전용으로 사용할 수 있습니다. 
거리가 가까워질 때 소리가 나는 경우 위험한 물건 주변에 두어 일정거리 안에 들어오면 소리와 불빛이 나서 주의를 기울일 수 있고,
방범용으로 창가에 두어 바깥에서 강제로 창문을 개방하려 할 시 소리와 불빛이 나서 범죄를 예방할 수 있습니다.
