import os
import re
import logging
import json
import math
import getpass
import shutil
import urllib
import base64
import string
from datetime import datetime
from collections import OrderedDict
from functools import wraps
from time import time
from random import randint, choice
from django.core.validators import validate_email
from django.core.mail.message import EmailMultiAlternatives

# from common.constants import FREQUENT_NAMES_LIST, CURRENCY_ISO_CODES

logger = logging.getLogger('GROUPIFY')


# def get_input(text, allow_blank=False, password_field=False):
#     method = raw_input if not password_field else getpass.getpass
#     v = ''
#     if not allow_blank:
#         while not v:
#             v = method(text)
#     else:
#         v = method(text)
#     return v


# def is_valid_email(email):
#     """Return True if given string is a valid email ID"""
#     if re.match('[^@]+@[^@]+\.[^@]+', email) is None:
#         logger.debug("IMPORTANT: Email ID [" + email + "] is invalid!")
#         return False
#     else:
#         return True


# def get_email_domain(email):
#     try:
#         return email.split("@")[1]
#     except (ValueError, AttributeError, IndexError):
#         return ''


# # Custom validator to validate comma separated emails
# def validate_comma_separated_emails(value):
#         if not value:
#             return False
#         value = value.split(',')
#         for email in value:
#             validate_email(email.strip())


def slugify(name):
    """Return slug for the given name"""
    if name is None:
        return None
    if not isinstance(name, str):
        name = unicode(name)

    name = name.strip().lower()
    # Any non word characters (letters, digits, and underscores) are replaced by '-'
    name = re.sub(r'\W+', '-', name)
    # Removing any trailing or leading dash
    name = re.sub(r'^-|-$', '', name)
    #Replace multiple continuous hipens with one
    name = re.sub('-+', '-', name)
    return name


# def remove_special_characters(name):
#     """Remove special characters and make it lower case"""
#     name = re.sub(r'[^\w\s]+', '', name)
#     return name.lower()


# def remove_duplicates(l):
#     """Remove duplicates from list while preserving the order"""
#     return list(OrderedDict.fromkeys(l))


# def stripall(val):
#     """Remove all dots, spaces, brackets, commas, apostrophes"""
#     return re.sub(r'\.|\s|\(|\)|\,|\'', '', val).lower()


# def is_integer(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False


# # Removes all the non ASCII characters from the string
# def removeNonAsciiChars(s):
#     if not isinstance(s, str) and not isinstance(s, unicode):
#         return str(s)
#     if not s:
#         return s
#     return "".join(i for i in s if ord(i) < 128)


# # Returns empty dict with given fields
# def get_empty_dict(fields):
#     obj = {}
#     for field in fields:
#         obj[field] = ''
#     return obj


# # Checks if dict is empty, i.e. all values are blank
# def is_empty_dict(obj):
#     for value in obj.values():
#         if value != None and value != '':
#             return False
#     return True


# def get_string_similarity_ratio(value1, value2):
#     """Get the similarity ratio between two given strings. A number between 0 and 1"""
#     import difflib
#     return difflib.SequenceMatcher(a=value1.lower(), b=value2.lower()).ratio()


# def is_string_similar(value1, value2, accuracy):
#     """
#     Checks similarity of two strings and returns true/false based on desired accuracy
#     """
#     if get_string_similarity_ratio(value1, value2) >= accuracy:
#         return True
#     else:
#         return False


# def is_name_similar(name1, name2, accuracy):
#     """
#     Check if two names are similar. They are similar only if:
#     1. One of the words in the two names match
#     2. The string similarity ratio is better than the given
#        accuracy, after removing the common words
#     """
#     common_words = set(name1.split(" ")).intersection(name2.split(" "))
#     if len(common_words) < 1:
#         return False
#     for word in common_words:
#         name1 = name1.replace(word, "")
#         name2 = name2.replace(word, "")
#     return is_string_similar(name1.strip(), name2.strip(), accuracy)


# def get_name_similarity_score(name1, name2, consider_close_words=False):
#     """Get a score that represents the similarity between two given names
#     Score = 50*(number of matching non frequent words with min 3 chars)
#             + 30*(number of matching frequent words)
#             + 20*(number of matching words with less than 3 characters)
#             if consider_close_words is True
#                 + 10*(number of close words)"""
#     words1 = filter(None, [remove_special_characters(word) for word in re.split("[\s|\.]", name1)])
#     words2 = filter(None, [remove_special_characters(word) for word in re.split("[\s|\.]", name2)])
#     common_words = list(set(words1) & set(words2))
#     if not common_words:
#         return 0
#     score = 0
#     for word in common_words:
#         if len(word) < 3:
#             score += 20
#         elif word in FREQUENT_NAMES_LIST:
#             score += 30
#         else:
#             score += 50

