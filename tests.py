from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_not_new_book(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_and_get_genre_for_book(self, collector):
        collector.add_new_book('О дивный новый мир')
        collector.set_book_genre('О дивный новый мир', 'Фантастика')
        assert collector.get_book_genre('О дивный новый мир') == 'Фантастика'

    def test_set_book_genre_set_genre_not_in_list(self, collector):
        collector.add_new_book('О дивный новый мир')
        collector.set_book_genre('О дивный новый мир','Драма')
        assert collector.get_book_genre('О дивный новый мир') == ''

    def test_get_books_with_specific_genre_get_horror(self, collector):
        books_data = [
        ('Кладбище домашних животных', 'Ужасы'),
        ('Дракула', 'Ужасы'),
        ('Двенадцать стульев', 'Комедии'),
        ('История игрушек', 'Мультфильмы')]
        for book, genre in books_data:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_get_dict_with_four_books(self, collector):
        books_data = [
        ('Кладбище домашних животных', 'Ужасы'),
        ('Дракула', 'Ужасы'),
        ('Двенадцать стульев', 'Комедии'),
        ('История игрушек', 'Мультфильмы')]
        for book, genre in books_data:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert len(collector.get_books_genre()) == 4

    def test_get_books_for_children_get_two_children_book(self, collector):
        books_data = [
        ('Кладбище домашних животных', 'Ужасы'),
        ('Дракула', 'Ужасы'),
        ('Двенадцать стульев', 'Комедии'),
        ('История игрушек', 'Мультфильмы')]
        for book, genre in books_data:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collector):
        collector.add_new_book('Кладбище домашних животных')
        collector.add_book_in_favorites('Кладбище домашних животных')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_one_book_twice(self, collector):
        collector.add_new_book('Коллекционер')
        collector.add_book_in_favorites('Коллекционер')
        collector.add_book_in_favorites('Коллекционер')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Понедельник начинается в субботу')
        collector.add_book_in_favorites('Понедельник начинается в субботу')
        collector.delete_book_from_favorites('Понедельник начинается в субботу')
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize('book, genre', [('Оно', 'Ужасы'), ('1984', 'Фантастика')])
    def test_get_book_genre_get_book_genre(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre