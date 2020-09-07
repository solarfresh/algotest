# -*- coding: utf-8 -*-


def search(pat: str, txt: str) -> list:
    """
    To search a string pattern inside the txt
    :param pat: a string pattern
    :param txt: text content
    :return: start index indicating the string inside text
    """
    txt_length = len(txt)
    pat_length = len(pat)
    indices = []
    for i in range(txt_length-pat_length+1):
        # j = 0
        # for j in range(pat_length):
        #     if pat[j] != txt[i+j]:
        #         break
        #
        # if j == n - 1:
        #     return i
        if pat == txt[i:i+pat_length]:
            indices.append(i)

    return indices


class KMP(object):
    """
    To search a string pattern inside the txt.
    When there are bunch of repeated letters in the text,
    we can counter count pattern to match the string.
    """
    def __init__(self, txt: str):
        """
        :param txt: text content
        """
        self.txt = txt

    def search(self, pat: str) -> list:
        """
        :param pat: a string pattern we are interested
        :return: start index indicating the string inside text
        """

        txt = self.txt
        pat_length = len(pat)
        txt_length = len(txt)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = self._lps(pat, pat_length)
        i = 0  # index for txt[]
        j = 0  # index for pat[]
        indices = []  # matching indices
        while i < txt_length:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1

            if j == pat_length:
                indices.append(i - j)
                j = lps[j - 1]

        return indices

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
