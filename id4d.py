import streamlit as st
import pandas as pd
import os
import math

     
st.set_page_config(
    page_title="ID4D", layout="wide"
)

#st.write(os.listdir('.'))
open('test.tmp','w').write('test')

st.header("DTA policy resource")
st.image("https://dta-www-drupal-20180130215411153400000001.s3.ap-southeast-2.amazonaws.com/s3fs-public/images/index/dta-logo-thumb_9.png")
st.subheader("Facial image quality stamndards")
st.markdown("""

# ISO/IEC 19794-5

ISO 19794-5 is an information technology standard that relates to biometric data interchange formats and is intended to provide a face image format for face recognition applications requiring exchange of face image data. This standard also provides information for the best practice of photography of faces, particularly in the ‘passport style’ for the creation of identity documents. All references to ‘quality scores’ are given in the context of sending files between endpoints, and the only reference to ‘sample quality’ is a direct refence to ISO 29794-1.

ISO 19794-5 does provide information relevant to quality scores, however this information is mostly related to the standardised storage and interchange of facial images, largely in the context of scene-controlled passport-style images for the purposes of creating definitive biometric anchors.

# ISO/IEC 29794-5

ISO 29794-5 is an information technology standard that relates to biometric sample quality and provides to definitions and specific methodologies for the computation of objective, qualitative quality scores for facial images. Additionally, this standard discusses the quality aspects of a facial image that will affect recognition outcomes and matching accuracy.


""")
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
    
