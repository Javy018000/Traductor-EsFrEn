from transformers import pipeline

# Pipeline para traducción de español a inglés
pipe_es_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")

# Pipeline para traducción de inglés a francés
pipe_en_to_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

# Texto de ejemplo
texto_es = "El sol brilla en el cielo azul."


# Traducción de español a inglés
resultado_es_to_en = pipe_es_to_en(texto_es)
print("Traducción de español a inglés:", resultado_es_to_en[0]['translation_text'])

# Traducción de inglés a francés
resultado_en_to_fr = pipe_en_to_fr(resultado_es_to_en[0]['translation_text'])
print("Traducción de inglés a francés:", resultado_en_to_fr[0]['translation_text'])
