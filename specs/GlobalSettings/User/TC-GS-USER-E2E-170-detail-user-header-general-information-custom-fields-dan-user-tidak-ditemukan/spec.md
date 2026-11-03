---
id: TC-GS-USER-E2E-170-detail-user-header-general-information-custom-fields-dan-user-tidak-ditemukan
title: "User Detail: Tanpa Guided Walkthrough, Subtitle Employee ID Kosong, Label Switch dan Severity Badge Header, Section Custom Fields Collapsed, serta User Tidak Ditemukan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1125
  - TC-GS-USER-1089
  - TC-GS-USER-1123
  - TC-GS-USER-1120
  - TC-GS-USER-1118
coverage:
  web: automated
---

# User Detail: Tanpa Guided Walkthrough, Subtitle Employee ID Kosong, Label Switch dan Severity Badge Header, Section Custom Fields Collapsed, serta User Tidak Ditemukan

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`). TC-GS-USER-1125 mengasersi bahwa Detail User tidak memunculkan walkthrough otomatis; spec mengikuti state hook (flag `seen`), lihat Temuan untuk QA.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Custom Field `Blood Type` (Dropdown A/B/O/AB) dan `Skills` (Multi-Dropdown Excel/SQL) (Tabel Data Uji Pre-setup No. 24), keduanya aktif. Data target Pre-setup No. 10 sampai 22 tidak dipakai sebagai target dan tidak diubah (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD), dan dihapus di hook `after`. Semua user Division `Finance`, Access `Fixed Asset`, email `<nama tanpa spasi huruf kecil>+{runId}-170@qwertysystem.net`:
  - `Ahmad Fauzi {runId}-170`: Activated (target TC-GS-USER-1125).
  - `Lilis Handayani {runId}-170`: Activated, Employee ID kosong (target TC-GS-USER-1089).
  - `Mike Tan {runId}-170`: Active (Global), Pending Activation, tanpa foto profil (target TC-GS-USER-1123).
  - `Jane Smith {runId}-170`: Inactive (dinonaktifkan manual) (target TC-GS-USER-1123).
  - `Dewi Lestari {runId}-170`: Activated, Blood Type `A`, Skills tanpa nilai (target TC-GS-USER-1120).
- ID user yang tidak ada (TC-GS-USER-1118): nilai ID dan pola URL halaman Detail ditentukan tim FE (TC tidak menyebutnya); ID tidak boleh sama dengan ID user mana pun.
- Kemampuan teknis: navigasi URL langsung ke halaman Detail; mengamati badge beserta severity-nya (success, warning, danger) dan avatar inisial.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus kelima user seed lewat API.

## Test Steps

### TC-GS-USER-1125: Halaman Detail User tidak memunculkan guided walkthrough

1. Ketik Search `Ahmad Fauzi {runId}-170`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-170` di User List
3. Verifikasi Header: breadcrumb `User > Detail` tampil
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi tidak ada guided tooltip yang muncul otomatis pada Detail User

### TC-GS-USER-1089: Header Detail menampilkan `—` pada subtitle Employee ID saat kosong

6. Klik menu User di sidebar Global Settings
7. Ketik Search `Lilis Handayani {runId}-170`, tekan Enter
8. Klik Name `Lilis Handayani {runId}-170` di User List
9. Verifikasi Baris 3 Header: subtitle Employee ID (muted) menampilkan `—`
10. Verifikasi Baris 3 Header tetap tampil, tidak disembunyikan

### TC-GS-USER-1123: Header Detail, label switch, severity badge status, dan fallback avatar inisial

11. Klik menu User di sidebar Global Settings
12. Ketik Search `Mike Tan {runId}-170`, tekan Enter
13. Klik Name `Mike Tan {runId}-170` di User List
14. Verifikasi avatar lingkaran dengan inisial pada Header
15. Verifikasi switch berlabel `Active` pada Header
16. Verifikasi badge `Active` severity success pada Header
17. Verifikasi badge `Pending Activation` severity warning pada Header
18. Klik menu User di sidebar Global Settings
19. Ketik Search `Jane Smith {runId}-170`, tekan Enter
20. Klik Name `Jane Smith {runId}-170` di User List
21. Verifikasi switch berlabel `Inactive` pada Header
22. Verifikasi badge `Inactive` severity danger pada Header

