def get_biggest(numbers):
    if numbers:  # if numbers not []
        numbers_str = [str(num) for num in numbers]  # convert a list of ints to a list of strings
        max_len = len(max(numbers_str, key=len))
        # create a reverse-sorted list from a set of first digits
        first_digits = sorted(list({num[0] for num in numbers_str}), reverse=True)
        sorted_list = []
        for digit in first_digits:  # for every digit in list of first digits
            # create a sublist of numbers starting with the same digit
            sublist = list(filter(lambda num: num[0] == digit, numbers_str))
            # sort multiplying number by the length of the longest string
            sorted_sublist = sorted(sublist, key=lambda num: num * max_len, reverse=True)
            sorted_list += sorted_sublist  # concatenate
        return int(''.join(sorted_list))
    return -1


print(get_biggest([0, 0, 0, 0, 0, 0]))
print(get_biggest([7, 71, 72]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([]))
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
print(get_biggest([62, 626]))

print(get_biggest([3347, 3737, 4919, 6296, 4984, 424, 8837, 2482, 6264, 6361, 3769, 650, 1334, 3100, 9107, 8723,
                   2048, 6495, 2018, 7716, 3747, 8417, 4632, 4684, 55, 4620, 7705, 9603, 6597, 5398, 9621, 1953, 2689,
                   6023, 6835,
                   1745, 5187, 3628, 5533, 4911, 8934, 4624, 1705, 8767, 1188, 2228, 4462, 1006, 816, 4053, 3929, 4843,
                   596, 5239,
                   8833, 8660, 4267, 4379, 6171, 452, 392, 1974, 1573, 6755, 8926, 1338, 460, 9346, 3882, 4892, 2511,
                   600, 5126, 3866,
                   587, 3048, 998, 9455, 5556, 256, 8237, 9719, 5465, 2138, 8552, 9341, 4208, 7938, 1231, 8413, 3903,
                   6151, 7235,
                   7176, 8073, 6097, 7686, 6092, 9191, 6215, 9788, 2327, 8652, 6473, 2667, 3497, 1768, 3481, 3561, 7,
                   1254, 9560,
                   3636, 5827, 7451, 1354, 6151, 3608, 274, 935, 3632, 4659, 2423, 5806, 6891, 953, 4975, 1754, 5085,
                   5735, 2568,
                   6914, 190, 6953, 9034, 6069, 5355, 1617, 5575, 895, 9132, 2472, 9157, 5168, 6368, 5223, 6233, 2890,
                   1576, 9845,
                   1859, 7012, 3782, 5471, 5736, 6735, 8970, 3417, 7009, 3253, 4603, 7697, 6277, 9123, 3318, 2794, 6772,
                   1390, 5061,
                   5404, 271, 7298, 2484, 8890, 4006, 5132, 109, 9721, 1650, 9107, 5224, 8546, 349, 7497, 7778, 3461,
                   4198, 317, 7795,
                   3201, 1797, 6991, 9766, 5076, 6813, 6279, 7919, 3224, 8526, 7608, 1355, 9022, 5912, 8750, 2592, 9506,
                   7882, 5375,
                   7718, 1922, 5528, 4260, 3957, 9232, 7827, 1919, 3690, 3314, 2631, 1328, 4655, 1092, 3643, 6231, 7947,
                   7826, 6380,
                   9664, 9522, 6950, 8748, 5205, 2907, 1208, 4326, 6354, 5978, 1115, 2462, 8308, 4642, 6724, 4698, 3925,
                   4175, 3136,
                   9880, 5696, 6034, 9164, 5627, 7139, 3784, 2271, 8815, 2458, 3154, 3632, 3867, 3150, 8358, 6684, 527,
                   2981, 6390,
                   5844, 1695, 2442, 9400, 780, 4342, 427, 431, 1551, 1055, 4468, 4800, 6835, 7639, 49, 4236, 4160,
                   4186, 7101, 2987,
                   2986, 3014, 3375, 2225, 8035, 8622, 4093, 5318, 9421, 5068, 3454, 6592, 9317, 72, 4509, 254, 790,
                   3696, 7037, 1549,
                   6636, 9421, 4426, 122, 1068, 7330, 2472, 2018, 3095, 6369, 4561, 9826, 6903, 1507, 9056, 6108, 9288,
                   7502, 8199,
                   6555, 1342, 5558, 8082, 5898, 4380, 2591, 3254, 6331, 1256, 6654, 2745, 2011, 7152, 1615, 7634, 4955,
                   8721, 2741,
                   8868, 8848, 2507, 5985, 6656, 2958, 5149, 4533, 127, 5501, 8083, 3884, 9059, 8872, 9129, 1481, 9508,
                   9227, 1731,
                   5072, 5471, 9247, 8914, 3438, 7241, 4124, 4404, 1857, 2342, 1431, 4694, 8976, 7477, 1112, 2224, 7161,
                   1694, 267,
                   461, 9369, 8151, 3218, 7553, 4649, 2528, 4011, 7829, 193, 4560, 2272, 8146, 5015, 8287, 4084, 7,
                   3284, 4317, 9662,
                   3664, 5272, 5228, 2731, 3308, 674, 8167, 8494, 5199, 6611, 7604, 1111, 3511, 3063, 1339, 93, 2750,
                   3512, 3703,
                   9034, 2874, 7955, 7212, 6525, 6281, 2810, 5829, 8520, 2199, 6584, 749, 8931, 7837, 3094, 1877, 3618,
                   7155, 4304,
                   6198, 5882, 7293, 4155, 7736, 9399, 9201, 8826, 2330, 2958, 8818, 2675, 2391, 9039, 1758, 4533, 6056,
                   32, 8358,
                   4360, 483, 1699, 2258, 5923, 8499, 4242, 4734, 5415, 2259, 3927, 4359, 2588, 3176, 670, 4881, 5225,
                   5248, 9221,
                   1003, 4366, 9297, 271, 6746, 3145, 776, 7119, 3890, 2078, 7523, 4656, 4310, 7360, 5929, 2997, 2044,
                   8771, 5628,
                   2969, 4641, 9623, 8922, 1599, 1751, 3402, 7839, 4633, 831, 3786, 3689, 5682, 669, 3623, 5507, 1966,
                   1721, 4898,
                   4009, 2165, 4612, 6111, 6055, 1344, 1302, 2222, 8951, 6959, 1053, 6557, 2663, 4302, 959, 7295, 9859,
                   6596, 4223,
                   4561, 5991, 8244, 6288, 5057, 8838, 3190, 9050, 2761, 7887, 5699, 5551, 8506, 8187, 5459, 1339, 7254,
                   6411, 9317,
                   3296, 2129, 6525, 3155, 4928, 4721, 8831, 3757, 3830, 7763, 2358, 9777, 6390, 5006, 5318, 1000, 4252,
                   6186, 1822,
                   4035, 7743, 5301, 5307, 5644, 3786, 3849, 6107, 291, 7293, 7042, 8, 7230, 3384, 6489, 2843, 5470,
                   672, 3542, 1323,
                   6970, 1526, 6830, 3447, 4064, 5022, 5661, 4089, 3451, 9130, 6595, 4421, 9671, 2984, 4729, 7831, 1273,
                   6664, 9150,
                   3860, 7822, 7311, 210, 3485, 2768, 7496, 6626, 3497, 3451, 3344, 4722, 8970, 4135, 4192, 59, 8915,
                   3156, 5772,
                   2270, 5470, 698, 3499, 8913, 4751, 2021, 7675, 7805, 8397, 3839, 4082, 4473, 5730, 2531, 6596, 3345,
                   7005, 241,
                   5955, 1121, 1086, 96, 9866, 9490, 5677, 7607, 3245, 5981, 3351, 5977, 1012, 2169, 8621, 682, 8118,
                   7569, 4084, 262,
                   2401, 5456, 3215, 6176, 5505, 2350, 3969, 6816, 8879, 7466, 9115, 4100, 4897, 8076, 257, 1206, 9811,
                   5708, 8506,
                   7850, 9186, 9784, 6435, 1081, 8889, 1845, 6186, 9255, 4800, 603, 686, 6825, 6208, 2576, 3164, 6004,
                   6772, 1349,
                   9390, 9223, 6977, 1496, 2789, 4242, 5296, 2394, 3647, 418, 9407, 7220, 8445, 2006, 6344, 5246, 5527,
                   9026, 5064,
                   2720, 3574, 4573, 5492, 9564, 9686, 812, 4654, 96, 9508, 8288, 1709, 8335, 2058, 5580, 4273, 8275,
                   9207, 6067,
                   5728, 9627, 1721, 7646, 4329, 5611, 3633, 7030, 4510, 440, 1010, 3588, 5922, 1929, 3569, 3922, 774,
                   9705, 5125,
                   7623, 47, 3655, 1368, 7259, 1610, 9745, 2989, 6114, 7204, 5592, 1621, 8001, 221, 7880, 4039, 3346,
                   89, 2280, 3101,
                   1243, 448, 54, 2699, 3365, 3495, 1356, 1443, 9323, 3903, 9028, 4461, 6249, 1577, 7964, 4207, 7341,
                   4994, 4219,
                   2277, 259, 1777, 3854, 7420, 552, 484, 737, 579, 4239, 560, 9693, 5864, 4975, 8747, 1427, 3140, 2335,
                   1833, 3755,
                   9187, 8806, 6581, 4222, 7480, 1086, 6893, 9048, 6917, 7203, 1345, 3546, 8320, 6601, 4428, 948, 3026,
                   4025, 465,
                   2150, 9022, 7663, 6272, 3850, 278, 2871, 6329, 7092, 1512, 5253, 7717, 8354, 6835, 8399, 3231, 1713,
                   2007, 2520,
                   4431, 8876, 2153, 4877, 919, 1269, 6148, 5435, 1779, 167, 681, 7862, 1831, 1823, 9842, 7388, 9460,
                   8960, 8526,
                   5478, 9078, 732, 7169, 6455, 6876, 2734, 6767, 2817, 9283, 1191, 750, 7165, 4954, 897, 2780, 8087,
                   3425, 4358,
                   8984, 7637, 1314, 5515, 2941, 4859, 1106, 1444, 4753, 975, 1166, 2131, 135, 3580, 7062, 1273, 772,
                   4447, 4997,
                   8833, 4467, 8311, 6052, 1191, 4625, 3608, 8167, 2954, 610, 5292, 3431, 8630, 372, 4019, 9926, 6147,
                   2792, 3708,
                   7372, 7150, 5164, 2756, 7936, 1250, 5748, 3992, 4838, 7166, 9811, 2227, 7492, 5954, 8611, 5067, 394,
                   9576, 9622,
                   9195, 295, 4965, 3321, 8770, 613, 2212, 9534, 6627, 9046, 9176, 7129, 645, 3512, 6205, 5283, 6171,
                   3639, 283, 3565,
                   1026, 4717, 2259, 4695, 7274, 6952, 623, 9193, 6457, 4436, 7953, 4708, 6022, 4771, 9419, 1416, 3485,
                   2514, 1378,
                   3676, 841, 6370, 8570, 507]))
