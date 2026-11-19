---
id: TC-FA-ASTL-UI-056-toolbar-search
title: "Siklus kotak Search di toolbar"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-SRC-4@tabel-all-assets"]
smoke: []
dependsOn: []
trace:
  "EB-SRC-4@tabel-all-assets": [2, 4, 6, 8, 10, 12, 14, 16]
anchor: []
coverage:
  web: automated
---
# Siklus kotak Search di toolbar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Toolbar All Assets
- Data:
  - DU-056-1: Aset pertama: Name `Printer Laser - 1`, Asset ID `AST-0031`, Status `Not Paired Yet`.
  - DU-056-2: Aset kedua: Name `Kursi Kerja - 1`, Asset ID `AST-0072`, Status `Available`.
- Kondisi:
  - K1: tabel memuat DU-056-1 dan DU-056-2, dan Search dengan kata kunci `AST-0031` hanya menjawab DU-056-1.

## Test Steps

### Ikon membuka input dan pencarian berjalan saat Enter
1. Tampilkan Toolbar All Assets dengan kondisi K1
2. Verifikasi hanya ikon Search yang tampil dan kotak input belum terlihat
3. Klik ikon Search
4. Verifikasi kotak Search terbuka dengan fokus pada input
5. Ketik Search `AST-0031` tanpa menekan Enter
6. Verifikasi tabel masih memuat `Printer Laser - 1` dan `Kursi Kerja - 1`
7. Tekan Enter
8. Verifikasi tabel memuat `Printer Laser - 1` dan tidak memuat `Kursi Kerja - 1`

### Hapus teks dengan ✕ tidak mereset sebelum Enter
9. Klik `✕` pada kotak Search
10. Verifikasi kotak Search kosong dan tabel tetap hanya memuat `Printer Laser - 1`
11. Tekan Enter
12. Verifikasi tabel memuat `Printer Laser - 1` dan `Kursi Kerja - 1`

### Panah kembali menutup kotak sekaligus mereset
13. Ketik Search `AST-0031`, tekan Enter
14. Verifikasi tabel memuat `Printer Laser - 1` dan `Kursi Kerja - 1` tidak tampil
15. Klik `(←)` pada kotak Search
16. Verifikasi kotak Search tertutup dan tabel memuat `Printer Laser - 1` dan `Kursi Kerja - 1`
