# العربية الحازمة | Assertive Arabic

## خط عربي تفاعلي (Assertive Arabic Font)
إن حذف علامات التشكيل من النصوص العربية المطبوعة يؤدي إلى فقدان معلومات صوتية جوهرية تنقل دلالات دقيقة ونوايا الكاتب، مما يزيل أي غموض محتمل. كما أن استخدام التشكيل يسهل فهم اللغة، ويوضح كيف يمكن للجذور المكونة من ثلاثة حروف ساكنة أن تكتسب معانٍ ودلالات مختلفة باختلاف الحركات (علامات التشكيل).

يُتيح هذا الخط استخدام صيغة "المبني للمعلوم" بوضوح (مما يساعد في معالجة مشكلة الإفراط في استخدام "المبني للمجهول" التي تعاني منها وسائل الإعلام الرقمية العربية المعاصرة)، كما يسمح بتوظيف علامات التشكيل بدقة عند الحاجة؛ فيحافظ على سهولة القراءة للمتعلمين وللأشخاص الذين يعتمدون على الجانب الصوتي للغة، بينما يجنب المتحدثين الأصليين ازدحام النص بالعلامات. إن هذا الوضوح الإضافي ذو قيمة كبيرة، ولم يعد يشكل عبئاً تقنياً كما كان الحال في المطابع قديماً.

وعليه، فإن هذا الخط يحتفظ بعلامات التشكيل، لكنه يعرضها بدرجة شفافية منخفضة (باهتة)، مما يتيح لك استخدامها في أي برنامج على حاسوبك يدعم خطوط "TrueType".

---

## Assertive Arabic Font
Dropping diacritics from typed Arabic removes spoken phonetic information that conveys nuance and intentions of the writer, removing ambiguity. It also makes the language easier to understand and helps people understand how 3-letter consonant constructs can get different nuances and meanings with different vowel diacritics. 

It allows for accountability to be conveyed with active voice (solving the passive voice crisis plaguing modern digital Arabic media), and allows for tashkeel to be used with nuance when necessary, preserving readablity for phonetic speakers and learners, while removing clutter from the display for native speakers. The additional clarity is worthwhile and no longer a hassle for printing presses. 

Thus this font preserves diacritics (Tashkeel), but renders them in the font as low opacity so you can use them with any program on your computer that supports True Type Fonts.

---

## مثال على صياغة مباشرة وحازمة
* **صيغة المبني للمعلوم:** تناول المقالُ الموضوعَ بأصالةٍ وأناقةٍ.
* **صيغة المبني للمجهول:** عولج الموضوعُ بطريقةٍ معقدةٍ تفتقر إلى الوضوح.

تحتوي هذه المكتبة على نص برمجي (script) بلغة "بايثون 3" (Python 3)، يقوم بمعالجة ملف خط عربي كامل وفصل علامات التشكيل عن الحروف الأساسية. وينتج عن ذلك ملف يحمل الاسم `fullArabic.ttf`، تظهر فيه علامات التشكيل (كالفتحة، والكسرة، والضمة، والسكون، وغيرها) بدرجة شفافية أقل (أي أنها تبدو باهتة).

إذا أردت تعديل درجة الشفافية، يمكنك تغيير قيمة `alpha` في السطر 21: **`faded_black = Color(blue=0, green=0, red=0, alpha=35)`**

بعد ذلك، وأثناء تواجدك داخل المجلد `assertivearabic`، قم بتنفيذ الأمر التالي:

```
python3 buildarabicfont.py NotoNaskhArabic-Regular.ttf fullArabic.ttf
```

يمكنك أيضاً استبدال `NotoNaskhArabic-Regular.ttf` بأي خط عربي آخر من نوع (TrueType) ترغب في استخدامه، كما يمكنك اختيار اسم للملف الناتج يكون مناسباً لك. لقد استخدمتُ الاسم `fullArabic.ttf`، لكن قد تفضل استخدام اسم مختلف؛ وذلك لتتمكن من تمييز الخطوط والأنماط المتنوعة بسهولة من خلال أسمائها.

زيادة قيمة `alpha` تجعل علامات التشكيل تبدو أكثر قتامةً أو أكثر بروزاً (أقل شفافية)؛ علماً بأن الحد الأقصى لهذه القيمة هو 255.
وعلى العكس من ذلك، فإن تقليل هذه القيمة يجعل علامات التشكيل أكثر شفافية (أبهت)؛ علماً بأن الحد الأدنى لهذه القيمة هو 0.

لقد اخترت القيمة `35` كبداية؛ فهي تضمن عدم ازدحام النص بصرياً، مع الحفاظ في الوقت ذاته على وضوح العلامات وقابليتها للقراءة عند الحاجة إليها.

---

## Assertive Text Example
* **Active Voice:** اِسْتَهْدَفَ المَقَالُ المَوْضُوعَ بِأَصَالَةٍ وَأَنَاقَةٍ.
* **Passive Voice:** اُسْتُهْدِفَ المَوْضُوعُ بِتَعْقِيدٍ دُونَ وُضُوحٍ.

This library contains a python3 script that takes a complete Arabic language font and separates the diacritics symbols from the glyphs. The resulting fullArabic.ttf file renders diacritics (fatah, kesrah, dummah, sukoon, etc) in a lower opacity transparency.

If you want to change the value of the opacity update the alpha in line 21: **`faded_black = Color(blue=0, green=0, red=0, alpha=35)`**

Then while inside the `assertivearabic` directory, run 

```
python3 buildarabicfont.py NotoNaskhArabic-Regular.ttf fullArabic.ttf
```

You can also replace `NotoNaskhArabic-Regular.ttf` with any other arabic truetype font you would like to use, and use an output name that makes sense to you. I used `fullArabic.ttf` but you may want to use something different to obviously keep track of different fonts and styles with different names.

Making the alpha value higher results in a darker/more solid opacity for diacritics. Maximum alpha value is 255.
Conversely, making the value lower results in a clearer opacity for diacritics. Minimum alpha value is 0. 

I chose an alpha value of `35` to start because it's clear enough that it's not cluttered but still legible for oen to see and read if needed.

