#Importing modules:

from prettytable import PrettyTable
import csv
from Bio import SeqIO
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
import os
import numpy as np
import glob





class Coronavar(): 

    def data_adder():
        global data
        data = [sequence_name,strain_name,geo_location]
        [data.append(a)for a in amino_acid_count]
        return(data)

    def heading_adder():
        global heading
        heading = ['ID','STRAIN','GEO_LOC','A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
        return heading

    def table_header():
        global myTable
        myTable = PrettyTable(Coronavar.heading_adder())

    def table_body():
        myTable.add_row(Coronavar.data_adder())

    def csv_header():
        #Deleting existing data:
        file = open(f'{main_folder}/result.csv','w')
        file.close()

        #Opening file:
        file = open(f'{main_folder}/result.csv', 'a+')

        #Writing CSV header:
        writer = csv.writer(file)
        header = Coronavar.heading_adder()
        writer.writerow(header)

        file.close()

    def csv_body():
        #Opening file:
        file = open(f'{main_folder}/result.csv','a+')
        
        #Writing data to CSV file:
        writer = csv.writer(file)
        writer.writerow(Coronavar.data_adder())
    
    def individual_csv_header(file):
        #Opening file:
        file = open(f'{file}.csv', 'w')
        
        #Writing CSV header:
        writer = csv.writer(file)
        header = Coronavar.heading_adder()
        writer.writerow(header)

        file.close()
    
    def individual_csv_body(file):
        #Opening file:
        file = open(f'{file}.csv','a+')
        
        #Writing data to CSV file:
        writer = csv.writer(file)
        writer.writerow(Coronavar.data_adder())
    
    def amino_analyzer(fasta_name): 
        #Adding header for individual files:
        Coronavar.individual_csv_header(fasta_name)
        
        #Looping the input sample fasta file:
        for sequence_record in SeqIO.parse(fasta_name,'fasta'):

            #single letter code of amino acids:
            single_letter_code = "ARDNCEQGHILKMFPSTWYV"

            #Getting sequence detials:
            sequence_detials = sequence_record

            #Getting amino_acidin sequence from fasta:
            amino_acid = sequence_detials.seq

            #Getting total length of amino acids from fasta:
            length_of_amino_acid= len(amino_acid)

            #Getting each amino acid count:
            global amino_acid_count
            amino_acid_count = [amino_acid.count(aa) for aa in single_letter_code ]

            #Getting sequnce name:
            global sequence_name
            sequence_name = sequence_detials.name
            
            #Geo location:
            Coronavar.geo_loc(fasta_name)
            
            #Strain_name:
            Coronavar.strain_name(description=sequence_record.description)
        
            #Calling table_body and csv_body function to add the analyzed data:
            Coronavar.table_body()
            Coronavar.csv_body()
            Coronavar.individual_csv_body(fasta_name)

        #Clearing out amino acid count list for the next fasta format:
        #amino_acid_count = []

    def printing_results():
        #printing myTable:
        return(myTable)

        #results.csv:
        print('The results are also stored in results.csv')

    def file_extractor():
        global folder_name
        folder_name = f'{main_folder}/**/*.fasta'
        for file_name in glob.iglob(folder_name, recursive=True):
            Coronavar.amino_analyzer(file_name)

    def geo_loc(fasta_name):
        #Geo location:
        global geo_location
        
        #seperat by /:
        slash_split = fasta_name.split('/')
        file_name = slash_split[-1]
        
        #seperat by . for fasta files:
        dot_split = file_name.split('.')
        geo_location = dot_split[0]
        
    def strain_name(description):
        #Strain_name:
        global strain_name
        
        #Splitting begins:
        split_1 = description.split('[')
        split_2 = split_1[-1].split(']')
        if split_2[0] == 'Middle East respiratory syndrome-related coronavirus':
            strain_name = 'MERS'
        elif split_2[0] == 'Severe acute respiratory syndrome coronavirus 2':
            strain_name = 'SARS 2'
        elif split_2[0] == 'Severe acute respiratory syndrome coronavirus':
            strain_name = 'SARS'
        else:
            split_3 = split_2[0].split()
            strain_name = split_3[2]
        print(strain_name)
            
    def main_folder_path(path):
        
        global main_folder
        
        #main_folder = input('Enter the folder path : ')
        #main_folder = '/home/abu/Documents/python project/coronavar/SPIKE/Spike glycoprotein'
        main_folder = path
        print(main_folder)
    
    def graph_output():
        
        #Reading csv file:
        #leucine_read = read_csv('high_leucine.csv')
        #valine_read = read_csv('high_valine.csv')
        
        #Heights of bars:
        amino_acids = ['A','R','D','N','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
        
            #For leucine high proteomes:
        total_leucine = []
        for x in amino_acids:
            y = leucine_read[f'{x}'].tolist()
            total_leucine.append(sum(y))
            
        leucine = []
        for l in total_leucine:
            #leucine.append(l/sum(total_leucine)*100)
            leucine.append(sum(total_leucine))
            
            #For valine high proteomes:
        total_valine = []
        for x in amino_acids:
            y = valine_read[f'{x}'].tolist()
            total_valine.append(sum(y))
            
        valine = []
        for l in total_valine:
           # valine.append(l/sum(total_valine)*100)
           valine.append(sum(total_valine))
        
        # set width of bar
        barWidth = 0.30
        #fig = plt.subplots(figsize =(12, 8))
        
        # Set position of bar on X axis
        br1 = np.arange(len(leucine))
        br2 = [x + barWidth for x in br1]
        
        # Make the plot
        plt.bar(br1, leucine, color ='r', width = barWidth,
        		edgecolor ='grey')
        plt.bar(br2, valine, color ='g', width = barWidth,
        		edgecolor ='grey')
        
        # Adding Xticks
        plt.xlabel('Amino acids', fontweight ='bold', fontsize = 12)
        plt.ylabel('Percentage of amino acid', fontweight ='bold', fontsize = 12)
        plt.xticks([r + barWidth for r in range(len(leucine))],
        		amino_acids)
        
        plt.legend()
        plt.show()

    def run_control(path):
        
        Coronavar.main_folder_path(path)
        Coronavar.table_header()
        Coronavar.csv_header()
        Coronavar.file_extractor()
        Coronavar.printing_results()
        #Coronavar.graph_output()
        
        
        
'''if __name__ == "__main__":            
    Coronavar.run_control()
'''