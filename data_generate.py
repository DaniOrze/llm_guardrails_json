from guardrails import Guard
from openai import OpenAI
from dotenv import load_dotenv
import os
from guardrails.hub import ValidJson


load_dotenv()

guard = Guard().use(ValidJson, on_fail="exception")
# Configurar o LLM
api_key = os.getenv("OPENAI_KEY_SECRET")

client = OpenAI(api_key=api_key)

# Gerar dados com o LLM
prompt = """
Gere exatamente 2 registros sintéticos no seguinte formato sem incluir outra coisa na resposta e os dias da semana devem ser em Português-Brasil e pode ter mais de um horário para o mesmo medicamento:

[{"name": "string", "dosage": 0, "administrationSchedules": [{"time": "string", "daysOfWeek": ["string"]}], "startDate": "2024-12-04", "endDate": "2024-12-04", "observations": "string"}]
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

# Validar e formatar os dados
print(response.choices[0].message.content)
validated_data = guard.validate(response.choices[0].message.content)
print(validated_data.validation_passed)