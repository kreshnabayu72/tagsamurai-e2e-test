---
id: TC-AUTH-SES-E2E-029-invalidasi-semua-sesi-saat-akun-dihapus-atau-dinonaktifkan
title: "Invalidasi Semua Sesi Web, Mobile, dan Sesi-produk saat Akun Dinonaktifkan atau Dihapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-93
  - TC-AUTH-SES-316
coverage:
  web: automated
  mobile: automated
---

# Invalidasi Semua Sesi Web, Mobile, dan Sesi-produk saat Akun Dinonaktifkan atau Dihapus

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-93: `Dewi Permata` (`dewipermata+{runId}-029@qwertysystem.net`)
  - TC-AUTH-SES-316: `Citra Puspita` (`citrapuspita+{runId}-029@qwertysystem.net`)
- Sesi web dan sesi-produk per TC dibuat lewat API oleh akun aktor, dan sesi mobile lewat login nyata, pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena perangkat Android uji A (Tabel Data Uji Pre-setup #10) dipakai bergantian oleh kedua user: sesi web Active di Browser A (Chrome on Windows) melalui login API pada konteks Browser A; sesi mobile Active di perangkat Android uji A lewat login nyata di aplikasi mobile dengan email dan password user, lalu ketuk [Not now] pada Prompt Enable Biometric (Tabel Data Uji Pre-setup #28; aplikasi menampilkan Portal — Product Hub); sesi-produk Fixed Asset Active milik user (seat terpakai).
- Konteks browser (hook `before`): Browser Admin login oleh akun aktor Total Control (Global Settings); Browser License login oleh akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Global Role Manage Global License, Tabel Data Uji Pre-setup #2, kredensial `Spectra.env.FA_MGL_PASSWORD`).
- Hook `after`: akhiri semua sesi dan sesi-produk seed (web, mobile), bersihkan data aplikasi mobile di perangkat Android uji A, tutup Browser A, Browser Admin, dan Browser License, lalu hapus kedua user (user TC-AUTH-SES-316 sudah terhapus oleh spec, pembersihan melewatinya). Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: Toggle Active dan keberadaan user milik spec ini, serta seat Fixed Asset Client `Alpha Logistik` (dilepas oleh spec), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-konteks): dua konteks browser aktor ditambah Browser A, satu perangkat Android uji A dengan aplikasi mobile terpasang dan dapat diamati oleh driver otomasi (login nyata, ketuk [Not now] pada Prompt Enable Biometric, bersihkan data aplikasi); push dialog lifecycle akun lewat SSE ke Browser A dan aplikasi mobile; pembacaan status sesi platform (Active, Force Logged Out), status sesi-produk (Active, Ended), dan hitungan seat dari BE oleh akun aktor; penyiapan sesi web Active dan sesi-produk Fixed Asset Active (seat terpakai) lewat API oleh akun aktor, disediakan tim FE/BE tanpa endpoint (langkah 1 dan 22).
- Akun yang dipakai: user uji masing-masing TC pada Browser A dan perangkat Android uji A; akun aktor Total Control (Global Settings) pada Browser Admin; akun aktor Manage Global License pada Browser License.

## Test Steps

### TC-AUTH-SES-93: Deactivate meng-invalidate semua sesi aktif user di web dan mobile beserta sesi-produknya

