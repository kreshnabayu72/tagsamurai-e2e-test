---
id: TC-FA-TDC-E2E-169-popup-versions-screening-badge-status-isi-kolom-dan-class-land
title: "Popup Versions: Screening, Badge Status, Isi Kolom, dan Class Land"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-603
  - TC-FA-TDC-604
  - TC-FA-TDC-605
  - TC-FA-TDC-606
coverage:
  web: automated
---

# Popup Versions: Screening, Badge Status, Isi Kolom, dan Class Land

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleDataBldNpVersions`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom sesuai Example Data kecuali BLD-NP yang memakai fixture khusus (bukan baris BLD-NP Example Data). Class BLD-NP (`Bangunan tidak permanen`) memiliki 5 versi: Jan 2028 Scheduled (UL 12, SL 8.33%, Straight Line, `PMK 72/2023`, Rina P); Jan 2027 Cancelled (UL 15, SL 6.67%, Straight Line, `PMK 72/2023`, Rina P); Jan 2026 Current (UL 10, SL 10%, Straight Line, `PMK 72/2023`, Rina P); Jan 2025 Past (UL 8, SL 12.5%, Straight Line, `PMK 72/2023`, Rina P); versi pertama tanpa Effective From Past (UL 10, SL 10%, Straight Line, `UU HPP 7/2021; PMK 72/2023`, System). LAND memakai baris Example Data (Land; satu versi pertama). Format tanggal General Settings company disediakan dari fixture.
- Kemampuan teknis: membuka Drawer class dengan klik Class Code dan membuka Popup Versions dengan `View versions`; membaca severity badge Status (info, danger, success, secondary).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-603: Screening Popup Versions

1. Klik Class Code BLD-NP
2. Klik `View versions`
3. Verifikasi Header: Title `Versions`
4. Verifikasi Header: satu baris teks polos `BLD-NP – Bangunan tidak permanen` di bawah judul
5. Verifikasi Header: ikon Close `(X)` tampil
6. Verifikasi Header: tidak ada tombol teks `[Close]`
7. Verifikasi Header: tidak ada Search dan tidak ada Download
8. Verifikasi Body: kolom `Effective From | Status | Useful Life (years) | Straight Line Rate | Declining Balance Rate | Allowed Methods | Regulation Reference | Modified By | Last Updated | Action`
9. Verifikasi Body: 5 baris versi (Jan 2028, Jan 2027, Jan 2026, Jan 2025, lalu versi pertama `—` di bawah)
10. Verifikasi Body: header kolom tanpa ikon sort dan tanpa kolom Column Visibility `⋯`
11. Verifikasi Footer: Pagination

### TC-FA-TDC-604: Badge Status versi: Current, Scheduled, Past, dan Cancelled

12. Verifikasi Jan 2028: badge `Scheduled` (severity info)
13. Verifikasi Jan 2027: badge `Cancelled` (severity danger)
14. Verifikasi Jan 2026: badge `Current` (severity success)
15. Verifikasi Jan 2025: badge `Past` (severity secondary)
16. Verifikasi versi pertama: badge `Past` (severity secondary)

### TC-FA-TDC-605: Isi kolom Popup Versions: Effective From, angka, metode, referensi, pembuat, dan tanggal

17. Verifikasi Effective From: `Jan 2028`, `Jan 2026`, dan `—` untuk versi pertama (format MMM YYYY)
18. Verifikasi Useful Life (years): `12`, `10`, `10`
19. Verifikasi Straight Line Rate: `8.33%`, `10%`, `10%`; Declining Balance Rate `—` pada ketiga baris
20. Verifikasi Allowed Methods `Straight Line` pada ketiga baris
21. Verifikasi Regulation Reference: `PMK 72/2023`, `PMK 72/2023`, `UU HPP 7/2021; PMK 72/2023`
22. Verifikasi Modified By: `Rina P`, `Rina P`, `System`
23. Verifikasi Last Updated tampil dalam format tanggal General Settings
24. Verifikasi Last Updated tidak pernah kosong
25. Tutup Popup Versions lewat ikon Close `(X)`
26. Tutup Drawer BLD-NP lewat `[×]`

### TC-FA-TDC-606: Popup Versions class Land: nilai kosong ditulis strip

27. Klik Class Code LAND
28. Klik `View versions`
29. Verifikasi tabel memuat satu baris versi pertama: Effective From `—`, Status `Current`, Useful Life `—`, Straight Line Rate `—`, Declining Balance Rate `—`, Allowed Methods `—`
30. Verifikasi tabel tidak kosong
31. Tutup Popup Versions lewat ikon Close `(X)`
32. Tutup Drawer LAND lewat `[×]`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-603, 604, 605, 606. TC-FA-TDC-603, 604, dan 605 memakai Popup Versions BLD-NP yang sama sehingga dibuka sekali (langkah 1 dan 2); TC-FA-TDC-606 memakai LAND.
- Langkah penghubung (S-03): langkah 25 dan 31 (menutup Popup Versions), langkah 26 dan 32 (menutup Drawer tanpa perubahan lewat `[×]`; Drawer tidak dirty sehingga dialog `Unsaved Changes` tidak muncul). Tabel utama memuat sembilan baris pada satu halaman; baris BLD-NP dan LAND tidak perlu dicari lewat Search (8b.13).
- Asersi absence langkah 6 dan 7 didahului anchor positif langkah 3 sampai 5 (judul dan ikon Close pada header yang sama; 8b.2), dan langkah 10 didahului langkah 8 (kolom tampil pada tabel yang sama).
- Temuan untuk QA:
  - TC-FA-TDC-605 butir g (Last Updated) tidak memuat nilai tanggal persis; spec mengasersi format General Settings saja.
  - TC-FA-TDC-604: severity badge (info, danger, success, secondary) tidak memberi cara observasi di TC; spec mengasersinya apa adanya.
  - TC-FA-TDC-605 butir g menyatakan Last Updated tidak pernah kosong tanpa memberi nilai pada tiap baris.
  - TC-FA-TDC-606 mensyaratkan baris LAND Example Data; langkah TC tidak menyebut cara menutup Drawer LAND.
  - Email akun Total Control dan user penyunting `Rina P` tidak tertulis di TC.
