import nmi_calculator
import ari_calculator
import vi_calculator
import purity_calculator

import igraph as ig

def calc_metrics(nodes, real_communities, detected_communities):
    """
    Calculate:

        1. Normalized Mutual Information
        2. Adjusted Rand Index
        3. Variation of Information
        4. Purity
    """
    print("Calculating metrics")
    nmi = nmi_calculator.nmi_calculator(real_communities, detected_communities)
    snmi = nmi_calculator.snmi(nmi, real_communities, detected_communities)
    ari = ari_calculator.ari_calculator(nodes, real_communities, detected_communities)
    vi = vi_calculator.variation_of_information(real_communities, detected_communities)
    purity = purity_calculator.purity(nodes, real_communities, detected_communities)
    f_measure = purity_calculator.f_measure(nodes, real_communities, detected_communities)
    print("NMI: {0}, SNMI: {1}, ARI: {2}, VI: {3}, Purity: {4}, F-Measure: {5}".format(round(nmi, 3), 
            round(snmi, 3), round(ari, 3),
            round(vi, 3), round(purity, 3), round(f_measure, 3)))
    return nmi, snmi, ari, vi, purity, f_measure

def avg(results):
    """
    Calculate average values of metrics 
    """
    avg_nmi, avg_snmi, avg_ari, avg_vi, avg_purity, avg_fmeasure = 0,0,0,0,0,0
    for nmi, snmi, ari, vi, purity, f_measure in results:
        avg_nmi += nmi
        avg_snmi += snmi
        avg_purity += purity
        avg_fmeasure += f_measure
        avg_vi += vi
        avg_ari += ari

    return round(avg_nmi/100, 3), round(avg_snmi/100, 3), round(avg_ari/100, 3), round(avg_vi/100, 3), round(avg_purity/100, 3), round(avg_fmeasure/100, 3)

def generate_igraph(edges):
    
    g = ig.Graph(edges=edges, directed=False)
    
    