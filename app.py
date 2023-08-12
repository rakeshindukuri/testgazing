import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Gazing for Fun")
st.title("Data gazing app")

# Upload data
uploaded_file = st.file_uploader("Please upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Display options
    display_option = st.radio("Display Option", ["Full Data", "Single Column", "Single Row"])

    if display_option == "Single Column":
        selected_column = st.selectbox("Select a column", data.columns)
        st.write("Selected Column:")
        st.write(data[selected_column])

    elif display_option == "Single Row":
        selected_row_index = st.slider("Select a row index", 0, len(data) - 1)
        st.write("Selected Row:")
        st.write(data.iloc[selected_row_index])

    else:
        st.write("Full Data:")
        st.write(data)

    # Display graph by user selection
    st.subheader("Data Visualization")
    selected_column = st.selectbox("Select a column for the x-axis", data.columns)
    y_column = st.selectbox("Select a column for the y-axis", data.columns)

    plt.figure(figsize=(11, 6))
    plt.scatter(data[selected_column], data[y_column])
    plt.xlabel(selected_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} vs {selected_column}")
    st.pyplot(plt)

if __name__ == "__main__":
    st.write("Upload a CSV file and visualize the data; Happy data gazing!")
