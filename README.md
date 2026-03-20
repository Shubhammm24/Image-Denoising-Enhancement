# 📘 Image Denoising & Enhancement Project

## 🎯 Project Title

**Image Denoising & Enhancement using Spatial and Frequency Domain Techniques**

---

## 👨‍💻 Developed By

* **Shubham Ranjan (23U03088)**
  Department of Information Technology
  IIIT Bhopal

---

## 📌 Project Description

This project focuses on removing different types of noise and blur from images using classical Digital Image Processing techniques. The implementation is divided into three levels of increasing complexity:

* **Easy Level** → Salt & Pepper Noise Removal
* **Medium Level** → Gaussian Noise Removal
* **Hard Level** → Motion Blur + Noise Restoration

Each level uses different filtering techniques and is evaluated using PSNR and SSIM metrics.

---

## 📂 Folder Structure

```
denoise_enhance/
 ├─ data/
 │   ├─ clean/            # Input images
 │   └─ results/          # Output images
 ├─ src/
 │   ├─ common.py         # Utility functions (I/O, conversion)
 │   ├─ degrade.py        # Noise and blur generation
 │   ├─ metrics.py        # PSNR & SSIM calculation
 │   ├─ visualize.py      # Visualization helpers
 │   ├─ level_easy.py     # Median filter + sharpening
 │   ├─ level_medium.py   # Gaussian, Wiener, NLM
 │   └─ level_hard.py     # RL, Wiener, NLM, sharpening
 ├─ run_easy.py
 ├─ run_medium.py
 ├─ run_hard.py
 ├─ results_plot.py
 └─ requirements.txt
```

---

## ⚙️ Requirements

Install all dependencies using:

```
pip install -r requirements.txt
```

### Required Libraries:

* OpenCV (`cv2`)
* NumPy
* SciPy
* scikit-image
* Matplotlib

---

## ▶️ How to Run

### 1️⃣ Place Input Image

Put your image inside:

```
data/clean/
```

---

### 2️⃣ Run Easy Level

```
python run_easy.py
```

✔ Removes Salt & Pepper noise using Median Filter
✔ Applies Unsharp Masking for sharpening

---

### 3️⃣ Run Medium Level

```
python run_medium.py
```

✔ Applies Gaussian Smoothing
✔ Wiener Filtering
✔ Non-Local Means (best result)

---

### 4️⃣ Run Hard Level

```
python run_hard.py
```

✔ Applies Motion Blur simulation
✔ Richardson–Lucy deblurring
✔ Blind Wiener deconvolution
✔ NLM denoising + sharpening

---

### 5️⃣ Plot Results

```
python results_plot.py
```

✔ Generates PSNR and SSIM comparison graphs

---

## 📊 Evaluation Metrics

| Metric | Description                    |
| ------ | ------------------------------ |
| PSNR   | Measures pixel-level accuracy  |
| SSIM   | Measures structural similarity |

Higher values indicate better quality.

---

## 🧠 Techniques Used

| Technique       | Purpose                       |
| --------------- | ----------------------------- |
| Median Filter   | Removes Salt & Pepper noise   |
| Gaussian Filter | Smooths Gaussian noise        |
| Wiener Filter   | Frequency-based noise removal |
| Non-Local Means | Preserves textures            |
| Richardson–Lucy | Motion blur removal           |
| Unsharp Masking | Enhances edges                |

---

## 🌍 Applications

* CCTV footage enhancement
* Medical image processing (MRI, X-ray)
* Satellite and drone imaging
* Old photo restoration
* Low-light photography
* Forensic analysis

---

## ⚠️ Notes

* Hard level results depend on correct PSF estimation
* Severe blur cannot be fully recovered
* NLM preserves details but is computationally expensive

---

## 🎯 Conclusion

This project demonstrates how different noise types require different filtering approaches. Classical image processing techniques such as Median, Wiener, and Richardson–Lucy provide effective restoration without the need for deep learning.

---

## 📎 Future Scope

* Deep Learning models (DnCNN, DeblurGAN)
* Real-time video denoising
* Adaptive PSF estimation
* Super-resolution integration

---

## 📌 End of Project
