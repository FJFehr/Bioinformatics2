# Week1 code
# Fabio Fehr

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
    for i in range(len(Text)-k +1):
        composition_list.append(Text[i:i+k])

    #Sort list making it lexicographic
    composition_list.sort()

    return(composition_list)

def main():

    print(Compositionk("CAATCCAAC", 5))

if __name__ == "__main__":
    main()
