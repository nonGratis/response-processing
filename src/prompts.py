Q_6 = """Визнач очікувану зарплату кур'єра для доставки продукції з їдальні в 31 корпусі у межах Студмістечка: визнач розмір та одиницю вимірювання (грн/місяць або грн/година); якщо вказана тільки сума без одиниці вимірювання, вважай, що це грн/місяць; якщо іде варіація цін (наприклад, 4-8 тисяч), то залиш цей діапазон; якщо людина вказала нестандартну або незрозумілу відповідь, конвертуй у формат "Важко відповісти"; видаляй зайві слова та символи; використовуй числовий формат для суми (наприклад, "10000 грн в місяць", "200 грн в час").
Приклад 1:
Вхід: 200 грн по годину
Вихід: 200 грн за годину
Приклад 2:
Вхід: 10к
Вихід: 10000 грн за місяць
Приклад 3:
Вхід: хз
Вихід: Важко відповісти"""

Q_11 = """Оброби відповідь так, щоб вона складалася лише з основних слів, розділених комами: вилучи зайві слова та збережи тільки ключові іменники/прикметники; не змінюй власні назви, але інші слова переводи в нижній регістр; якщо відповідь містить лише загальне судження (наприклад, "нормально", "непогано"), не змінюй її; якщо відповідь незрозуміла або містить тільки емоційні вигуки без змісту, вкажи "Важко відповісти".
Приклад 1:
Вхід: тут потрібен ремонт
Вихід: ремонт
Приклад 2:
Вхід: Їжа
Вихід: їжа
Приклад 3:
Вхід: підземелля страху і голоду
Вихід: підземелля
Приклад 4:
Вхід: Чудове обслуговування, вайб столовки, саме те, що ти очікуєш побачити після слів "студентська їдальня"
Вихід: чудове обслуговування, вайб, їдальня"""

Q_18 = """Оброби відповідь так, щоб вона містила тільки список страв, розділений комами: якщо вказана відповідь типу "достатньо", "не знаю", заміни її на "Все влаштовує" або "Важко відповісти"; вилучи зайві слова та описові елементи; форматуй список у називному відмінку, використовуючи загальноприйняті назви страв; якщо відповідь містить помилки у написанні страв, виправ їх.
Приклад 1:
Вхід: достатньо
Вихід: Все влаштовує
Приклад 2:
Вхід: Різні сезонні супи, як в пузатій хаті, шуба
Вихід: супи, шуба
Приклад 3:
Вхід: котлети/м'ясо на пару. запіканки, сочники, тортики, млинці. зробити супи смачнішими
Вихід: котлети, м'ясо на пару, запіканки, сочники, торти, млинці
Приклад 4:
Вхід: не знаю
Вихід: Важко відповісти
Приклад 5:
Вхід: дируни
Вихід: деруни"""
