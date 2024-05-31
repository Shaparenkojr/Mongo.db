## Миграция базы данных себе на хост:
1. Зайдите в директорию mongo
2. В файле load.js в переменную current_dir запишите полный путь к директории. Например:
``` javascript
let current_dir = "D:\\mongo_task\\mongodb"
```
3. Зайдите в mongosh
4. Выполните:
```bash
load("<path-to-load.js>")
```