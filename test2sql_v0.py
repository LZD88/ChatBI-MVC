"""
第5课实战版本0: Zero-shot基础版
仅提供角色定义和用户问题，不注入任何 Schema 信息。
无 Schema 信息时 LLM 生成 SQL 的准确性边界。

运行方式:
uv run python text2sql_v0.py
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()

def generate_sql(query: str) -> str:
    # call openai llm to generate sql
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL")
    )

    prompt = f"请根据以下自然语言查询生成对应的SQL语句：\n\n{query}\n\n请使用标准的 SQL语法，并确保生"

    response = client.chat.completions.create(
        model=os.environ.get("LLM_MODEL"),
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
    )

    output = response.choices[0].message.content
    sql = re.sub(r'```sql|```', '', output).strip()
    return sql

if __name__ == "__main__":
    query = "欧洲市场最近三个月的销售额是多少？"
    print(generate_sql(query))