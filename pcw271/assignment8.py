import numpy as np
import operator
import collections
import matplotlib.pyplot as plt

N = 1000
position = np.array([1, 10, 100, 1000], dtype=np.int)
num_trials = 10000


def cumu_ret(position, N, num_trials):
    try:

        new_list = list()

        for t in range(num_trials):

            for k in range(0, len(position)):

                arr = np.zeros((1, int(N / position[k])))

                for j in range(arr.shape[1]):
                    arr[0][j] = (1 + np.random.choice([1, -1], p=[0.51, 0.49])) * (position[k])

                    b = sum(arr[0])

                new_list.append(b)

        return new_list


    except ValueError:
        print('Please input the integer')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')


a = cumu_ret(position, N, num_trials)


def daily_ret(cumu_ret):
    new_list = list()
    for i in cumu_ret:
        for_hist = (i / 1000) - 1
        new_list.append(for_hist)
    return [tuple(new_list[i:i + len(position)]) for i in range(0, len(new_list), len(position))]


b = daily_ret(a)


def make_hist_list(position, b, num_trials):
    for_hist = list()
    num = 0
    for i in range(len(position)):
        for i in range(len(b)):
            for_hist.append(b[i][num])
        num = num + 1

    return [tuple(for_hist[i:i + num_trials]) for i in range(0, len(for_hist), num_trials)]


c = make_hist_list(position, b, num_trials)

c_array1 = np.array(c[0])
hist_1 = plt.hist(c_array1, 100, range=[-1, 1])
plt.title("histogram_0001_pos")
plt.savefig('/Users/KateWu/desktop/histogram_0001_pos.pdf')
plt.close()

c_array2 = np.array(c[1])
hist_2 = plt.hist(c_array2, 100, range=[-1, 1])
plt.title("histogram_0010_pos")
plt.savefig('/Users/KateWu/desktop/histogram_0010_pos.pdf')
plt.close()

c_array3 = np.array(c[2])
hist_3 = plt.hist(c_array3, 100, range=[-1, 1])
plt.title("histogram_0100_pos")
plt.savefig('/Users/KateWu/desktop/histogram_0100_pos.pdf')
plt.close()

c_array4 = np.array(c[3])
hist_4 = plt.hist(c_array4, 100, range=[-1, 1])
plt.title("histogram_1000_pos")
plt.savefig('/Users/KateWu/desktop/histogram_1000_pos.pdf')
plt.close()

f = open('/Users/KateWu/desktop/results.txt', 'w')
p1_mean = np.mean(c[0])
p1_sd = np.std(c[0])
p10_mean = np.mean(c[1])
p10_sd = np.std(c[1])
p100_mean = np.mean(c[2])
p100_sd = np.std(c[2])
p1000_mean = np.mean(c[3])
p1000_sd = np.std(c[3])
s = 'The mean value of position 1 is ' + str(p1_mean) + ' and the SD value is ' + str(
    p1_sd) + '\n' + 'The mean value of position 10 is ' + str(p10_mean) + ' and the SD value is ' + str(
    p10_sd) + '\n' + 'The mean value of position 100 is ' + str(p100_mean) + ' and the SD value is ' + str(
    p100_sd) + '\n' + 'The mean value of position 1000 is ' + str(p1000_mean) + ' and the SD value is ' + str(
    p1000_sd) + '\n'
f.write(s)
f.close()
