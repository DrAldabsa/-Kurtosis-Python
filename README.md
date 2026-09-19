# 📊 تحليل التفرطح (Kurtosis) باستخدام Python

## 📌 نظرة عامة

يهدف هذا المشروع إلى توضيح مفهوم **التفرطح (Kurtosis)** بصورة عملية وبصرية باستخدام لغة البرمجة **Python**.

يقوم البرنامج بإنشاء ثلاثة أنواع مختلفة من التوزيعات ومقارنتها:

1. **التوزيع الطبيعي (Mesokurtic)**
2. **التوزيع ذو الذيول الثقيلة (Leptokurtic)**
3. **التوزيع ذو الذيول الخفيفة (Platykurtic)**

ثم يقوم البرنامج بحساب:

* التفرطح الزائد (Excess Kurtosis)
* وعرض شكل التوزيعات باستخدام منحنيات الكثافة (KDE)

والهدف الأساسي هو توضيح الفرق بين التوزيعات من حيث **سلوك الذيول واحتمالية ظهور القيم البعيدة عن مركز التوزيع**.

---

# 🎯 هدف المشروع

عند تحليل البيانات، لا يكفي معرفة:

* المتوسط (Mean)
* الانحراف المعياري (Standard Deviation)

بل من المهم أيضًا فهم **شكل توزيع البيانات**.

ومن المقاييس المهمة في هذا السياق:

**Kurtosis**

والذي يساعد في وصف خصائص توزيع البيانات، وخصوصًا ما يتعلق بالذيول والقيم المتطرفة مقارنة بالتوزيع المرجعي.

يمكن تمثيل الفكرة بصورة مبسطة:

```text
البيانات
   ↓
شكل التوزيع
   ↓
Skewness + Kurtosis
   ↓
فهم الذيول والقيم المتطرفة
   ↓
اختيار وتفسير التحليل الإحصائي
```

---

# 📚 ما هو Kurtosis؟

**Kurtosis** هو مقياس إحصائي مرتبط بالعزم المركزي الرابع للتوزيع.

في هذا المشروع يتم استخدام تعريف **Fisher** من خلال:

```python
kurtosis(data, fisher=True)
```

وبهذا التعريف يتم طرح 3 من قيمة Kurtosis التقليدية، بحيث يصبح:

```text
Normal Distribution ≈ 0
```

بدلًا من:

```text
Normal Distribution ≈ 3
```

وهو الفرق بين **Excess Kurtosis** و **Pearson Kurtosis**.

---

# 📊 أنواع التوزيعات المستخدمة

يتم في المشروع مقارنة ثلاثة أنواع:

| النوع           | المصطلح     | Excess Kurtosis | الخاصية العامة            |
| --------------- | ----------- | --------------: | ------------------------- |
| التوزيع الطبيعي | Mesokurtic  |             ≈ 0 | مرجع للمقارنة             |
| الذيول الثقيلة  | Leptokurtic |             > 0 | احتمال أكبر للقيم البعيدة |
| الذيول الخفيفة  | Platykurtic |             < 0 | ذيول أخف مقارنة بالطبيعي  |

> **ملاحظة مهمة:** لا ينبغي تفسير Kurtosis ببساطة على أنه "ارتفاع أو انخفاض قمة التوزيع" فقط. في هذا السياق، التركيز الأهم هو **سلوك الذيول واحتمالية القيم المتطرفة**.

---

# 1️⃣ التوزيع الطبيعي — Mesokurtic

يتم إنشاء التوزيع الطبيعي باستخدام:

```python
normal_data = np.random.normal(
    loc=0,
    scale=1,
    size=n_samples
)
```

حيث:

* `loc = 0` يمثل المتوسط.
* `scale = 1` يمثل الانحراف المعياري.
* `n_samples = 1000` يمثل عدد المشاهدات.

وبالنسبة إلى **Excess Kurtosis**، نتوقع أن تكون القيمة قريبة من:

