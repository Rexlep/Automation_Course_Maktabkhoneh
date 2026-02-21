import os


def generate_fake_notes():
    folder_name = "my_notes"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")

    fake_files = {
        "work_report.txt": """
            The quarterly project meeting was held today. We discussed the new software 
            architecture and decided to migrate our servers to AWS. The deadline for 
            the first prototype is next Friday. All team members must submit their 
            progress reports by Wednesday evening.
        """,
        "personal_diary.txt": """
            Today was a wonderful day at the park. I spent hours reading a new book 
            and enjoying the sunshine. I also met an old friend for coffee, and we 
            talked about our childhood memories. It's important to take some time 
            off and relax every once in a while.
        """,
        "finance_update.txt": """
            The stock market showed significant volatility this morning. Investors are 
            concerned about the rising inflation rates and the central bank's next 
            move regarding interest rates. It is recommended to diversify the 
            portfolio and include more gold and stable bonds to minimize risk.
        """,
        "science_news.txt": """
            Astronomers have discovered a new exoplanet that might have liquid water 
            on its surface. This planet orbits a red dwarf star located 40 light-years 
            away from Earth. Using the James Webb Telescope, scientists are now 
            analyzing the atmosphere for signs of oxygen and methane.
        """
    }

    for filename, content in fake_files.items():
        file_path = os.path.join(folder_name, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"File created: {filename}")

    print("\n--- All fake test files are ready in 'my_notes' folder! ---")


if __name__ == "__main__":
    generate_fake_notes()