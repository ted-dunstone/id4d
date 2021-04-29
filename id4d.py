import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ID4D", layout="wide"
)

st.sidebar.header('ID4D')
st.sidebar.write('The following app will help to select standards should be utilized as part of a foundational identity system.')
st.sidebar.write('The answers provided below will customise the standards list.')
modalities=st.sidebar.select_slider("Population Size",['1-5M','5-50M','50-100M','100M+'])
modalities=st.sidebar.multiselect("Modalities",['Face','Fingerprint','Iris'])
apptype=st.sidebar.multiselect("Applications Required",['Foundational ID','Population Registry'])

standards = pd.read_csv('standards.csv')
#df = pd.DataFrame({'a':[1,2,3,4],'b':[1,2,3,4]})
#st.write(modalities)
standards.sort_values('Category')
# ![Image Description](https://id4d.worldbank.org/themes/id4d/logo.png)
if modalities and apptype:
    st.write(f'''
        
        # Standards Requirements

        The following are base level requirements that are recommended for a 
        foundational ID having modilities 
        *{','.join(modalities)}*
        ''')
    last_cat = ""
#    modalities.extend(['All'])
    standards=standards[standards['Modality'].isin(modalities+['All'])]
    
    for row in standards.itertuples():
        if type(row.Standard)==type(''):
            if row.Category!=last_cat:
                st.header(row.Category)
            cols = st.beta_columns(3)
            cols[0].write('**'+row.Standard+'**')
            cols[1].write(row.Description)
            if row.Modality!='All':
                cols[1].write('Modality :'+row.Modality)
            #cols[2].write(row.Category)
            last_cat = row.Category
    