```text
0
```

---

# 2️⃣ التوزيع ذو الذيول الثقيلة — Leptokurtic

يستخدم البرنامج **Student's t-distribution**:

```python
heavy_tail_data = np.random.standard_t(
    df=3,
    size=n_samples
)
```

ويتميز توزيع Student's t بدرجات حرية منخفضة بذيول أثقل من التوزيع الطبيعي.

في هذا المثال:

```text
df = 3
```

وبالتالي نتوقع:

```text
Excess Kurtosis > 0
```

أي أن البيانات تحتوي على احتمالية أكبر نسبيًا لظهور قيم بعيدة عن مركز التوزيع.

---

# 3️⃣ التوزيع ذو الذيول الخفيفة — Platykurtic

يستخدم البرنامج **Uniform Distribution**:

```python
light_tail_data = np.random.uniform(
    low=-2,
    high=2,
    size=n_samples
)
```

يمتلك التوزيع المنتظم نطاقًا محدودًا للقيم، مما يجعله مناسبًا لتوضيح حالة ذات **ذيول أخف من التوزيع الطبيعي**.

وبالتالي نتوقع:

```text
Excess Kurtosis < 0
```

---

# 🔢 تثبيت النتائج

في بداية البرنامج يتم استخدام:

```python
np.random.seed(42)
```

والهدف هو ضمان إمكانية إعادة إنتاج البيانات والنتائج عند تشغيل البرنامج مرة أخرى.

كما يتم تحديد حجم العينة:

```python
n_samples = 1000
```

أي أن كل توزيع يحتوي على:

```text
1000 observations
```

---

# 🗃️ تخزين البيانات باستخدام Pandas

يقوم البرنامج بتجميع التوزيعات الثلاثة داخل:

```python
DataFrame
```

باستخدام:

```python
df = pd.DataFrame({
    'Normal_Distribution': normal_data,
    'Heavy_Tail_Leptokurtic': heavy_tail_data,
    'Light_Tail_Platykurtic': light_tail_data
})
```

وبذلك تصبح البيانات منظمة في ثلاثة أعمدة:

| العمود                   | المحتوى                   |
| ------------------------ | ------------------------- |
| `Normal_Distribution`    | التوزيع الطبيعي           |
| `Heavy_Tail_Leptokurtic` | التوزيع ذو الذيول الثقيلة |
| `Light_Tail_Platykurtic` | التوزيع ذو الذيول الخفيفة |

---

# 💾 تصدير البيانات إلى CSV

الكود يحتوي أيضًا على إمكانية حفظ البيانات في ملف CSV.

يتم ذلك باستخدام:

```python
df.to_csv(
    csv_filename,
    index=False
)
```

وفي الكود الحالي تم تعطيل هذه الأوامر باستخدام `#`.

يمكن تفعيلها إذا أردت حفظ البيانات:

```python
csv_filename = 'kurtosis_example_data.csv'

df.to_csv(
    csv_filename,
    index=False
)

print(
    f"Data saved to '{csv_filename}'"
)
```

وسيتم إنشاء الملف:

```text
kurtosis_example_data.csv
```

---

# 📐 حساب Excess Kurtosis

يتم حساب التفرطح باستخدام:

```python
kurtosis(
    data,
    fisher=True
)
```

وفي الكود:

```python
kurt_normal = kurtosis(
    df['Normal_Distribution'],
    fisher=True
)

kurt_heavy = kurtosis(
    df['Heavy_Tail_Leptokurtic'],
    fisher=True
)

kurt_light = kurtosis(
    df['Light_Tail_Platykurtic'],
    fisher=True
)
```

---

# 🔬 لماذا استخدمنا `fisher=True`؟

هذه نقطة مهمة جدًا.

في SciPy:

```python
fisher=True
```

يعني استخدام تعريف Fisher، بحيث تكون قيمة التوزيع الطبيعي المرجعية:

