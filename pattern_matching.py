from hamming_distance import hamming_distance


def pattern_matching(genome, sequence):
    """
    Return a set of starting positions where sequence is found in genome
    :param genome: the genome
    :param sequence: the sequence
    :return: a ascending sorted list of positions
    """
    result = set()
    index = genome.find(sequence)
    while index != -1:
        result.add(index)
        index = genome.find(sequence, index + 1)
    return sorted(result)


def general_pattern_matching(genome, sequence, distance):
    """
    Return a set of starting positions where sequence is found in genome
    :param genome: the genome
    :param sequence: the sequence
    :return: a ascending sorted list of positions
    """
    result = set()
    len_sequence = len(sequence)
    max = len(genome) - len_sequence
    for i in range(0, max + 1):
        if hamming_distance(genome[i:i + len_sequence], sequence) <= distance:
            result.add(i)
    return sorted(result)


def __main__():
    genome = open("genome.txt", "r").read()
    pattern = "CTTGATCAT"

    print(' '.join(str(x) for x in pattern_matching(genome, pattern)))


def __main2__():
    genome = "ATAGCCCTTTAACAACCTAGTGGGTGCTAGTAGGCCCGGTATGATACCCTACCAGATCCCATCGGACTGCTATGACTCGCCCGGTGGATGTATATCACCACGTCAGGTTCGGTGTTAATCTAAATGTTAAGACACAGTCTATTAGGCACGAGTAAACCAACACACACTCTGAAGTCTCTTGTTGAGTTTGCAAGGCCTGTACGGGTTATACTAGCGAACTCACTTATCTCGGTTGCGGTTTAGTAATAATCCCGGGTTTTCTCACTTAATCCCAGGAGGAATGCCTGCCGCCCGTACGGTGTCGTGGCGAGAACCCTCGCGCTGTTTGTCCTTCGTTCACGAGCTGCGAATACGATCCTCTAGTTGGGCGAAGACTATATCATTGAGGCGATCTACTCAAGTGATCTGTCTATTTTTCCACCCGCTATAGATGAACTAACTTGTGAGGACGAGGCATTTAATCCAACATCGTCGCGCTCCCTGCTGGGCCACGGTTCGTGTTTCGCTGGACTGAGGCAAGTCCTTGCGCGAAACTCTGCCACTTGGGCTCTGAGCTTGGTAGGAACCAACCGGCGAGAGTAGGCCCTAGCCTGTAGTTTTATTGAATAGGGATGCTTGACTAGAAACAGAACCGTAACTGATGAAGATTGTATGAGTAGACCGCTTTCTCTGCCGTGGGCGAGCATATTTAGCAGGAGCTGATTTCGTCCGCTTCTTCGACCACGGGAGTTGCAGGTGGGTTTGACTTCATTTAATTGTGTTCACCAACCGGTCACTGCCGCTACCTTATTCTAAACTCGTCAGGGAGGAAGGGGTATCGGCTCTTAACTCTCGTCATTAGACTTCTTCAATCGAGTGCCCTCAAAAGTTCCGAGTGGAGAGACACCGCTCTGTAAGCTCCGAGTAACGTGGAGATTAGACCCTAATGTTATTAACACTCACAGGCCTATTGAAATGCGATCCGTCATACGAGTTTCTGTTTTCAGTGTATCCTTTTTGGGCTGCGCCCGTAATAGCGAAGATGGGTACTGGGATGCTGAATCGTCCTAACACCTTTTTAAACTCGAAGATATCAAACTCGGGAACCATAGAGAAATCGTACCCTTTTAAGCTCAATGCCTGCAGTTGTTCTTACTGCGAGTGAATCTGTCGGAGACAGAGGGATCACCGCGAAAATTAAGCTCAGAGAACGGGGAACCTTCTTCACGTGCGGGTTAAGACTACTGGCTCTAACTTCGATCGTCATGAGCTTGTAAAGTCGATTTAGTACTACTTGGCCCAAAAGACGGGAGCTCTACCGTCATAAGTCAGCCTCAGTCCCTTAAGGGAGCGCCGGAATTAGGATTCTGCACCGTGATTCTTAATTCTAGCTCGCTCGCATTCGAGCCCCTGCCGGTGTGTACCACCGAACTGAACTATGGGTGTGAAAAGGAGCGCCATGGTTTAGCCTGCGCATATTAGTAGCGCCACGGAAGTCTATTGAGACAAGCACACTTCAGCGAGACCCAGCCCGTCTCGAGGGTGCGATCTAAGCTGCTGACCGTAGTTAATCGGTCCGTTGGTGTATCGTATTGGCTTCCCGAACGTGGTAATTACAACTTGACCGTATAGGCAGGGGACCCTACTTATGGGTTGGGTTGAATGACATGAGCTGATGACAACCAGGAGCCGGTAACAGGGGACGGGAACACGCGGGACCATTTGCTAGTGACGAATCATTCTGCCGGCCCAGTTTGACTGCCACTAGGTGGTTTCCCACGCCCCGCCAAGTGGAACCACGGCGCTGTCCCACTCGCTCCCGTCATACTCAACTTAAGATTGGCTTTTGCTGCTACACGAGATGACCCGATTATGCGCGCAGTTCCAGTCCGGGGGTTTTCTACGCGCCTGATGACTGTACGGGGAGGAATGTTACTGGTACCGACCTCCTAACTTGCCGGAATTATTATTACAGGTAGAGAAAATGTGTAAAGTATGTTAAAATTCGGGCACCCTAAAAGGGGACGGCCACTTTGGTTGCTGACACCCGGAGGACTCATACTATACGCATGTTGTCATTATCATCTGCGACACTCATCAAAGGGTCTTCACATGGCAAGCTCAGCTGCACTGGTCTATGCATGTACAGTTTGGTCTCACCGGGAGCCAAAAGACGACAGCATACTTTAATCTAAATCCCATCGTAGATATTAAGCAATCCACGTCAGAACGGTACAGTGGGTTTTGTCGCTGCACTTGGTGGAGATAAGAGTTTGGCTACACTGACCCCGTATTTTTGCCTAAACTGCACGGTAGGGGGGCCACACATTAGCTAAATCGGTCTCGTTGACGGAGAATAGCTATCTGTTGTCCTGCCGTGCGCGTTTCCCTTATCGTAGTAGTTGAAAAAAGAAAGTGGCAGGAAAACCTGTTACTCTAAGGCGATACGGATCCCCGAAGCTAGGTAGGCTGTGGACCGGGCAATTTCGTTGGTACCTGCTACATTAGGGCAATCCTCTGGCTATATCAAGTGGTTAGGCGCTCACCGCAACATCAAAAAGGGATACCTCTTCCTGAGAACCACTGCATGTCTGGTGGTCGCTAATAAAAGAGGAGAAGAGGAGCTATGTAAGCAGTCTTATCATGCGTTCCGACCTTGAGTGAACTGCCCATCGTAGGGGCGATCGTAGTCCTGTTCCTGCTTTACAGATTCCCACGAAGGAGCTAACGCTTTTACTTACTATCAACAGCTCTGGTTAGGTCTTACGCATAAGCTGCCTCCCTCGGATAAGTATCGCCTCCAACAGGGTACACCACCCCAGCGTGTGGTTAATGAGTCAGGCCATTGAAGCACTGTTTCCAATGCAGTTTCCTCCATTTAGACGTCCACATCTTTGCAGGGGCGGGTATGATCTCATAGGTTAAGCGCGTCAAGGAACCTCCCTGCGGACAAATTAAAAGTTTTACGCGGTAACATGCTATCACTTTTTTTAAGGGATAGGTTCGAGCCAACGAACCGCGGTGGTAAGGCGTGGCGATGGTACCGAACGTCTGAGTTACATGCCGTCAACGTTTCCAGAAGGCACCGGGGCCCATTGAGGGGGTGCATCAGTTGGTGGGTGCCTTCTAATGAAATTGTTGGACGCTGCCTGTGCAGTAATTATTCGCGATGATGGCCACTGGGTTTTGCTTGGAGTCCCCTGAGTACCCATCATGTTATAGGCCCTTATGGTAACTAAAGATCATGTCAGACCTTCACTTCACGGCTGTCGGTAGGTTTATATTAACCCTTTTAAGGGCTCACATCCAGGACACGCATATGAGCATTGGTGCCTATAGTCGCTACAACTATTGGCCCCTCCAAAGCCACATTCGACGAGGAAACGGAGACAATGGAACCTATATCGGTCTATCAACCTAAATGATCCGCTGCGGAGCCCTACTTTCGGTATGTGGCAACGCTGTTCTACAACTTCGCCAGGGCCCATACTCGGTTCCGATAGAGCGTGGCGTGAATAGGCGCCTGCTCATTTAAGAGAAACGTGGTGCCCCCTGAATCTTCGTGGACGCCAAAGCGTTTGCTACTATGTCCGAAATCGGACACGTTTTACTAGGACGGCCACAATACGGCCGAATTGTGCTGATTAGCCAGGGCCGTAGGTGGACCTCGGTAACGCCAAGACTCTAAGTATCCAGCCAACGTATTCTCTCTTCATATAAATCATGCAGTACACTTGAATCATGGATTACTACTAGCGGATATTGCGCTGACCCCAAGATCGTCACGACGTGGACCTGACCCTAGGCTGAAGCATCTCGTGATACAAGTCGTTGCAGCTTCCTACTCCCGCATAAGTCCACACTAAGGAATGGTGTTTAGTGTATTGGGAGAGAGTAAAATGTGTACTTCTCACTGTCTTTGGGTATACTTGTTCTCCACTATACACAGAAAACTTTCGTTATTCCGTATGTGATGAGACTACTGATGTGGGGTACCCTGGCCGGATGGTCGTAGACCTCGGAAGCTTGCTAAGTAAGCAACTATCAACCAAACAGCGTAGGTATCTAAAGGACCAGGGTCTACCTTATTTTCCCTTATATCGCCTTAAACACATGTGGTCAGGCAGGATATATGGCGCATAACCCATCTCACATACTGGCACGCACGGTAAGGTGAGGTCGTCGGTCGGTACGGGCTCAGCCAGCGTTTCTCGGCAATTACATTGACTGACGAGCCTCGCTTACTAAATTAAACTTCATCGATGAAGTGGGTCTTGAGCCACCGGATCACTGTACCATTGCAGCAACTCTTCCTAAGTTACGGGATTATTGTTACGCTGTCCCGTTTCTTTTGGGAGGCTACCGGCCAACGCAGGGACGCGACCGCTCTTAATCTCTAGGTCTCAGATGTAATTTCACTATAGGGAAGACTATATGATGCGGGGGAAGCTTATGGGCTAACAGGGAATAGCAGAGAATCGTAAAGTAGTCAAAGTCACAGGCTCTGGGGTGCCCATGATGTGCTCATTGTAACATGAAGCTGGCGTGAGGGCCCGTGTGGGAACAACACTGCCTCCAGGAGGCTGATGTTCCAGAATCGTATTCTTCAGTGTCACTATCTCCATGGTGTAATAGGCTTCGGTGATCGCGCTTGCGTGAGGGGTGTACCGGAAGAGTACCGCTCAACTTTGGAGGTCAATGAGTACTCATGCAGTCGTTCCAGTTACGGTCAACACAAACCTTTCCAGTTCTCTTCCGGGAGCGTATCGTTACGGCGTTATAATTGTACCTTGGCCGTCATCGGCCGAGGAGGGCGCGTGGACCTCTAGCCGATAGCTAAGTGGGGGAGCTCGGTCAGCTCTGGTATCGTTCCTGCCTTTGCGGTTGCTGCTGGCTACCCTTAAAAGAGAACGCTCATCGACCACGCATCTTGATCTCGGAAGTTATATGGAGCGATGCCGGGCGCCGTACCTCAACAACGCGGACTATAAGGGCACGCCTCTGAACTTCTCAAGGTGTGACCCTCGCTACTCCAGGCTATCTAAAGGAGCGTGGACGATCGTCGCCATGATGGTTGACAGCTGACCACTCTTATAACCACCGACTCAACCACACGGGATCGCATGGACATATTCGCTGGACGCGCCATAATTTGTGGCTCGAGCGCCATGCTACCAAGGAAATGGAGGACTGTGGGATGACGAAGCGAGTAATCGCCTATAATGCAATAATGGTGCGGCAGGTTGACCTGAATCGTTCGGTAGAATGACCGGCGATGTGTGTGCGCGTATGTTATGGAACTTCGTAGTCGCCTTATCGTTCGGAACTGGATTTGTCTTATTGACCGGTAGACTGAAATTTCTTGCCAAAAACCTTTATCCCGACACCGCACGATGTGTTCTGGGCAGCGCTCCACGACGACAAAGCCATTTAGTTTAGGTCGACATAGAGTATGAAGTAGGGCACTATGGAAAGGGGGCGCGACCAGGAATGGAAGTTAGGTCGGTATATGGACTGCGTCGATTTGCCCGCCACCAGGTGCTGCAGTTGGTCATAAATTTTATCTCTATGGCCCACAGATCGGAAGGCGCCTATCTATTCGGATCTAGCATGCTTAGTTTAGGTCTCGTGCGTACAAAAAGTTTTCCGACCCTTTAACTTTGGCTGCAACCCTACTAACTTAGTGGCGACCCGGTCACAAGTCTTAGCTAGACGCTGCTGGCGATACTTCGGAAACCGCGTACAGGAATATTAGTCCTTAGCATCAGAAGGCTGGCACATTTCCCCACCAGACTCGTAGTGCCCTCGTCGTTTTAAAACGCCTAGACGCGTCTAGAGCGATTCTTATGGTTTTGCCTGGCCCCATCCGGACGTCCACATGTGCACGATTTCATTTAACGGGGTACGGTATATTCATGACCGGTTGGGTTTCGTGCTGCTGAGCATCCTCTCATAATCCTATAACTGTCTTGGACAATGCATTAGGTCTTCGAGTGTAGTTCAATTAGTAAACACATACTCGTCAGTTCGATCGGGTACCATAACTAGTACTGAATTTGACTGGATCCTGCCGCCTACTCGGAAAGAATCCGGCATACTTCGGCTGAGCCGATTCGACATACGCCCTGAAGCATAGCAGTAAAAGTCCGGTAGATAAAGGCGCCATATTAAACTTACCCGTATCCCGATTTGCAAGAGGTCCAGCACCGGTATGGCTGCGCGCGGCCTTCTGAAAACTTGGTAACCAATAGGTTAGGTATTGTGTCGCCGTACCTCCTTCGTATTGCTAAGCTCGTCCCGTTCAAGGGTGGACACTACACGACCGCACGCCAAGGCGTCTGATGTACATAAAAGGAGCATTTGGTCTTCATCCTCGCGAGGAGAAAGACCACTGCCCGTTGACGCTGCGTGACTTTCAAATCCCCCTAGGTACATGGTTACGCCCTGAGAGTCGGGCTATTGAAAGCTTCCATAAACGGGGCATGTGACGTGTAGTCCCCCATCGGGCTGCTGCGCGACGGATCTAGAGGCAATACACATTACGTTGGGCACGTGGTCTTAATGAAAGCGCCTGGTAAGGGTCCGCGACCGATCGCGAAGTGGAACGTATCTACAAACGATGCTAGAAGTAGTTCATATACCATAGAGCGAATACACCCCACGTTTACTAAACCGTTCACTACCACTTTTACTGAACTGTCGCATCCTTCTAGGTGGGTAGGATGACTTTCAATGTGTCTGGAAAGGACTCTCGCTCCAGGTGAGGTGCCGTATATTAGCACGGTTATCTATGAAAAATTCAAGGAATAAGGTTGTCCTCATTTACCTCCCTACCTCGACAATCAGCACGGATTGCTCGTCTGATATGGCTGACAGGTAGTGCCCTATGCGATTTAGCATAGTAGAGTCTTTCTCTTGGTGGCAGGCGGGGGGCGTGACCGTTGTCAGGACGGGCAGCTGAACTAATCCTTCGGCTGTACTATGGAACATTTGTCGTGTTGATCTGAGCAACGTTACGTTGCCAGGTTGGACTCCTCCGACTCTGGTTTCAGCAACGTGGGTTCAGAACCAGGTGACCCTTCTTTTGATTGACATCTCACGATGAGTGGTGTCATGACTTTCCGGGAATCCTGTCCCTGATGGATGTCTATAGACCGACCCTTACGCGCCTTACTTTACGTATGCGAAGGAACGGTCCATCGTGTCAATACGTTGGGGAAACCCGGCTCGACCGTTTACACCATGCCCTGTCATGATGGAGCTCGCGGACCGAGTTTATACTCTGATCGTAGACTTCGAAATATATTGCTATTCCATTACCTTGGGTTAAGGTGTCACCCCCTCAATCAGCGCAGGTCACCACCATTACCCACCGGACGGTCCTGCGTGTGGGGGCGAATGTTCCCAAACCTTGCCGCCCCAGAAATGGGCCCTACTCGAACTGTTGGTCAATCCTCCAGCCCCTACAGGTGGGGTTACAACTTAACAGAATTGAGGCGTAGCATACACTTTGCTGTAACCGTACACTGATCTCGACTCGACATTGGAAACTGCGTGCGAACGTTCACTATTGCTCTAAGCTATGTAGCCTGATCTACCCTAGAGCTCTGATACAGGTAGCATATCGGTAGGATTTCTATCAACAGAAGGGGCACTAAATCAGATGATGGCTTGAGTTGCCTCCGTACGACTCGATGCAAACCCTTTACACCGTTGGGTGTTCGTGATTCGGAGAGCCGGAATCGGTACTAGCTCTTTTGTTATAGCTACAGAGCGATAGTGAGCAGAGGTTGATAATCATATTTCTGCCCGATTATTCCGTTGGGTAGGACAGGAAATGTGGCTGAATTGCTTTTGGTGTGTATTATGAATCCATGAAGTTTCTTCGTTCCCGGTGTAACCACGCCGTGAAAAACTTATACGTCCCTAGCATACAGGCCTCCGCTGCCTGGGTGGAGCACGTGCGAGTTCCTTTGCATCACAGAAGGCCGGCGTGCGTAATATATGAATTTATTGCGACTTATAGCGTCGTCTAACCCTGATCCCGTGCCCCAACGTCCCCGCGCAAGCACTAGGCACTGAGGGGGGCCAGTGGAAGTCCTCGCCCCTACACGCTTCACATCTCTGATGGCGCAAGCGCGTCGGATGCCGAACCCTTCTTCTCGTTTTCCAGATGTTAACAGAGTTACTAGGCTCTATCGCGTTAGAAACTAAGGGATCAGTTGCTTCACTCGACAGGAACCTCCACTTTCACAGTACGAGATTAGAGCTAGCGCAGCGGTCACAATAGCCTTTTTAATCAATCTCTAACCGGTGAAGTTTCCGCCGTGCCACTTGGACTACTAAGTTATTTGTCTGACCCGCCAGTCAGCGCGCAATTTATTTGCGTTTTTCTGACTAATAGGAAAGACATTGCGCAGCACCATTGCCCCCAGCCTATGGGACTGCTAATTAGACGCGCCGGCTAGAAGGCTTCCATCTAACTAGATGTTGTTGTTGTACATGGGAAGCTAAACGCGTACCATGGGTGCCTCTATATCTACGACGCGAAACTCGTTAACACTTTCTGCCGCGGTTCCAGGCCTGAGAAAGTCCAGTAGCGGACCTCGTAACCTAGATGCGGTTTTAAAAGGTCCCAGTGTTTAAAACACCAGAAACCTTACGCGGCCTACTGCAGCTAAGCAAGTTAAACGATGGTGGAGAGGAATGTTTAACAGTGGGTGTCGTGCCAATTTCATAATCGAGTCGCCTAGCTATGCCGGCCGGCCTCGGTTATTGGGAGCATCTGGAGGCTACGGCTCAAGGCGCCGTACGGATGACTCATGCGTCCGGTTAGTTGATTCTATGTACCAGAATATTCCTGCTAGTGTTTACGCTCTACTAGAGTCGCGCGATTGATCCGCCGATTCGGCTGTTGAGTCGTCAATTCGCGCAGAGTTGCGATCCCCTTTTTGTATTGGGCACCAGCGCTAATTGGTGACCCTGCGGGTAATGCCTCGAATGGCAGCTCCCCATAACTGGAACGCCAAATTGGGGATTTAGCCATTTAGATGCGCGGGCTAGTCCGTCACGTAAAATGAGGCCACCGCAGCAAAGCGGGTGCAATCCAAACCAGCATCCGCCGACATTAGACGGAGAGACTAGTTGGACCACACGTTTGTTGTAGACAAGATTCCACACACTTCGAAAAAGTACGTTCCGGAGCCGCCGGGACGTCAGAGTCCGATACAGTCCAAGCTGATCTAAGTGAAGACTGTCAGACGAATGGCGAATTGGCCTCGCGGCGTCGTCGACACTAGACATTCGTCTAGTAAAGTACATGCACCAACCCTTGTTGCCTATTTAGTTAGACAGGGTGATTAGAGATCTTATTCGGACCTAGCAGCGGGAAGCACCCTAGTCCAATGGGCTCATGCATGGACTATACCGAACCCTGCCCTCAGTGCTAACCCCGATTTGTAAGCTCAATTGGATTAACGCCCATGGGGAACATCCTTTTTTTAGCGCAGATTTGAGTAACAATACAACACGGTAAACACCTCCACTGGATGAGGGCGCATCTAAGGCACCCCACAATCCCGGGAACATTTTCAGGGGGAGGCGAGTGAGAGTATATGTCATTTCCATTCGTCATATGTGGATCTCTCATCTTACTGTTCTCGGAGCATGACTACGGGGGGTAAGCCAAACGGCGAGGTGATGTATAAGTTAGTGAGCCACTTGTCGCATGAGCCCGCAAGATGCAGCCTGGTAATGAAACTTCATAATACTACAAAGGGAGAAAGCTGCAGGGAAGGTGTTTGTTCTCTGGACTCCAGGCGTGGGGTTTGCTCTTTAAGGTAACTGTGCGCGGGTACCAACGCTCGGTGTGACCCTGGTCACGTTGAGGTAGGTAATAGTGGTTTGTTGGAGGTGGCTTCAGAAGATTATGACAACGGTGCCAGGGGCCAGGCGTCAAGACCATTTGAAATGCGTTCTTTACTAAGGAAATTACTGTAACTATCGAGATCCCACATGCCGTCCCTTTCCTATTGACTGGATACAGAAATCGCGCACGAGAACAGATAGCAAAGATGATATCGATGTGCGCTTATACTGAGAAACAAGTTCCAAGCTTTGGTCCACCTTGCTAGCCGGCTTGCGATGGCCGCCGTCCAGGGAAGCCCCTACCAGTAATTCTAAGAAAAAGTACGATAGCGCGATGTAGCTCCCGATCGGCTTCATGCTCGATGAAGCCGACCCGCCGGGCTGGGGCGTCGCGGACCGAAGACCGTTCCCCCACCGACACCCACACTGAAAGATGTACTGTAGAATACGGGGCTTCGGCGTCGGGGGGTATACTCCCAGGATAAGGTTCCTCGGGTCGTGGCTTAATAGTCGGATCAGGCTTACTAAATCCTAGGTGCTTGTCGAACGGAGGGATATCCTTTATAACTCATAACATGGGACGAACGAGCTGGTACTAGAGCTGACGACAGTAACTATGACGGATATGAACAGACCTGTTGGTATATGGGGCACACGCCATAAAGCTGCCCCCGTCGATTTGTTGCGTCGGCTAATCTATCGAGAGGATCAAGAGGATTGCCTACCAGGCAATCGAACTTGCCGGCAGCGCATCGACTACCGCCCAGGGTGCATAGTAGATTCGCTGCACCAGTTCATTCGTCGATAACAACAACGTCGTCTAGATTCAGAACGAATAACCCACTACGTCCCCGGCTCCCACTGGGAGAGTATAATACGATATTCTTGATTGCATTCTTTAGTCAGCACGTGAATGAGCATGCTTACGGATTTTAGTACCAACACGCAAGGATCCAAACTGTGGAACAAGCAAACCCTTGGCTTTAAAGTTGTGCTAGAACGCTGACGACTTTAATGAAATATCGCCTGAAGCAAATGGCTGAGGTAGCTCGAGATCATGAAGAGACCAACGGTCCCGAGGAAGGGAGGTGCACCACTCACCCAAGGTCGAGACGTCAATAATGGCTACTCCTGTTGTGATACACTCCTCTCAGATAGCTGTTGCCTAGATCAACCCTCGCACCAGACGTCATACTCGGGGATTATTAGGCGGTCCCGTAAACATTTTAGTCCGCTTGGGCGCCAGAGTACCTGGTGCGGTTTCCATTATTCCACCGTTAAGTTTTCTTGATTGTTAGTACCCGTAGACGGTGTAGCGTAGTCTGCCTCGGATAGGCATACAAGTCATAAGGTTCGAGACCCCCTGCTGTGGATATTAAAGCACTGCCAGCTCTTGGTATTCGGCCATTTAAGTAGAATCACAAGGGCGATCCCGAGACATTTGCCCAGTGGCCATAGTAATCCAAAACCACTATTGGGAAGCAGGACATTTAGCCAGACCCAACCGGTCTACATTAAAAGTAGTCTCGCTAGGCTCACCGATCCTATTGCAGACTCCAGCCCTCCGTCGCTTGATGTAAGTCGCCTGATGCGCTGGGGGTGAATCAGCCCCAACGGTTTCACGGTTAGGCTGTCGAGTTCTCCTTTCCCCAAGGATCGTTGCGCCCTTATGGATTTCCATTTCGTGATAATGTTCAGAAGGGTTGTGAGCGCAGCGGACCTAGAAAACGCTCTTTGAATATTCAGGTCTGGGCTTTGCAGAAGAAATCGAGAAAACTTCGGGGAAGTTTTAACAGGACGGTTGGAACAGCCGGCACGTCCTCCTGGTCATGCGTACCAATGTTGAACAACGAGACTTTACCATAAAAAATCCAGTCCTTCCTAAGTTATTAAATTGACGCAATGACCCAGGTCCTGGCGCTGAGGAAAGAGACTTACGGACTAGTCTAGGGCACCAGGTCTAACGATTCCATGCGCTATTGGCTGACTTCATTAATATCTAGGGTACAGCTGTGTCCTTCATAAGCGCTGGCATGCAGACTAGGGCATGACCGACATCATCGACCGCAACCTTCCGAGTACGCTGCAACTAAGTACGGAACTCGCCAGGTGGACAAGTGCGGGCGGTGCAATTAAATCTGGTGGATAACGTCAGTGCCCGCACTGCGATCAACGCCGAGTAGCCTTGTACGGAGAAAGACGGAGTGCTCCCGGGCTCTTTGCATGATCTACGAGATCGCCAGTAACAAGCATGTACCGAAACGGCGGCAAAAGACATGTTACGTCAGGTCCCGCTCATAGTTAGTATTGTGAGGCATTGTTTCTTTACCTTTATGTCATCGAGTAACTCGGTCCCAGGGTTCAATCAGATTCACGTGGCCCTTTCATGTCGTGTAACAGGGAGCGTGGCCTTGGTCCATGTACCGGGCCTCTTGATGCCCCAAATCAGGATTTTCTGGACTTGAAAAGTACCAAGTGAGCTATTGCTAGGCGAATATACCCCGATGCATAAAAGGCTTCCGGTGCGGGTTTGCGAAAAACCTATGGGGCGATATAGTTTTGATTATGAGATGTCGTCATTTGGGTGAGGCTGACGGCATAGGGGGTAGCACCCGTATTCCCGAATCGCTAACGGTTCAACCTGGCTACAAGAAAGACCGAAAACAACGTGAGCCACGACAGGCAGCTGGATTTACCGCAGGCTTGATCACATTTCGAACCTCCAAAACGGTGACCGCAAGTCCCGTGGTGTGAAGGTGCTGTCTGAAGAGAGGATTTTTCGCCCATCGGGACGATTATCCATCCGTCTCGTTGAATTCTGCGTCATGCCCTTTCTCGCTTACCTTTACGAAATTGGCGGGCGCTGCCCAACTACACTCAGAAGGCCAGACCCGCTAGTCAAAATGAGTTCATCACCTAACGTTCGCGTCCAGAAGAAACAATCTCGGACCCATGGCGGATCATAAAATTAGATCGCCAGCCGCTTACCGGCCGTATAACTCGACAAGACCCCCCTTTGGGATTAAGCAGCTTGTTCCCAGTCTTGCTATGAAACGTTCGTAACTTCGCAACCAAGAAGAAGACATAGATGTGTAAAATTGTCTACTTGTGATCAGGTAACTTCCTAAGGAACCGGGTAGTTTCACCCGATGTTAAGTGCTGACAATAAAGCAACCCGGAGTACCGCTACAGTCCCGAATACTGAGACCTGTATTAGATCACGGGACTGCACTGTTAACCGTCCATTCAGAATCAAACGCTTATCCGAATTCGGCATATCATTAGTTCTGAGGCGCAGTAACCGTTGTAGGTTAGGCTTTTGAGACATTGCTGAACTTGCTGATCGATTCCCAATCCGTGCTACTACCAAGGCGGGGTAGGCCTGTTCACCTGGGATCTGCATCTCGCAGTACTCTCACATAGAATGGAAGTATGGGGTAAAAGGTAGTCCAAGCATGGCGCTAACCATGGCCGACCTAACTGTACGGAACCTAACGGAAATGCTTTGCGCTAAACGTATGTTACGCGTTTAAACTCCGAAATAGACTCACAAAGGATGGAGGTTACCGATGTCGTTATCCTGCAGGATTGTGAGCCAGCGAGGATTGAAAGCAAGAACATATTCAGTGCGACCCTTTGACTGCCATCGACCAGCGCAGGTTGGAAACCAGTATATACATAAATAAGGGGAGAGGTGGACCTACACGGAACTCTAGTTCATTCCGAAAGCTCGCGGCATAACGGTACTTGCGTTTCACCTATGCGTACAGATCATTGACCCCAAACTGTCTCGCGTAATCTAGCCACGCCGTACGGGCCGGGATTATTAATGGAGGCAGTTAAGTCATATGAAGTTGGGAAGCAAAAGACCTGCGGACGTGGAGATCAAGACAGGTTCATGTGGCGATATACACCGAATTACTACCTGCAAAGACAAATAAGGACTTAGCCTCTTCTACGAGTCTTCAGCGCTGTCCTGGTTTCACCGAAGGAGCGAGCGTCAATGGGCCGCTAGCGCCCTTACTCCGTACCTGTTTGTCACCCGAGTCCTCGGCCGAACTGAGGTGCAAAGGAGTCCCGAGCGCTATACACCTAGACGGGAATCTTATCTTACATGCATGATGACCGGGCGGAATAAAATTAATGACCTTGGCCGGCCGTGGTGCAAGAGGTTACTAATCCCGGCACTTCTTCGGAGCGCCTTAGCCGTAAAACTGGGTTTATTCGGGGTGGCAAATGTGATTTTTCGCCTAATCCGTGGTTCTTACGTTGCTGTGCAATCGGTTACGGCAACTTTCCCTCCCTTGTTCGTCTAAGGGCTGGAAGAGTTTGCCTACATCACGTACGTTAAGCTTAAGGTGAGGCCTAACAATTTACTGAGCGGCAGGGGTGGACCGTTAGTCTTTTATTCTGCCGGTCGCTACTGATGACACCCGGAATCTGACATCGCTATATACAGCAGTGTTTCGCAAGAGTTACCCACTTTTAATGAGCCTTGTGAGGGCCATGTATCCTTTTTAACTCTTTGCCGAGCTGCCTGAACCGTGAGATTACTCTCCGACTAGGTTGCGTGCTAACAACCTTATCTCGGACCAGATCTCCTAAGGGCTCAAACCACTCCGTCGTTCCCACAATCCTGTGGGTTCTCGCTCTCATATCTAAGCGAAGGGTGATCGGAGCCCTGGATTAGGCTTGAGACAATTTTAGCACGGGAACTTTCCTGGCTCATGCATCACTGTGAAGTGCCCGGGTCTCTGTCCTTCTTTTCTCAATCGGGTTACGGCTACCCCCAGCGAGGTCTATTTTCGGGAGCAAGACACAGCTCTAATCAGAGAGCTAAAGAAAATTTCCACGATTTGAGCGTATTGCATCGGACCCCAATTGACGGATATGACCGTTTATGACACTTTTCTTATTGGCGTTGGCCGCGCAGCGCTATGTTGGTCAGACGTGCTGGTCGGAGTCGAGAGCGGGCTGGAAGAGCGAACCCAGAAGATGTACCCCAATCATTGCTTGAAACTTACTGGGTTACCCTCATAGTGCTCCCCCTCACTTTGTCGAGTCCCTCCTAAGGGTCACGCCTGGAGACGATTTGCAACACTGAATACAGAGTACGATGAACTGGCTTACTGGGATCTTCCTTGCGATGAGTTAGCCTGATAGAAATACGGTCTACGAAAAATGGATCAACGAGACCTGCACTGATCCCGTGACGGTCATTATTGGCCGATATTTGATCTGTTTTGAGAGATAAACATTGTAACAGTACGTACGATGGAGTGCAACTCACACGAGTCACCACGGACCCTTGTCTGTATCTGAAAGCAGGTGATCCACTATGCGCTGGGTTCAAGGGAATTTTAAAAACATTAAATCTCGATGCGACTTGCCTCTACTGACCTTATAGAAAAGATTACTGTACCGCTGGAGAGAGTTATACGAATGGTCCGATCTCCGTCTTTGATTCAACTACGGAGCCTCCGACAACGCGTTGATCTGGGAAGCGACTGCGTAGGTTACAGTCCTTCTCGTAGGTCCTTCCCGTAGCTGCCTGGCGTCTGTGGTGAGGAGAAAGCATATGGATATGCTGACACAATCGGCCAAGTCCTGATTCGTATCTGAGAATATAGGTTTGACCGAGGAGTTTCCCTTGAATCAAATTCCCTAATCTCGCAACCTCACTGTTTGCAATGGCAGCATTTAATGAACCGCCCCATACATCGTCCTGTATCTCTATTAAGCTCGAGCGTATTGTTATGCTGATGGATAGAATAAGAGAATACCTTGCCTGTGGAAAGCCGAGTTATTCGGTTAACAACTAAATGTCGAGCAAGGTACGTTATCGGGGTGCGTGCAGCAGTTTTCTCTGTCTGTTAGGCTCCTACTATACCCCTGGGAACGGGTTGATGTACCTTCCTTTTTGCGTCGGGTAACATCTTATACGCGTGTCTATCCGAATTCGGTATATCAAAAAACCCATATCATATTGTATCGTACAGATGAGATGCGGTGATGGTGTTGAGTATTCACCTTGATGGCGGCGTCCTCTGTAGCTGGGTCAAACTGCTGGTGCACGTTGTCCCCAAACTCCGAGTCGAGACAGGGGAAAGAACGGCTTAGAAGTCATGTCGACACACCGAACCTTCTTCTCAACGGGCATATAATGTACGACTCCCAGAGCATGTCTTATATGAACGTTTACCCCACTCTTAATGCGATATAGATAGATCACCTGAGTAGGGAGCGAGGAAGACATCTCGATGAACACGACCGTCCCCCCGGGGCCACATACGAAGAGCACTCGAAGATCAATATTCTGACCCCCCTACCGTACACACGACGCTTAAAGACACATGGTTATTCGCCCTGACAACTTACGGTTTCCTGAAAGCGCTGCTAGGCCGCATTCGTGCCAAGCCCTAGTTTGATATGGTTACACGCGGGTGGTCATTATTAGGACGCAGCTTATGGGAAAGGTTCCTTGACTGGTGAGAACCCCGGCGTAGAACATTACTGATCTTGATCCGGGTGCTATCTAGCCGAAGAACGACGCTTACAGCTTGTGATTTACTGCAAGTTATTGGACTTACTAAGGACCGCTGTCAAGATGTCAGCTCCGCAGGGGAAAACTCTGTTAAATAAGCACCGACTGAAGTATCAGGCCGTTCCGGAGTAGGGTGACGCAACGATTTGACGAAGGCGAGACTGACCCCCGGCATGACCCGTGGCGACGTGGCGCCGTGTTGCGATAGCCGCGCCCGCAGAGTCCTGCACATGGTACTGTTTAAGCCAATGGTCTGAACGACAGTAGTGTGACCAGGGGGGGGCTGTATACTGAGCTTTCGGAAATGTCATTACTGTCTCTCGGGTGACTTTCCCTGGCTTCCCATTAGCCCCACCAGTATTAGGCGAAAAAAAAAGGAACTTGTGGCTCAGCCGTCTTGTATTGCGGCCTCAGCCCCCCGTACGCGTCCCGTTGCTTCCAGAGAGGGGTGGAGTAAGTCATTAAAATCCTATCGTGCCAGCCGATAGTGCTTACTGGACCTTCTTCAGGGTTGAAAAATGTAAGTCATAGGCCTCCCGACTGATTTGGGCCTGGGGGGGAACTAACGTGGGTAATTCCTAGACCGGGGACGCTTCTGTCCAAGCGCTGTGTTACAAGGACCCCCTCCGCTTTTATTCTTATCCGTAAAGCGGTTACGTAGCTTGCCTCAGTCGGCCCGCTGCTACCTAGCAACGGCCCAATGCGCCCTCCGCGTCAGGAGACTCGGGTAATCCGGGAGGCGTGATTAGACCGGCAGTAGTAGCCATTATGTACTACCGCTAATATCATAATTACGTAGCAGGTTGTTTCAGTCTTCGACGGTGTACCCGATCGGTTTTTTACAGCTGATGCCAATCAATCTGAGTGATCCCACTTTGTTCCATTCTCATACAAATGCATGACTCTGTTGTGAATGCGCTGTCGACTCGAACCCCTTTGGGAAGTGCGGAGGGCCAAACAAAGGGTGTTAACTCAACTGTCAATACCGGCCCCAATCATGAAGCGTAAGTCCGGAGATCGGGATCTGGTCAACGTAAAGAGCATTCGATGCCAGAAAAATCAATGAACACAGTATTCTCCATTCTAGCTCATATTGCATTTTTTCCTACCTTTTAGTACAAGAGGATCCTAAAACGCCAGCACTGGCCTAACTTCAGTTCGCTGACGAAGTTTCGTATCGACAGTGCTCCGGTAATCGTACGCAGGACATCGGCGAGACCTCTTTTCCTCGGATTACTGGTCTAAAAATTGGGTACGAAACGGACCGCTGACGTGAGTAGGAGTTCTTCCTATAGTTGCGAACATCTGAGGTAAGATGTGGGTATGAGATTCCTTATTATAATGACAAATCTCCTATGGTTTACTCTACTGGTGGAAAGCTAGCGACGCCTTACGCCCAATATCTGGATACACCAGAGACGTGATACCAAGAGCGTTTTTTAATGCGGCAGCAAATCATGGTAGCACCTCTCCGCCACACCCCTCGTGTCTTCTCGACTTATACGGGCGACCCAGGACTCGTGCTTGGCGCATGTAGCCAAATCAGACAAAATAATCTCAGATCCAAGTGATAGTAAAATTACTCGACGTAAAAGGGCCTTGGCGCAGGGGTAGCGTGATATTAGAAACAGTTTGTATTCCTATCGCGTTTTGCGTTGGCTCCGAACTTATGCTAACGGAGATGTGCAACTAATTACGCCCTTAGAACCCGGCCGGGATATAATAATTTCTTGGAACCGGACCTCGGGCCCAGAGATATTAACAATCATCTCGCACCGCGCCCTAGATGTTACCCCAAATCCTATAGTGTACGCTCGATTCAAACGACTACGACGTTATACCGCCCAACATCCAATCCATGACTGGCTAGTATAAGCCTCCCCAGTAAAAGCAACAACTCTTATCGTTCTAGTCTTAACGGAGCTTAACACTATGGTATACAGATTGCGGCTCTATTTCTTCGCCGACGCCCCGATCTCGTTGTGTCATCCCCCGTCATAGCTGTAGGTTGGTTGGAGGTAAGCCTTGTCGTGTGCGAGAGAGGGCTGGCCAGCCTGCGGACCATGGCCCAAGCGTACTGGCTCAGGCTATAGTGTTTCGTCCCAGCGGTCGGAGAGCCTAAGCCATTAAGGGGTGAGCTAGGTGCTTGACCGGCCCACGGATTAAGATAAGAGCGGGTACCTAAAAGTCATGACTGCTTCTCACACATTCTACTCAAAGCCCCCGCCCTTCCGTGCAGCGAAGTTATCAGTTGAAATTTCAGCACTGAGTGACATGACGGGGTTTTAAGTAGACGGGATAAAAGGCCTGGCCCCAGGTCGCCCCTGGGTTTTGGGAGGACAGAAATAGCCTTTTCTTAAGTATACGCTAGGTACCTAATTGAGACTTGATGTAGTCTCTGCTGCTGAGTGACACTGATGTATAGCACCGAACCATATCGGTGTAAGTGGGATCGATGAGACATTTACTTATTAGTGACCGTTTGTACCAGCAGTTATGATATTTTGTGACTGTCCTCTCTGTATAGGCCAGCGGAGTGGATAATTTCACTTATCAGGAACTGACAAGATGAAATATTTCATTTACAGCATAAGCTCAGCGGTTTAGTGAAGCTCTCGGGTTAAATGGTGCCCAATGCGAACCACGATCTACTTCAGATGTCTTATTGCAGTGGGGGATTGCGTTTCCTGCAGCATGTGTTGTGGAATTGGCTCACTCCATGGGCAATGACGATCAGGGAAAGCT"
    pattern = "CAGGGAAAGCT"
    distance = 6
    print(' '.join(str(x) for x in general_pattern_matching(genome, pattern, distance)))


if __name__ == '__main__':
    __main__()
