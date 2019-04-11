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


def Overlap(Patterns):
    """
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns).
    """

    # Define the placeholder
    pattern_dict = {}

    # Set up all our keys
    for pattern in Patterns:
        pattern_dict[pattern] = []

    for pattern in Patterns:

        for pattern_key in pattern_dict:
            if (pattern_key[1:] == pattern[:-1]):
                pattern_dict[pattern_key].append(pattern)

    return(pattern_dict)


def main():

    # #'dataset_198_10.txt'
    with open('dataset_198_10.txt', 'r') as myfile:
        dat = myfile.read().replace('\n', ' ')
    myfile.close()

    dat = dat.split()

    # kmer_array = Compositionk(dat[1], int(dat[0]))

    # with open("Compositionk_output.txt", "w") as text_file:
    #     for kmer in kmer_array:
    #         print(f"{kmer}", file=text_file)

    # print(PathToGenome(dat))

    overlap_dict = Overlap(dat)

    # for key, val in overlap_dict.items():
    #     if(val != []):
    #         print(key, " => ", val)

    # for item in overlap_dict:
    #     if overlap_dict[item]:
    #         print(item + " => " + overlap_dict[item][0])

    #print(overlap_dict)

    with open("Overlap_output.txt", "w") as text_file:
        for key, val in overlap_dict.items():
            if (val != []):
                val_str = val[0]
                if len(val) > 1:
                    for i in range(len(val)-1):
                        val_str = val_str + ", " + val[i+1]

                string_temp = key + " -> " + val_str
                print(f"{string_temp}", file=text_file)


if __name__ == "__main__":
    main()