1. Siapkan lewat API: sesi web Active milik `Dewi Permata` di Browser A dan sesi-produk Fixed Asset Active milik `Dewi Permata` (seat terpakai)
2. Buka aplikasi mobile di perangkat Android uji A, login sebagai `dewipermata+{runId}-029@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
3. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
4. Catat hitungan seat aktif Fixed Asset Client `Alpha Logistik` dan pastikan baris `Dewi Permata` (`dewipermata+{runId}-029@qwertysystem.net`) tampil pada daftar
5. Di Browser Admin buka `Global Settings > Activity Log > Session` dan catat baseline: jumlah entri Note `Session ended` dengan email `dewipermata+{runId}-029@qwertysystem.net`
6. Di Browser Admin buka `Global Settings > User` dan cari `Dewi Permata` (`dewipermata+{runId}-029@qwertysystem.net`)
7. Matikan Toggle Active untuk `dewipermata+{runId}-029@qwertysystem.net` → Toggle Active OFF
8. Amati Browser A dan perangkat Android uji A tanpa interaksi → Dialog muncul di kedua perangkat
9. Verifikasi Browser A menampilkan Dialog "Account Deactivated"
10. Verifikasi Perangkat Android uji A menampilkan Dialog "Account Deactivated"
11. Verifikasi Sesi web `Dewi Permata` berstatus Force Logged Out
12. Verifikasi Sesi mobile `Dewi Permata` berstatus Force Logged Out
13. Verifikasi Sesi-produk Fixed Asset `Dewi Permata` berstatus Ended
14. Verifikasi Seat Fixed Asset `Dewi Permata` dilepas
15. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri berdasarkan Note `Session ended` dan email `dewipermata+{runId}-029@qwertysystem.net` → halaman log tampil
16. Verifikasi Jumlah entri `Session ended` untuk `Dewi Permata` di `Global Settings > Activity Log > Session` bertambah 1 terhadap baseline
17. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
18. Verifikasi Baris `Dewi Permata` hilang dari daftar sesi aktif
19. Verifikasi Hitungan seat aktif berkurang 1 dari hitungan yang dicatat pada langkah 4

### TC-AUTH-SES-316: Delete akun meng-invalidate sesi web dan mobile beserta sesi-produknya

20. Tutup konteks Browser A milik `Dewi Permata` dan buka konteks Browser A baru untuk `Citra Puspita`
21. Bersihkan data aplikasi mobile di perangkat Android uji A (akun sebelumnya) lalu tutup aplikasi
22. Siapkan lewat API: sesi web Active milik `Citra Puspita` di Browser A dan sesi-produk Fixed Asset Active milik `Citra Puspita` (seat terpakai)
23. Buka aplikasi mobile di perangkat Android uji A, login sebagai `citrapuspita+{runId}-029@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
24. Di Browser Admin buka `Global Settings > User` dan cari `Citra Puspita` (`citrapuspita+{runId}-029@qwertysystem.net`)
25. Hapus user tersebut sampai konfirmasi selesai → user terhapus
26. Amati Browser A dan perangkat Android uji A tanpa interaksi selama 10 detik → Dialog muncul di kedua perangkat
27. Verifikasi Browser A menampilkan Dialog "Account no longer Active"
28. Verifikasi Perangkat Android uji A menampilkan Dialog "Account no longer Active"
29. Verifikasi Sesi web `Citra Puspita` berstatus Force Logged Out
30. Verifikasi Sesi mobile `Citra Puspita` berstatus Force Logged Out
31. Verifikasi Sesi-produk Fixed Asset `Citra Puspita` berstatus Ended
32. Verifikasi Seat Fixed Asset `Citra Puspita` dilepas

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness c (multi-konteks: web, mobile, dan dua akun aktor).
- Urutan mengikuti TC sumber dan prinsip 3: Deactivate (TC-AUTH-SES-93) dahulu, Delete (TC-AUTH-SES-316) di akhir. Tiap TC memakai user sendiri sehingga tidak saling bergantung.
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-316 berdependensi pada TC-AUTH-SES-88; langkah 24 dan 25 menyalin langkah Delete oleh admin pada TC tersebut, dan langkah 26 melanjutkan pengamatan sesi.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan sesi lewat API di awal tiap TC (perangkat Android uji A dipakai bergantian, sehingga sesi mobile tidak disiapkan di `before`); mencatat hitungan seat; membuka halaman log; memuat ulang daftar Concurrent User.
- Pencatatan `Session ended` pada TC-AUTH-SES-93 (butir c) dibaca di `Global Settings > Activity Log > Session` sesuai TC, dengan baseline jumlah entri sebelum Toggle Active dimatikan (langkah 5) dan pencarian entri berdasarkan Note dan email (S-12). Asersi pencatatan `Account deactivated` dan `Account deleted` diuji di spec pencatatan modul ini (S-05).
- Langkah penghubung tambahan (S-03): penutupan konteks Browser A milik `Dewi Permata` dan pembukaan konteks baru untuk `Citra Puspita` (langkah 20), serta pembersihan data aplikasi mobile sebelum login `Citra Puspita` (langkah 21). Sesi mobile dibuat lewat login nyata dengan [Not now] pada Prompt Enable Biometric (Tabel Data Uji Pre-setup #28).
- Temuan untuk QA: (1) TC-AUTH-SES-93 dan 316 tidak menyebut permukaan tempat status sesi, status sesi-produk, dan seat dibaca selain License > Concurrent User (hanya daftar dan hitungan seat); spec membaca status sesi dari BE oleh akun aktor. (2) TC-AUTH-SES-93 menulis "hitungan seat aktif berkurang 1" tanpa menyebut langkah pencatatan hitungan awal; spec menambah langkah penghubung 3. (3) Akun #2 `manageGlobalLicenseFixedAsset` pada Tabel Data Uji Pre-setup tidak menyebut Client cakupannya; TC-AUTH-SES-93 memakainya untuk user Client `Alpha Logistik`, sedangkan TC lain memakainya di Client Q2. Spec mengasumsikan akun itu dapat membaca Concurrent User Fixed Asset kedua Client. (4) TC-AUTH-SES-316 tidak menyebut bentuk "dilepas" untuk seat selain status Ended; spec mengasersi seat dilepas lewat pembacaan BE. (5) TC-AUTH-SES-93 dan 316 (precondition b dan d) tidak menyebut cara membuat sesi web Active dan sesi-produk Fixed Asset Active; spec menyiapkannya lewat API oleh akun aktor (langkah 1 dan 22) sebagai langkah penghubung, kemampuan tersebut disediakan tim FE/BE tanpa mengarang endpoint.
