def get_ai_solution(problem_title: str, problem_description: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Siz global muammolar uchun yechim taklif qiladigan AI assistantsiz."},
            {"role": "user", "content": f"Muammo: {problem_title}\nTavsif: {problem_description}\nIltimos, yechim taklif qiling."}
        ]
    )
    return response["choices"][0]["message"]["content"]
