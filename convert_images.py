import os
from PIL import Image

images_dir = os.path.join(os.getcwd(), 'images')

def optimize_image(input_name, output_name, target_size, max_kb):
    in_path = os.path.join(images_dir, input_name)
    out_path = os.path.join(images_dir, output_name)
    
    if not os.path.exists(in_path):
        print(f"File not found: {in_path}")
        return

    with Image.open(in_path) as img:
        # Resize image
        if isinstance(target_size, tuple):
            img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
        else:
            # Maintain aspect ratio for hero width
            w_percent = target_size / float(img.size[0])
            h_size = int(float(img.size[1]) * float(w_percent))
            img_resized = img.resize((target_size, h_size), Image.Resampling.LANCZOS)

        # Convert to RGB if RGBA
        if img_resized.mode in ("RGBA", "P"):
            img_resized = img_resized.convert("RGB")

        # Tune WebP quality to be strictly under max_kb
        quality = 85
        while quality >= 20:
            img_resized.save(out_path, 'WEBP', quality=quality, optimize=True)
            size_kb = os.path.getsize(out_path) / 1024.0
            if size_kb <= max_kb:
                break
            quality -= 5

        size_kb = os.path.getsize(out_path) / 1024.0
        print(f"[OK] {output_name}: {size_kb:.2f} KB (Quality: {quality}, Dimensions: {img_resized.size})")

print("--- Optimizing Product Images (800x800, < 150 KB) ---")
for i in range(101, 109):
    optimize_image(f"p{i}.png", f"p{i}.webp", (800, 800), 150)

print("\n--- Optimizing Hero Banner (1600px width, < 250 KB) ---")
optimize_image("hero-banner.png", "hero-banner.webp", 1600, 250)
