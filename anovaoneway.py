import streamlit as st
import pandas as pd
from scipy.stats import f_oneway
import numpy as np
from scipy.stats import shapiro
import scipy.stats as stats

st.title('ANOVA ONE WAY TEST for Five Populations')

#sidebar
with st.sidebar:
    tipe = st.radio('Tahapan Pengujian', ['1. Uji Normalitas','2. Uji Homogenitas', '3. Uji ANOVA One Way'])
                                        
#banyak data
with st.expander('Data'):
    with st.form('Data'):
     row_1 = st.number_input('Banyak Sampel 1', min_value=3)
     row_2 = st.number_input('Banyak Sampel 2', min_value=3)
     row_3 = st.number_input('Banyak Sampel 3', min_value=3)
     row_4 = st.number_input('Banyak Sampel 4', min_value=3)
     row_5 = st.number_input('Banyak Sampel 5', min_value=3)
     st.form_submit_button('Kirim')

#input data
df_1 = pd.DataFrame(columns=range(1, 2), index=range(1, row_1+1), dtype=float) 
df_1_input = st.experimental_data_editor(df_1, use_container_width=True, key = 1)
df_2 = pd.DataFrame(columns=range(1, 2), index=range(1, row_2+1), dtype=float) 
df_2_input = st.experimental_data_editor(df_2, use_container_width=True, key = 2)
df_3 = pd.DataFrame(columns=range(1, 2), index=range(1, row_3+1), dtype=float) 
df_3_input = st.experimental_data_editor(df_3, use_container_width=True, key = 3)
df_4 = pd.DataFrame(columns=range(1, 2), index=range(1, row_4+1), dtype=float) 
df_4_input = st.experimental_data_editor(df_4, use_container_width=True, key = 4)
df_5 = pd.DataFrame(columns=range(1, 2), index=range(1, row_5+1), dtype=float) 
df_5_input = st.experimental_data_editor(df_5, use_container_width=True, key = 5)

df_1_array = np.array(df_1_input, dtype=int)
df_2_array = np.array(df_2_input, dtype=int)
df_3_array = np.array(df_3_input, dtype=int)
df_4_array = np.array(df_4_input, dtype=int)
df_5_array = np.array(df_5_input, dtype=int)

alpha_value = st.number_input('Nilai Alpha', step=0.001, min_value=0., max_value=1.)

#untuk pengujian normalitas
if tipe == '1. Uji Normalitas':
   st.write('## UJI NORMALITAS')
   st.write('Uji Normalitaas adalah sebuah uji yang dilakukan dengan tujuan untuk menilai sebaran data pada sebuah kelompok data atau variabel, apakah sebaran data tersebut berdistribusi normal ataukah tidak. Salah satu metodenya yaitu dengan uji Shapiro, dimana lks digunakan untuk mengidentifikasi apakah suatu peubah acak berdistribusi normal atau tidak.')
   st.write('Hipotesis:')
   st.write('H0 : Populasi berdistribusi normal')
   st.write('H1 : Populasi tidak berdistribusi normal')
   st.write('Daerah Kritis:')
   st.write('Jika nilai p-value > alpha, maka H0 diterima. Jika nilai p-value < alpha, maka H0 ditolak.')
   clicked_1 = st.button('Lakukan Uji Shapiro!!')

   if clicked_1:
      Z_value1, p_value_s1 = shapiro(df_1_array)
      Z_value2, p_value_s2 = shapiro(df_2_array)
      Z_value3, p_value_s3 = shapiro(df_3_array)
      Z_value4, p_value_s4 = shapiro(df_4_array)
      Z_value5, p_value_s5 = shapiro(df_5_array)

      st.write(f'Data-1: Z-value = {Z_value1}, p-value = {p_value_s1}')
      if p_value_s1 < alpha_value:
         st.write('Keputusan: Tolak H0')
      else:
         st.write('Keputusan: Terima H0')
      st.write(f'Data-2: Z-value = {Z_value2}, p-value = {p_value_s2}')
      if p_value_s2 < alpha_value:
         st.write('Keputusan: Tolak H0')
      else:
         st.write('Keputusan: Terima H0')
      st.write(f'Data-3: Z-value = {Z_value3}, p-value = {p_value_s3}')
      if p_value_s3 < alpha_value:
         st.write('Keputusan: Tolak H0')
      else:
         st.write('Keputusan: Terima H0')
      st.write(f'Data-4: Z-value = {Z_value4}, p-value = {p_value_s4}')
      if p_value_s4 < alpha_value:
         st.write('Keputusan: Tolak H0')
      else:
         st.write('Keputusan: Terima H0')
      st.write(f'Data-5: Z-value = {Z_value5}, p-value = {p_value_s5}')
      if p_value_s5< alpha_value:
         st.write('Keputusan: Tolak H0')
      else:
         st.write('Keputusan: Terima H0')

      st.write('Maka,')
      if p_value_s1 < alpha_value:
         st.write('Kesimpulan: Terdapat Populasi yang Tidak Berdistribusi Normal')
      elif p_value_s2< alpha_value:
         st.write('Kesimpulan: Terdapat Populasi yang Tidak Berdistribusi Normal')
      elif p_value_s3 < alpha_value:
         st.write('Kesimpulan: Terdapat Populasi yang Tidak Berdistribusi Normal')
      elif p_value_s4 < alpha_value:
         st.write('Kesimpulan: Terdapat Populasi yang Tidak Berdistribusi Normal')
      elif p_value_s5 < alpha_value:
         st.write('Kesimpulan: Terdapat Populasi yang Tidak Berdistribusi Normal')
      else:
         st.write('Kesimpulan: Seluruh Populasi Berdistribusi Normal')

