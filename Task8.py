import sqlite3

conn = sqlite3.connect("articles.db")
cursor = conn.cursor()


def view_article(name):
    cursor.execute(f"SELECT content FROM articles WHERE title = '{name}'")
    rows = cursor.fetchall()
    index = 0

    if rows:
        for row in rows:
            print(f'{row[index]}\n')
            index += 1

        return f'There is articles'
    else:
        return f'There is no such articles'


def delete_article(name):
    cursor.execute(f"DELETE FROM articles WHERE title = '{name}'")

    return f'Article "{name}" was deleted'


def creat_article(a_title, a_content, a_author):
    cursor.execute(f'''
        INSERT INTO articles (title, content, author) VALUES (?, ?, ?)
    ''', (a_title, a_content, a_author))
    return f'Article "{a_title}" was added'


def main():
    while True:
        print('''Menu:
1. Create new article
2. Delete a article
3. View a content of article
4. Exit
        ''')

        choice = int(input("Enter your choice(1-3): "))

        match choice:
            case 1:
                article_title = input("Enter title of article: ")
                article_content = input("Enter content of article: ")
                article_author = input("Enter author of article: ")
                print(creat_article(article_title, article_content, article_author))
            case 2:
                article_title = input("Enter title of article: ")
                print(delete_article(article_title))
            case 3:
                article_title = input("Enter title of article: ")
                print(view_article(article_title))
            case 4:
                print("Programm is ending...")
                break
            case _:
                print("Invalid choice")



if __name__ == "__main__":
    main()

cursor.close()
