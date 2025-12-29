import matplotlib.pyplot as plt

def plot_skill_gap(matched: int , missing: int):
    labels = ['Matched Skills', 'Missing Skills']
    value = [matched, missing]

    fig, ax = plt.subplots()
    ax.bar(labels, value, color=['green', 'red'])
    ax.set_title('Skill Match Analysis')
    ax.set_ylabel('count')

    return fig