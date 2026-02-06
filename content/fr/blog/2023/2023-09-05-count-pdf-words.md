---
title: "How to count number of words in a pdf file from Linux cli"
date: 2023-09-05T04:30:03+00:00
# weight: 1
# aliases: ["/first"]
# tags: ["first"]
author: "Me"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
# description: "Desc Text."
# canonicalURL: "https://canonical.url/to/page"
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
categories:
    - Development
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
# editPost:
#     URL: "https://github.com/<path_to_repo>/content"
#     Text: "Suggest Changes" # edit text
#     appendFilePath: true # to append file path to Edit link
---
### Utilisation de `pdftotext` :

1. **Installation** :
    - Si ce n’est pas déjà installé, vous devrez installer le paquet `poppler-utils`, qui inclut `pdftotext` :
    ```
    sudo apt install poppler-utils
    ```
    ou
    ```
    yum install poppler-utils
    ```
    selon votre distribution.

2. **Utilisation** :
    - Une fois installé, vous pouvez convertir un PDF en texte et compter les mots comme suit :
    ```
    pdftotext input.pdf - | wc -w
    ```
    Ici, `input.pdf` est votre fichier PDF source, et `wc -w` compte le nombre de mots. Le `-` dans `pdftotext` indique que la sortie doit être envoyée à stdout, qui est ensuite redirigée vers `wc`.

### Utilisation de `pdfgrep` :

1. **Installation** :
    - Installez `pdfgrep` à l’aide de votre gestionnaire de paquets :
    ```
    sudo apt install pdfgrep
    ```
    ou
    ```
    yum install pdfgrep
    ```

2. **Utilisation** :
    - `pdfgrep` est généralement utilisé pour la recherche de motifs, mais vous pouvez l’utiliser pour correspondre à tout caractère de mot et le rediriger vers `wc -w` comme suit :
    ```
    pdfgrep -o '\w+' input.pdf | wc -w
    ```
    Cela peut être plus lent, et est généralement utile uniquement lorsque vous cherchez des mots spécifiques.

### Utilisation de Python avec PyPDF2 :

Vous pouvez également créer un petit script Python pour effectuer cette tâche en utilisant la bibliothèque `PyPDF2`.

1. **Installation** :
    - Installez PyPDF2 à l’aide de pip :
    ```
    pip install PyPDF2
    ```

2. **Utilisation** :
    - Voici un simple script Python que vous pouvez utiliser :

    ```python
    import PyPDF2

    def count_words_in_pdf(file_path):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            total_words = 0
            for i in range(reader.numPages):
                page = reader.getPage(i)
                text = page.extractText()
                total_words += len(text.split())
        return total_words

    if __name__ == "__main__":
        file_path = "input.pdf"
        print(count_words_in_pdf(file_path))
    ```

    Enregistrez ce script, rendez-le exécutable, puis exécutez-le. Il lira `input.pdf` et affichera le nombre de mots.

### Utilisation de `pdf2txt.py` du paquet `pdfminer` :

1. **Installation** :
    - Vous pouvez installer `pdfminer` comme suit :
    ```
    pip install pdfminer.six
    ```

2. **Utilisation** :
    ```
    pdf2txt.py input.pdf | wc -w
    ```
    Cette commande convertira le PDF en texte, puis le redirigera vers `wc` pour compter les mots.

### Considérations sur les performances :

- **Précision** : Toutes les méthodes n’ont pas le même niveau de précision. La mise en page du texte dans les PDFs peut être complexe, et les méthodes ci-dessus pourraient ne pas capturer toutes les subtilités.

- **Vitesse** : Les outils CLI natifs comme `pdftotext` et `pdfgrep` sont généralement plus rapides que les solutions basées sur Python, qui doivent démarrer un interpréteur Python.

- **Complexité** : `pdftotext` et `pdfgrep` sont plus simples à utiliser pour des tâches simples, mais les solutions basées sur Python offrent plus de flexibilité et de contrôle.

- **Portabilité** : Les outils CLI dépendent de certains paquets qui doivent être installés, mais un script Python pourrait être plus portable, notamment si vous devez l’exécuter sur différents systèmes.

Le choix de la méthode dépendra probablement de vos besoins spécifiques. Si vous avez besoin d’une solution rapide et simple, `pdftotext` redirigé vers `wc` est facile et efficace. Pour des besoins plus complexes, comme le traitement de plusieurs PDFs, l’intégration de logique supplémentaire, ou même l’utilisation de techniques avancées d’analyse de texte (comme le traitement du langage naturel), vous pourriez préférer les solutions basées sur Python. Elles offrent les briques de base pour concevoir une solution sur mesure qui peut évoluer avec vos besoins. L’élégance de la ligne de commande Linux réside dans le fait qu’elle propose une vaste gamme d’outils pouvant être combinés de presque une infinité de façons pour résoudre des problèmes, grands comme petits. Ce coffre à outils devient encore plus puissant lorsque vous l’intégrez à des langages de script comme Python, vous permettant ainsi de relever non seulement des tâches de traitement de texte, mais aussi de nombreuses autres défis.
