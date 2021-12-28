# vdpau-va-driver-vp9
Experimental VP9 codec support for vdpau-va-driver (NVIDIA VDPAU-VAAPI wrapper) and chromium-vaapi.

 1. Install Chrome or Chromium 
 2. Modify your existing desktop file:
```bash
sudo vi /usr/share/applications/{google-chrome,chromium}.desktop

# Add '--enable-features=VaapiVideoDecoder  --ignore-gpu-blocklist --enable-gpu-rasterization --enable-zero-copy --use-gl=desktop' to the arguments of each Exec line
```
3. Enable this copr repo:
```bash
sudo dnf copr enable dcrdev/vdpau-va-driver-vp9
```
4. Install driver:
```bash
sudo dnf remove -y libva-vdpau-driver
sudo dnf install -y vdpau-va-driver-vp9
```
