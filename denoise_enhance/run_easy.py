from src.common import imread_gray, imwrite
from src.degrade import add_salt_pepper
from src.level_easy import median_restore, unsharp
from src.metrics import psnr, ssim_wrap

img = imread_gray("data/clean/ai-future.jpg") 


noisy = add_salt_pepper(img, 0.08)


restored = median_restore(noisy, 3)


sharpened = unsharp(restored)


imwrite("data/results/e_easy_noisy.png", noisy)
imwrite("data/results/e_easy_restored.png", restored)
imwrite("data/results/e_easy_sharp.png", sharpened)


print("PSNR:", psnr(img, restored))
print("SSIM:", ssim_wrap(img, restored))