#     if consider_close_words:
#         words1 = [word for word in words1 if word not in common_words]
#         words2 = [word for word in words2 if word not in common_words]
#         for word1 in words1:
#             for word2 in words2:
#                 if is_string_similar(word1, word2, 0.8):
#                     score += 10

#     return score


# def get_initial_matching_score(name1, name2):
#     """Ignore common words and among the remaining words find out if there is are words matching
#     initials. For eg: M matches Maneru, V matches Varma, Ch matches Choudary"""
#     score = 0
#     words1 = filter(None, [remove_special_characters(word) for word in re.split("[\s|\.]", name1)])
#     words2 = filter(None, [remove_special_characters(word) for word in re.split("[\s|\.]", name2)])
#     for word in words1:
#         if word in words2:
#             words1.remove(word)
#             words2.remove(word)
#     for word1 in words1:
#         if word1 not in words2:
#             for word2 in words2:
#                 if len(word1) <= 2 and word1 == word2[:len(word1)]:
#                     try:
#                         words1.remove(word1)
#                         words2.remove(word2)
#                         score += 40
#                     except ValueError:
#                         pass
#                 if len(word2) <= 2 and word2 == word1[:len(word2)]:
#                     try:
#                         words1.remove(word1)
#                         words2.remove(word2)
#                         score += 40
#                     except ValueError:
#                         pass

#     return score


# def get_month_year_from_date_string(dt_str, dt_format):
#     try:
#         dt = datetime.strptime(dt_str, dt_format)
#         return [dt.month, dt.year]
#     except ValueError:
#         return [None, None]


# def get_key_from_value_in_dict(obj, value):
#     for key, val in obj.items():
#         if val == value:
#             return key
#     return None


# def get_display_name_from_tuples(tuples, key):
#     """
#     Input:
#     Tuple -
#     DUP_TYPES = ((DT_ALIAS, "Alias"),
#              (DT_SPELL_CORRECTION, "Spell Mistake"),
#              (DT_BULK_UPLOAD, "Bulk upload Synonym"))
#     Key -  DT_ALIAS

#     Output:
#     "Alias"

#     """
#     for mapping in tuples:
#         if mapping[0] == key:
#             return mapping[1]
#     return None


# def copy_file(curr_file_path, dest_folder_path, dest_filename=''):
#     """Copy the file from the current path to the destination directory, creating the
#     directory if necessary. Return the file path after copy"""
#     if not dest_filename:
#         dest_filename = os.path.basename(curr_file_path)
#     else:
#         curr_extension = os.path.splitext(curr_file_path)[1]
#         dest_filename = dest_filename + curr_extension
#     if not os.path.isdir(dest_folder_path):
#         logger.info("Creating directory [" + dest_folder_path + "]")
#         os.makedirs(dest_folder_path)
#     dest_file_path = dest_folder_path + '/' + dest_filename
#     try:
#         shutil.copy(curr_file_path, dest_file_path)
#         return dest_file_path
#     except:
#         logger.error("Exception while copying file [" + curr_file_path + "] to ["
#                      + dest_folder_path + "]")
#         return ''


# def timed(f):
#     @wraps(f)
#     def wrapper(*args, **kwds):
#         start = time()
#         result = f(*args, **kwds)
#         elapsed = (time() - start)
#         print "$$$$$$--------- %s took '%s sec' time to finish" % \
#                         (f.__name__.rjust(25), str(math.ceil(elapsed * 1000) / 1000))
#         return result
#     return wrapper


# def show_differences_in_json_strings(a, b):
#     """Show differences between two jsons.
#     Assumption 1: at a parent level it is a dict.
#     Assumption 2: no complex structures. Just dicts, lists & simple types.
#     Assumption 3: Lists can only contain simple types
#     """
#     a = json.loads(a)
#     b = json.loads(b)
#     show_differences_in_dicts(a, b)


# def show_differences_in_dicts(a, b):
#     diff_keys = list(set(a.keys()).union(set(b.keys())) - set(a.keys()).intersection(set(b.keys())))
#     if diff_keys:
#         logger.info("Added/removed keys: " + str(diff_keys))
#     for ka, va in a.items():
#         if ka in diff_keys:
#             continue
#         if type(va) == dict:
#             show_differences_in_dicts(va, b[ka])
#         elif type(va) == list:
#             show_differences_in_lists(va, b[ka])
#         elif va != b[ka]:
#             logger.info("Value for " + ka + " is different. " + str(va) + " vs " + str(b[ka]))


