import json
import pandas as pd
import matplotlib.pyplot as plt


def parse_json(json_data):
    operations = list(json_data.keys())

    execution_time_data = {}
    correctness_data = {}
    violation_data = {}
    correction_data = {}

    for op in operations:
        if not json_data[op]['execution time']:
            execution_time_data[op] = ""
        else:
            execution_time_data[op] = json_data[op]['execution time'][0]
        for slot, slot_data in json_data[op]['slot'].items():
            correctness_data[f"{op}_{slot}"] = slot_data['correctness']
            violation_data[f"{op}_{slot}"] = slot_data['violation of biology knowledge']
            correction_data[f"{op}_{slot}"] = slot_data['correction of biology knowledge']

    return execution_time_data, correctness_data, violation_data, correction_data


def save_tables_to_excel(data, title, filename):
    df = pd.DataFrame(data.items(), columns=['Operation_Slot', title])
    df.to_excel("./output/auto/analysis/" + filename + ".xlsx", index=False)


def save_combined_data_to_excel(correctness, violation, correction, filename):
    df_correctness = pd.DataFrame(correctness.items(), columns=['Operation_Slot', 'Correctness'])
    df_violation = pd.DataFrame(violation.items(), columns=['Operation_Slot', 'Violation of Biology Knowledge'])
    df_correction = pd.DataFrame(correction.items(), columns=['Operation_Slot', 'Correction of Biology Knowledge'])

    # Merging the dataframes on Operation_Slot column
    df = df_correctness.merge(df_violation, on='Operation_Slot').merge(df_correction, on='Operation_Slot')

    # Filtering the dataframe to only show rows where Correctness is 'N'
    df_filtered = df[df['Correctness'] == 'N']

    df_filtered.to_excel("./output/auto/analysis/" + filename + ".xlsx", index=False)


def plot_correctness_distribution(correctness):
    # Convert the correctness dictionary values into a list
    values = list(correctness.values())

    # Count the number of 'Y' and 'N' values
    y_count = values.count('Y')
    n_count = values.count('N')

    # Plotting
    labels = ['Y', 'N']
    counts = [y_count, n_count]

    plt.bar(labels, counts, color=['green', 'red'])
    plt.xlabel('Correctness')
    plt.ylabel('Count')
    plt.title('Distribution of Correctness')
    for i, v in enumerate(counts):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10)
    plt.savefig('./output/auto/analysis/correctness_distribution.png')


if __name__ == "__main__":
    with open("./output/auto/reconstructed-labeled-human-modified-isa.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    execution_time_data, correctness_data, violation_data, correction_data = parse_json(data)

    # plot_execution_time(execution_time_data)
    save_combined_data_to_excel(correctness_data, violation_data, correction_data, 'combined_data')
    save_tables_to_excel(execution_time_data, 'Execution Time', 'execution_table')
    plot_correctness_distribution(correctness_data)
