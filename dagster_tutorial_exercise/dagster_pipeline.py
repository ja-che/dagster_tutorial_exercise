'''Dagster pipeline
'''
from dagster import job

from load_data import download_cereals
from compute_kpi import compute_kpi
from plot_kpi import display_results


@job
def my_pipeline():
    '''Dagster pipeline'''
    data = download_cereals()

    # Integrate preprocessed_data and create_models ops
    # create_models takes as input the output of preprocessed_data

    # Complete compute_kpi arguments
    most_calories, most_protein, accuracy = compute_kpi(data)
    _ = display_results(most_calories, most_protein, accuracy)


def main():
    '''Main function'''
    my_pipeline.execute_in_process()


if __name__ == '__main__':
    main()
