from googletrans import Translator, LANGUAGES

def translate_with_googletrans(phrase, target_language="en"):
    translator = Translator()

    try:
        translation = translator.translate(phrase, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return phrase


allowed_languages = {"ar": "Arabic", "de": "German", "nl": "Dutch", "es": "Spanish"}


user_phrase = input("Enter a sentence: ")
allowed_language_codes = ', '.join([f"{code} for {language}" for code, language in allowed_languages.items()])
user_language = input(f"Enter the target language code (e.g., {allowed_language_codes}): ")

if user_language not in allowed_languages:
    print("Translation for the specified language is not allowed.")
else:
    translated_phrase = translate_with_googletrans(user_phrase, user_language)
    print("Translated phrase:", translated_phrase)
