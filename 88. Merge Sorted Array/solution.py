index_m1 = m - 1
        index_m2 = len(nums1) - 1
        index_n = n - 1
        
        while index_n >= 0 and index_m1 >=0:
            if nums2[index_n] > nums1[index_m1]:
                nums1[index_m2] = nums2[index_n]
                index_n -= 1
            else:
                nums1[index_m2] = nums1[index_m1]
                index_m1 -= 1
            index_m2 -= 1
        while index_n >=0:
            nums1[index_m2] = nums2[index_n]
            index_m2 -= 1
            index_n -= 1