#untuk pengujian bartlett
if tipe == '2. Uji Homogenitas':
   st.write('## UJI HOMOGENITAS')
   st.write('Uji homogenitas adalah pengujian mengenai sama tidaknya variansi-variansi dua buah distribusi atau lebih. Salah satu metodenya yaitu dengan uji Bartlett, dimana pengujian ini digunakan untuk menguji apakah k sampel berasal dari populasi dengan varians yang sama.')
   st.write('Hipotesis:')
   st.write('H0 : Seluruh populasi memiliki keragaman yang sama')
   st.write('H1 : Minimal terdapat satu populasi yang memiliki keragaman yang berbeda')
   st.write('Daerah Kritis:')
   st.write('Jika nilai p-value > alpha, maka H0 diterima. Jika nilai p-value < alpha, maka H0 ditolak.')
   clicked_2 = st.button('Lakukan Uji Bartlett!!')

   if clicked_2:
      Chi_Square, p_value_b = stats.bartlett(df_1_array.flatten(), df_2_array.flatten(), df_3_array.flatten(), df_4_array.flatten(), df_5_array.flatten())
      
      st.write(f'Chi-Square-hitung = {Chi_Square}, p-value = {p_value_b}')
      
      if p_value_b < alpha_value:
         st.write('Kesimpulan: Varians Tiap Populasi Data Tidak Sama')
      else:
         st.write('Kesimpulan: Varians Tiap Populasi Data Sama')

#untuk pengujian anova
if tipe == '3. Uji ANOVA One Way':
   st.write('## Uji ANOVA One Way')
   st.write('ANOVA satu arah adalah jenis uji statistik yang membandingkan varians dalam rata-rata grup dalam sampel sambil mempertimbangkan hanya satu variabel atau faktor independen.')
   st.write('Hipotesis:')
   st.write('H0 : Rata-rata seluruh populasi bernilai sama')
   st.write('H1 : Ada setidaknya satu populasi yang memiliki rata-rata yang berbeda') 
   st.write('Daerah Kritis:')
   st.write('Jika nilai p-value > alpha, maka H0 diterima. Jika nilai p-value < alpha, maka H0 ditolak.')
      
   clicked_3 = st.button('Lakukan Uji ANOVA One Way!!')
   
   if clicked_3: 
      F_hitung, p_value = f_oneway(df_1_array, df_2_array, df_3_array, df_4_array, df_5_array)
      
      st.write(f'F-hitung = {F_hitung}, p-value = {p_value}')
      
      if p_value < alpha_value:
         st.write('Keputusan: Tolak H0')
         st.write('Kesimpulan: Terdapat setidaknya satu populasi yang memiliki rata-rata yang berbeda')
         st.write('*lakukan Uji Tukey untuk mengetahui populasi mana yang memiliki rata-rata yang berbeda')
      else:
         st.write('Keputusan: Terima H0')
         st.write('Kesimpulan: Rata-rata seluruh populasi bernilai sama')