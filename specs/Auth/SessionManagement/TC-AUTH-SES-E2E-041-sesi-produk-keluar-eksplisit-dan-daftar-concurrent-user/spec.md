---
id: TC-AUTH-SES-E2E-041-sesi-produk-keluar-eksplisit-dan-daftar-concurrent-user
title: "Sesi-Produk: Keluar Eksplisit, Daftar License Concurrent User, dan Pelepasan Seat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-132
  - TC-AUTH-SES-270
coverage:
  web: automated
---

# Sesi-Produk: Keluar Eksplisit, Daftar License Concurrent User, dan Pelepasan Seat

## Prerequisites

- Mode: FE+BE.
- Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; batas idle 15 menit. Tidak ada kuota yang diubah spec ini.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) milik Client Q2 dengan App Access Fixed Asset dan Supply Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-132: `Eko Wulandari` (`ekowulandari+{runId}-041@qwertysystem.net`); sesi platform web dan sesi-produk Fixed Asset Active di Browser A (seat terpakai 1), dibuat di `before` lewat login API dan pembukaan Fixed Asset; Browser A menampilkan halaman Fixed Asset saat TC dimulai.
  - TC-AUTH-SES-270: `Andi Setiawan` (`andisetiawan+{runId}-041@qwertysystem.net`); sesi platform web Active di Browser A di Portal — Product Hub, belum ada sesi-produk.
  - Browser A tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuat di `before` dari sesi hasil seeding API).
- Akun aktor lain (login di hook `before`, satu konteks browser per akun):
  - Browser License: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License di Client Q2), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
  - Browser Admin: akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) di atas (`Spectra.env.GS_TC_PASSWORD`), membaca `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log`.
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): akhiri semua sesi seed dan sesi-produk, tutup semua konteks browser, hapus kedua user.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: API Open Product Session dan End Product Session (Auth - Session Management) oleh sesi platform user seed; pembacaan hitungan seat aktif dan baris sesi-produk di License > Concurrent User; pembacaan status sesi-produk (Ended) milik user uji dari sisi backend, disediakan tim FE/BE (langkah 6).
- Akun yang dipakai: user uji pada Browser A; Browser License dan Browser Admin memakai akun aktor di atas.

## Test Steps

### TC-AUTH-SES-132: Keluar produk secara eksplisit mengakhiri sesi-produk dan melepas seat

1. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan catat hitungan seat aktif serta baris `Eko Wulandari`
2. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan catat jumlah entri dengan Note `Session ended` untuk `ekowulandari+{runId}-041@qwertysystem.net` sebagai baseline
3. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Eko Wulandari` dan catat jumlah entri `Session ended (Fixed Asset)` sebagai baseline
4. Di Browser A (sesi `Eko Wulandari`, di halaman Fixed Asset) klik App Switcher (ikon kembali ke Portal) di header Fixed Asset
5. Di Browser License muat ulang daftar License > Concurrent User
6. Verifikasi Sesi-produk Fixed Asset `Eko Wulandari` berstatus Ended
7. Verifikasi Seat dilepas
8. Verifikasi Baris `Eko Wulandari` hilang dari daftar
9. Verifikasi Hitungan seat aktif berkurang 1
10. Di Browser Admin muat ulang `Activity Log > Session` milik Fixed Asset
11. Verifikasi Jumlah entri `Session ended` untuk `Eko Wulandari` (dicari berdasarkan Note dan email) bertambah 1 dari baseline di `Activity Log > Session` milik Fixed Asset [DEFERRED]
12. Di Browser Admin muat ulang `Global Settings > User > Detail > User Log` milik `Eko Wulandari`
13. Verifikasi User Log `Eko Wulandari` menampilkan entri baru `Session ended (Fixed Asset)` (jumlah bertambah 1 dari baseline) [DEFERRED]

### TC-AUTH-SES-270: Daftar License > Concurrent User memuat sesi-produk Active dan berubah saat sesi berakhir

14. Di Browser License muat ulang daftar License > Concurrent User dan catat hitungan seat aktif (baris `Andi Setiawan` belum ada)
15. Di Browser A (sesi `Andi Setiawan`, di Portal — Product Hub) klik card Fixed Asset
16. Di Browser License muat ulang daftar License > Concurrent User
17. Verifikasi Baris `Andi Setiawan` muncul di daftar
18. Verifikasi Hitungan seat aktif bertambah 1
19. Di Browser A keluar lewat App Switcher ke Portal
20. Di Browser License muat ulang daftar License > Concurrent User
21. Verifikasi Baris `Andi Setiawan` hilang dari daftar
22. Verifikasi Hitungan seat aktif berkurang 1

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-SES-132 dan 270 ada di spec ini; TC-AUTH-SES-130 dan 131 (time-travel dan sweep dinonaktifkan, kelas d) ada di spec `TC-AUTH-SES-E2E-076-product-session-sweep-and-time-travel`.
- Seat Client Q2 (kuota 2) dijaga: pada TC-AUTH-SES-270 hanya `Andi Setiawan` yang memegang seat setelah `Eko Wulandari` keluar pada TC-AUTH-SES-132.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "catat hitungan seat aktif" dan "muat ulang daftar" di Browser License (langkah 1, 5, 14, 16, 20) membentuk keadaan yang dibandingkan asersi seat (S-14). Langkah 2, 3, 10 dan 12 mencatat baseline jumlah entri log dan memuat ulang surface log (S-12).
- Expected b TC-AUTH-SES-132 dibaca di `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` (akun Total Control Global Settings scope Client Q2, Browser Admin); surface produk `Activity Log > Session` Fixed Asset adalah forward-dependency bertanda `[DEFERRED]` (NC-15).
- Cara membaca daftar License > Concurrent User mengikuti `fixed-asset/license/PRD/license.md` §3.2 dan tidak di-assert ulang (butir c TC-AUTH-SES-270).
- Temuan untuk QA: TC-AUTH-SES-132 dan 270 menyebut "periksa seat aktif" tanpa nilai awal; spec mencatat hitungan awal sebelum aksi.
- Temuan untuk QA: TC-AUTH-SES-132 butir a ("Sesi-produk berstatus Ended") tidak memberi cara membaca status itu karena baris Ended tidak tampil di daftar License; spec memakai pembacaan status dari backend yang disediakan tim FE/BE tanpa endpoint karangan.
- Temuan untuk QA: TC-AUTH-SES-132 langkah 3 tidak menyebut akun yang membuka `Activity Log > Session` milik Fixed Asset; spec memakai akun Total Control Global Settings scope Client Q2 (Pre-setup #26).
