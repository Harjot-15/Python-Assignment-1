def count_words(file_name):
    word_counts = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts

def save_report(word_counts, report_file_name):
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    with open(report_file_name, 'w') as file:
        for word, count in sorted_word_counts:
            file.write(f"{word}: {count}\n")

file_name = "sample.txt"
report_file_name = "report.txt"

word_counts = count_words(file_name)
save_report(word_counts, report_file_name)
