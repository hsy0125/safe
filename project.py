import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

# LED, 버저, 버튼, TRIG, ECHO에 연결된 핀 번호 설정
LED = 23
buzzer_pin = 12
BUTTON = 24
TRIG_pin = 13
ECHO_pin = 19

#
scale = [261, 294, 329, 349, 392, 440, 493, 523]
notes = [5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5]
durations = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.5, 0.2, 0.2, 0.2, 0.2, 0.5, 0.2]
term = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.3, 0.1]

# MQTT 브로커 정보
broker_address = "broker.emqx.io"
broker_port = 1883
MQTT_SUB_TOPIC = "mobile/hsy/sensing"
MQTT_KEPALIVE_INTERVAL = 60


# MQTT 클라이언트 생성
client = mqtt.Client()

# 버튼 상태를 저장하기 위한 변수
button_pressed = False
GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(TRIG_pin, GPIO.OUT)
GPIO.setup(ECHO_pin, GPIO.IN)

def play_tone(frequency, duration):
    if frequency == 0:
        time.sleep(duration)
        return

    period = 1.0 / frequency
    delay = period / 2
    cycles = int(duration * frequency)

    for _ in range(cycles):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(delay)

def send_mqtt_message(message):
    client = mqtt.Client()
    client.connect(broker_address, 1883, 60)
    client.publish(MQTT_SUB_TOPIC, message)
    client.disconnect()

def button_callback(channel):
    print("버튼이 눌렸습니다.")
    global button_pressed
    button_pressed = not button_pressed
    if button_pressed:
        print("stop")
        send_mqtt_message("stop")
        running = False
    

    else:
        print("running")
        send_mqtt_message("running")
        running = True

GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=button_callback)

try:

    while True:
        # 거리 측정을 위해 TRIG 신호를 10us 동안 발생
        GPIO.output(TRIG_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_pin, GPIO.LOW)

        # 에코 펄스의 시작과 끝 시간을 측정
        start_time = time.time()  # start_time 초기화
        while GPIO.input(ECHO_pin) == 0:
            start_time = time.time()
        while GPIO.input(ECHO_pin) == 1:
            end_time = time.time()

        # 거리 계산
        duration = end_time - start_time
        distance = (duration * 34300) / 2  # 소리의 속도는 초당 343m

        if distance > 10:
            # 거리가 10cm보다 멀어지면 스피커와 LED로 소리와 함께 표시
            GPIO.output(LED, GPIO.HIGH)

            for i in range(len(notes)):
                note = scale[notes[i]-1]
                duration = durations[i]
                play_tone(note, duration)

                time.sleep(term[i])

            GPIO.output(LED, GPIO.LOW)
        else:
            # 거리가 10cm보다 가까워지면 동작 멈춤
            GPIO.output(LED, GPIO.LOW)

           
except KeyboardInterrupt:
    GPIO.cleanup()

