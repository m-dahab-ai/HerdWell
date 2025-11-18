مشروع مراقبة صحّة وسلوك الماشية باستخدام إنترنت الأشياء والذكاء الاصطناعي
Smart Livestock Health & Behavior Intelligence - SLHBI
يهدف هذا المشروع إلى إنشاء نظام ذكي شامل لمتابعة **صحة الماشية (Livestock Health) وتحليل سلوكها (Behavior Analysis) في الزمن الحقيقي، وذلك باستخدام منصة ESP32 لالتقاط البيانات الحيوية، وبروتوكول MQTT لنقلها، وبيئة InfluxDB لتخزينها، إضافة إلى Node-RED لمعالجة البيانات، ولوحة تحكّم Grafana لعرض المؤشرات الصحية والسلوكية بصورة بصرية واضحة.
كما يتضمن المشروع وحدة ذكاء اصطناعي مبنية بلغة Python لتحليل الأنماط Predictive Analytics والتنبؤ بالحالات غير الطبيعية قبل حدوثها.

الأهداف الرئيسية للمشروع
* مراقبة درجة حرارة الحيوان ونشاطه وحالته الحيوية على مدار الساعة.
* جمع البيانات بشكل مستمر عبر ESP32 وإرسالها إلى السحابة.
* إنشاء Dashboards تفاعلية في Grafana لمتابعة كل العوامل لحظة بلحظة.
* استخدام الذكاء الاصطناعي للتنبؤ بالسلوك غير الطبيعي أو المشكلات الصحية.
* تمكين المزارع من اتخاذ قرارات سريعة ودقيقة لتحسين صحة القطيع.

 المكوّنات التقنية
Hardware:
  * ESP32 + DHT22 + Accelerometer + MQTT Client
Software & Cloud:
  * Node-RED) Data Pipeline)
  * InfluxDB)  Time-series Database)
  * Grafana)  Dashboards)
  * Python) AI Models – Anomaly Detection)
Communication:

  * MQTT over Wi-Fi
لوحة التحكّم في Grafana
تم إنشاء عدة Panels لحظية لعرض:
* درجة الحرارة Temperature
* مستوى النشاط Activity
* معدل الحركة Acceleration
* مؤشر الصحة العام Health Index

تنبيهات المشاكل  Alerts 

تعمل كل Panel بتحديث كل 3 ثوانٍ، وتوفر رؤية فورية للحالة الصحية لكل حيوان.

الذكاء الاصطناعي في المشروع
تقوم وحدة Python بتحليل 3 عناصر:
1. اكتشاف الحالات الشاذة (Anomaly Detection)
2. توقع الانخفاض أو الارتفاع غير الطبيعي في درجة الحرارة
3. تصنيف السلوك (سكون – نشاط – نشاط زائد)
هذا يساعد في التنبؤ المبكر بأي مشكلة صحية قبل تفاقمها.
السيناريو التطبيقي
1. الحيوان يرسل بياناته عبر حساس الحرارة + حساس الحركة.
2. ESP32 يرسل البيانات إلى MQTT Broker.
3. Node-RED يعالج البيانات ويرسلها إلى InfluxDB.
4. Grafana تعرض البيانات في واجهة تفاعلية فورية.
5. Python AI يقوم بتحليل البيانات وإصدار تقارير وتنبيهات.

هيكلة المشروع في GitHub

```
SLHBI/
│── hardware/
│   └── esp32_code/
│── nodered/
│   └── flows.json
│── influxdb/
│   └── setup_instructions.md
│── grafana/
│   └── dashboards.json
│── ai/
│   ├── anomaly_detection.py
│   └── requirements.txt
│── docs/
│   ├── system_architecture.png
│   └── README_assets/
│── README.md
```
القيمة المضافة
* مشروع واقعي قابل للتطبيق في المزارع.
* يقدّم رؤية متقدمة لتحسين رفاه الحيوان والإنتاجية.
* يجمع بين IoT + AI + Cloud + Real-time Dashboards في حل واحد.