### TC-GS-USER-1120: Section Custom Fields collapsed secara default dan field tanpa nilai tampil `—`

23. Klik menu User di sidebar Global Settings
24. Ketik Search `Dewi Lestari {runId}-170`, tekan Enter
25. Klik Name `Dewi Lestari {runId}-170` di User List
26. Verifikasi header Section Custom Fields tampil
27. Verifikasi daftar `Label: Value` Custom Fields tidak tampil (collapsed)
28. Klik header Section Custom Fields
29. Verifikasi daftar `Label: Value` tampil dengan Blood Type `A`
30. Verifikasi Custom Field aktif tanpa nilai Skills tampil `—`
31. Klik header Section Custom Fields
32. Verifikasi daftar `Label: Value` Custom Fields tidak tampil (kembali collapsed)

### TC-GS-USER-1118: Detail untuk user yang tidak ditemukan menampilkan toast netral dan kembali ke User List

33. Buka halaman Detail dengan ID user yang tidak ada (navigasi URL langsung)
34. Verifikasi toast netral: "This user is no longer available."
35. Verifikasi Header dan tab Detail tidak dirender
36. Verifikasi User List tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (36 langkah). Alasan: kelima TC berada di satu kelas harness (fungsional, baca saja) dan satu layar (User Detail); tiap blok berdiri sendiri pada user seed sendiri, dan 14 langkah (1, 2, 6 sampai 8, 11 sampai 13, 18 sampai 20, dan 23 sampai 25) adalah pembukaan Detail berulang (klik menu User, Search, dan klik Name) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-USER-1125 di awal (kunjungan pertama ke Detail), TC-GS-USER-1118 di akhir karena berpindah lewat URL langsung ke ID yang tidak ada.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1, 7, 12, 19, 24 (Search), 6, 11, 18, 23 (kembali ke User List lewat menu User), 4 (Tunggu 5 detik supaya walkthrough, bila ada, sempat muncul sebelum asersi absence), 28 dan 31 (membuka dan menutup Section Custom Fields, bagian dari langkah TC-GS-USER-1120), dan 33 (navigasi URL langsung, pemicu TC-GS-USER-1118).
- Asersi absence/Hidden: langkah 5 didahului halaman Detail termuat (langkah 3, bagian 8b butir 2 untuk "walkthrough tidak muncul"); langkah 27 dan 32 didahului header Section Custom Fields tampil (langkah 26); langkah 35 didahului toast netral (langkah 34, anchor positif dari respons server).
- Pembagian TC lintas spec: header Detail dasar, badge Pending Activation, dan Inactive ada di spec 061; Section Custom Fields inline edit ada di spec 060; Guided Tooltip halaman User List ada di spec 005 dan 006.
- Temuan untuk QA:
  - TC-GS-USER-1125 Precondition c ("walkthrough halaman User sudah selesai atau belum") ambigu; hook suite menyetel flag `seen`, sehingga spec hanya menguji varian "sudah selesai". Varian "belum selesai" membutuhkan pengecualian flag seperti spec 005 dan 006. Need Confirmation: apakah varian "belum selesai" dipisah menjadi spec sendiri.
  - TC-GS-USER-1118 Expected c ("User List yang di-refresh") tidak menyebut cara mengamati refresh; spec hanya mengasersi User List tampil. Pola URL dan ID yang tidak ada tidak disebut TC (lihat Prerequisites).
  - TC-GS-USER-1120 menyebut Skills sebagai contoh ("mis.") Custom Field aktif tanpa nilai; spec memakai Skills (Pre-setup No. 24) dengan nilai dikosongkan pada user seed.
  - TC-GS-USER-1089, 1123, dan 1120 memakai Lilis Handayani, Mike Tan, Jane Smith, dan Dewi Lestari Pre-setup; spec memakai seed bersuffix milik spec (S-06, S-12). Lilis Handayani tidak ada pada Tabel Pre-setup No. 10 sampai 22.
