== Как учить машины 🤖 : простые примеры про ML.

* Материалы онлайн:
https://github.com/alex-bochkarev/ML-SMTB-2022[Github repo] (или см.
папку курса)
* Дискорд: `co05-как-учить-машины-простые-примеры-про-ml`

=== [ 𝚺 ] Аннотация

Методы машинного обучения (``Machine Learning'' — ML) используются в
самых разных областях. Распознавание лиц людей и номеров автомобилей,
рекомендации фильмов и книг, предсказание вероятности аварии, развития
опасных заболеваний или оптимальной пространственной структуры белка
(см. отдельный курс в секции ``Биология'').

На этом курсе мы на примерах попытаемся разобраться, как работают
некоторые базовые ML-модели: линейная регрессия, логистическая регрессия
и нейросеть (кто заказывал ``глубинное обучение''?) В каждом случае мы
обсудим минимально необходимый кусочек теории, интуитивно поймем как это
работает, и построим маленькую, но осмысленную с практической точки
зрения модель такого типа.

*Что нужно:* Знание школьной математики старших классов (понятие
``производной'') поможет, но не необходимо: мы постараемся обсудить ``на
пальцах'' все необходимые термины и понятия. Примеры будут реализованы
на языке Python, но навыки программирования по сути тоже не требуются,
достаточно желания читать уже написанный код.

*Основная цель курса:* составить общее интуитивное понимание этих
подходов и добавить смелости глубже разбираться с темой, если это
потребуется в будущем.

*Количество занятий:* 4

=== [ ☰ ] Стуктура курса

Курс состоит из трех тем, соответствующих трем типам моделей (список
далеко не исчерпывающий, конечно).

==== ① Линейная регрессия

Предсказание линейных (ну почти) взаимосвязей

* 📝 *практика:* эксперты и модели, цены на вино.
* 📓 *jupyter notebook:* `T1-linear-reg.ipynb`
https://github.com/alex-bochkarev/ML-SMTB-2022/blob/main/T1-linear-reg.ipynb[(GitHub)]
https://nbviewer.jupyter.org/github/alex-bochkarev/ML-SMTB-2022/blob/main/T1-linear-reg.ipynb[(nbviewer)]
https://colab.research.google.com/github/alex-bochkarev/ML-SMTB-2022/blob/main/T1-linear-reg.ipynb[(colab)]
* 💾 *данные:* link:./wine-data.csv[wine-data.csv]

==== ② Логистическая регрессия

Что делать, если нужно предсказать факт (вопрос на ``да / нет'')?

* 📝 *практика:* риски сердечных заболеваний, Framingham Risk Score.
* 📓 *jupyter notebook:* `T2-logistic-reg.ipynb`
https://github.com/alex-bochkarev/ML-SMTB-2022/blob/main/T2-logistic-reg.ipynb[(GitHub)]
https://nbviewer.jupyter.org/github/alex-bochkarev/ML-SMTB-2022/blob/main/T2-logistic-reg.ipynb[(nbviewer)]
https://colab.research.google.com/github/alex-bochkarev/ML-SMTB-2022/blob/main/T2-logistic-reg.ipynb[(colab)]
* 💾 *данные:* link:./CHD-data.csv[CHD-data.csv] — см., например,
https://www.kaggle.com/datasets/5d359d0259d8325396aff882594f0c59e5e0c3da49c5bf4df3c23121109b4955[Kaggle]

==== ③ Нейросеть (два занятия)

Нелинейные взаимосвязи. Нейросеть – пример на трех узлах.

* 📝 *практика:* распознавание рукописного текста (с помощью скотча,
старых тряпок, и `torch`).
* 📓 *jupyter notebooks:*
** Простая нейросеть: `T3-NN.ipynb`
https://github.com/alex-bochkarev/ML-SMTB-2022/blob/main/T3-NN.ipynb[(GitHub)]
https://nbviewer.jupyter.org/github/alex-bochkarev/ML-SMTB-2022/blob/main/T3-NN.ipynb[(nbviewer)]
https://colab.research.google.com/github/alex-bochkarev/ML-SMTB-2022/blob/main/T3-NN.ipynb[(colab)]
** Рукописный текст / MNIST dataset: `T4-NN-MNIST.ipynb`
https://github.com/alex-bochkarev/ML-SMTB-2022/blob/main/T4-NN-MNIST.ipynb[(GitHub)]
https://nbviewer.jupyter.org/github/alex-bochkarev/ML-SMTB-2022/blob/main/T4-NN-MNIST.ipynb[(nbviewer)]
https://colab.research.google.com/github/alex-bochkarev/ML-SMTB-2022/blob/main/T4-NN-MNIST.ipynb[(colab)]
* 💾 *данные:* мы скачали автоматически с помощью PyTorch
(`torchvision`).

=== 👓 Что еще почитать?

Очень, очень широкая тема. Чтобы я тут не написал, будет мало 🤷. Но я
попробую субъективно выделить, например:

* По Линейной Алгебре (Linear Algebra):
** Gilbert Strang, Linear Algebra:
https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/[MiT
OCW Course]
** _может быть_ лекции МФТИ:
https://www.youtube.com/results?search_query=%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F+%D0%B0%D0%BB%D0%B3%D0%B5%D0%B1%D1%80%D0%B0+%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8+%D0%BC%D1%84%D1%82%D0%B8+[поиск
в YouTube]
* Про теорвер, можно посмотреть например ссылки к моему прошлогоднему
курсу https://github.com/alex-bochkarev/zpsh-21-probs[тут]. Но вообще
можно попробовать смотреть разные курсы (coursera / EdX / stepik / etc)
и читать разные книжки, чтобы посмотреть, что зайдет именно вам.
* В целом про аналитику, мне очень понравился курс
https://www.edx.org/course/the-analytics-edge[Analytics Edge] на EdX
(см. также книгу The Analytics Edge by Bertsimas, O’Hair, and
Pulleyblank). Там достаточно коротко и понятно описаны примеры про вино
и про Framingham Risc Score (и есть много других!)
* В обсуждении возникла пару ссылок на курсы по мат. анализу (спасибо,
Alexey Matyash!):
** https://youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr[красивый]
** https://www.khanacademy.org/math/ap-calculus-ab[подробный]
* Наконец, про ML в целом. Я очень рекомендую вдумчиво почитать на эту
тему отзывы и обсуждения на Reddit, Quora и т.п. и посмотреть, что
понравится именно вам. Мне понравились некоторые курсы на Coursera /
EdX, но, к сожалению, сейчас доступны не все. Можно попробовать начать с
классики, Andrew Ng
(https://www.coursera.org/specializations/machine-learning-introduction?[Coursera]
или даже
https://www.youtube.com/watch?v=jGwO_UgTS7I&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU[CS229]).
В целом, всякие сертификаты, с моей точки зрения, достаточно бесполезны;
а вот любые проекты (когда вы сами делаете что-то осмылсенное, даже если
очень простое) – это очень здорово. Добавляет много понимания и даже код
на Github, который можно потом кому-то показать.
