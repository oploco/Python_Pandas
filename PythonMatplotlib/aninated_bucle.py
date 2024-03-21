import io
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation
import random


PLOT_LIMIT = 20
ANIM_FILENAME = "video.gif"


fig, ax = plt.subplots(1, 1, figsize=(10,8))
ax.set_title("Plot of random numbers")
ax.set_xlabel("time / s")
ax.set_ylabel("random number / #")
ax.set_ylim([0, 1])

def get_data():
    start_time = time.time()
    elapsed_time = time.time() - start_time
    data=""
    while elapsed_time < 2:
        data += (f"{time.time():10.10f} {random.random():30.10f}\n")  # produces 64 bytes
        elapsed_time = time.time() - start_time
        return data

def animate(i, xs, ys, limit=PLOT_LIMIT, verbose=False):
    # grab the data
    try:
        data = get_data()
        print(data)

        if verbose:
            print('Verbose',data)
        x, y = map(float, data.split())
        if x > xs[-1]:
            # Add x and y to lists
            xs.append(x)
            ys.append(y)
            # Limit x and y lists to 10 items
            xs = xs[-limit:]
            ys = ys[-limit:]
            print("if")
        else:
            print(f"W: {time.time()} :: STALE!")
    except ValueError:
        print(f"W: {time.time()} :: EXCEPTION!",data)
    else:
        # Draw x and y lists
        ax.clear()
        ax.set_ylim([0, 1])
        ax.plot(xs, ys)
        print("else")


# save video (only to attach here)
#anim = mpl.animation.FuncAnimation(fig, animate, fargs=([time.time()], [None]), interval=1, frames=3 * PLOT_LIMIT, repeat=False)
#anim.save(ANIM_FILENAME, writer='imagemagick', fps=10)
#print(f"I: Saved to `{ANIM_FILENAME}`")

# show interactively
anim = mpl.animation.FuncAnimation(fig, animate, fargs=([time.time()], [None]), interval=1)
plt.show()
plt.close()