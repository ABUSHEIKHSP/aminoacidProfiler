#Importing modules:

from Bio import SeqIO
import pandas as pd
import numpy as np
import glob

class aminoacidProfiler(): 

    global sample_storage 
    sample_storage = []

    
    def amino_analyzer(fasta_name): 
        
        #Looping the input sample fasta file:
        for sequence_record in SeqIO.parse(fasta_name,'fasta'):

            #single letter code of amino acids:
            single_letter_code = "ARDNCEQGHILKMFPSTWYV"

            #Getting sequence detials:
            fasta_detials = sequence_record
                        
            try:
                if 'partial' not in fasta_detials:
                    #Getting amino_acidin sequence from fasta:
                    seq = fasta_detials.seq
                    id = fasta_detials.id
                    strain = fasta_detials.description.split('[')[-1].split(']')[-2]
                    #strain = des.split('/')[-1].split('.')[0]
                    geo = fasta_name.split('/')[-1].split('.')[0]
                    id_des = [id,strain,geo]
                    aa_count = [round((seq.count(aa)/len(seq))*100,1) for aa in single_letter_code ]
                    final_det = id_des + aa_count
                    sample_storage.append(final_det)
            except:
                pass
            

    def file_extractor():

        global folder_name
        folder_name = f'{main_folder}/**/*.fasta'
        for file_name in glob.iglob(folder_name, recursive=True):
            aminoacidProfiler.amino_analyzer(file_name)

            
    def main_folder_path(path):
        
        global main_folder
        main_folder = path
        
    


    def df_creater():

        df = pd.DataFrame(sample_storage,columns='ID STRAIN GEO_LOC A R D N C E Q G H I L K M F P S T W Y V'.split())
        df.to_csv(f'{main_folder}/result.csv',index=False)
        #print(df)
        


    def run_control(path):
        
        aminoacidProfiler.main_folder_path(path)
        aminoacidProfiler.file_extractor()
        aminoacidProfiler.df_creater()
        
        
            
if __name__ == "__main__":            
    aminoacidProfiler.run_control()
