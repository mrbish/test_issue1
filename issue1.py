"""Module for finding substring and works with it."""

import re


def find_substring(string1, string2):
    """Finding max substring in two strings.

    Modified from: http://ru.stackoverflow.com/questions/478172/

    :param str string1: first string
    :param str string2: second string
    :rtype: str or None
    """
    strings = [string1.lower(), string2.lower()]
    strings = sorted(strings, key=len)
    str_len = len(strings[0])
    if str_len == 0:
        return strings[0]

    for current_length in range(str_len, 0, -1):
      for start_index in range(str_len - current_length + 1):
          found_string = strings[0][start_index:start_index+current_length]
          founds = [False]
          for string_number in range(1, 2):
              founds[string_number-1] = \
                  strings[string_number].find(found_string) > 0
              if not founds[string_number-1]:
                  break
          if all(found for found in founds):
              return found_string.strip()
    return None


def get_nouns(file_path):
    """List of nouns.

    List from: http://www.desiquintans.com/nounlist

    :param str file_path: path to file with nouns
    :rtype: list
    """
    nouns = []
    with open(file_path) as source_file:
        nouns = list(noun.strip() for noun in source_file)
    return nouns


def is_noun(substring, nounslist_file):
    """Check if word is noun.

    :param str substring: max substring
    :param sts nounslist_file: path to file
    :rtype: bool
    """
    if substring in get_nouns(nounslist_file):
        return True
    return None


ABERRANT_PLURAL_MAP = {
    'appendix': 'appendices',
    'barracks': 'barracks',
    'cactus': 'cacti',
    'child': 'children',
    'criterion': 'criteria',
    'deer': 'deer',
    'echo': 'echoes',
    'elf': 'elves',
    'embargo': 'embargoes',
    'focus': 'foci',
    'fungus': 'fungi',
    'goose': 'geese',
    'hero': 'heroes',
    'hoof': 'hooves',
    'index': 'indices',
    'knife': 'knives',
    'leaf': 'leaves',
    'life': 'lives',
    'man': 'men',
    'mouse': 'mice',
    'nucleus': 'nuclei',
    'person': 'people',
    'phenomenon': 'phenomena',
    'potato': 'potatoes',
    'self': 'selves',
    'syllabus': 'syllabi',
    'tomato': 'tomatoes',
    'torpedo': 'torpedoes',
    'veto': 'vetoes',
    'woman': 'women',
    }


def make_plural(noun):
    """Make noun plural.

    Modified from: http://www.diveintopython.net/dynamic_functions/stage1.html

    :param str noun: noun
    :rtype: str
    """
    if not noun:
        return ''
    plural = ABERRANT_PLURAL_MAP.get(noun)
    if plural:
        return plural
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


def main(string1, string2, file_path):
    """Main function.

    :param str string1
    :param str string2
    :param str file_path
    :rtype: str
    """
    substring = find_substring(string1, string2)
    if is_noun(substring, file_path):
        return make_plural(substring)
    return ''


if __name__ == '__main__':
    print(main(string1=str(raw_input()),
               string2=str(raw_input()),
               file_path='nounlist.txt'))
