{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNvVFT9riik0FS6pYhgKDWM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/suhanawadhwa/First-Day-in-Python/blob/main/stdtmanagement.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Student Result Management System\n",
        "# Concepts Used: Variables, Input/Output, If-Else, Loops, Functions, Lists, Dictionaries\n",
        "\n",
        "# Function to calculate total marks\n",
        "def calculate_total(marks):\n",
        "    total = sum(marks)\n",
        "    return total\n",
        "\n",
        "\n",
        "# Function to calculate percentage\n",
        "def calculate_percentage(total):\n",
        "    percentage = total / 5\n",
        "    return percentage\n",
        "\n",
        "\n",
        "# Function to calculate grade\n",
        "def calculate_grade(percentage):\n",
        "    if percentage >= 75:\n",
        "        return \"A\"\n",
        "    elif percentage >= 60:\n",
        "        return \"B\"\n",
        "    elif percentage >= 50:\n",
        "        return \"C\"\n",
        "    elif percentage >= 40:\n",
        "        return \"D\"\n",
        "    else:\n",
        "        return \"Fail\"\n",
        "\n",
        "\n",
        "# Dictionary to store student records\n",
        "students = {}\n",
        "\n",
        "while True:\n",
        "    print(\"\\n--- Student Result Management System ---\")\n",
        "    print(\"1. Add Student Result\")\n",
        "    print(\"2. Display All Results\")\n",
        "    print(\"3. Exit\")\n",
        "\n",
        "    choice = input(\"Enter your choice (1/2/3): \")\n",
        "\n",
        "    if choice == \"1\":\n",
        "        name = input(\"Enter student name: \")\n",
        "\n",
        "        marks = []\n",
        "        for i in range(1, 6):\n",
        "            mark = float(input(f\"Enter marks for Subject {i}: \"))\n",
        "            marks.append(mark)\n",
        "\n",
        "        total = calculate_total(marks)\n",
        "        percentage = calculate_percentage(total)\n",
        "        grade = calculate_grade(percentage)\n",
        "\n",
        "        # Store student data in dictionary\n",
        "        students[name] = {\n",
        "            \"Marks\": marks,\n",
        "            \"Total\": total,\n",
        "            \"Percentage\": percentage,\n",
        "            \"Grade\": grade\n",
        "        }\n",
        "\n",
        "        print(\"\\nStudent result added successfully!\")\n",
        "\n",
        "    elif choice == \"2\":\n",
        "        if not students:\n",
        "            print(\"\\nNo student records available.\")\n",
        "        else:\n",
        "            print(\"\\n--- Student Result Summary ---\")\n",
        "            for name, details in students.items():\n",
        "                print(\"\\nStudent Name:\", name)\n",
        "                print(\"Marks:\", details[\"Marks\"])\n",
        "                print(\"Total Marks:\", details[\"Total\"])\n",
        "                print(\"Percentage:\", details[\"Percentage\"])\n",
        "                print(\"Grade:\", details[\"Grade\"])\n",
        "\n",
        "    elif choice == \"3\":\n",
        "        print(\"\\nThank you for using the system.\")\n",
        "        break\n",
        "\n",
        "    else:\n",
        "        print(\"\\nInvalid choice. Please try again.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ex-P7hPli-Ct",
        "outputId": "d092d5a4-401c-4052-bc45-b6a02665c686"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- Student Result Management System ---\n",
            "1. Add Student Result\n",
            "2. Display All Results\n",
            "3. Exit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "dYAxwMuUm716"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}