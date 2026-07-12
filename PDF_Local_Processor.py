{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/anokhina-rgb/Google-Colabs/blob/main/PDF_Local_Processor.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import tkinter as tk\n",
        "from tkinter import filedialog, messagebox, simpledialog\n",
        "from pypdf import PdfReader, PdfWriter\n",
        "\n",
        "def process_pdf_locally():\n",
        "    root = tk.Tk()\n",
        "    root.withdraw()  # Ховаємо технічне вікно\n",
        "\n",
        "    # 1. Обираємо файл\n",
        "    input_filename = filedialog.askopenfilename(title=\"Виберіть PDF файл\", filetypes=[(\"PDF files\", \"*.pdf\")])\n",
        "    if not input_filename:\n",
        "        return\n",
        "\n",
        "    # 2. Вводимо всі діапазони разом\n",
        "    ranges_input = simpledialog.askstring(\"Діапазони\", \"Введіть діапазони через кому (наприклад: 1-3, 66-69):\")\n",
        "    if not ranges_input:\n",
        "        return\n",
        "\n",
        "    try:\n",
        "        reader = PdfReader(input_filename)\n",
        "        writer = PdfWriter()\n",
        "        total_pages = len(reader.pages)\n",
        "\n",
        "        # Обробка введеного рядка\n",
        "        ranges = ranges_input.split(',')\n",
        "        for r in ranges:\n",
        "            start, end = map(int, r.strip().split('-'))\n",
        "\n",
        "            # Перевірка меж\n",
        "            if 1 <= start <= end <= total_pages:\n",
        "                # Додаємо сторінки методом, що не викликає помилок аргументів\n",
        "                for i in range(start - 1, end):\n",
        "                    writer.add_page(reader.pages[i])\n",
        "            else:\n",
        "                messagebox.showerror(\"Помилка\", f\"Діапазон {r} виходить за межі (1-{total_pages})!\")\n",
        "                return\n",
        "\n",
        "        # 3. Зберігаємо результат\n",
        "        output_filename = filedialog.asksaveasfilename(title=\"Зберегти як\", defaultextension=\".pdf\", filetypes=[(\"PDF files\", \"*.pdf\")])\n",
        "        if output_filename:\n",
        "            with open(output_filename, \"wb\") as output_file:\n",
        "                writer.write(output_file)\n",
        "            messagebox.showinfo(\"Успіх\", \"PDF готовий!\")\n",
        "\n",
        "    except Exception as e:\n",
        "        messagebox.showerror(\"Помилка\", f\"Щось пішло не так: {e}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    process_pdf_locally()"
      ],
      "outputs": [],
      "execution_count": null,
      "metadata": {
        "id": "FcpGVs3ERzGG"
      }
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}