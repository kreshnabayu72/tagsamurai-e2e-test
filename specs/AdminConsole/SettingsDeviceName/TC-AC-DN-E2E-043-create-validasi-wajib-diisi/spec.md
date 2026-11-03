---
id: TC-AC-DN-E2E-043-create-validasi-wajib-diisi
title: "Create Device Name: Validasi Wajib Diisi (Device Name, Measurement, Category)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-87
  - TC-AC-DN-88
  - TC-AC-DN-101
  - TC-AC-DN-102
  - TC-AC-DN-103
coverage:
  web: automated
---

# Create Device Name: Validasi Wajib Diisi (Device Name, Measurement, Category)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`).
- Data Dinamis: nama yang diketik `Wireless Gateway 2 {runId}-043` dan `Wireless Gateway 3 {runId}-043`; lima spasi sebagai Device Name (TC-AC-DN-88). Semua [Submit] ditolak validasi sehingga tidak ada record yang dibuat dan tidak ada cleanup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-87: Submit Create dengan Device Name kosong

1. Klik tombol `+ Device Name` pada toolbar
2. Klik field Measurement lalu pilih `Unit`
3. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
4. Klik `[Submit]` dengan field Device Name dibiarkan kosong
5. Verifikasi error inline di bawah field Device Name: "Device name must not be empty"
6. Verifikasi popup form tetap terbuka
7. Verifikasi Measurement `Unit` dipertahankan
8. Verifikasi Category `Antenna` dipertahankan
9. Verifikasi tidak ada toast

### TC-AC-DN-88: Device Name hanya spasi diperlakukan sebagai kosong

10. Klik `[Clear Field]`
11. Ketik lima spasi pada field Device Name
12. Klik field Measurement lalu pilih `Unit`
13. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
14. Klik `[Submit]`
15. Verifikasi error inline di bawah field Device Name: "Device name must not be empty"
16. Verifikasi popup form tetap terbuka

### TC-AC-DN-101: Submit Create tanpa Measurement

17. Klik `[Clear Field]`
18. Ketik `Wireless Gateway 2 {runId}-043` pada field Device Name
19. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
20. Klik `[Submit]` dengan field Measurement dibiarkan kosong
21. Verifikasi error inline di bawah field Measurement: "Measurement must not be empty"
22. Verifikasi popup form tetap terbuka
23. Verifikasi Device Name `Wireless Gateway 2 {runId}-043` dipertahankan
24. Verifikasi Category `Antenna` dipertahankan

### TC-AC-DN-102: Submit Create tanpa Category

25. Klik `[Clear Field]`
26. Ketik `Wireless Gateway 3 {runId}-043` pada field Device Name
27. Klik field Measurement lalu pilih `Unit`
28. Klik `[Submit]` dengan field Category dibiarkan kosong
29. Verifikasi error inline di bawah field Category: "Category must not be empty"
30. Verifikasi popup form tetap terbuka
31. Verifikasi Device Name `Wireless Gateway 3 {runId}-043` dipertahankan
32. Verifikasi Measurement `Unit` dipertahankan

### TC-AC-DN-103: Submit Create dengan ketiga field kosong

33. Klik `[Clear Field]`
34. Klik `[Submit]` tanpa mengisi apa pun
35. Verifikasi error inline "Device name must not be empty" di bawah field Device Name
36. Verifikasi error inline "Measurement must not be empty" di bawah field Measurement
37. Verifikasi error inline "Category must not be empty" di bawah field Category
38. Verifikasi popup form tetap terbuka
39. Verifikasi tidak ada toast
40. Klik icon close `[✕]` pada popup

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Kelima TC bertanda FE Test "Need API" (validasi wajib diisi tetap melewati halaman dengan backend nyata).
- Alasan lebih dari sekitar 35 langkah (prinsip 13 bagian 3, "Halaman yang sama dipakai berulang"): kelima TC memakai form Create yang sama dengan Submit yang selalu diblokir validasi, sehingga satu pembukaan popup dipakai bersama dan tidak ada record yang dibuat. Jumlah langkah (40) berasal dari pemecahan `Verifikasi` per klausa (S-01) dan dari pengisian ulang field yang dikosongkan antar-TC; tiap bagian tetap bermakna bila bagian sebelumnya gagal.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 10, 17, 25, dan 33 (`[Clear Field]` menghapus error inline dan isian TC sebelumnya, sesuai S-09 dan R-12, sebelum TC berikutnya) serta langkah 40 (menutup form yang kosong tanpa dialog `Unsaved Changes`).
- Urutan TC pada `sourceTc` mengikuti pengelompokan error per field (Device Name kosong dan hanya spasi, lalu Measurement, Category, dan ketiganya kosong).
- Temuan untuk QA:
  - Post Condition "Tidak ada record baru tersimpan" pada kelima TC tidak punya langkah observasi di TC sehingga tidak diasersi; yang diasersi adalah error inline dan popup yang tetap terbuka.
