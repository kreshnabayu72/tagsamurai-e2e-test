---
id: TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber
title: "User Detail Tab Responsibilities: Screening Client FAMS Aktif, Empty State Global, Sinkron Modul Sumber, Client tanpa Subscription FAMS, dan Entitas Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-384
  - TC-GS-USER-385
  - TC-GS-USER-386
  - TC-GS-USER-1019
  - TC-GS-USER-399
coverage:
  web: automated
---

# User Detail Tab Responsibilities: Screening Client FAMS Aktif, Empty State Global, Sinkron Modul Sumber, Client tanpa Subscription FAMS, dan Entitas Principal

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor (ganti akun eksplisit di Test Steps; ketiga entitas berbeda):
  - Total Control Client dengan subscription FAMS aktif (Siti Nurhaliza, Client PT Maju Bersama) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2 dan 26; kredensial `Spectra.env.GS_TC_PASSWORD`): aktor pertama, login di hook `before` (akun default suite). Dipakai TC-GS-USER-384, 1019, dan 399.
  - Total Control Client tanpa subscription FAMS: disediakan tim FE (tidak ada di Tabel Pre-setup; kredensial `Spectra.env.GS_NOFAMS_TC_PASSWORD`). Dipakai TC-GS-USER-385.
  - Total Control entitas Principal: disediakan tim FE (kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`). Dipakai TC-GS-USER-386.
  - Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_NOFAMS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (dibaca, tidak diubah): Dewi Lestari (No. 12) di Client dengan FAMS aktif untuk TC-GS-USER-1019; Dewi Lestari tidak memiliki borrowed asset, assigned asset, pending approval, dan pending task (precondition TC-GS-USER-1019 c; Tabel Pre-setup tidak menyebut state ini).
- Data Dinamis, di-seed lewat API di hook `before` (HK1 dan HK8) dan dihapus di hook `after`:
  - `Ahmad Fauzi {runId}-065`, email `ahmadfauzi+{runId}-065@qwertysystem.net`, Client FAMS aktif: 1 borrowed asset, 1 assigned asset, 1 pending approval, dan 1 pending task (FAMS) (TC-GS-USER-384 dan 399). Tabel Pre-setup mencatat data Responsibilities Ahmad Fauzi (No. 13); TC-GS-USER-399 mengembalikan aset, sehingga spec memakai user seed milik spec.
  - `Dewi Lestari {runId}-065`, email `dewilestari+{runId}-065@qwertysystem.net`, di Client tanpa subscription FAMS (dibuat lewat sesi admin Client tersebut) (TC-GS-USER-385).
  - `Rizal Akbar {runId}-065`, email `rizalakbar+{runId}-065@qwertysystem.net`, Staff Principal, approver-eligible untuk 1 approval Admin Console (AC) (TC-GS-USER-386).
- Kemampuan teknis (disediakan tim FE/BE): seeding data Responsibilities FAMS (borrowed, assigned, pending approval, pending task) dan approval AC untuk Principal lewat API, serta Client tanpa subscription FAMS dan akun Total Control-nya (TC, PRD, dan Tabel Pre-setup tidak menyebut mekanismenya; nama endpoint ditentukan tim FE di tahap script); halaman Fixed Asset > Borrow untuk mengembalikan aset (TC-GS-USER-399).
- State global yang diubah: tidak ada. Hook `after` (tetap berjalan walau spec gagal di tengah) menghapus tiga user seed beserta data Responsibilities-nya dan mengembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-USER-384: Screening Tab Responsibilities entitas Client dengan FAMS aktif

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Ahmad Fauzi {runId}-065`, tekan Enter
3. Klik Name `Ahmad Fauzi {runId}-065` di User List
4. Verifikasi label tab `Responsibilities (4)`
5. Klik Tab `Responsibilities`
6. Verifikasi sub-tab `Borrowed Assets (1)` | `Assigned Assets (1)` | `Pending Approvals (1)` | `Pending Tasks (1)`
7. Verifikasi tanpa aksi tulis di Tab `Responsibilities`
8. Verifikasi tanpa deep-link di Tab `Responsibilities`

### TC-GS-USER-1019: Tab Responsibilities semua sub-tab kosong menampilkan empty state global

9. Klik menu User di sidebar Global Settings
10. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
11. Klik Name `Dewi Lestari` di User List
12. Klik Tab `Responsibilities`
13. Verifikasi ilustrasi empty state tampil
14. Verifikasi teks `"No pending responsibilities"`
15. Verifikasi teks `"This user has no active custody, pending approvals, or tasks."`
16. Verifikasi sub-tab switcher tidak tampil

### TC-GS-USER-399: Data Responsibilities read-only mencerminkan perubahan di modul sumber

17. Buka Fixed Asset > Borrow
18. Kembalikan aset yang dipinjam `Ahmad Fauzi {runId}-065`
19. Buka Global Settings > User > User List (sub-tab Login User)
20. Klik icon Search, ketik `Ahmad Fauzi {runId}-065`, tekan Enter
21. Klik Name `Ahmad Fauzi {runId}-065` di User List
22. Klik Tab `Responsibilities`
23. Klik sub-tab `Borrowed Assets`
24. Verifikasi sub-tab `Assigned Assets (1)` | `Pending Approvals (1)` | `Pending Tasks (1)` tampil
25. Verifikasi baris aset yang dikembalikan tidak lagi tampil di sub-tab `Borrowed Assets`
26. Verifikasi label tab `Responsibilities (3)`

### TC-GS-USER-385: Tab Responsibilities disembunyikan saat subscription FAMS Client tidak aktif

27. Logout, lalu login sebagai Total Control Client tanpa subscription FAMS
28. Buka Global Settings > User > User List (sub-tab Login User)
29. Klik icon Search, ketik `Dewi Lestari {runId}-065`, tekan Enter
30. Klik Name `Dewi Lestari {runId}-065` di User List
31. Verifikasi Tab `Role`, `Non-Login User`, `Changelog`, `System Log`, dan `User Log` tampil
32. Verifikasi Tab `Responsibilities` tidak dirender

### TC-GS-USER-386: Tab Responsibilities entitas Principal hanya Pending Approvals tanpa switcher

33. Logout, lalu login sebagai Total Control entitas Principal
34. Buka Global Settings > User > User List
35. Klik icon Search, ketik `Rizal Akbar {runId}-065`, tekan Enter
36. Klik Name `Rizal Akbar {runId}-065` di User List
37. Klik Tab `Responsibilities`
38. Verifikasi satu tabel Pending Approvals (Admin Console) tampil
39. Verifikasi switcher sub-tab tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (39 langkah) karena lima blok TC berada di satu kelas harness (fungsional) pada satu layar Tab Responsibilities. Tiap blok berdiri sendiri dan tetap bermakna walau blok sebelumnya gagal, karena ganti akun entitas ditulis eksplisit dan tiap blok memuat user dan langkah bukanya sendiri.
- Urutan TC sumber diubah: TC-GS-USER-399 (mengubah data seed Ahmad Fauzi) setelah TC-GS-USER-384 dan 1019 pada akun yang sama; TC-GS-USER-385 dan 386 menyusul dengan ganti akun eksplisit ke entitas masing-masing, dan tiap ganti akun hanya dilakukan sekali. TC-GS-USER-399 hanya mengubah user seed milik TC-GS-USER-399 dan 384, sehingga TC lain tidak terdampak.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 2, 9 sampai 10, 19 sampai 20, 28 sampai 29, dan 34 sampai 35 (membuka User List dan mencari user target), 27 dan 33 (ganti akun entitas), 17 sampai 18 (aksi TC di modul sumber).
- Anchor absence (bagian 8b butir 2): langkah 6 (label sub-tab tampil) mendahului langkah 7 dan 8; langkah 13 sampai 15 (empty state tampil) mendahului langkah 16; langkah 24 (sub-tab lain tampil) mendahului langkah 25; langkah 31 (tab lain tampil di Detail yang sama) mendahului langkah 32; langkah 38 mendahului langkah 39. Langkah 24 dan 31 tidak ada di TC dan ditambahkan hanya sebagai anchor.
- Langkah 4 (label tab `Responsibilities (4)`) diamati sebelum tab diklik karena label berada pada daftar tab di Detail.
- Temuan untuk QA:
  - TC-GS-USER-385 precondition c ("Client tanpa subscription FAMS") tidak menyebut Client, akun Total Control-nya, dan lokasi user `Dewi Lestari` di Client itu; Tabel Pre-setup No. 12 memuat Dewi Lestari di Client dengan FAMS (Access Fixed Asset). Spec memakai user seed bersuffix dan akun "disediakan tim FE".
  - TC-GS-USER-386 menyebut Staff Principal `Rizal Akbar` approver-eligible 1 approval AC tanpa mekanisme seeding dan tanpa baris di Tabel Pre-setup; spec memakai user seed bersuffix.
  - TC-GS-USER-399 langkah 1 tidak menyebut cara mengembalikan aset di Fixed Asset > Borrow (tombol, dialog); spec hanya menulis aksi pengembaliannya. Ahmad Fauzi di Tabel Pre-setup (No. 13) memiliki satu borrowed asset dan spec men-seed user milik spec dengan data yang sama.
  - TC-GS-USER-399 Expected tidak menyebut label sub-tab `Borrowed Assets` sesudah kosong (`Borrowed Assets (0)` atau tersembunyi); tidak diasersi.
  - TC-GS-USER-384 Expected c ("tanpa aksi tulis dan tanpa deep-link") tidak menyebut elemen yang diperiksa; spec mengasersi di tampilan Tab `Responsibilities` secara umum.
  - TC-GS-USER-1019 precondition c (Dewi Lestari tanpa borrowed, assigned, pending approval, pending task) tidak ada di Tabel Pre-setup No. 12.
