import matplotlib.pyplot as plt

from Algoritmos_eficientes.teste import algoritmos_eficientes
from Algoritmos_nao_eficientes.teste import algoritmos_nao_eficientes

sizes = [10, 100, 1000, 10000]

nao_eficientes = [algoritmos_nao_eficientes(size) for size in sizes]
eficientes = [algoritmos_eficientes(size) for size in sizes]

def ordenada_chart():
    lista_type = 'lista ordenada'

    bubble = [p['ordenada_bubble'] for p in nao_eficientes]
    insertion = [p['ordenada_insertion'] for p in nao_eficientes]
    selection = [p['ordenada_selection'] for p in nao_eficientes]
    quick = [p['ordenada_quick'] for p in eficientes]
    heap = [p['ordenada_heap'] for p in eficientes]
    merge = [p['ordenada_merge'] for p in eficientes]

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    ax[0].plot(sizes, bubble, label='bubble', color='blue')
    ax[0].plot(sizes, insertion, label='insertion', color='green')
    ax[0].plot(sizes, selection, label='selection', color='orange')
    ax[0].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos não eficientes')
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[0]
    fig.legend(lines, labels, bbox_to_anchor=(0.17, 0.87), borderaxespad=0)

    ax[1].plot(sizes, quick, label='quick', color='purple')
    ax[1].plot(sizes, heap, label='heap', color='red')
    ax[1].plot(sizes, merge, label='merge', color='grey')
    ax[1].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos eficientes')
    fig.savefig(f"{lista_type}.png")
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[1]
    fig.legend(lines, labels, bbox_to_anchor=(0.66, 0.87), borderaxespad=0)
    plt.tight_layout()
    plt.show()

def inversamente_ordenada_chart():
    lista_type = 'lista inversamente ordenada'

    bubble = [p['inversamente_ordenada_bubble'] for p in nao_eficientes]
    insertion = [p['inversamente_ordenada_insertion'] for p in nao_eficientes]
    selection = [p['inversamente_ordenada_selection'] for p in nao_eficientes]
    quick = [p['inversamente_ordenada_quick'] for p in eficientes]
    heap = [p['inversamente_ordenada_heap'] for p in eficientes]
    merge = [p['inversamente_ordenada_merge'] for p in eficientes]

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    ax[0].plot(sizes, bubble, label='bubble', color='blue')
    ax[0].plot(sizes, insertion, label='insertion', color='green')
    ax[0].plot(sizes, selection, label='selection', color='orange')
    ax[0].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos não eficientes')
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[0]
    fig.legend(lines, labels, bbox_to_anchor=(0.17, 0.87), borderaxespad=0)

    ax[1].plot(sizes, quick, label='quick', color='purple')
    ax[1].plot(sizes, heap, label='heap', color='red')
    ax[1].plot(sizes, merge, label='merge', color='grey')
    ax[1].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos eficientes')
    fig.savefig(f"{lista_type}.png")
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[1]
    fig.legend(lines, labels, bbox_to_anchor=(0.66, 0.87), borderaxespad=0)
    plt.tight_layout()
    plt.show()


def quase_ordenada_chart():
    lista_type = 'lista quase ordenada'

    bubble = [p['quase_ordenada_bubble'] for p in nao_eficientes]
    insertion = [p['quase_ordenada_insertion'] for p in nao_eficientes]
    selection = [p['quase_ordenada_selection'] for p in nao_eficientes]
    quick = [p['quase_ordenada_quick'] for p in eficientes]
    heap = [p['quase_ordenada_heap'] for p in eficientes]
    merge = [p['quase_ordenada_merge'] for p in eficientes]

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    ax[0].plot(sizes, bubble, label='bubble', color='blue')
    ax[0].plot(sizes, insertion, label='insertion', color='green')
    ax[0].plot(sizes, selection, label='selection', color='orange')
    ax[0].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos não eficientes')
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[0]
    fig.legend(lines, labels, bbox_to_anchor=(0.17, 0.87), borderaxespad=0)

    ax[1].plot(sizes, quick, label='quick', color='purple')
    ax[1].plot(sizes, heap, label='heap', color='red')
    ax[1].plot(sizes, merge, label='merge', color='grey')
    ax[1].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos eficientes')
    fig.savefig(f"{lista_type}.png")
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[1]
    fig.legend(lines, labels, bbox_to_anchor=(0.66, 0.87), borderaxespad=0)
    plt.tight_layout()
    plt.show()


def aleatoria_chart():
    lista_type = 'lista aleatória'

    bubble = [p['aleatoria_bubble'] for p in nao_eficientes]
    insertion = [p['aleatoria_insertion'] for p in nao_eficientes]
    selection = [p['aleatoria_selection'] for p in nao_eficientes]
    quick = [p['aleatoria_quick'] for p in eficientes]
    heap = [p['aleatoria_heap'] for p in eficientes]
    merge = [p['aleatoria_merge'] for p in eficientes]

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    ax[0].plot(sizes, bubble, label='bubble', color='blue')
    ax[0].plot(sizes, insertion, label='insertion', color='green')
    ax[0].plot(sizes, selection, label='selection', color='orange')
    ax[0].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos não eficientes')
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[0]
    fig.legend(lines, labels, bbox_to_anchor=(0.17, 0.87), borderaxespad=0)

    ax[1].plot(sizes, quick, label='quick', color='purple')
    ax[1].plot(sizes, heap, label='heap', color='red')
    ax[1].plot(sizes, merge, label='merge', color='grey')
    ax[1].set(xlabel='tamanho arranjo', ylabel='tempo (s)',
              title=f'{lista_type} algoritmos eficientes')
    fig.savefig(f"{lista_type}.png")
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = lines_labels[1]
    fig.legend(lines, labels, bbox_to_anchor=(0.66, 0.87), borderaxespad=0)
    plt.tight_layout()
    plt.show()

