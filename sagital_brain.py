import numpy as np

def run_averages(file_input='brain_sample.csv', file_output='brain_average.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagital/horizontal planes

    The result is an average for each sagital/horizontal plane (rows)
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')
    averages = np.mean(planes, axis=0)

    # write it out on my file
    np.savetxt(file_output, averages.reshape((1, averages.shape[0])), fmt='%.1f', delimiter=',')

if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description = "Calculates the average for each sagital-horizontal plane.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default="brain_sample.csv", help="Input CSV file with the results from scikit-brain binning algorithm. If not provided it looks at brain_sample.csv")
    parser.add_argument('--file_output', '-o', default="brain_average.csv", help="Name of the output CSV file. Defaults to brain_average.csv")
    arguments = parser.parse_args()

    run_averages(arguments.file_input, arguments.file_output)