# def show_differences_in_lists(a, b):
#     if len(a) != len(b):
#         logger.info("Lengths of lists different. \n" + str(a) + "\n" + str(b))
#         return
#     for i in range(len(a)):
#         if type(a[i]) == dict:
#             show_differences_in_dicts(a[i], b[i])
#         elif type(a[i]) == list:
#             show_differences_in_lists(a[i], b[i])
#         elif a[i] != b[i]:
#             logger.info("List values different. " + str(a[i]) + " vs " + str(b[i]))


# def get_first_and_last_names(name):
#     names = name.split(' ', 1)
#     return (names[0], names[1] if len(names) > 1 else '')


# def send_html_mail(subject, html_content, sender, recipients):
#     """Send a HTML email from sender to one or many recipients"""
#     if not isinstance(recipients, list):
#         recipients = [recipients]
#     msg = EmailMultiAlternatives(subject, '', sender, recipients)
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()


# def get_extension_from_mime_type(mime_type):
#     if mime_type == 'image/jpeg' or mime_type == 'image/pjpeg':
#         return '.jpg'
#     elif mime_type == 'image/png':
#         return '.png'
#     elif mime_type == 'image/gif':
#         return '.gif'
#     elif mime_type == 'image/svg+xml':
#         return '.svg'
#     logger.error('Unknown MIME type [' + mime_type + ']')
#     return ''


# def do_names_exactly_match(name1, name2):
#     """Perform a match on the two names based on these criteria
#     1. Dont consider word order
#     2. Dont consider case
#     3. Dont consider special characters"""
#     name1 = re.sub(r'[^a-zA-Z0-9 ]', r'', name1.lower())
#     name2 = re.sub(r'[^a-zA-Z0-9 ]', r'', name2.lower())
#     name1_words = filter(None, name1.split(' '))
#     name2_words = filter(None, name2.split(' '))
#     if len(name1_words) == len(name2_words):
#         name1_words.sort()
#         name2_words.sort()
#         if name1_words == name2_words:
#             return True
#     return False


# def download_file_from_url(url, directory):
#     """Download the file from the given url and save it to the given directory.
#     If the directory is not present, create it.
#     Return complete path to the file that has been created."""
#     response = urllib.urlopen(url)
#     filename = os.path.basename(url)
#     if not os.path.isdir(directory):
#         os.makedirs(directory)
#     path = directory + '/' + filename
#     with open(path, 'wb+') as destination:
#         destination.write(response.read())
#     logger.debug("Downloaded file from [" + url + "] to [" + path + "]")
#     return path


def format_and_split_name(name):
    """Given a name, do some basic formatting and return the first name and last name"""
    if not name:
        return ''
    name = removeNonAsciiChars(name).strip().title()
    words = name.split(' ', 1)
    if len(words) > 1:
        return words[0], words[1]
    else:
        return words[0], ''


# def get_random_number(num_digits):
#     """Generate and return a random number with the given number of digits"""
#     range_start = 10 ** (num_digits - 1)
#     range_end = (10 ** num_digits) - 1
#     return randint(range_start, range_end)


# def get_random_string(length):
#     """Generate and return a random string with given number of alphabets"""
#     return ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))


# def slugify_filename(filename):
#     """Slugify a filename"""
#     name, ext = os.path.splitext(filename)
#     return slugify(name) + ext


# def simple_encode(secret, msg):
#     """A simple utility encryption function"""
#     enc = []
#     for i in range(len(msg)):
#         key_c = secret[i % len(secret)]
#         enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)
#         enc.append(enc_c)
#     return base64.urlsafe_b64encode("".join(enc))


# def simple_decode(secret, encoded):
#     """A simple utility decryption function for the above encryption function"""
#     dec = []
#     enc = base64.urlsafe_b64decode(encoded)
#     for i in range(len(enc)):
#         key_c = secret[i % len(secret)]
#         dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
#         dec.append(dec_c)
#     return "".join(dec)


# def construct_query_string(query_dict):
#     val = '?'
#     for k, v in query_dict.items():
#         val += str(k) + '=' + str(v) + '&'
#     return val[:-1]


# def get_currency_iso_code(currency):
#     return CURRENCY_ISO_CODES.get(currency, '')


# def replace_apostrophe(text):
#     """To fix an issue with froala editor
#     It users &apos; for the apostrophe character(') but that is not standard so Django doesn't escape it
#     So without this fix users would see &apos; on the page wherever an apostrophe was used."""
#     return text.replace('&apos;', '&#39;')
