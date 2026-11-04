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
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) berupa seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (total pada modal dapat lebih besar karena entri yang ditulis spec lain, sehingga urutan diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26`), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup #29, #30, #33, #35 ke keadaan awal sebelum spec; Changelog audit trail permanen; entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-408: Sort modal Changelog kelas alfabetis: Action, SKU, dan Field

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik ikon Filter pada modal
4. Pada field Date pilih rentang `01/09/26` sampai `03/10/26`
5. Klik `[Apply]` pada Filter Panel modal
6. Klik header kolom Action sekali
7. Verifikasi Action Ascending: baris pertama bernilai `Create`
8. Klik header kolom Action sekali lagi
9. Verifikasi Action Descending: baris pertama bernilai `Edit`
10. Klik header kolom Action sekali lagi
11. Verifikasi urutan kembali ke Date Newest First
12. Klik header kolom SKU sekali
13. Verifikasi SKU Ascending: baris pertama `4-Port Fixed Reader (SFR-VEL-4P)`
14. Klik header kolom SKU sekali lagi
15. Verifikasi SKU Descending: baris pertama `UHF Handheld Reader (HHR-ARC-300)`
16. Klik header kolom SKU sekali lagi (siklus ketiga, kembali ke Date Newest First)
17. Klik header kolom Field sekali
18. Verifikasi Field Ascending: baris pertama berField `Model/Type`
19. Klik header kolom Field sekali lagi
20. Verifikasi Field Descending: baris pertama berField `SKU`
21. Klik header kolom Field sekali lagi (siklus ketiga, kembali ke Date Newest First)

### Pemulihan state antar TC

22. Tutup modal Changelog, lalu klik ikon Changelog
23. Verifikasi modal "Changelog: Device SKU" tampil
24. Klik ikon Filter pada modal
25. Pada field Date pilih rentang `01/09/26` sampai `03/10/26`
26. Klik `[Apply]` pada Filter Panel modal

### TC-AC-DS-409: Sort Date modal Changelog default Newest First dengan siklus tiga tahap

27. Verifikasi urutan awal Newest First (rentang Date seed diterapkan): baris pertama Delete `HHR-ARC-300` (03/10/26 14:20)
28. Klik header kolom Date sekali
29. Verifikasi Oldest First: baris pertama entri Edit Model/Type `HHR-BIG-01` tanggal 01/09/26 08:00
30. Klik header kolom Date sekali lagi
31. Verifikasi urutan Newest First
32. Klik header kolom Date sekali lagi
33. Verifikasi urutan kembali ke default Newest First

### Pemulihan state akhir

34. Tutup modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 3 sampai 5 dan 24 sampai 26 (menerapkan Filter Date seed `01/09/26` sampai `03/10/26` sesuai langkah TC-AC-DS-408 dan TC-AC-DS-409), langkah 16 dan 21 (menuntaskan siklus tiga klik kolom SKU dan Field sesuai langkah TC "Ulangi siklus tiga klik"; TC hanya mengasersi Ascending dan Descending untuk kedua kolom), langkah 22 (membuka ulang modal agar "urutan awal" TC 409 diamati dari modal baru), dan langkah 34 (S-03, S-09).
- Expected 409 butir c dipecah: langkah 31 (klik kedua Newest First) dan langkah 33 (klik ketiga kembali ke default).
- Temuan untuk QA:
  - S-12: baris pertama (mis. `HHR-ARC-300`) diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26` sesuai TC-AC-DS-408 dan TC-AC-DS-409, sehingga tidak bergantung pada entri buatan spec lain; nilai literal Pre-setup #29 dan #33 memakai pengecualian S-12 A-11 (`suite.md`).
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - TC 408 Expected butir a menyebut klik ketiga kembali ke Date Newest First hanya untuk Action; untuk SKU dan Field TC tidak mengasersi klik ketiga.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
