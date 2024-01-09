import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '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'


def generate_sql_query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 Turbo engine
        prompt=prompt,
        max_tokens=50,  # Adjust as needed
        stop=None  # Let the model decide when to stop
    )
    return response.choices[0].text.strip()


def main():
    st.title("Translate to SQL Query")

    user_input = st.text_area("Enter your data question:", value="Translate the following text to SQL: ")

    if st.button("Translate to SQL"):
        if user_input:
            sql_query = generate_sql_query(user_input)
            st.write("Generated SQL Query:")
            st.code(sql_query, language="sql")
        else:
            st.warning("Please enter a data question.")


if __name__ == "__main__":
    main()
