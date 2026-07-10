## Sprint_4 - Unit-тесты для BooksCollector

- **test_add_new_book_add_not_new_book** - проверка для add_new_book, добавляем НЕ новую книгу и проверяем, что она не добавилась
- **test_set_book_genre_add_and_get_genre_for_book** - проверка для set_book_genre и get_book_genre, добавляем жанр книге и проверяем его
- **test_set_book_genre_set_genre_not_in_list** - проверка для set_book_genre, добавляем жанр НЕ из genre и проверяем, что жанр НЕ добавлен
- **test_get_books_with_specific_genre_get_horror** - проверка для get_books_with_specific_genre, добавляем 4 книги и проверяем количество книг в жанре "Ужасы"
- **test_get_books_genre_get_dict_with_four_books** - проверка для get_book_genre, добавляем 4 книги и проверяем количество книг в коллекции 
- **test_get_books_for_children_get_two_children_book** - проверка для get_books_for_children, добавляем 4 книги и проверяем количество книг в жанрах 'Фантастика', 'Мультфильмы', 'Комедии'
- **test_add_book_in_favorites_add_one_book** - проверка для add_book_in_favorites и get_list_of_favorites_books, добавляем книгу в избранное и проверяем количество книг в избранном
- **test_add_book_in_favorites_add_one_book_twice** - проверка для add_book_in_favorites, добавляем одну книгу в избранное дважды и проверяем, что она НЕ добавлена
- **test_delete_book_from_favorites_delete_one_book** - проверка для delete_book_from_favorites, добавляем книгу в избранное, удаляем книгу из избранного и проверяем количество книг в избранном
- **test_get_book_genre_get_book_genre** - проверка для get_book_genre, добавляем 2 книги в разном жанре и проверяем, что получаем соответствующий жанр для каждой книги