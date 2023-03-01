import numpy as np
from patchify import patchify as p
import cv2

raw_img = cv2.imread('HillShade_30.png')
# raw_mask = cv2.imread('mask.png')

# for img in range(raw_img.shape[0]):
#     img2 = raw_img[img]
#     patch_img = p(img2, (256, 256), step=192)
#     for i in range(patch_img.shape[0]):
#         for j in range(patch_img.shape[1]):
#             single_patch_img = patch_img[i,j,:,:]
#             cv2.imwrite('hsd_patch/' + 'img_' + str(img) + '_' + str(i) + '_' + str(j) + '.png')

# for mask in range(raw_mask.shape[0]):
#     mask2 = raw_mask[mask]
#     patch_mask = p(mask2, (256, 256), step=192)
#     for i in range(patch_mask.shape[0]):
#         for j in range(patch_mask.shape[1]):
#             single_patch_mask = patch_mask[i,j,:,:]
#             cv2.imwrite('mask_patch/' + 'img_' + str(mask) + '_' + str(i) + '_' + str(j) + '.png')

patches_img = p(raw_img, (512, 512, 3), step=(448))
# patches_mask = p(raw_mask, (512, 512, 3), step=448)

for i in range(patches_img.shape[0]):
    for j in range(patches_img.shape[1]):
        single_patch_img = patches_img[i, j, 0, :, :, :]
        if not cv2.imwrite('hsd_patch/' + 'hillshade_' + str(i) + '_' +str(j)+'.png', single_patch_img):
            raise Exception("Gaiso nulis image")

# for i in range(patches_mask.shape[0]):
#     for j in range(patches_mask.shape[1]):
#         single_patch_mask = patches_mask[i, j, 0, :, :, :]
#         if not cv2.imwrite('mask_patch/' + 'mask_' + str(i) + '_' +str(j)+'.png', single_patch_mask):
#             raise Exception("Gaiso nulis mask")

