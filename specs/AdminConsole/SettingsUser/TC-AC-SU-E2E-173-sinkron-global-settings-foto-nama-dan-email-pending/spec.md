---
id: TC-AC-SU-E2E-173-sinkron-global-settings-foto-nama-dan-email-pending
title: "Sinkron dari Global Settings ke Detail User untuk Foto, Nama, Email Pending, dan Pembatalan Email Pending tanpa Entri Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-595
  - TC-AC-SU-596
  - TC-AC-SU-597
coverage:
  web: automated
---

# Sinkron dari Global Settings ke Detail User untuk Foto, Nama, Email Pending, dan Pembatalan Email Pending tanpa Entri Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-173A` | `miketan+{runId}-173a@qwertysystem.net` | Activated, tanpa foto (TC-595); setelah blok diganti nama `Michael Tan {runId}-173A` |
| U2 | `Mike Tan {runId}-173B` | `miketan+{runId}-173b@qwertysystem.net` | Activated (TC-596); email pending baru `michaeltan+{runId}-173b@qwertysystem.net` |
| U3 | `Mike Tan {runId}-173C` | `miketan+{runId}-173c@qwertysystem.net` | Pending Email Confirmation dengan email pending `michaeltan+{runId}-173c@qwertysystem.net` (TC-597) |

- Kemampuan teknis: Fixture BE (seeding user, email pending); berkas foto JPG berukuran maksimal 1 MB (`Fixture.settingsUser.photoJpg`, disediakan tim FE). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-595: Foto dan nama tercermin read-only
1. Buka Global Settings > User, unggah foto JPG untuk U1 dan ubah namanya menjadi `Michael Tan {runId}-173A`
2. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Michael Tan {runId}-173A`, tekan Enter
3. Verifikasi Name baris U1 pada User List bernilai `Michael Tan {runId}-173A`
4. Klik Name baris U1 untuk membuka Detail, lalu hover avatar
5. Verifikasi avatar menampilkan foto baru
6. Verifikasi tidak ada overlay edit atau delete pada avatar saat hover
7. Verifikasi Name di header Detail bernilai `Michael Tan {runId}-173A`
8. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `{runId}-173A` pada Popup Changelog: User, tekan Enter
9. Verifikasi Popup Changelog: User menampilkan empty state `No results found` untuk U1 (tidak ada entri untuk perubahan foto atau nama)
### TC-AC-SU-596: Email pending dari Global Settings
10. Tutup popup, buka Global Settings > User, lalu ubah email U2 (`Mike Tan {runId}-173B`) ke `michaeltan+{runId}-173b@qwertysystem.net`
11. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-173B`, tekan Enter
12. Verifikasi badge `Pending Email Confirmation` tampil di samping nama baris U2 pada User List
13. Klik Name baris U2 untuk membuka Detail
14. Verifikasi field Email menampilkan `Pending email change to michaeltan+{runId}-173b@qwertysystem.net`
15. Verifikasi teks pada field Email berwarna on-surface
16. Verifikasi tidak ada tombol aksi pada field Email
17. Verifikasi badge `Pending Email Confirmation` tampil di header Detail
18. Verifikasi header Detail menampilkan button Resend Confirmation Email
### TC-AC-SU-597: Pembatalan email pending dari Global Settings
19. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-173C` pada Popup Changelog: User, tekan Enter, dan catat jumlah baris U3 sebagai N0
20. Tutup popup, buka Global Settings > User, lalu klik Cancel pending email change untuk U3 (`Mike Tan {runId}-173C`)
21. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-173C`, tekan Enter
22. Klik Name baris U3 untuk membuka Detail
23. Verifikasi Name di header Detail U3 bernilai `Mike Tan {runId}-173C`
24. Verifikasi teks `Pending email change to ...` tidak tampil
25. Verifikasi badge `Pending Email Confirmation` tidak tampil
26. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-173C` pada Popup Changelog: User, tekan Enter
27. Verifikasi jumlah baris U3 pada Popup Changelog: User sama dengan N0 (tidak ada entri baru)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pembukaan Global Settings > User dan aksinya, navigasi sidebar, Search nama target dan pembukaan Detail (langkah 2 dan langkah serupa, R-16), Search nama user di Popup Changelog: User, pencatatan N0 (langkah 19), dan menutup popup.
- Absence di Popup Changelog: User pada TC-595 memakai empty state hasil Search sebagai anchor positif (bagian 8b butir 2); TC-597 memakai baseline N0 dan asersi jumlah. Absence teks atau badge pada Detail TC-597 didahului Verifikasi Name di header Detail U3 tampil (anchor permukaan).
- Temuan untuk QA:
  - TC-595 butir c ("Tidak ada entri Changelog: User untuk perubahan foto/nama") dan TC-597 butir c tidak menyebut cara mengecek; spec mengecek lewat Search di Popup Changelog: User (keberadaan Search tidak ditegaskan TC).
  - TC-595 menyebut foto "JPG ≤1MB" tanpa berkas; berkas disediakan tim FE. Nama baru TC-595 `Michael Tan` diganti bersuffix.
  - TC-597 langkah 1 berbunyi "Konfirmasi atau Cancel email" pada judul tetapi hanya Cancel yang diberi langkah; spec hanya menjalankan Cancel.
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
