import sys
import os


def sort_properties_file(file_path):
    """Ordina un file .properties in base alle chiavi, mantenendo i commenti iniziali."""

    comments = []
    properties = {}
    with open(file_path, 'r', encoding='latin-1') as file:  # Usa l'encoding corretto
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                comments.append(line)
            elif '=' in line:
                key, value = line.split('=', 1)
                properties[key] = value

    sorted_properties = sorted(properties.items())

    with open(file_path, 'w', encoding='latin-1') as file:
        for comment in comments:
            file.write(f"{comment}\n")
        for key, value in sorted_properties:
            file.write(f"{key}={value}\n")


def process_folder(folder_path):
    count = 0
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".properties"):
                file_path = os.path.join(root, filename)
                try:
                    sort_properties_file(file_path)
                    count += 1
                    print(f"'{count}'File '{file_path}' ordinato con successo.")
                except FileNotFoundError:
                    print(f"Errore: File '{file_path}' non trovato.")
                except Exception as e:
                    print(f"Errore durante l'elaborazione di '{file_path}': {e}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Errore: Percorso della cartella mancante.")
        print("Utilizzo: python script.py <percorso_cartella>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)
