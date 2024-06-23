import argostranslate.package
import argostranslate.translate

from_code = "ar"
to_code = "en"

def download_and_install_translate():
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

def translate_to_en(ar_word):
    return ""
    translatedText = argostranslate.translate.translate(ar_word, from_code, to_code)
    return translatedText