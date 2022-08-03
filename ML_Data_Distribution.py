# Code by @AmirMotefaker

# Machine Learning - Data Distribution

# # Solution 1
# # Create an array containing 250 random floats between 0 and 5
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

# # Output:
# # [3.14817900e+00 1.55703591e+00 3.60561743e+00 1.28976220e+00
# #  4.25518241e+00 2.77179524e+00 5.30857776e-01 1.85509002e+00
# #  1.00278821e+00 3.31086039e-01 3.56379641e+00 4.31704554e+00
# #  2.81416403e+00 3.72047571e+00 9.92122421e-01 4.25650673e+00
# #  4.75057384e+00 3.96499337e+00 1.81849002e+00 3.77027247e+00
# #  1.98702451e+00 2.91732708e+00 4.82268763e-01 4.68898637e+00
# #  8.60969810e-02 2.80445964e+00 3.13845036e-01 3.95584117e+00
# #  1.64264558e+00 3.28495322e+00 2.15518542e+00 4.13830575e+00
# #  3.12985236e+00 2.94476895e+00 3.93387898e-01 4.05792795e+00
# #  1.69168489e+00 4.02390042e+00 2.45961940e+00 3.26557033e+00
# #  1.42256861e+00 1.73926462e+00 1.05601975e+00 1.88848015e+00
# #  9.09008762e-01 7.92500261e-01 3.32978170e+00 1.30681384e+00
# #  4.47005246e+00 4.21681491e+00 2.13669165e+00 4.02941348e-01
# #  2.65505835e+00 4.01644614e+00 2.46754290e+00 1.64685653e+00
# #  1.09286063e+00 2.36204984e+00 4.30686249e+00 2.48181130e+00
# #  2.67513931e+00 4.50456274e+00 3.28557507e+00 2.99238957e+00
# #  4.48229101e+00 1.02267924e+00 3.02253747e+00 1.62216010e+00
# #  2.17068470e-01 2.96296572e+00 3.75923214e-01 3.08489651e+00
# #  2.05534867e+00 6.75586460e-01 4.73219131e+00 2.14830024e+00
# #  6.00836232e-01 1.25176581e+00 1.18661925e+00 2.75612952e+00
# #  1.85061700e-01 3.99160586e+00 2.43286960e+00 3.64163391e+00
# #  4.73409741e+00 4.87863718e+00 4.22611611e+00 3.72930599e+00
# #  1.99813124e+00 4.37098040e+00 1.74239825e+00 4.61539428e+00
# #  3.01605472e+00 1.47635585e+00 2.01814377e+00 1.37077027e+00
# #  3.60572321e+00 4.85963925e+00 2.20258532e+00 3.83491795e+00
# #  9.37487418e-01 3.36431041e+00 4.81994270e+00 2.11581949e-01
# #  4.81149308e+00 1.48897501e+00 4.46699462e+00 3.82196212e+00
# #  5.22616182e-01 8.99903964e-01 2.21410967e+00 4.65388139e+00
# #  2.39441518e+00 2.60744299e+00 3.38369341e+00 5.51159441e-01
# #  1.47043049e+00 2.96732734e-01 1.64776045e-01 5.11326361e-01
# #  2.46014582e+00 2.49122256e+00 3.93878975e+00 6.95636816e-01
# #  4.22185018e+00 2.07726880e+00 1.86627545e+00 3.16065303e+00
# #  1.62905109e+00 3.30842707e-01 4.07594202e+00 8.16472240e-01
# #  2.79758037e+00 3.25107641e+00 1.66476118e+00 1.20319696e+00
# #  4.39075302e+00 4.88332913e+00 3.50267976e+00 3.54665271e+00
# #  1.78125352e+00 7.96304919e-01 2.55458746e+00 4.66770162e+00
# #  2.65276792e+00 1.22838257e+00 2.36499959e+00 2.28431616e+00
# #  2.29957121e+00 3.98201136e+00 5.17773047e-01 3.36493364e+00
# #  4.43791220e-01 4.72349007e+00 1.82159407e+00 1.46859684e-01
# #  4.21972949e+00 2.63264159e+00 4.78133927e+00 2.71451794e-03
# #  5.15596465e-01 4.45120371e+00 1.98635648e+00 4.91615770e+00
# #  4.09874977e+00 2.27931362e-01 3.03742336e+00 7.93922082e-01
# #  8.76114467e-01 5.24828161e-01 2.64069816e+00 3.47670380e+00
# #  2.09436200e+00 3.84627770e+00 1.82819056e-01 4.83954166e+00
# #  1.35497549e+00 4.22083442e-01 5.99544217e-01 3.41995764e+00
# #  1.22450652e+00 2.58251615e-01 8.62805217e-01 2.63873869e+00
# #  3.02569398e+00 1.74552295e+00 2.28656624e-01 9.02390614e-01
# #  1.25776664e+00 4.33481524e+00 1.67550491e+00 2.22580939e+00
# #  4.41711808e+00 1.24096617e+00 1.96316343e-01 1.36325900e-01
# #  2.79581369e+00 3.25328136e-01 4.66394154e+00 4.36126799e-01
# #  2.79119460e+00 1.71492726e+00 7.68612094e-01 3.41229477e+00
# #  1.61345111e+00 4.49829878e+00 4.27898880e+00 4.85746152e+00
# #  4.62687353e+00 3.08833153e+00 3.36855918e+00 1.77497389e+00
# #  4.81055462e-01 2.16299891e+00 3.85841936e+00 2.75674360e+00
# #  1.32872828e+00 3.50193033e+00 3.71655520e+00 2.84284089e+00
# #  2.93718683e+00 4.97660819e+00 7.60597025e-01 1.95791608e+00
# #  2.77288474e+00 3.60958647e+00 5.32669891e-01 2.19375385e+00
# #  3.12039593e+00 1.68489445e+00 4.31420317e+00 1.46272095e+00
# #  3.40963453e+00 4.43558381e+00 1.98104034e+00 3.92719904e+00
# #  2.16555132e+00 4.25656331e+00 2.15468955e+00 1.48406391e+00
# #  4.44654407e+00 1.68986289e+00 4.06734264e+00 4.48035074e+00
# #  2.75336238e+00 2.66787353e-01 8.25920049e-01 3.93353436e+00
# #  1.71346527e+00 4.49548114e+00]


