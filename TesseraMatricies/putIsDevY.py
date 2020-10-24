def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


replace_dict = {
        "z\n":"z[i]\n",
        "y\n":"y[i]\n",
        "x\n":"x[i]\n",
        "rr\n":"rr[i]\n",
        "rr ":"rr[i] ",
        "x*":"x[i]*",
        "y*":"y[i]*",
        "z*":"z[i]*",
        "rr*":"rr[i]*",
        "x2":"x2[i]",
        "x3":"x3[i]",
        "x3":"x3[i]",
        "x4":"x4[i]",
        "x5":"x5[i]",
        "x6":"x6[i]",
        "x7":"x7[i]",
        "x8":"x8[i]",
        "x9":"x9[i]",
        "x10":"x10[i]",
        "x11":"x11[i]",
        "x12":"x12[i]",
        "x13":"x13[i]",
        "x14":"x14[i]",
        "x15":"x15[i]",
        "x16":"x16[i]",
        "x17":"x17[i]",
        "x18":"x18[i]",
        "x19":"x19[i]",
        "x20":"x20[i]",
        "x21":"x21[i]",
        "x22":"x22[i]",
        "x23":"x23[i]",
        "x24":"x24[i]",
        "x25":"x25[i]",
        "x26":"x26[i]",
        "x27":"x27[i]",
        "x28":"x28[i]",
        "x29":"x29[i]",
        "x30":"x30[i]",
        "x31":"x31[i]",
        "x32":"x32[i]",
        "x33":"x33[i]",
        "x34":"x34[i]",
        "x35":"x35[i]",
        "x36":"x36[i]",
        "x37":"x37[i]",
        "x38":"x38[i]",
        "x39":"x39[i]",
        "x40":"x40[i]",
        "x41":"x41[i]",
        "x42":"x42[i]",
        "x43":"x43[i]",
        "x44":"x44[i]",
        "x45":"x45[i]",
        "x46":"x46[i]",
        "x47":"x47[i]",
        "x48":"x48[i]",
        "x49":"x49[i]",
        "x50":"x50[i]",
        "x51":"x51[i]",
        "x52":"x52[i]",
        "x53":"x53[i]",
        "x54":"x54[i]",
        "x55":"x55[i]",
        "x56":"x56[i]",
        "x57":"x57[i]",
        "x58":"x58[i]",
        "x59":"x59[i]",
        "x60":"x60[i]",
        "x61":"x61[i]",
        "x62":"x62[i]",
        "x63":"x63[i]",
        "x64":"x64[i]",
        "x65":"x65[i]",
        "x66":"x66[i]",
        "x67":"x67[i]",
        "x68":"x68[i]",
        "x69":"x69[i]",
        "x70":"x70[i]",
        "x71":"x71[i]",
        "x72":"x72[i]",
        "x73":"x73[i]",
        "x74":"x74[i]",
        "x75":"x75[i]",
        "x76":"x76[i]",
        "x77":"x77[i]",
        "x78":"x78[i]",
        "x79":"x79[i]",
        "x80":"x80[i]",
        "x81":"x81[i]",
        "x82":"x82[i]",
        "x83":"x83[i]",
        "x84":"x84[i]",
        "x85":"x85[i]",
        "x86":"x86[i]",
        "x87":"x87[i]",
        "x88":"x88[i]",
        "x89":"x89[i]",
        "x90":"x90[i]",
        "x91":"x91[i]",
        "x92":"x92[i]",
        "x93":"x93[i]",
        "x94":"x94[i]",
        "x95":"x95[i]",
        "x96":"x96[i]",
        "x97":"x97[i]",
        "x98":"x98[i]",
        "x99":"x99[i]",
        "x100":"x100[i]",
        "y2":"y2[i]",
        "y3":"y3[i]",
        "y3":"y3[i]",
        "y4":"y4[i]",
        "y5":"y5[i]",
        "y6":"y6[i]",
        "y7":"y7[i]",
        "y8":"y8[i]",
        "y9":"y9[i]",
        "y10":"y10[i]",
        "y11":"y11[i]",
        "y12":"y12[i]",
        "y13":"y13[i]",
        "y14":"y14[i]",
        "y15":"y15[i]",
        "y16":"y16[i]",
        "y17":"y17[i]",
        "y18":"y18[i]",
        "y19":"y19[i]",
        "y20":"y20[i]",
        "y21":"y21[i]",
        "y22":"y22[i]",
        "y23":"y23[i]",
        "y24":"y24[i]",
        "y25":"y25[i]",
        "y26":"y26[i]",
        "y27":"y27[i]",
        "y28":"y28[i]",
        "y29":"y29[i]",
        "y30":"y30[i]",
        "y31":"y31[i]",
        "y32":"y32[i]",
        "y33":"y33[i]",
        "y34":"y34[i]",
        "y35":"y35[i]",
        "y36":"y36[i]",
        "y37":"y37[i]",
        "y38":"y38[i]",
        "y39":"y39[i]",
        "y40":"y40[i]",
        "y41":"y41[i]",
        "y42":"y42[i]",
        "y43":"y43[i]",
        "y44":"y44[i]",
        "y45":"y45[i]",
        "y46":"y46[i]",
        "y47":"y47[i]",
        "y48":"y48[i]",
        "y49":"y49[i]",
        "y50":"y50[i]",
        "y51":"y51[i]",
        "y52":"y52[i]",
        "y53":"y53[i]",
        "y54":"y54[i]",
        "y55":"y55[i]",
        "y56":"y56[i]",
        "y57":"y57[i]",
        "y58":"y58[i]",
        "y59":"y59[i]",
        "y60":"y60[i]",
        "y61":"y61[i]",
        "y62":"y62[i]",
        "y63":"y63[i]",
        "y64":"y64[i]",
        "y65":"y65[i]",
        "y66":"y66[i]",
        "y67":"y67[i]",
        "y68":"y68[i]",
        "y69":"y69[i]",
        "y70":"y70[i]",
        "y71":"y71[i]",
        "y72":"y72[i]",
        "y73":"y73[i]",
        "y74":"y74[i]",
        "y75":"y75[i]",
        "y76":"y76[i]",
        "y77":"y77[i]",
        "y78":"y78[i]",
        "y79":"y79[i]",
        "y80":"y80[i]",
        "y81":"y81[i]",
        "y82":"y82[i]",
        "y83":"y83[i]",
        "y84":"y84[i]",
        "y85":"y85[i]",
        "y86":"y86[i]",
        "y87":"y87[i]",
        "y88":"y88[i]",
        "y89":"y89[i]",
        "y90":"y90[i]",
        "y91":"y91[i]",
        "y92":"y92[i]",
        "y93":"y93[i]",
        "y94":"y94[i]",
        "y95":"y95[i]",
        "y96":"y96[i]",
        "y97":"y97[i]",
        "y98":"y98[i]",
        "y99":"y99[i]",
        "y100":"y100[i]",
        "z2":"z2[i]",
        "z3":"z3[i]",
        "z3":"z3[i]",
        "z4":"z4[i]",
        "z5":"z5[i]",
        "z6":"z6[i]",
        "z7":"z7[i]",
        "z8":"z8[i]",
        "z9":"z9[i]",
        "z10":"z10[i]",
        "z11":"z11[i]",
        "z12":"z12[i]",
        "z13":"z13[i]",
        "z14":"z14[i]",
        "z15":"z15[i]",
        "z16":"z16[i]",
        "z17":"z17[i]",
        "z18":"z18[i]",
        "z19":"z19[i]",
        "z20":"z20[i]",
        "z21":"z21[i]",
        "z22":"z22[i]",
        "z23":"z23[i]",
        "z24":"z24[i]",
        "z25":"z25[i]",
        "z26":"z26[i]",
        "z27":"z27[i]",
        "z28":"z28[i]",
        "z29":"z29[i]",
        "z30":"z30[i]",
        "z31":"z31[i]",
        "z32":"z32[i]",
        "z33":"z33[i]",
        "z34":"z34[i]",
        "z35":"z35[i]",
        "z36":"z36[i]",
        "z37":"z37[i]",
        "z38":"z38[i]",
        "z39":"z39[i]",
        "z40":"z40[i]",
        "z41":"z41[i]",
        "z42":"z42[i]",
        "z43":"z43[i]",
        "z44":"z44[i]",
        "z45":"z45[i]",
        "z46":"z46[i]",
        "z47":"z47[i]",
        "z48":"z48[i]",
        "z49":"z49[i]",
        "z50":"z50[i]",
        "z51":"z51[i]",
        "z52":"z52[i]",
        "z53":"z53[i]",
        "z54":"z54[i]",
        "z55":"z55[i]",
        "z56":"z56[i]",
        "z57":"z57[i]",
        "z58":"z58[i]",
        "z59":"z59[i]",
        "z60":"z60[i]",
        "z61":"z61[i]",
        "z62":"z62[i]",
        "z63":"z63[i]",
        "z64":"z64[i]",
        "z65":"z65[i]",
        "z66":"z66[i]",
        "z67":"z67[i]",
        "z68":"z68[i]",
        "z69":"z69[i]",
        "z70":"z70[i]",
        "z71":"z71[i]",
        "z72":"z72[i]",
        "z73":"z73[i]",
        "z74":"z74[i]",
        "z75":"z75[i]",
        "z76":"z76[i]",
        "z77":"z77[i]",
        "z78":"z78[i]",
        "z79":"z79[i]",
        "z80":"z80[i]",
        "z81":"z81[i]",
        "z82":"z82[i]",
        "z83":"z83[i]",
        "z84":"z84[i]",
        "z85":"z85[i]",
        "z86":"z86[i]",
        "z87":"z87[i]",
        "z88":"z88[i]",
        "z89":"z89[i]",
        "z90":"z90[i]",
        "z91":"z91[i]",
        "z92":"z92[i]",
        "z93":"z93[i]",
        "z94":"z94[i]",
        "z95":"z95[i]",
        "z96":"z96[i]",
        "z97":"z97[i]",
        "z98":"z98[i]",
        "z99":"z99[i]",
        "z100":"z100[i]",
        "rr2":"rr2[i]",
        "rr3":"rr3[i]",
        "rr3":"rr3[i]",
        "rr4":"rr4[i]",
        "rr5":"rr5[i]",
        "rr6":"rr6[i]",
        "rr7":"rr7[i]",
        "rr8":"rr8[i]",
        "rr9":"rr9[i]",
        "rr10":"rr10[i]",
        "rr11":"rr11[i]",
        "rr12":"rr12[i]",
        "rr13":"rr13[i]",
        "rr14":"rr14[i]",
        "rr15":"rr15[i]",
        "rr16":"rr16[i]",
        "rr17":"rr17[i]",
        "rr18":"rr18[i]",
        "rr19":"rr19[i]",
        "rr20":"rr20[i]",
        "rr21":"rr21[i]",
        "rr22":"rr22[i]",
        "rr23":"rr23[i]",
        "rr24":"rr24[i]",
        "rr25":"rr25[i]",
        "rr26":"rr26[i]",
        "rr27":"rr27[i]",
        "rr28":"rr28[i]",
        "rr29":"rr29[i]",
        "rr30":"rr30[i]",
        "rr31":"rr31[i]",
        "rr32":"rr32[i]",
        "rr33":"rr33[i]",
        "rr34":"rr34[i]",
        "rr35":"rr35[i]",
        "rr36":"rr36[i]",
        "rr37":"rr37[i]",
        "rr38":"rr38[i]",
        "rr39":"rr39[i]",
        "rr40":"rr40[i]",
        "rr41":"rr41[i]",
        "rr42":"rr42[i]",
        "rr43":"rr43[i]",
        "rr44":"rr44[i]",
        "rr45":"rr45[i]",
        "rr46":"rr46[i]",
        "rr47":"rr47[i]",
        "rr48":"rr48[i]",
        "rr49":"rr49[i]",
        "rr50":"rr50[i]",
        "rr51":"rr51[i]",
        "rr52":"rr52[i]",
        "rr53":"rr53[i]",
        "rr54":"rr54[i]",
        "rr55":"rr55[i]",
        "rr56":"rr56[i]",
        "rr57":"rr57[i]",
        "rr58":"rr58[i]",
        "rr59":"rr59[i]",
        "rr60":"rr60[i]",
        "rr61":"rr61[i]",
        "rr62":"rr62[i]",
        "rr63":"rr63[i]",
        "rr64":"rr64[i]",
        "rr65":"rr65[i]",
        "rr66":"rr66[i]",
        "rr67":"rr67[i]",
        "rr68":"rr68[i]",
        "rr69":"rr69[i]",
        "rr70":"rr70[i]",
        "rr71":"rr71[i]",
        "rr72":"rr72[i]",
        "rr73":"rr73[i]",
        "rr74":"rr74[i]",
        "rr75":"rr75[i]",
        "rr76":"rr76[i]",
        "rr77":"rr77[i]",
        "rr78":"rr78[i]",
        "rr79":"rr79[i]",
        "rr80":"rr80[i]",
        "rr81":"rr81[i]",
        "rr82":"rr82[i]",
        "rr83":"rr83[i]",
        "rr84":"rr84[i]",
        "rr85":"rr85[i]",
        "rr86":"rr86[i]",
        "rr87":"rr87[i]",
        "rr88":"rr88[i]",
        "rr89":"rr89[i]",
        "rr90":"rr90[i]",
        "rr91":"rr91[i]",
        "rr92":"rr92[i]",
        "rr93":"rr93[i]",
        "rr94":"rr94[i]",
        "rr95":"rr95[i]",
        "rr96":"rr96[i]",
        "rr97":"rr97[i]",
        "rr98":"rr98[i]",
        "rr99":"rr99[i]",
        "rr100":"rr100[i]"
        }


f1 = open('finalSoapFunctionsWithoutSqrtPi3DevY.txt', 'r')
f2 = open('finalSoapFunctionsWithoutSqrtPi3IsDevY.txt', 'w')
for line in f1:
    text=line
    text = replace_all(text,replace_dict)
    f2.write(text)
f1.close()
f2.close()




#finalSoapFunctionsWithoutSqrtPi3.txt
