import imageio as iio
import numpy as np

# read bug image as numpy array
bugimg = np.asarray(iio.imread("C:/Users/abel/Desktop/Github/fish-tank-one/Bug Final_0.1x.png"))
bugimg.astype(int)
print(bugimg.shape)

# read prepared chicken with bugs image as numpy array
testimg = np.asarray(iio.imread("C:/Users/abel/Desktop/Github/fish-tank-one/chicken_w_bugs_0.1x.png"))
testimg.astype(int)
print(testimg.shape)

#convert both images into 2D array [:,:,0]
bugimg = bugimg[:,:,0]
print(bugimg.shape)
testimg = testimg[:,:,0]
print(testimg.shape)

# convert all the values to either 1 or 0
bugimg[bugimg < 128] = 1
bugimg[bugimg >= 128] = 0
testimg[testimg < 128] = 1
testimg[testimg >= 128] = 0

# this step is just to make sure my converted pictures make sense.
import matplotlib.pyplot as plt
plt.imshow(bugimg, interpolation='none')
plt.show()
plt.imshow(testimg, interpolation='none')
plt.show()

# Compare bugimg array with sliced windows of testimg array to find the bug image
test_window_emp = np.zeros((36,45))
test_window_emp = test_window_emp.astype(int)
i_list = []
m_list = []
for i in range(testimg.shape[0]-36+1):
    for m in range(testimg.shape[1]-45+1):
        test_window_cur = testimg[i:i+36, m:m+45]
        #print(test_window_cur)
        test_progress = np.add(test_window_emp,test_window_cur)
        #print(test_progress)
        if np.array_equal(test_progress, bugimg):
            print("Found a bug at: ", i, ",", m)
            i_list.append(i)
            m_list.append(m)

# Mark out the bugs in the original test image
print(i_list)
result_img = np.asarray(iio.imread("C:/Users/abel/Desktop/Github/fish-tank-one/chicken_w_bugs_0.1x.png"))
for n in range(len(i_list)):
        result_img[i_list[n]:i_list[n]+36,m_list[n]:m_list[n]+45, 1:3] = 0

plt.imshow(result_img, interpolation='none')
plt.show()