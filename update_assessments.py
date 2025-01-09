import requests
from dotenv import load_dotenv
import os
import yaml

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém o token do arquivo .env
TOKEN = os.getenv("TOKEN")
COURSE_INSTANCE_ID = os.getenv("COURSE_INSTANCE_ID")  # Substitua pelo ID do curso correto
API_URL = f"https://us.prairielearn.com/pl/api/v1/course_instances/{COURSE_INSTANCE_ID}/assessments"

def get_assessments(token, api_url):
    """Obtém todos os assessments de um curso."""
    if not token:
        print("Erro: Token não encontrado. Certifique-se de que está definido no arquivo .env.")
        return None
    
    headers = {
        "Private-Token": token
    }
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Retorna os dados dos assessments
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        print(f"Mensagem: {response.text}")
        return None

if __name__ == "__main__":
    assessments = get_assessments(TOKEN, API_URL)
    if assessments:
        assessment_dict = {}
        for assessment in assessments:
            assessment_dict[assessment["assessment_name"]] = assessment["assessment_id"]

        with open(f'mkdocs.yml', 'r') as f:
            data = yaml.safe_load(f)
            keys = data["extra"]["custom_variables"].keys()
            for key in keys:
                if key.startswith("pl_"):
                    tema = key[3:]
                    id = assessment_dict.get(tema+"/exercises")
                    data["extra"]["custom_variables"][key] = f'https://us.prairielearn.com/pl/course_instance/{COURSE_INSTANCE_ID}/assessment/{id}'
        with open(f'mkdocs.yml', 'w') as file:
            yaml.dump(data,file,sort_keys=False,allow_unicode=True)
        print('done!') 
            
    