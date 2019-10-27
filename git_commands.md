1. git clone https://bitbucket.ru/quickstart.git - клонировать репо
2. git pull - стянуть изменения
3. git push - отправить изменения на сервер
4. git log - история комитов
   - git log --pretty=oneline - однострочный лог
   - git log --all --pretty=format:"%h %cd %s (%an)" --since='7 days ago' --author=Denis
   - git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
5. git status - индексация изменений
6. git add . - добавить файлы в индекс
7. git commit - закомитить изменения в индексе
8. git checkout git_commands.md - откатить изеннения по файлу
9. git reset --soft HEAD~1 - отмена комита но оставить правки локальные
10. git reset --hard HEAD~1 - отмена комита и правок
11. git revert HEAD -  реверт последнего комита
12. git tag -d v1 - удаление тега
13. git tag v1 - добавление тега
14. git commit --amend  - изменить предыдущий комит
15. git checkout -b style - создание новой ветки и переключение на нее
16. git branch style - созданеи ветки
17. git branch style - переключение на ветку
18. git merge origin master
19. git rebase

