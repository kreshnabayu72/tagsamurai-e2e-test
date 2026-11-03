---
id: TC-FA-PREF-E2E-097-modal-changelog-screening-isi-9-baris-contoh-dan-hover-modified-by
title: "Modal Changelog: Screening, Isi 9 Baris Contoh, dan Hover Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-289
  - TC-FA-PREF-290
  - TC-FA-PREF-291
coverage:
  web: automated
---

# Modal Changelog: Screening, Isi 9 Baris Contoh, dan Hover Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PB-1; Changelog Preferences berisi 9 entri contoh PB-C1 (Date 27/10/26 16:40 sampai 20/10/26 09:12; Modified By Budi Santoso "Budi S" dan Rina Anggraini "Rina A"; format tanggal General Settings dd/MM/yy dan 24 jam). Urutan tulis seed: pada Date yang sama baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6 (id baris 2 > id baris 3; id baris 6 > id baris 7), sehingga urutan baris pada langkah 17 sampai 25 mengikuti seed. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed PB-C1 mengatur Changelog company seed ke tepat 9 entri (lihat Temuan untuk QA).
- Spec ini tidak menulis ke Changelog.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-289: Screening modal Changelog: Preferences dari ikon View history

1. Klik ikon View history di header tab Preferences
2. Verifikasi modal terbuka di tengah halaman dengan latar overlay gelap
3. Verifikasi modal berjudul "Changelog: Preferences" dengan ikon [✕] di header
4. Verifikasi toolbar modal memuat ikon Search, ikon Filter, dan ikon Download tanpa tombol aksi lain
5. Arahkan kursor ke ikon Search pada toolbar modal
6. Verifikasi tooltip "Search" tampil
7. Arahkan kursor ke ikon Filter
8. Verifikasi tooltip "Filter" tampil
9. Arahkan kursor ke ikon Download
10. Verifikasi tooltip "Download" tampil
11. Arahkan kursor ke header kolom Actions (⋯)
12. Verifikasi tooltip "Column Visibility" tampil
13. Verifikasi header tabel memuat kolom berurutan: Date, Action, Section, Field, Old Value, New Value, Modified By, diikuti header kolom Actions (⋯) tanpa isi data
14. Verifikasi kolom Date menampilkan indikator sort Newest First
15. Verifikasi tabel menampilkan 9 baris data
16. Verifikasi paginasi menampilkan ukuran halaman 10

### TC-FA-PREF-290: Isi 9 baris contoh Changelog tampil sesuai urutan terbaru di atas

17. Verifikasi baris 1: Date 27/10/26 16:40, Action Edit, Section Chart of Accounts, Field Default Capitalization Offset, Old Value —, New Value 1-2900 – Biaya Dikapitalisasi, Modified By Budi S
18. Verifikasi baris 2: Date 26/10/26 14:05, Action Edit, Section Disposal, Field Disposal Documents — Sell, Old Value Optional, New Value Required, Modified By Rina A
19. Verifikasi baris 3: Date 26/10/26 14:05, Action Edit, Section Disposal, Field Disposal Documents — Scrap, Old Value Optional, New Value Required, Modified By Rina A
20. Verifikasi baris 4: Date 25/10/26 11:20, Action Edit, Section Journal Export, Field Journal Grouping, Old Value Group, New Value Group, Category, Modified By Budi S
21. Verifikasi baris 5: Date 24/10/26 10:02, Action Edit, Section Disposal, Field Default Gain on Disposal, Old Value 4-9100 – Laba Pelepasan Aset, New Value —, Modified By Rina A
22. Verifikasi baris 6: Date 23/10/26 08:45, Action Edit, Section General, Field Fiscal Year Start, Old Value January, New Value April, Modified By Rina A
23. Verifikasi baris 7: Date 23/10/26 08:45, Action Edit, Section General, Field First Accounting Period, Old Value Mar 2026, New Value Jan 2026, Modified By Rina A
24. Verifikasi baris 8: Date 22/10/26 13:30, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 10.000.000, Modified By Rina A
25. Verifikasi baris 9: Date 20/10/26 09:12, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Budi S

### TC-FA-PREF-291: Hover Modified By menampilkan nama lengkap user

26. Arahkan kursor ke sel Modified By "Rina A" pada baris 2
27. Verifikasi sel Modified By baris 2 menampilkan teks "Rina A"
28. Verifikasi tooltip "Rina Anggraini" tampil
29. Arahkan kursor ke sel Modified By "Budi S" pada baris 1
30. Verifikasi sel Modified By baris 1 menampilkan teks "Budi S"
31. Verifikasi tooltip "Budi Santoso" tampil
32. Klik ikon [✕] di header modal Changelog

## Notes

- Langkah penghubung (S-03, S-10): modal dibuka satu kali pada langkah 1 dan dipakai bersama TC-FA-PREF-289, 290, dan 291 karena precondition ketiganya sama dan tidak ada aksi yang mengubah state modal; langkah "Klik ikon View history" TC-FA-PREF-290 dan 291 dipenuhi pembukaan itu. Langkah 32 menutup modal.
- Langkah 6, 8, 10, dan 12 mengasersi tooltip tepat setelah hover (bagian 8b butir 5); langkah 5, 7, 9, dan 11 adalah aksi hover TC-FA-PREF-289 langkah 3.
- Temuan untuk QA:
  - TC-FA-PREF-289 Expected f ("9 baris") dan TC-FA-PREF-290 Expected a sampai i (posisi baris 1 sampai 9) bergantung pada Changelog yang tepat berisi 9 entri seed; Changelog adalah audit trail permanen yang tumbuh karena Save pada spec lain (S-12, S-14). Spec memakai asumsi bahwa seed PB-C1 mereset Changelog company seed ke tepat 9 entri (seed terisolasi menurut Catatan TC) dan menulis total absolut; bila reset tidak tersedia, Expected perlu ditulis ulang relatif terhadap baseline atau dibatasi Filter Date pada tanggal seed (20/10/26 sampai 27/10/26).
  - TC-FA-PREF-291 tidak menyebut apakah teks sel diasersi; spec mengasersi teks "Rina A" dan "Budi S" sesuai Expected a dan b.
  - TC-FA-PREF-289 mengasersi paginasi "ukuran halaman 10" tanpa menyebut elemen paginasi lain; spec mengasersi ukuran halaman 10 saja.
