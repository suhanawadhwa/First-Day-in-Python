{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOiZjDGwUW48RoJVbbag0c5",
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
        "<a href=\"https://colab.research.google.com/github/suhanawadhwa/First-Day-in-Python/blob/main/studentmanagement.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate_total(marks):\n",
        "    total = sum(marks)\n",
        "    return total"
      ],
      "metadata": {
        "id": "HmcGwICAhsk-"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate_percentage(total):\n",
        "    percentage = total / 5\n",
        "    return percentage"
      ],
      "metadata": {
        "id": "dn3VNjzfiKAF"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
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
        "        return \"Fail\""
      ],
      "metadata": {
        "id": "zbdrWn4RiKim"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
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
        "    else:\n",
        "        print(\"\\nInvalid choice. Please try again.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 547
        },
        "id": "W5CigbZCij3z",
        "outputId": "dd2090ca-1403-4136-b7e6-37cf29176542"
      },
      "execution_count": 18,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n",
            "--- Student Result Management System ---\n",
            "1. Add Student Result\n",
            "2. Display All Results\n",
            "3. Exit\n",
            "Enter your choice (1/2/3): 1\n",
            "Enter student name: A\n",
            "Enter marks for Subject 1: 200000000000000000000000\n",
            "Enter marks for Subject 2: 666666666666\n",
            "Enter marks for Subject 3: 87777777777777777777777\n",
            "Enter marks for Subject 4: 666666666666666666666\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1988813959.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     15\u001b[0m         \u001b[0mmarks\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m6\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m             \u001b[0mmark\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Enter marks for Subject {i}: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     18\u001b[0m             \u001b[0mmarks\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmark\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ex-P7hPli-Ct"
      },
      "execution_count": 16,
      "outputs": []
    }
  ]
}