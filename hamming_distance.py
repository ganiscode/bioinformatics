from kmer import kmers


def hamming_distance(seq1, haystack):
    """
     - CASE 1: the second parameter is a string, return the hamming distance between the two strings.
       Efficiency: O(n) n being the size of the strings
     - CASE 2: the second parameter is a bigger string than the first one, this will return the minimum hamming distance
    it finds between the first k-mer, and all the possible k-mers in the second string.
       Efficiency: O(kn) n being the size of the first string, k the size of the second
     - CASE 3: the second parameter is an list of strings, it will return the sum of the hamming distances between seq1
     and each string in the list.
       Efficiency: O(kns) n being the size of the first string, k the size of the second and s the size of the list

    :param seq1: the first string
    :param haystack: the second string (can be bigger than the first one), or an list of these strings
    :return: the hamming distance (case 1), the minimum hamming distance (case 2) or the sum of minimum hamming
    distances (case 3)
    """

    def hamming_distance_same_size(s1, s2):
        """
        Compute the hamming distance of two strings that have the same size.

        Efficiency: O(k) with k being the size of the strings

        :param s1: the first string
        :param s2: the second string
        :return: the hamming distance between the two strings
        """
        distance = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:  # We compare the two string char-by-char
                distance += 1
        return distance

    def hamming_distance_two_strings(s1, s2):
        """
        Compute the hamming distance between two strings.
        If the second string if bigger than the first one, this will return the minimum hamming distance it finds
        between the first k-mer, and all the possible k-mers in the second string.

        Efficiency: O(nk) with k being the size of the first string, and n the size of the second

        :param s1: the first string
        :param s2: the second string
        :return:
        """
        k = len(s1)

        min_distance = float("inf")

        # We compute the hamming distance between seq1 and s for s being all the possibles strings the same size as seq1
        # in seq2.
        for s in kmers(s2, k):
            distance = hamming_distance_same_size(s1, s)
            if distance < min_distance:  # If the current newly found distance is lower than the minimum we have now
                min_distance = distance
        return min_distance

    if isinstance(haystack, list):  # If the second parameters is a list
        return sum([hamming_distance_two_strings(seq1, s) for s in haystack])
    else:  # If it is a string
        return hamming_distance_two_strings(seq1, haystack)


def __main__():
    s1 = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
    s2 = "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"
    print(hamming_distance(s1, s2))


if __name__ == '__main__':
    __main__()
