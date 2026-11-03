---
id: TC-AC-DS-E2E-128-detail-sku-buka-screening-dan-info-grid
title: "Popup Device SKU Detail: Jalur Buka, Screening, Backdrop, dan Info Grid"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-426
  - TC-AC-DS-427
  - TC-AC-DS-428
  - TC-AC-DS-429
coverage:
  web: automated
---

# Popup Device SKU Detail: Jalur Buka, Screening, Backdrop, dan Info Grid

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` dan `SFR-VEL-4P` serta seed (#29, #30); data Usage by Company dan jaringan entitas (#32, #24). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-426: Popup Detail dibuka lewat klik SKU dan lewat row action Detail ke tujuan yang sama

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Tutup popup dengan ikon close `[✕]`
4. Klik ⋯ pada baris `HHR-ARC-100`, pilih `Detail`
5. Verifikasi Popup `Device SKU Detail` yang sama persis untuk SKU `HHR-ARC-100` tampil

### TC-AC-DS-427: Screening Popup Device SKU Detail: Header, Body, dan Footer

6. Verifikasi Header memuat judul flat "Device SKU Detail" (tidak diinterpolasi dengan kode SKU)
7. Verifikasi satu-satunya kontrol penutup berupa ikon close `[✕]`
8. Verifikasi tidak ada tombol teks "Close"
9. Verifikasi Info Grid berpasangan label dan nilai: `SKU`, `Device Name`, `Brand`, `Model/Type`
10. Verifikasi bagian Usage by Company memuat Table Tools `Search`, `Filter`, `Download`
11. Verifikasi placeholder Search "Search company, entity type..."
12. Verifikasi kolom `Company` (sortable), `Entity Type` (sortable), `Total Stock` (sortable), dan `Column Visibility (⋯)` (unsortable: klik header membuka overlay Column Visibility, body per baris berupa row action menu)
13. Verifikasi tidak ada row action pada baris tabel Usage by Company
14. Verifikasi baris pertama (default sort Company A-Z) adalah `PT Arunika Prima`
15. Verifikasi Footer memuat Pagination lokal pada tabel Usage by Company

### TC-AC-DS-428: Klik backdrop pada Popup Device SKU Detail tidak menutup popup

16. Klik area backdrop di luar popup
17. Verifikasi Popup `Device SKU Detail` masih tampil
18. Tekan Esc
19. Verifikasi Popup `Device SKU Detail` tertutup dan List Device SKU tampil

### TC-AC-DS-429: Info Grid Popup Detail menampilkan SKU, Device Name, Brand, dan Model/Type

20. Klik SKU `SFR-VEL-4P`
21. Verifikasi Info Grid memuat SKU `SFR-VEL-4P`
22. Verifikasi Info Grid memuat Device Name `4-Port Fixed Reader`
23. Verifikasi Info Grid memuat Brand `Veltrix`
24. Verifikasi Info Grid memuat Model/Type `SF-4`

### Pemulihan state akhir

25. Tutup popup dengan ikon close `[✕]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 3 dan 25 (S-03). Pada TC-AC-DS-426 langkah 3 menutup popup sebelum jalur buka kedua.
- Langkah 1, 20 dibuka dari List yang dibuka hook `beforeEach`; tidak ada Search yang dipakai untuk menemukan baris (kedua SKU tampil di halaman pertama List pada urutan bawaan).
- Expected 427 butir a.i dipecah menjadi langkah 6 sampai 8; butir b.ii menjadi langkah 10 dan 11; butir b.iii langkah 12 dan 13 (kolom disebut utuh, row action dipisah).
- TC-AC-DS-428 butir a ditulis langkah 17 dan butir b langkah 19 (anchor: List Device SKU tampil).
- Temuan untuk QA:
  - S-14: TC 426 dan 429 tidak menyebut Search untuk menemukan baris `HHR-ARC-100` dan `SFR-VEL-4P`; spec mengandalkan keduanya tampil di halaman pertama List (urutan bawaan). Bila tidak, perlu langkah Search.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
