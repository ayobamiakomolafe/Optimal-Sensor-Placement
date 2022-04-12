def  main():
    import streamlit as st
    st.set_page_config(page_title='OPTIMAL SENSOR PLACEMENT',layout="wide")
    from PIL import Image
    import pandas as pd
    with st.form('OPTIMAL SENSOR PLACEMENT'):
        st.markdown("<h1 style='text-align: center; color: green;'>OPTIMAL SENSOR PLACEMENT</h1>", unsafe_allow_html=True)

        container_1=st.container()
        container_2=st.container()
        container_3=st.container()
        container_4=st.container()
        container_5=st.container()
        container_6=st.container()


        with container_1:
            col1, col2=st.columns(2)
            Sensor_Data=col1.file_uploader('Sensor Data', type=['csv','xlsx'])
            Sensor_Coordinate_Data=col2.file_uploader('Sensor Co-ordinate Data', type=['csv', 'xlsx'])
        
        
        with container_2:
            col3, col4,col5= st.columns(3)
            Dynamic_Partition=col3.number_input('Dynamic Partition',min_value=1, step=1, value=20)
            Cluster_Number=col4.number_input('Cluster/Total Number of Sensors', min_value=1, step=1, value=20)
            Number_of_green_house_section=col5.number_input('Number of Green-house Section', min_value=1, step=1, value=7)

        
        with container_4:
            none_key_word_arguments=st.multiselect('None Key Word Parameter: ', ['humid', 'dewpt', 'spev', 'humr', 'comb', 'entha', 'temp'] )
            
    
        column_data1 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7','B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7','C1', 'C2', 'C3','C4', 'C5', 'C6', 'C7','D1', 'D2', 'D3', 'D4',
                       'D5', 'D6', 'D7','E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7','F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7','G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7','H1',
                       'H2', 'H3', 'H4', 'H5', 'H6', 'H7']
                        
        column_data_default = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7','B1', 'B2', 'B3', 'B4', 'B5', 'B6','B7','C1', 'C2', 'C3','C4', 'C5', 'C6', 'C7','D1', 'D2', 'D3', 'D4',
                       'D5', 'D6', 'D7','E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7','F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7','G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7','H1',
                       'H2', 'H3', 'H4', 'H5', 'H6', 'H7']
        
        with container_5:
            column_data=st.text_area('Specify the Column name(s) for the Data(Seperate with comma e.g Col1, Col2, Col3 etc...), (AUTOMATICALLY SETS TO USE DEFAULT VALUES) :',
                                      value=column_data1, placeholder ='Seperate with comma e.g Col1, Col2, Col3 etc...')
            
    
                

        button= st.form_submit_button('RUN')
    
    
        
        
            
            
         
    if button:
        if column_data== str(column_data1):
            column_data= column_data_default
        else:
            column_data= column_data.split(',')
        try:
            import warnings
            warnings.filterwarnings("ignore")
            import optimal_new_AB
            with st.spinner('RUNNING...'):
                import time
                #time.sleep(2)
                
                testing = optimal_new_AB.optimal_sensor (Sensor_Data, Sensor_Coordinate_Data, Dynamic_Partition, Cluster_Number, column_data, Number_of_green_house_section,none_key_word_arguments)
                testing.model()
            for i in range(2):
                st.write('\n')
            with st.expander("VIEW RESULT"):
                df1=pd.read_csv('ed_df.csv', index_col=0)
                df2=pd.read_csv('ia_df.csv', index_col=0)
                st.table(df1)
                st.table(df2)
                for i in none_key_word_arguments:
                    
                    title="<h1 style='text-align: center; color:white;'>" + i + "</h1>"
                    st.markdown(title, unsafe_allow_html=True)
                    
                    image_path1= 'silhouette_plot_'+ i + '.png' 
                    image_path2= 'polygon_plot_'+ i + '.png'
                    image_path3= 'polygon_opt_sensor_'+ i + '.png'
                    image_path4= 'install_opt_sensor_'+ i + '.png'
                    image_path5= 'dynamic_plot_'+ i + '.png'
                    image1 = Image.open(image_path1)
                    st.image(image1, caption= 'silhouette_plot_'+ i)
                    image2 = Image.open(image_path2)
                    st.image(image2,caption='polygon_plot_'+ i )
                    image3 = Image.open(image_path3)
                    st.image(image3, caption= 'polygon_opt_sensor_'+ i)
                    image4 = Image.open(image_path4)
                    st.image(image4, caption= 'install_opt_sensor_'+ i)
                    image5 = Image.open(image_path5)
                    st.image(image5, caption= 'dynamic_plot_'+ i)

                    
        except Exception as e:
            st.write(e)
            st.error('A WRONG/EMPTY INPUT WAS DETECTED,KINDLY CHECK AND RUN AGAIN')


                
import streamlit 
import sys
from streamlit import cli as stcli
if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