```text
Excess Kurtosis = 0
```

بينما:

```python
fisher=False
```

يعطي **Pearson Kurtosis**، وفي هذه الحالة تكون القيمة المرجعية للتوزيع الطبيعي:

```text
Pearson Kurtosis = 3
```

وهذا موثق في توثيق SciPy الرسمي.

لذلك يجب عدم الخلط بين:

```text
Kurtosis ≈ 3
```

و:

```text
Excess Kurtosis ≈ 0
```

فهما طريقتان مختلفتان للتعبير عن المقياس نفسه.

---

# 📊 تفسير قيم Excess Kurtosis

يمكن تفسير القيم بصورة عامة كالتالي:

### Mesokurtic

```text
Excess Kurtosis ≈ 0
```

يمثل التوزيع الطبيعي كمرجع.

---

### Leptokurtic

```text
Excess Kurtosis > 0
```

يشير إلى ذيول أثقل مقارنة بالتوزيع الطبيعي المرجعي.

وهذا يعني أن القيم البعيدة عن مركز التوزيع يمكن أن تكون أكثر حضورًا نسبيًا.

---

### Platykurtic

```text
Excess Kurtosis < 0
```

يشير إلى ذيول أخف مقارنة بالتوزيع الطبيعي المرجعي.

---

# 📈 تصور مبسط

يمكن تصور الأنواع الثلاثة كالتالي:

```text
Mesokurtic
     Normal
       │
       ▼
    ╭─────╮
  ╭─╯     ╰─╮
─╯           ╰─
```

```text
Leptokurtic
  Heavy Tails

      ╭─╮
     ╭╯ ╰╮
────╯     ╰────
  ↑         ↑
ذيول أثقل
```

```text
Platykurtic
   Light Tails

    ╭──────╮
───╯        ╰───
```

> الرسومات أعلاه توضيحية فقط؛ الشكل الحقيقي يعتمد على البيانات وحجم العينة.

---

# 📉 استخدام KDE

يستخدم البرنامج:

```python
sns.kdeplot()
```

لرسم منحنى الكثافة الاحتمالية لكل توزيع.

يتم رسم التوزيعات الثلاثة على شكل واحد حتى يمكن مقارنتها بصريًا.

الفكرة الأساسية هي مقارنة:

```text
Normal
   ↓
Heavy Tails
   ↓
Light Tails
```

مع التركيز على اختلاف شكل الذيول.

---

# 🔎 تحديد نطاق الرسم

يستخدم البرنامج:

```python
plt.xlim(-5, 5)
```

وذلك للتركيز على نطاق محدد من القيم وإظهار الفروق بين التوزيعات بصورة أوضح.

ولكن يجب الانتباه إلى أن هذه الخطوة **تقص جزءًا من التوزيع خارج هذا النطاق بصريًا**.

أي أن البيانات نفسها لا يتم حذفها؛ وإنما يتم فقط تحديد حدود المحور السيني في الرسم.

وهذا مهم جدًا عند تفسير التوزيع ذي الذيول الثقيلة.

---

# 🎨 تنسيق الرسم

يتم إعطاء الرسم عنوانًا:

```python
plt.title(
    'Visualizing Kurtosis: Tails and Peakedness',
    fontsize=14,
    fontweight='bold'
)
```

كما تتم إضافة:

* تسمية المحور X
* تسمية المحور Y
* Legend
* Grid
* حجم مناسب للشكل

وأخيرًا:

```python
plt.tight_layout()
```

لتحسين ترتيب العناصر داخل الشكل.

---

# 🧠 Kurtosis والـ Outliers

من أهم النقاط التعليمية في هذا المشروع أن **الذيول الثقيلة ترتبط بوجود احتمالية أكبر نسبيًا للقيم البعيدة عن مركز التوزيع**.

لذلك يمكن أن يكون Kurtosis مفيدًا عند فحص البيانات التي تحتوي على:

