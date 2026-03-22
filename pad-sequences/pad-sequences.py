import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None, padding='right'):
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)
    
    result = np.full((len(seqs), max_len), pad_value, dtype=int)
    
    for i, seq in enumerate(seqs):
        if len(seq) > max_len:
            if padding == 'right':
                seq = seq[:max_len]
            else:
                seq = seq[-max_len:]
        
        if padding == 'right':
            result[i, :len(seq)] = seq
        else:
            result[i, -len(seq):] = seq
    
    return result