# -*- coding: utf-8 -*-


# def search(pat: str, txt: str) -> list:
#     """
#     To search a string pattern inside the txt
#     :param pat: a string pattern
#     :param txt: text content
#     :return: start index indicating the string inside text
#     """
#     txt_length = len(txt)
#     pat_length = len(pat)
#     indices = []
#     for i in range(txt_length-pat_length+1):
#         # j = 0
#         # for j in range(pat_length):
#         #     if pat[j] != txt[i+j]:
#         #         break
#         #
#         # if j == n - 1:
#         #     return i
#         if pat == txt[i:i+pat_length]:
#             indices.append(i)
#
#     return indices


class KMP(object):
    """
    To search a string pattern inside the txt.
    When there are bunch of repeated letters in the text,
    we can counter count pattern to match the string.
    """
    def __init__(self, text: str):
        """
        :param txt: text content
        """
        self.text = text
        self.index = []

    def find_index(self, pat: str):
        """
        :param pat: a string pattern we are interested
        :return: start index indicating the string inside text
        """
        return self.search(pat, 0, 0)

    def search(self, pat: str, i, j) -> list:
        """
        :param pat: a string pattern we are interested
        :param i: index for txt[]
        :param j: index for pat[]
        """

        txt = self.text
        pat_length = len(pat)
        txt_length = len(txt)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = self._lps(pat, pat_length)
        # indices = []  # matching indices
        if j == pat_length:
            self.index.append(i - j)
            return self.search(pat, i, lps[j - 1])

        if i >= txt_length:
            return self.index

        if pat[j] == txt[i]:
            return self.search(pat, i+1, j+1)
        elif j != 0:
            return self.search(pat, i, lps[j - 1])
        else:
            return self.search(pat, i + 1, j)

    @staticmethod
    def _lps(pat: str, pat_length: int) -> list:
        """
        To indicate longest proper prefix which is also suffix
        :return: lps
        """
        lps = pat_length * [0]
        prefix_suffix_length = 0
        for i in range(1, pat_length):
            if pat[i] == pat[prefix_suffix_length]:
                prefix_suffix_length += 1
                lps[i] = prefix_suffix_length
            elif prefix_suffix_length != 0:
                prefix_suffix_length = lps[prefix_suffix_length - 1]
            else:
                lps[i] = 0

        return lps


class BoyerMoore(object):
    def __init__(self, text):
        self.text = text
        self.index = []

    def match(self, pat, text=None):
        text = text if text else self.text
        # s is shift of the pattern with respect to text
        pat_length = len(pat)
        text_length = len(text)
        # initialize all occurrence of shift to 0
        shift = [0] * (pat_length + 1)
        # border position
        bpos = [0] * (pat_length + 1)

        # do preprocessing
        shift, bpos = self.preprocess_strong_suffix(pat, shift, bpos, pat_length, pat_length+1, pat_length)
        shift = self.preprocess_no_occurrence(shift, bpos, pat_length)

        self.search(pat, shift, pat_length, text_length, 0, text=text)

    # preprocessing for strong good suffix rule
    def preprocess_strong_suffix(self, pat, shift, bpos, i, j, pat_length):
        bpos[i] = j

        if i <= 0:
            return shift, bpos

        shift, j = self.search_right_pattern_border(shift, bpos, i, j, pat_length)
        ''' p[i-1] matched with p[j-1], border is found.  
        store the beginning position of border '''
        i -= 1
        j -= 1
        bpos[i] = j

        return self.preprocess_strong_suffix(pat, shift, bpos, i, j, pat_length)

    def preprocess_no_occurrence(self, shift, bpos, pat_length):
        j = bpos[0]
        for i in range(pat_length + 1):

            ''' set the border position of the first character  
            of the pattern to all indices in array shift 
            having shift[i] = 0 '''
            if shift[i] == 0:
                shift[i] = j

            ''' suffix becomes shorter than bpos[0],  
            use the position of next widest border 
            as value of j '''
            if i == j:
                j = bpos[j]

        return shift

    def search(self, pat, shift, pat_length, text_length, pat_shift_index, text=None):
        if pat_shift_index > text_length-pat_length:
            return 0

        j = pat_length - 1
        while j >= 0 and pat[j] == text[pat_shift_index + j]:
            j -= 1

        if j < 0:
            self.index.append(pat_shift_index)
            pat_shift_index += shift[0]
            return self.search(pat, shift, pat_length, text_length, pat_shift_index, text=text)
        else:
            '''pat[i] != pat[s+j] so shift the pattern  
            shift[j+1] times '''
            pat_shift_index += shift[j + 1]
            return self.search(pat, shift, pat_length, text_length, pat_shift_index, text=text)

    def search_right_pattern_border(self, shift, bpos, i, j, pat_length):
        """
        if character at position i-1 is
        not equivalent to character at j-1,
        then continue searching to right
        of the pattern for border
        """
        if j <= pat_length and pat[i - 1] != pat[j - 1]:
            ''' the character preceding the occurrence  
            of t in pattern P is different than the  
            mismatching character in P, we stop skipping 
            the occurrences and shift the pattern  
            from i to j '''
            if shift[j] == 0:
                shift[j] = j - i

                # Update the position of next border
            j = bpos[j]

            return self.search_right_pattern_border(shift, bpos, i, j, pat_length)
        else:
            return shift, j


if __name__ == '__main__':
    text = "ABAAAABAACD"
    pat = "ABA"
    bm = BoyerMoore(text)
    bm.match(pat)