* قيم متطرفة
* أحداث نادرة
* توزيعات ذات ذيول طويلة
* بيانات مالية
* بيانات بيئية
* بيانات زراعية
* بيانات هيدرولوجية

لكن يجب عدم استخدام Kurtosis وحده للحكم على وجود Outliers.

يفضل دمجه مع:

```text
Histogram
+
Boxplot
+
Descriptive Statistics
+
Domain Knowledge
```

---

# 🌾 مثال تطبيقي في البحوث الزراعية

لنفترض أن الباحث قام بقياس **محتوى رطوبة التربة** في عدد كبير من المواقع.

قد تكون معظم القياسات قريبة من المتوسط، ولكن توجد بعض المواقع التي تحتوي على قيم بعيدة جدًا بسبب:

* اختلاف نوع التربة
* ظروف الري
* الأمطار الغزيرة
* الصرف
* اختلاف الموقع
* خصائص التربة الفيزيائية

إذا ظهرت ذيول ثقيلة في توزيع البيانات، فقد تكون هناك قيم بعيدة عن مركز التوزيع بصورة أكبر مما نتوقعه من توزيع طبيعي مرجعي.

وهنا يمكن للباحث دراسة:

```text
Distribution
      ↓
Kurtosis
      ↓
Tail Behavior
      ↓
Extreme Observations
      ↓
Scientific Interpretation
```

---

# 🔬 الفرق بين Skewness و Kurtosis

هذا المشروع يمكن استخدامه مع مشروع **Skewness Analysis** لفهم مقياسين مختلفين:

| المقياس      | ماذا يصف؟                            |
| ------------ | ------------------------------------ |
| **Skewness** | اتجاه وعدم تماثل التوزيع             |
| **Kurtosis** | خصائص الذيول مقارنة بالتوزيع المرجعي |

بصورة مبسطة:

```text
Skewness
    ↓
هل التوزيع يميل إلى اليمين أم اليسار؟
```

بينما:

```text
Kurtosis
    ↓
ماذا يحدث في الذيول؟
```

ولهذا فإن استخدام المقياسين معًا يعطي وصفًا أكثر شمولًا لشكل البيانات.

---

# 📁 هيكل المشروع المقترح

يمكن تنظيم المشروع على GitHub بالشكل التالي:

```text
kurtosis-analysis/
│
├── kurtosis_analysis.py
├── kurtosis_example_data.csv
├── kurtosis_distribution.png
├── requirements.txt
└── README.md
```

---

# 📦 المكتبات المطلوبة

يمكن إنشاء ملف:

```text
requirements.txt
```

ويحتوي على:

```text
numpy
pandas
matplotlib
seaborn
scipy
```

ثم تثبيتها باستخدام:

```bash
pip install -r requirements.txt
```

---

# 🚀 طريقة التشغيل

احفظ البرنامج باسم:

```text
kurtosis_analysis.py
```

ثم شغله:

```bash
python kurtosis_analysis.py
```

سيقوم البرنامج بـ:

1. توليد البيانات.
2. إنشاء DataFrame.
3. حساب Excess Kurtosis.
4. طباعة النتائج.
5. رسم منحنيات KDE.
6. مقارنة التوزيعات الثلاثة.

---

# 💻 الكود الكامل

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis

# 1. Set seed for reproducibility
np.random.seed(42)

n_samples = 1000

# Normal Distribution
normal_data = np.random.normal(
    loc=0,
    scale=1,
    size=n_samples
)

# Heavy-Tailed Distribution
heavy_tail_data = np.random.standard_t(
    df=3,
    size=n_samples
)

# Light-Tailed Distribution
light_tail_data = np.random.uniform(
    low=-2,
    high=2,
    size=n_samples
)

# 2. Create DataFrame
df = pd.DataFrame({
    'Normal_Distribution': normal_data,
    'Heavy_Tail_Leptokurtic': heavy_tail_data,
    'Light_Tail_Platykurtic': light_tail_data
})

