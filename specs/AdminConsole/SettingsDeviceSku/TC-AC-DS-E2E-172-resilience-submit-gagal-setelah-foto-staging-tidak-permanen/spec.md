---
id: TC-AC-DS-E2E-172-resilience-submit-gagal-setelah-foto-staging-tidak-permanen
title: "Resilience Foto Staging: Submit atau Save Gagal setelah Foto di Staging Tidak Membuat Foto Permanen"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-143
  - TC-AC-DS-230
coverage:
  web: automated
---

# Resilience Foto Staging: Submit atau Save Gagal setelah Foto di Staging Tidak Membuat Foto Permanen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37).
- Data Dinamis: tidak ada; tidak ada SKU baru yang tersimpan. Target Edit `HHR-ARC-200` tidak berubah (Save ditolak).
- Kemampuan teknis (disediakan tim FE/BE): fixture BE untuk memeriksa penyimpanan file (staging versus permanen, referensi record SKU).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-143: Submit gagal setelah foto di staging tidak membuat foto menjadi permanen tanpa referensi

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `Asset TAG`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `T-ORP` pada field Model/Type
6. Ketik `HHR-ARC-100` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Klik `[Submit]`
9. Verifikasi SKU baru tidak tersimpan
10. Verifikasi popup tetap terbuka
11. Verifikasi foto tetap tampil di staging
12. Periksa penyimpanan file lewat fixture BE
13. Verifikasi fixture BE menunjukkan foto hanya berada di staging tanpa referensi record SKU
14. Verifikasi foto tidak berstatus permanen (Pola A)
15. Klik `[✕]` untuk menutup popup
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik `[Leave]`

### TC-AC-DS-230: Save gagal setelah foto di staging tidak membuat foto permanen tanpa referensi

18. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
19. Ubah SKU menjadi `HHR-ARC-100` (duplikat)
20. Unggah `foto-b.png` pada slot kedua
21. Klik `[Save]`
22. Verifikasi Save ditolak karena duplikat
23. Verifikasi popup tetap terbuka
24. Periksa penyimpanan file lewat fixture BE
25. Verifikasi fixture BE menunjukkan `foto-b.png` hanya berada di staging tanpa referensi record SKU (Pola A)
26. Klik `[✕]`, klik `[Leave]` pada dialog `Unsaved Changes`, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search `HHR-ARC-200` (menemukan baris target, R-16, langkah 18) dan langkah 26 (menutup form dirty dan Search, S-08).
- Temuan untuk QA:
  - Plan memberi kelas b (resilience) pada spec ini, tetapi TC 143 dan 230 memakai kode duplikat sebagai pemicu kegagalan (bukan respons 5xx atau timeout yang dipaksa); tidak ada intercept. TC tidak menyatakan istilah "Pola A" di PRD yang diketahui spec; dipakai apa adanya. Kemampuan fixture BE pemeriksaan penyimpanan file disediakan tim FE/BE (S-13). Dialog `Unsaved Changes` di akhir TC 230 diasumsikan muncul karena form dirty; TC tidak menyatakannya.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
