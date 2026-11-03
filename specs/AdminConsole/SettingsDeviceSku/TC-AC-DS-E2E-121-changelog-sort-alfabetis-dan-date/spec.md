---
id: TC-AC-DS-E2E-121-changelog-sort-alfabetis-dan-date
title: "Sort Changelog: Alfabetis Action, SKU, Field dan Date Default Newest First Tiga Tahap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-408
  - TC-AC-DS-409
coverage:
  web: automated
---

# Sort Changelog: Alfabetis Action, SKU, Field dan Date Default Newest First Tiga Tahap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) dalam keadaan awal 35 entri, General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup #29, #30, #33, #35 ke keadaan awal sebelum spec; Changelog audit trail permanen sehingga keadaan awal 35 entri dijamin fixture BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-408: Sort modal Changelog kelas alfabetis: Action, SKU, dan Field

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik header kolom Action sekali
4. Verifikasi Action Ascending: baris pertama bernilai `Create`
5. Klik header kolom Action sekali lagi
6. Verifikasi Action Descending: baris pertama bernilai `Edit`
7. Klik header kolom Action sekali lagi
8. Verifikasi urutan kembali ke Date Newest First
9. Klik header kolom SKU sekali
10. Verifikasi SKU Ascending: baris pertama `4-Port Fixed Reader (SFR-VEL-4P)`
11. Klik header kolom SKU sekali lagi
12. Verifikasi SKU Descending: baris pertama `UHF Handheld Reader (HHR-ARC-300)`
13. Klik header kolom SKU sekali lagi (siklus ketiga, kembali ke Date Newest First)
14. Klik header kolom Field sekali
15. Verifikasi Field Ascending: baris pertama berField `Model/Type`
16. Klik header kolom Field sekali lagi
17. Verifikasi Field Descending: baris pertama berField `SKU`
18. Klik header kolom Field sekali lagi (siklus ketiga, kembali ke Date Newest First)

### Pemulihan state antar TC

19. Tutup modal Changelog, lalu klik ikon Changelog
20. Verifikasi modal "Changelog: Device SKU" tampil

### TC-AC-DS-409: Sort Date modal Changelog default Newest First dengan siklus tiga tahap

21. Verifikasi urutan awal Newest First: baris pertama Delete `HHR-ARC-300` (03/10/26 14:20)
22. Klik header kolom Date sekali
23. Verifikasi Oldest First: baris pertama entri Edit Model/Type `HHR-BIG-01` tanggal 01/09/26 08:00
24. Klik header kolom Date sekali lagi
25. Verifikasi urutan Newest First
26. Klik header kolom Date sekali lagi
27. Verifikasi urutan kembali ke default Newest First

### Pemulihan state akhir

28. Tutup modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 13 dan 18 (menuntaskan siklus tiga klik kolom SKU dan Field sesuai langkah TC "Ulangi siklus tiga klik"; TC hanya mengasersi Ascending dan Descending untuk kedua kolom), langkah 19 (membuka ulang modal agar "urutan awal" TC 409 diamati dari modal baru), dan langkah 28 (S-03, S-09).
- Expected 409 butir c dipecah: langkah 25 (klik kedua Newest First) dan langkah 27 (klik ketiga kembali ke default).
- Temuan untuk QA:
  - S-12: TC menetapkan nilai literal Pre-setup (mis. baris pertama `HHR-ARC-300`, jumlah 35 entri) pada audit trail permanen; spec mengikuti TC dan bergantung pada keadaan awal yang dijamin fixture BE. Pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - TC 408 Expected butir a menyebut klik ketiga kembali ke Date Newest First hanya untuk Action; untuk SKU dan Field TC tidak mengasersi klik ketiga.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
