import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# -----------------------------
# Jar capacities
# -----------------------------
CAP1 = 3
CAP2 = 5

NUM_STRIPS = 50

# -----------------------------
# Sequence of states
# (jar1, jar2)
# -----------------------------
states = [
    (0,0),
    (0,5),      # Fill 5L
    (3,2),      # Pour 5 -> 3
    (0,2),      # Empty 3L
    (2,0),      # Pour 5 -> 3
    (2,5),      # Fill 5L
    (3,4)       # Pour 5 -> 3 (goal: 4L)
]

# -----------------------------
# Create intermediate frames
# -----------------------------
frames = []

prev1, prev2 = states[0]
frames.append((prev1, prev2))

for next1, next2 in states[1:]:

    s1 = int(prev1/CAP1*NUM_STRIPS)
    e1 = int(next1/CAP1*NUM_STRIPS)

    s2 = int(prev2/CAP2*NUM_STRIPS)
    e2 = int(next2/CAP2*NUM_STRIPS)

    distance = max(abs(e1-s1), abs(e2-s2))

    for k in range(1, distance+1):

        t = k/distance

        a = s1 + (e1-s1)*t
        b = s2 + (e2-s2)*t

        frames.append((a,b))

    prev1 = next1
    prev2 = next2

# -----------------------------
# Figure
# -----------------------------
fig, ax = plt.subplots(figsize=(8,6))

ax.set_xlim(0,10)
ax.set_ylim(0,6)
ax.set_aspect("equal")
ax.axis("off")

# -----------------------------
# Draw strips
# -----------------------------
jar1 = []
jar2 = []

strip_height = 4/NUM_STRIPS

for i in range(NUM_STRIPS):

    r1 = Rectangle((2,1+i*strip_height),
                   1.5,
                   strip_height,
                   facecolor="white",
                   edgecolor="none")

    r2 = Rectangle((6,1+i*strip_height),
                   1.5,
                   strip_height,
                   facecolor="white",
                   edgecolor="none")

    ax.add_patch(r1)
    ax.add_patch(r2)

    jar1.append(r1)
    jar2.append(r2)

# outlines
ax.add_patch(Rectangle((2,1),1.5,4,fill=False,lw=3))
ax.add_patch(Rectangle((6,1),1.5,4,fill=False,lw=3))

ax.set_title(
    "El problema de las 2 jarras",
    fontsize=20,
    fontweight='bold',
    color='darkblue'
)

text1 = ax.text(2.75,0.5,"",ha="center",fontsize=13)
text2 = ax.text(6.75,0.5,"",ha="center",fontsize=13)

# -----------------------------
# Animation
# -----------------------------
def update(frame):

    strips1, strips2 = frames[frame]

    for i in range(NUM_STRIPS):

        jar1[i].set_facecolor(
            "deepskyblue" if i < strips1 else "white"
        )

        jar2[i].set_facecolor(
            "deepskyblue" if i < strips2 else "white"
        )

    liters1 = abs(round(strips1/NUM_STRIPS*CAP1,1))
    liters2 = abs(round(strips2/NUM_STRIPS*CAP2,1))

    text1.set_text(f"{liters1:.0f} / {CAP1} L")
    text2.set_text(f"{liters2:.0f} / {CAP2} L")

    return jar1 + jar2 + [text1,text2]

ani = FuncAnimation(
    fig,
    update,
    frames=len(frames),
    interval=40,
    repeat=False
)

plt.close(fig)

HTML(ani.to_jshtml())