# # Solution 2 - Histogram
# # Draw a histogram
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

# # Output:
# # [3.40882847 3.64927406 3.23135115 4.96657512 0.57307378 2.55598844
# #  2.4498071  4.53031297 0.01735712 0.96618117 0.96801711 3.17465815
# #  1.12657105 3.92481419 4.59902293 0.52774245 2.86044713 1.41252613
# #  3.61277399 4.50605103 2.96984699 1.60349414 0.91537106 0.89572839
# #  4.9377144  2.01476377 3.73384106 0.14476462 0.65508657 1.57594942
# #  3.40725381 3.90185456 0.58525407 0.75958024 1.19661512 2.24893465
# #  4.81109638 0.8453077  0.5733334  3.48210361 4.10412085 0.206451
# #  1.29761347 0.52855341 0.19248561 2.06096463 4.81366795 2.02647772
# #  1.12841828 3.86887849 1.90536033 4.34723199 3.91123438 1.30801591
# #  3.59459321 2.94941551 0.4481122  4.70944318 1.76905816 2.89175165
# #  2.67413238 1.66971355 0.4178406  2.67942674 4.4988256  4.94523164
# #  3.88348266 1.9905963  2.26849137 2.6900355  1.32895658 0.25776857
# #  3.80074983 4.69889612 3.93706641 4.53896818 1.13465392 2.90315113
# #  0.17784074 3.85244266 0.34247227 4.32316274 2.83989092 4.93704048
# #  4.11996171 3.07018861 4.99211638 2.13116329 3.06948491 3.55270534
# #  4.01089078 3.05529459 2.29438801 1.15743809 4.6271464  1.94233342
# #  2.24306156 2.78555163 3.67407094 0.59278502 3.18755642 0.1196076
# #  4.35570356 0.35219438 1.62505937 3.74130732 4.40029059 2.93355832
# #  0.3636874  3.52385917 1.91324615 1.90908668 4.62412938 0.22420771
# #  1.3243758  1.1043803  1.16471722 2.85244235 3.30155827 0.67713693
# #  2.35201478 0.1320391  3.35815497 0.60631186 0.2772137  2.71556999
# #  4.73824253 1.32595344 3.10744658 4.51425919 1.77631813 2.10117507
# #  0.04723054 4.24917408 2.78946094 4.14442291 2.9011607  1.15505989
# #  1.75118201 0.47390665 2.3061373  1.46664773 4.03174993 2.20032712
# #  0.89930056 2.49078589 0.80049746 0.5723739  3.50631762 0.61260876
# #  0.290015   3.34283945 4.29815832 2.76214411 1.94301753 2.32268042
# #  4.84012698 1.40160511 0.94395177 4.87814623 3.79590765 1.52732594
# #  1.12233493 0.34395982 0.55308557 3.83952795 0.94575153 4.89097571
# #  0.34040425 0.47034175 1.16247116 3.75589327 1.13176353 2.83933977
# #  0.13531687 4.32355943 2.23041416 0.03403947 4.61792691 4.15474307
# #  3.06912665 1.46852149 3.95626868 2.63741628 4.32586192 0.36897549
# #  3.18259563 1.77946531 2.92242886 0.31318968 2.55077668 1.4330763
# #  4.06520499 2.82050383 2.49693542 1.73505585 3.69265875 4.11008295
# #  0.29165402 2.55005748 0.887574   0.37144806 4.8385181  3.07582596
# #  3.3417094  0.71920825 2.4013966  1.70150425 4.02891255 1.31910796
# #  1.32118659 2.05148277 2.21362314 2.38010008 4.23270893 4.11248858
# #  3.33171346 1.21454448 1.80976775 4.93451545 1.32454871 4.11284218
# #  3.46984859 3.90184235 4.98437839 2.3516325  1.81775852 0.33352035
# #  1.85310674 2.68537933 3.87017372 3.23852215 4.07751942 2.6814931
# #  0.21818177 3.99934219 3.43288787 2.6236212  2.89015962 4.62085324
# #  3.58657633 4.83183221 2.63010038 2.15772857 0.77750646 0.58191583
# #  2.07958136 0.77775384 4.12321746 2.09418374]


# Solution 3 - Big Data Distributions
# Create an array with 100000 random numbers, and display them using a histogram with 100 bars
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()



# Solution 4 - Normal Data Distribution
# A typical normal data distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
