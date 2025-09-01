import subprocess
from PIL import Image
import matplotlib.pyplot as plt

original_image = "input.jpeg"
output_jxl = "output.jxl"
decoded_image = "decoded.jpeg"

# --- KOMPRESIJA ---
subprocess.run([
    r"C://Users//krstic//Desktop//MISOS//jxl//cjxl.exe",
    original_image, output_jxl, "-q", "30", "--lossless_jpeg=0"
])

# --- DEKOMPRESIJA ---
subprocess.run([
    r"C://Users//krstic//Desktop//MISOS//jxl//djxl.exe",
    output_jxl, decoded_image
])

# --- UČITAVANJE SLIKA ---
img_original = Image.open(original_image)
img_decoded = Image.open(decoded_image)

# --- PRIKAZ JEDNA DO DRUGE ---
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(img_original)
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(img_decoded)
axes[1].set_title("Kompresovana (JPEG XL → JPEG)")
axes[1].axis("off")

plt.tight_layout()
plt.show()

# --- ČUVANJE ---
print(f"✅ Dekodirana slika sačuvana kao: {decoded_image}")
