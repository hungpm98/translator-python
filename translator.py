def translate(phrase):
    translation = ""
    for letter in phrase:
      if letter in "UEOAIueoai":
        translation = translation + "h"
      else:
        translation = translation + letter
    return translation

print(translate("cate"))