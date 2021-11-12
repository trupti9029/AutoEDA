

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.image as mpimg

imageha = mpimg.imread('eda.png')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title='Automated Exploratory Data Analysis App',layout='wide')

st.write("""
# Automated Exploratory Data Analysis App

""")

st.image(imageha)

Selection = st.sidebar.selectbox("Select Option", ("Exploratory Data Analysis App","Source Code"))

if Selection == "Exploratory Data Analysis App":

        #data_file = st.file_uploader("Upload a csv file", type=["csv"])
        #data = pd.read_csv(data_file)
        
        st.title('Data Analysis')
        uploaded_file = st.file_uploader("Choose a file")
        
        if uploaded_file is not None:
            uploaded_file.seek(0)
            data = pd.read_csv(uploaded_file, low_memory=False)
        
            #pr = ProfileReport(data, explorative=True)

            #st_profile_report(pr)
        
            st.title('** Glimpse of dataset **')
            st.table(data.head(5))
        
            st.title('** Dataset Details **')
            st.write(data.shape)
        
            st.title('** Dataset Variables **')
            st.table(data.columns)
            
            st.title('** Variables Description **')
            st.table(data.describe())
            
            st.title('** Variables with Null Values **')
            st.table(data.isnull().sum())
            
            st.title("** Unique Values in the variables **")
            st.table(data.nunique())
            
            st.title("** Correlation Matrix **")
            st.write(sns.heatmap(data.corr(),annot=True,fmt='.1f'))
            st.pyplot(use_container_width=False)
            
            for i in data.columns:
                
                st.title("** Variable **")
                st.title(i)
                st.write("Value Counts of the Variable", i)

                st.write(data[i].value_counts())
                uniq = data[i].nunique(dropna = False)
                
                if uniq < 7:
                    
                    st.write(sns.countplot(data[i]))
                    st.pyplot(use_container_width=False)
                    
                
                else:
                    
                    st.write(sns.distplot(data[i], hist=True, kde=True, bins=int(180/5), color = 'darkblue', hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4}))
                    st.pyplot(use_container_width=False)
else:
    
    st.subheader("Source Code")
    
    code = """
    
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title='Automated Exploratory Data Analysis App',layout='wide')

st.write(
 Automated Exploratory Data Analysis App




Selection = st.sidebar.selectbox("Select Option", ("Exploratory Data Analysis App","Source Code"))

if Selection == "Exploratory Data Analysis App":

        #data_file = st.file_uploader("Upload a csv file", type=["csv"])
        #data = pd.read_csv(data_file)
        
        st.title('Report Analysis')
        uploaded_file = st.file_uploader("Choose a file")
        
        if uploaded_file is not None:
            uploaded_file.seek(0)
            data = pd.read_csv(uploaded_file, low_memory=False)
        
            #pr = ProfileReport(data, explorative=True)

            #st_profile_report(pr)
        
            st.title('** Glimpse of dataset **')
            st.table(data.head(5))
        
            st.title('** Dataset Details **')
            st.write(data.shape)
        
            st.title('** Dataset Variables **')
            st.table(data.columns)
            
            st.title('** Variables Description **')
            st.table(data.describe())
            
            st.title('** Variables with Null Values **')
            st.table(data.isnull().sum())
            
            st.title('** Unique Values in the variables **')
            st.table(data.nunique())
            
            st.title('** Correlation Matrix **')
            st.write(sns.heatmap(data.corr(),annot=True,fmt='.1f'))
            st.pyplot(use_container_width=False)
            
            for i in data.columns:
                
                #if data[i].nunique < 7:
                st.title('** Variable **')
                st.title(i)
                st.write('Value Counts of the Variable', i)

                st.write(data[i].value_counts())
                uniq = data[i].nunique(dropna = False)
                
                if uniq < 7:
                    
                    st.write(sns.countplot(data[i]))
                    st.pyplot(use_container_width=False)
                    #st.countplot(data[i], width=0, height=0, use_container_width=True)
                    
                else:
                    
                    st.write(sns.distplot(data[i], hist=True, kde=True, bins=int(180/5), color = 'darkblue', hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4}))
                    st.pyplot(use_container_width=False)
    """
    st.code(code, language='python')

