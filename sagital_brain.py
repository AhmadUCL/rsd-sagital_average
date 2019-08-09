
def run_averages():
    # Open the file to analyse
    with open('brain_sample.csv', 'r') as myfile:
            # Create a plane list to keep a list per row
            planes = []
            for line in myfile.readlines():
                planes.append([int(x) for x in line.split("\n")[0].split(',')])

    # Create new list to save the averages per each plane
    # The number of steps coronal planes may change in the future
    coronal_planes = 20
    sagital_averages = []
    for i in range(20):
        total = 0
        for j in range(coronal_planes):
            total = total + int(planes[i][j])
        sagital_averages.append(str(total/coronal_planes))

    # write it out on my file
    with open('brain_average.csv', 'w') as myoutput:
             myoutput.write(','.join(sagital_averages) +  '\n')

if __name__ == "__main__":
    run_averages()
