from langdetect import detect, detect_langs
from langdetect import DetectorFactory


def detect_language(sentence):

    DetectorFactory.seed = 0

    #Dictionary of ISO 639-1 standard language codes : language name in English, in case we need it?

    languages = {'af' : 'Afrikaans', 'ar' : 'Arabic', 'bg' : 'Bulgarian', 'bn' : 'Bengali', 'ca' : 'Catalan',
                 'cs' : 'Czech', 'cy' : 'Welsh', 'da' : 'Danish', 'de' : 'German', 'el' : 'Greek',
                 'en' : 'English', 'es' : 'Spanish', 'et' : 'Estonian', 'fa' : 'Persian', 'fi' : 'Finnish',
                 'fr' : 'French', 'gu' : 'Gujarati', 'he' : 'Hebrew', 'hi' : 'Hindi', 'hr' : 'Croatian',
                 'hu' : 'Hungarian', 'id' : 'Indonesian', 'it' : 'Italian', 'ja' :'Japanese', 'kn' : 'Kannada',
                 'ko' : 'Korean', 'lt' : 'Lithuanian', 'lv' : 'Latvian', 'mk' : 'Macedonian', 'ml' : 'Malayalam',
                 'mr' : 'Marathi', 'ne' : 'Nepali', 'nl' : 'Dutch', 'no' : 'Norwegian', 'pa' : 'Punjabi',
                 'pl' : 'Polish', 'pt' : 'Portuguese', 'ro' : 'Romanian', 'ru' : 'Russian', 'sk' : 'Slovak',
                 'sl' : 'Slovenian', 'so' : 'Somali', 'sq' : 'Albanian', 'sv' : 'Swedish', 'sw' : 'Swahili',
                 'ta' :'Tamil', 'te' : 'Telugu', 'th' :'Thai', 'tl' :'Tagalog', 'tr' : 'Turkish',
                 'uk' : 'Ukrainian', 'ur' : 'Urdu', 'vi' : 'Vietnamese', 'zh-cn' : 'Chinese', 'zh-tw' :'Taiwanese Mandarin'
    }

    target_languages = ['bg', 'cs', 'da', 'de', 'el', 'en', 'es', 'et',
                        'fi', 'fr', 'hu', 'id', 'it', 'ja', 'lt', 'lv', 'nl',
                        'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'tr', 'sv', 'zh']

    lang = detect(sentence.capitalize())

    if lang not in target_languages:
        return f"I'm sorry, I don't speak {languages[lang]}. Please try a different language."

    return lang

if __name__ == '__main__':
    print(detect_language('wie geht es dir?'))
