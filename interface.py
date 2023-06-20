import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from BinaryTree import *


class BinaryTreeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Tree")

        self.tree = BTree()

        style = ThemedStyle(self.root)
        style.set_theme("yaru")

        self.root.geometry("665x800")

        self.entry_label = ttk.Label(self.root, text="Введите значение узла:")
        self.entry_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.add_button = ttk.Button(self.root, text="Добавить узел", command=self.add_node)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.remove_button = ttk.Button(self.root, text="Удалить узел", command=self.remove_node)
        self.remove_button.grid(row=2, column=1, padx=10, pady=5)

        self.min_button = ttk.Button(self.root, text="Поиск минимального", command=self.find_min)
        self.min_button.grid(row=4, column=0, padx=10, pady=5)

        self.search_button = ttk.Button(self.root, text="Поиск узла", command=self.search_node)
        self.search_button.grid(row=3, column=0, padx=10, pady=5)

        self.max_button = ttk.Button(self.root, text="Поиск максимального", command=self.find_max)
        self.max_button.grid(row=4, column=1, padx=10, pady=5)

        self.display_button = ttk.Button(self.root, text="Отобразить дерево", command=self.display_tree)
        self.display_button.grid(row=3, column=1, padx=10, pady=5)

        self.inorder_button = ttk.Button(self.root, text="Сортировка значений", command=self.inorder_traversal)
        self.inorder_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.find_neighbors_button = ttk.Button(self.root, text="Найти предшественника и последователя",
                                                command=self.find_neighbors)
        self.find_neighbors_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.output_text = tk.Text(self.root, height=50, width=80)
        self.output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def validate_entry(self, value):
        if value.isdigit():
            return True
        return False

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def add_node(self):
        value = self.entry.get()
        if value:
            if not value.isdigit():
                messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")
                return
            value = int(value)
            if self.tree.search(value):
                messagebox.showerror("Ошибка", "Узел уже существует в дереве.")
            else:
                self.tree.add(value)
                messagebox.showinfo("Успешно", "Узел успешно добавлен.")
                self.clear_entry()
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите значение.")

    def remove_node(self):
        value = self.entry.get()
        if value:
            if not value.isdigit():
                messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")
                return
            value = int(value)
            if not self.tree.search(value):
                messagebox.showerror("Ошибка", "Узел не существует в дереве.")
            else:
                self.tree.remove(value)
                messagebox.showinfo("Успешно", "Узел успешно удален.")
                self.clear_entry()
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите значение.")

    def display_tree(self):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self._display_tree(self.tree.root)
        self.output_text.configure(state="disabled")

    def _display_tree(self, node, level=0):
        if node is None:
            return
        else:
            self._display_tree(node.right, level + 1)
            self.output_text.insert(tk.END, '     ' * level + '->' + str(node.value) + '\n')
            self._display_tree(node.left, level + 1)

    def search_node(self):
        value = self.entry.get()
        if value:
            if not value.isdigit():
                messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")
                return
            value = int(value)
            if self.tree.search(value):
                messagebox.showinfo("Успешно", "Узел найден в дереве.")
            else:
                messagebox.showinfo("Не найдено", "Узел не найден в дереве.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите значение.")

    def find_min(self):
        min_node = self.tree.find_min()
        if min_node:
            messagebox.showinfo("Минимальное значение", "Минимальное значение в дереве: " + str(min_node.value))
        else:
            messagebox.showinfo("Дерево пусто", "Дерево пусто.")

    def find_max(self):
        max_node = self.tree.find_max()
        if max_node:
            messagebox.showinfo("Максимальное значение", "Максимальное значение в дереве: " + str(max_node.value))
        else:
            messagebox.showinfo("Дерево пусто", "Дерево пусто.")

    def inorder_traversal(self):
        self.output_text.configure(state="normal")
        values = self.tree.inorder_traversal()
        result = "Отсортированный порядок значений: " + " ".join(str(value) for value in values)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.configure(state="disabled")

    def find_neighbors(self):
        value = self.entry.get()
        if value:
            if not value.isdigit():
                messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")
                return
            value = int(value)
            previous_node, next_node = self.tree.find_neighbors(value)
            if previous_node or next_node:
                messagebox.showinfo("Найти предшественника и последователя",
                                    "Предшественник: {}\nПоследователь: {}".format(
                                        previous_node.value if previous_node else None,
                                        next_node.value if next_node else None))
            else:
                messagebox.showinfo("Найти предшественника и последователя", "Элемент {} не найден.".format(value))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите значение.")


# Создание главного окна
root = tk.Tk()

# Применение стиля и кастомизация окна
style = ThemedStyle(root)
style.set_theme("yaru")
root.configure(bg=style.lookup("TFrame", "background"))

# Создание объекта класса BinaryTreeGUI
binary_tree_gui = BinaryTreeGUI(root)

# Запрет изменения размеров окна
root.resizable(False, False)

# Запуск главного цикла обработки событий
root.mainloop()
