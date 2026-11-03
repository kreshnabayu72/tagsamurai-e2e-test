---
id: TC-FA-RP-E2E-079-edit-matriks-crud-detail-role-1
title: "Edit matriks CRUD Detail Role (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-265
  - TC-FA-RP-266
  - TC-FA-RP-267
  - TC-FA-RP-268
coverage:
  web: automated
---

# Edit matriks CRUD Detail Role (1/3)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: pool #15 (Ahmad Fauzi) dan #18. Ahmad Fauzi memegang Global Role `Manage asset master data` dengan hanya Read aktif (Create, Update, Delete tidak tercentang) dan Global Role `Import data` dengan hanya Read aktif; kedua penugasan disiapkan lewat seed API di hook `before` (TC tidak menyebut kepemilikan role pada TC-FA-RP-265 sampai TC-FA-RP-267, lihat Temuan untuk QA).
- Kemampuan teknis: pencatat request jaringan untuk membuktikan klik sel `—` tidak mengirim permintaan (disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Global Role Ahmad Fauzi `Manage asset master data` dan `Import data` pada keadaan awal pool #15), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).
- Parameter kolom pada langkah 2 sampai 28 (satu blok per kolom, diulang tiga kali): Create (langkah 2 sampai 10), Update (langkah 11 sampai 19), Delete (langkah 20 sampai 28).

## Test Steps

### TC-FA-RP-265, 266, 267: Edit kolom Create, Update, dan Delete pada Global Role CRUD penuh (autosave per cell)

1. Klik Tab `System`, klik Role Name `Manage asset master data` pada section Global Role
2. Centang Create pada baris Ahmad Fauzi
3. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
4. Verifikasi checkbox Create tercentang
5. Muat ulang halaman
6. Verifikasi checkbox Create tetap tercentang
7. Verifikasi checkbox Read tetap tercentang Disabled
8. Hapus centang Create pada baris yang sama
9. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
10. Verifikasi checkbox Create tidak tercentang
11. Centang Update pada baris Ahmad Fauzi
12. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
13. Verifikasi checkbox Update tercentang
14. Muat ulang halaman
15. Verifikasi checkbox Update tetap tercentang
16. Verifikasi checkbox Read tetap tercentang Disabled
17. Hapus centang Update pada baris yang sama
18. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
19. Verifikasi checkbox Update tidak tercentang
20. Centang Delete pada baris Ahmad Fauzi
21. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
22. Verifikasi checkbox Delete tercentang
23. Muat ulang halaman
24. Verifikasi checkbox Delete tetap tercentang
25. Verifikasi checkbox Read tetap tercentang Disabled
26. Hapus centang Delete pada baris yang sama
27. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
28. Verifikasi checkbox Delete tidak tercentang

### TC-FA-RP-268: Sel `—` pada role berkolom CR (Import data) tidak interaktif dan kolom berlaku dapat diedit

29. Klik Tab `System`, klik Role Name `Import data` pada section Global Role
30. Klik sel Update dan sel Delete pada baris Ahmad Fauzi
31. Verifikasi sel Update dan Delete berupa teks `—` tanpa elemen interaktif
32. Verifikasi klik tidak mengirim permintaan
33. Verifikasi klik tidak menampilkan toast
34. Centang kolom Create pada baris Ahmad Fauzi
35. Verifikasi kolom Create dan Read berupa checkbox
36. Verifikasi Read tercentang Disabled
37. Verifikasi muncul toast sukses: `Success, permissions have been updated.`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-265, TC-FA-RP-266, TC-FA-RP-267, TC-FA-RP-268).
- Langkah 2 sampai 28 adalah tiga iterasi berparameter kolom (Create, Update, Delete) atas blok yang identik; tiap iterasi memulihkan nilai awal pada akhirnya (centang dihapus), sehingga iterasi berikutnya tidak bergantung pada hasil iterasi sebelumnya (S-09). Langkah 1 membuka Detail Role sekali untuk ketiganya; muat ulang halaman mempertahankan Detail Role yang sama.
- Langkah penghubung (S-03): membuka Tab System dan Detail Role (langkah 1 dan 29).
- Temuan untuk QA:
  - TC-FA-RP-265, 266, 267 tidak menyebut precondition kepemilikan Global Role `Manage asset master data` oleh Ahmad Fauzi (hanya "Pre-setup #15 tersedia"); spec mengasumsikan penugasan dengan hanya Read aktif.
  - Post Condition TC-FA-RP-265, 266, 267 (sinkron ke Tab Role Settings > User dan berlaku pada request berikutnya) tidak memuat langkah observasi dan tidak diasersi (S-01).
  - TC-FA-RP-268 tidak menyebut apakah penugasan `Import data` Ahmad Fauzi memiliki Create aktif sebelum aksi; spec mengasumsikan hanya Read aktif sehingga centang Create menghasilkan toast sukses.
- Spec ini 37 langkah, di atas smell 35 langkah. Alasan: tiga iterasi berparameter kolom atas blok yang identik (bagian 8b butir 7) ditambah satu blok sel `—`; semua satu kelas pada Detail Role yang sama dan tiap iterasi memulihkan nilai awalnya.
