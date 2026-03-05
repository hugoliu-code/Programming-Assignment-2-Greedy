import math, random, os
from comparison import read_input, print_output
from fifo import fifo
from lru import lru
from optff import optff
import pandas as pd
import matplotlib.pyplot as plt

def generate_inputs():
    for i in range(1,4):
        # choose a k 
        k = random.randint(5, 20)
        m = random.randint(50, 100)
        requests = [str(random.randint(1, m)) for _ in range(m)]
        file = f'inputs/q1/random_{i}.in'
        
        os.makedirs('inputs/q1', exist_ok=True)
        with open(file, 'w') as f:
            f.write(f'{k} {m} \n')
            f.write(' '.join(requests))


def main():
    output_dir = 'outputs/q1'
    os.makedirs(output_dir, exist_ok=True)
    generate_inputs()
    cols = {'input_files': [], 'k': [], 'm': [], 'fifo_misses': [], 'lru_misses': [], 'optff_misses': []}
    for i in range(1,4):
        input_file = f'inputs/q1/random_{i}.in'
        k, m, requests = read_input(input_file)
        cols['k'].append(k)
        cols['m'].append(m)
        
        fifo_miss = fifo(k, m, requests)
        lru_miss = lru(k, m, requests)
        optff_miss = optff(k, m, requests)

        cols['fifo_misses'].append(fifo_miss)
        cols['lru_misses'].append(lru_miss)
        cols['optff_misses'].append(optff_miss)
        cols['input_files'].append(f'random_{i}.in')


        print_output(fifo_miss, lru_miss, optff_miss, output_dir+f'/random_{i}.out')
    
    df = pd.DataFrame(cols)
    print(df.head())

    fig, ax = plt.subplots(figsize=(4, 2))
    ax.axis('off')
    # Render and save the table
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(5)
    table.scale(1,2)
    plt.savefig(output_dir+'/q1.svg', bbox_inches='tight')

if __name__ == '__main__':
    main()