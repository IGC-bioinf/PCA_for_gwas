#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:20:42 2022

@author: roma
"""
import os
os.chdir('/home/roma/PCA_1000G/abr') ########################
from plotnine import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file = '/home/roma/PCA_1000G/abr/plink.eigenvec' ########################
df = pd.read_csv(file, header=None, sep =  ' ', index_col=0, names = ['ID', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5','PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11','PC12','PC13', 'PC14', 'PC15', 'PC16', 'PC17','PC18', 'PC19', 'PC20'])
del df['ID']
file2 = '/home/roma/Chakova/to_mv/anev_test/racefile.txt'
df2 = pd.read_csv(file2, sep=' ', names=['ID', 'Race'], header = None)
#df = df[[2,1]]
imap = df2.groupby('Race')['ID'].apply(list).to_dict()
#abr
imap['BEL Affected'] = ['129E_S9','231e_S2', '25E_S8', '286E_S4', '301E_S2', '35E_S6', '432E_S12', '434E_S10', '460E_S7', '470E_S1', '471e_S9', '482E_S9', '49E_S3', '538E_S12', '556E_S2', '557E_S7', '58NF_S6', '64E_S5', '95E_S11', '100_father', '100_mother', '10_father', '10_mother', '111_father', '111_mother', '11_father', '11_mother', '141_father', '141_mother', '150_father', '150_mother', '15_father', '15_mother', '238E_S5', '243E_S10', '248E_S11', '253E_S5', '27_father', '27_mother', '349E_S8', '352E_S6', '406E_S8', '407E_S7', '445E_S7', '450E_S1', '455E_S12', '461E_S3', '462E_S2', '475E_S4', '4_father', '4_mother', '533E_S12', '537E_S1', '540E_S10', '543E_S8', '555E_S6', '5_father', '5_mother', '620E_S9', '62E_S11', '632E_S7', '633E_S3', '635E_S9', '639E_S5', '654E_S2', '676E_S1', '677E_S10', '683E_S9', '7_father', '7_mother', '85_father', '85_mother', '8_father', '8_mother', '90nf_S2' '96_father', '96_mother', '96nf_S3', '9_father', '9_mother', 'Ja_father', 'Ja_mother', 'Ko_father', 'Ko_mother', 'Li_father', 'Li_mother', 'Mar_father', 'Mar_mother']
#nek
#imap['BEL Affected'] = ['100_father','100_mother','100_proband','10_father','10_mother','111_father','111_mother','111_proband','119_S22','11_father','11_mother','130_S27','140_S25','141_father','141_mother','141_proband','145_S17','146_S13','147_S20','149','150_father','150_mother','150_proband','152_S8','153_S26','154','156_S24','15_father','15_mother','15_proband','160_S12','163_S30','164_S7','165_S4','166_S1','167_S14','168_S16','169_S3','170','171','172','173nek','174nek','175nek','176nek','177nek','178nek','179nek','180nek','181nek','182nek','183nek','184nek','185nek','186nek','187nek','188nek','189nek','190nek','1_S5','27_father','27_mother','27_proband','29_S10','2_S29','31_S21','34_S18','38_S19','3_S6','40_S9','41_S23','4_father','4_mother','53_S28','59_S32','5_father','5_mother','7_S15','7_father','7_mother','85_father','85_mother','85_proband','87_S31','8_father','8_mother','96_father','96_mother','96_proband','97_S2','9_father','9_mother','Ja_father','Ja_mother','Ko_father','Ko_mother','Li_father','Li_mother','Mar_father','Mar_mother']
#ep
#imap['BEL Affected'] = ['100_father','100_mother','10_father','10_mother','10_proband','111_father','111_mother','11_father','11_mother','11_proband','12ep','13ep','141_father','141_mother','14ep','150_father','150_mother','15_father','15_mother','15ep','16ep','17ep','18ep','19ep','1ep','20ep','21ep','23ep','24ep','25ep','27_father','27_mother','27ep','28ep','29ep','2ep','30ep','31ep','32ep','33ep','34ep','35ep','36ep','37ep','38ep','39ep','40ep','41ep','42ep','43ep','44ep','45ep','46ep','47ep','48ep','49ep','4_father','4_mother','4_proband','50ep','51ep','52ep','53ep','54ep','55ep','56ep','57ep','5_father','5_mother','5_proband','6','7_father','7_mother','7_proband','85_father','85_mother','8_father','8_mother','8_proband','96_father','96_mother','9_father','9_mother','9_proband','Ja_father','Ja_mother','Ko_father','Ko_mother','Li_father','Li_mother','Li_proband','Mar_father','Mar_mother']
#kid
#imap['BEL Affected'] = ['/storage/analysis/cnv/Full_exome/bam/11nf_S5.bam','/storage/analysis/cnv/Full_exome/bam/12NF_S3.bam','/storage/analysis/cnv/Full_exome/bam/13nf_S10.bam','/storage/analysis/cnv/Full_exome/bam/13nf_S4.bam','/storage/analysis/cnv/Full_exome/bam/15nf_S4.bam','/storage/analysis/cnv/Full_exome/bam/18nf_S7.bam','/storage/analysis/cnv/Full_exome/bam/20nf_S11.bam','/storage/analysis/cnv/Full_exome/bam/22nf_S3.bam','/storage/analysis/cnv/Full_exome/bam/23nf_S12.bam','/storage/analysis/cnv/Full_exome/bam/25nf_S1.bam','/storage/analysis/cnv/Full_exome/bam/26nf_S6.bam','/storage/analysis/cnv/Full_exome/bam/27nf_S5.bam','/storage/analysis/cnv/Full_exome/bam/28nf_S1.bam','/storage/analysis/cnv/Full_exome/bam/29nf_S11.bam','/storage/analysis/cnv/Full_exome/bam/30NF_S4.bam','/storage/analysis/cnv/Full_exome/bam/31nf_S10.bam','/storage/analysis/cnv/Full_exome/bam/33NF_S8.bam','/storage/analysis/cnv/Full_exome/bam/35NF_S6.bam','/storage/analysis/cnv/Full_exome/bam/36NF_S5.bam','/storage/analysis/cnv/Full_exome/bam/4NF_S1.bam','/storage/analysis/cnv/Full_exome/bam/51nf_S9.bam','/storage/analysis/cnv/Full_exome/bam/52nf_S5.bam','/storage/analysis/cnv/Full_exome/bam/53NF_S1.bam','/storage/analysis/cnv/Full_exome/bam/56nf_S12.bam','/storage/analysis/cnv/Full_exome/bam/56nf_S2.bam','/storage/analysis/cnv/Full_exome/bam/57nf_S8.bam','/storage/analysis/cnv/Full_exome/bam/59NF_S11.bam','/storage/analysis/cnv/Full_exome/bam/60nf_S1.bam','/storage/analysis/cnv/Full_exome/bam/62nf_S8.bam','/storage/analysis/cnv/Full_exome/bam/63nf_S9.bam','/storage/analysis/cnv/Full_exome/bam/64NF_S3.bam','/storage/analysis/cnv/Full_exome/bam/66nf_S10.bam','/storage/analysis/cnv/Full_exome/bam/69nf_S7.bam']


imap['BEL Unaffected'] = ['100_father','100_mother','10_father','10_mother','111_father','111_mother','11_father','11_mother','141_father','141_mother','150_father','150_mother','15_father','15_mother','27_father','27_mother','4_father','4_mother','5_father','5_mother','7_father','7_mother','85_father','85_mother','8_father','8_mother','96_father','96_mother','9_father','9_mother','Ja_father','Ja_mother','Ko_father','Ko_mother','Li_father','Li_mother','Mar_father','Mar_mother']
imap['BEL Affected'] = list(set(imap['BEL Affected']) - set(imap['BEL Unaffected']) )
########################
df_imap = pd.DataFrame(columns = ['Race', 'ID'], index = range(2592))
counter = 0
for i in imap.keys():
    for k in imap[i]:
        df_imap['Race'][counter] = i
        df_imap['ID'][counter] = k
        counter += 1
    
df_imap.index =df_imap['ID']

fin_df = pd.merge(df, df_imap, left_index=True, right_index=True)
bel_df_a = fin_df[fin_df['Race'].str.contains('BEL Affected')]
bel_df_u = fin_df[fin_df['Race'].str.contains('BEL Unaffected')]

fig = (
    ggplot(data = fin_df,
          mapping = aes(x = 'PC1', y = 'PC2')) +
    geom_point(aes(color = 'Race',
                   fill = 'Race')) + scale_color_manual(values = ["red",
 "#f81d00",
 "#f03800",
 "#e95200",
 "#e16a00",
 'blue',
 'darkblue',
 "#da8000",
 "#d29400",
 "#cba700",
 "#c3b800",
 "#b1bc00",
 "#94b400",
 "#7aad00",
 "#61a500",
 "#4a9e00",
 "#359600",
 "#228f00",
 "#108700",
 "green"]) +
 geom_point(data = bel_df_u, color = 'blue', size =3) +
 geom_point(data = bel_df_a, color = 'darkblue', size =3) +
    labs(
        title ='',
        x = 'PC1',
        y = 'PC2',
    ) + 
    theme(figure_size = (15, 10)) 
).draw()
                                                                  
                                                                  
plt.savefig('abr_pca.2.png', bbox_inches='tight') ########################


pc_pairplot = fin_df.iloc[:,:10]
pc_pairplot['Race'] = fin_df['Race']
g = sns.PairGrid(pc_pairplot, hue="Race")
g.map_diag(sns.histplot)
g.map_lower(sns.scatterplot,alpha=0.35)
g.add_legend()
plt.savefig('abr_pca.10.png', bbox_inches='tight') ########################