# 3. Calculate Excess Kurtosis
kurt_normal = kurtosis(
    df['Normal_Distribution'],
    fisher=True
)

kurt_heavy = kurtosis(
    df['Heavy_Tail_Leptokurtic'],
    fisher=True
)

kurt_light = kurtosis(
    df['Light_Tail_Platykurtic'],
    fisher=True
)

print("\nCalculated Excess Kurtosis:")
print(
    f"Normal Distribution: "
    f"{kurt_normal:.4f}"
)

print(
    f"Heavy Tail: "
    f"{kurt_heavy:.4f}"
)

print(
    f"Light Tail: "
    f"{kurt_light:.4f}"
)

# 4. Plot distributions
plt.figure(figsize=(12, 6))

sns.kdeplot(
    df['Normal_Distribution'],
    label='Normal / Mesokurtic',
    linewidth=2.5
)

sns.kdeplot(
    df['Heavy_Tail_Leptokurtic'],
    label='Heavy-Tailed / Leptokurtic',
    linewidth=2.5
)

sns.kdeplot(
    df['Light_Tail_Platykurtic'],
    label='Light-Tailed / Platykurtic',
    linewidth=2.5
)

plt.title(
    'Visualizing Kurtosis: Tails and Peakedness',
    fontsize=14,
    fontweight='bold'
)

plt.xlabel('Values')
plt.ylabel('Density')

plt.xlim(-5, 5)

plt.legend(fontsize=10)

plt.grid(
    axis='y',
    alpha=0.3
)

plt.tight_layout()

plt.show()
```

---

# 📌 أهم النتائج التعليمية

من خلال هذا المشروع يمكن فهم النقاط التالية:

* **Kurtosis** مرتبط بالعزم المركزي الرابع للتوزيع.
* `fisher=True` يعطي **Excess Kurtosis**.
* التوزيع الطبيعي له Excess Kurtosis يساوي تقريبًا `0`.
* التوزيع ذو الذيول الثقيلة يكون عادةً ذا Excess Kurtosis موجب.
* التوزيع ذو الذيول الخفيفة يكون عادةً ذا Excess Kurtosis سالب.
* Leptokurtic يرتبط بذيول أثقل مقارنة بالتوزيع الطبيعي المرجعي.
* Platykurtic يرتبط بذيول أخف مقارنة بالتوزيع الطبيعي المرجعي.
* لا ينبغي تفسير Kurtosis على أنه مجرد مقياس لـ"ارتفاع القمة".
* لا يكفي Kurtosis وحده لتحديد أو إثبات وجود Outliers.
* استخدام الرسم البياني مع الإحصاءات الوصفية يعطي فهمًا أفضل للبيانات.

---

# 👨‍🔬 الفئة المستهدفة

هذا المشروع مناسب لـ:

* الباحثين الزراعيين
* الباحثين في علوم التربة والمياه
* الباحثين في العلوم البيئية
* طلبة الماجستير والدكتوراه
* طلبة الإحصاء
* الباحثين الذين يتعلمون Python
* المهتمين بالتحليل الاستكشافي للبيانات (EDA)

---

# 👤 المؤلف

**د. عبدالكريم سحاب الدبسا**

باحث في العلوم الزراعية والبيئية
إدارة الأراضي والموارد المائية | التحسس النائي | Python | R | التحليل الإحصائي

---

# 📚 المراجع والتوثيق

* [SciPy – Kurtosis Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html)
* [NumPy Documentation](https://numpy.org/doc/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib Documentation](https://matplotlib.org/stable/)
* [Seaborn Documentation](https://seaborn.pydata.org/)

---

# 📄 الترخيص

يمكن استخدام هذا المشروع وتعديله لأغراض تعليمية وبحثية، مع الإشارة إلى المؤلف الأصلي عند إعادة استخدام الكود أو تطويره.
