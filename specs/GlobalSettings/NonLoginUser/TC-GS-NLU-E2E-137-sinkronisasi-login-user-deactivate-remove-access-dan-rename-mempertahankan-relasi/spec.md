---
id: TC-GS-NLU-E2E-137-sinkronisasi-login-user-deactivate-remove-access-dan-rename-mempertahankan-relasi
title: "Sinkronisasi Login User: Deactivate, Remove Access, dan rename mempertahankan relasi Represented By"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-418
  - TC-GS-NLU-480
  - TC-GS-NLU-419
coverage:
  web: automated
---

# Sinkronisasi Login User: Deactivate, Remove Access, dan rename mempertahankan relasi Represented By

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Division `Operations`, Email `<nama>+{runId}-137@qwertysystem.net`):
  - TC-GS-NLU-418: Login User `Lukman Hakim {runId}-137` (First Name `Lukman`, Last Name `Hakim {runId}-137`, Active, Position `Manager`, Division `Finance`) dan Non-Login User `Nina Sari {runId}-137` dengan Represented By `Lukman Hakim {runId}-137`.
  - TC-GS-NLU-480: Login User `Hana Akses {runId}-137` (First Name `Hana`, Last Name `Akses {runId}-137`, Active, memiliki sedikitnya dua produk pada field Access) dan Non-Login User `Akses Sari {runId}-137` dengan Represented By `Hana Akses {runId}-137`.
  - TC-GS-NLU-419: Login User `Ahmad Fauzi {runId}-137` (First Name `Ahmad`, Last Name `Fauzi {runId}-137`, Active) dan Non-Login User `Budi Rename {runId}-137` dengan Represented By `Ahmad Fauzi {runId}-137`; hook `before` mengaitkan Represented By itu lewat API dari `Dewi Anggraini` sehingga Changelog memuat entri `Edit` Field `Represented By` dengan New Value `Ahmad Fauzi {runId}-137` sebelum rename.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-137` yang tersisa (Login User dan Non-Login User).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-418: Deactivate Login User yang menjadi Represented By mempertahankan relasi

1. Buka sub-tab Login User lewat Global Settings > User > User List, ketik Search `Hakim {runId}-137`, tekan Enter, klik switch Active baris `Lukman Hakim {runId}-137` (ON)
2. Klik `[Deactivate]` pada dialog konfirmasi
3. Tunggu aksi selesai (dialog Deactivate menutup)
4. Buka sub-tab Non-Login User, ketik Search `Nina Sari {runId}-137`, tekan Enter
5. Verifikasi sel Represented By baris `Nina Sari {runId}-137` tetap `Lukman H`

### TC-GS-NLU-480: Remove Access Login User yang menjadi Represented By mempertahankan relasi

6. Buka sub-tab Login User, ketik Search `Akses {runId}-137`, tekan Enter, klik `⋯` baris `Hana Akses {runId}-137` > `Edit`
7. Hapus centang satu produk pada field Access
8. Klik `[Save]`
9. Konfirmasi dialog Remove Access
10. Tunggu aksi selesai (dialog dan popup Edit menutup)
11. Buka sub-tab Non-Login User, ketik Search `Akses Sari {runId}-137`, tekan Enter
12. Verifikasi sel Represented By baris `Akses Sari {runId}-137` tetap `Hana A`

### TC-GS-NLU-419: Rename Login User yang menjadi Represented By tercermin di List dan Detail tanpa error

13. Buka sub-tab Login User, ketik Search `Fauzi {runId}-137`, tekan Enter, klik `⋯` baris `Ahmad Fauzi {runId}-137` > `Edit`
14. Ubah First Name `Ahmad` menjadi `Ahmadi`, lalu klik `[Save]`
15. Tunggu aksi selesai (popup Edit menutup)
16. Buka sub-tab Non-Login User, ketik Search `Budi Rename {runId}-137`, tekan Enter
17. Verifikasi sel Represented By baris `Budi Rename {runId}-137` menampilkan `Ahmadi F`
18. Hover sel Represented By baris `Budi Rename {runId}-137`
19. Verifikasi tooltip `Ahmadi Fauzi {runId}-137` tampil
20. Klik Name baris `Budi Rename {runId}-137` untuk membuka Detail
21. Verifikasi Represented By pada Detail menampilkan `Ahmadi F`
22. Hover Represented By pada Detail
23. Verifikasi tooltip `Ahmadi Fauzi {runId}-137` tampil
24. Klik tab `Changelog`
25. Verifikasi entri lama `Edit` Field `Represented By` tetap menampilkan New Value `Ahmad Fauzi {runId}-137`, nama sebelum rename

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 4, 6, 11, 13, 16 (membuka sub-tab dan Search record yang dicari), serta langkah 3, 10, 15 (Tunggu aksi selesai).
- Nama Login User milik spec memakai suffix pada Last Name (`Hakim {runId}-137`, `Akses {runId}-137`, `Fauzi {runId}-137`) sehingga tampilan singkat `[First Name] [Last Initial]` (`Lukman H`, `Hana A`, `Ahmadi F`) sama dengan nilai di TC.
- Temuan untuk QA:
  - TC-GS-NLU-480 langkah 1 menulis "konfirmasi dialog Remove Access bila muncul" (bersyarat) dan tidak menyebut label tombol dialog; spec menulis konfirmasi dialog Remove Access sebagai langkah pasti sesuai nama aksi (S-08) tanpa label tombol; QA perlu memastikan dialog itu selalu muncul pada pengurangan produk dan label tombolnya.
  - TC-GS-NLU-419 Expected b ("entri log lama tetap menampilkan nama sebelum rename") tidak menyebut entri mana yang memuat nama Login User; spec memakai entri `Edit` Field `Represented By` yang dihasilkan hook `before`, dan mekanisme itu disediakan tim FE/BE.
  - TC-GS-NLU-419 menyebut record Budi Kurniawan (Pre-setup) sebagai pemakai Represented By Ahmad Fauzi; spec memakai Login User dan Non-Login User milik spec supaya rename tidak mengubah data bersama (S-06).
  - TC-GS-NLU-418 dan 480 tidak menyebut langkah kembali ke Non-Login User; spec membukanya lewat sub-tab.
