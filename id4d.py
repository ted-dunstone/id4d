import streamlit as st
import pandas as pd
import os
import math

     
st.set_page_config(
    page_title="ID4D", layout="wide"
)

st.write(os.listdir('.'))
open(str(math.random())+'.tmp','w').

st.sidebar.header('ID4D')
st.sidebar.write('The following app will help to select standards should be utilized as part of a foundational identity system.')
st.sidebar.write('The answers provided below will customise the standards list.')
#modalities=st.sidebar.select_slider("Population Size",['1-5M','5-50M','50-100M','100M+'])
apptype=st.sidebar.multiselect("Applications Required",['Foundational ID','Population Registry'])
modalities=st.sidebar.multiselect("Attributes",['Face','Fingerprint','Iris'])

if st.sidebar.checkbox('Require mobile applications',False):
    modalities+=['Mobile'] 
show_link = st.sidebar.checkbox('Show link to Standard')
standards = pd.read_csv('standards.csv')
#df = pd.DataFrame({'a':[1,2,3,4],'b':[1,2,3,4]})
#st.write(modalities)
# ![Image Description](https://id4d.worldbank.org/themes/id4d/logo.png)
checked={}

if modalities and apptype:
    with st.beta_expander('Settings',True):
        st.write(f'''
            
            # Standards Requirements

            The following are base level requirements that are recommended for a 
            foundational ID having attributes  
            *{', '.join(modalities)}*
            ''')
        last_cat = ""
    #    modalities.extend(['All'])
        standards=standards[standards['Modality'].isin(modalities+['All'])]
        standards=standards.sort_values('Category')
        for row in standards.itertuples():
            if type(row.Standard)==type(''):
                if row.Category!=last_cat:
                    st.header(row.Category)
                cols = st.beta_columns(4)
                checked[row.Standard]=cols[0].checkbox(row.Standard)
                cols[1].write('**'+row.Standard+'**')
                cols[2].write(row.Description)
                if row.Modality!='All':
                    cols[2].write('Attribute :'+row.Modality)
                if show_link:
                    cols[3].write(f"[Link]({row.Link})")
                last_cat = row.Category
    with st.beta_expander('final'):
        st.write(checked)
    
