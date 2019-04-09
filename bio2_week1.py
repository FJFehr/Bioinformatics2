# Week1 code
# Fabio Fehr

# Genome assembly is the reverse of this


def Compositionk(Text, k):
    """
    Input:
    Text is a single genome sequence
    k is the length of the kmer

    Output:
    A list of kmers in lexicographic order
    """
    composition_list = []

    # First slice up into a list
    for i in range(len(Text)-k + 1):
        composition_list.append(Text[i:i+k])

    # Sort list making it lexicographic
    composition_list.sort()

    return(composition_list)


def PathToGenome(path):
    """
    Input:
    path is an array of kmers

    Output:
    A single genome joined together by last k-1 symbols
    """

    genome = ""
    k = len(path[0])

    for kmer in path:
        if(genome == ""):
            genome = kmer
        else:
            if(genome[len(genome)-k+1:len(genome)] == kmer[0:k-1]):
                genome = genome[0:len(genome)-k+1] + kmer
            else:
                print("Sozzz doesnt match so nicely")

    return(genome)


def main():

    # #'dataset_197_3.txt'
    with open('dataset_198_3.txt', 'r') as myfile:
        dat = myfile.read().replace('\n', ' ')
    myfile.close()

    dat = dat.split()

    # kmer_array = Compositionk(dat[1], int(dat[0]))

    # with open("Compositionk_output.txt", "w") as text_file:
    #     for kmer in kmer_array:
    #         print(f"{kmer}", file=text_file)

    # print(PathToGenome(dat))


if __name__ == "__main__":
    main()
