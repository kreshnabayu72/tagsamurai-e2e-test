---
id: TC-AUTH-SES-E2E-078-end-product-admin-console-dan-global-settings
title: "End Product Admin Console dan Global Settings lewat App Switcher Tanpa Seat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-329
  - TC-AUTH-SES-330
coverage:
  web: automated
---

# End Product Admin Console dan Global Settings lewat App Switcher Tanpa Seat

## Prerequisites

- Mode: FE+BE.
- Client Alpha `Alpha Logistik` (Tabel Data Uji Pre-setup #5): batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5. Tidak ada kuota yang diubah spec ini.
- Seeding (hook `before`, lewat API oleh akun aktor Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #4, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`): satu user Principal staff (Tabel Data Uji Pre-setup #20) dengan akses Admin Console (Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-329: `Ayu Firmansyah` (`ayufirmansyah+{runId}-078@qwertysystem.net`); sesi platform web Active di Browser A dan sesi-produk Admin Console Active (Browser A menampilkan halaman Admin Console saat TC dimulai), dibuat di `before` lewat login API dan pembukaan card Admin Console.
- TC-AUTH-SES-330 memakai akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`) sebagai subjek uji sesuai TC; Browser A untuk TC ini adalah konteks browser baru yang login dengan akun itu lalu membuka card Global Settings pada langkah penghubung.
- Akun aktor lain (login di hook `before`, satu konteks browser per akun):
  - Browser Principal: akun aktor Principal Admin Console di atas, membaca `Activity Log > Session` milik Admin Console (TC-AUTH-SES-329).
  - Browser Admin: akun aktor Total Control (Global Settings) di atas, membaca `Global Settings > User > Detail > User Log` milik `Ayu Firmansyah` (TC-AUTH-SES-329).
  - Browser License: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): akhiri sesi seed dan sesi-produk `Ayu Firmansyah`, akhiri sesi Browser A milik akun aktor Total Control yang dibuka di TC-AUTH-SES-330, tutup semua konteks browser, hapus user `Ayu Firmansyah`.
- Suite berjalan serial (`parallel: false`); state global yang dipakai: akun aktor Total Control (Global Settings) dipakai sebagai subjek uji di TC-AUTH-SES-330, sehingga tidak boleh ada spec lain yang memakai akun itu bersamaan.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: konteks browser bersamaan (Browser A, Browser Principal, Browser Admin, Browser License); pembacaan status sesi-produk milik user uji (Ended) dari sisi backend, disediakan tim FE/BE; pembacaan hitungan seat aktif di License > Concurrent User; reCAPTCHA mode uji di environment (login Browser A akun aktor Total Control pada TC-AUTH-SES-330).
- Akun yang dipakai: `Ayu Firmansyah` di Browser A (TC-AUTH-SES-329); akun aktor Total Control (Global Settings) di Browser A (TC-AUTH-SES-330) dan Browser Admin; akun aktor Principal Admin Console di Browser Principal; Admin License di Browser License.

## Test Steps

### TC-AUTH-SES-329: End Product Admin Console mengakhiri sesi-produk tanpa melepas seat dan dicatat Session ended

1. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan catat hitungan seat aktif
2. Di Browser A (sesi `Ayu Firmansyah`, di halaman Admin Console) klik App Switcher (ikon kembali ke Portal) di header Admin Console
3. Verifikasi Tidak ada dialog yang tampil di Browser A
4. Verifikasi Sesi-produk Admin Console `Ayu Firmansyah` berstatus Ended
5. Di Browser License muat ulang daftar License > Concurrent User
6. Verifikasi Tidak ada perubahan kuota atau seat: hitungan seat aktif sama dengan catatan langkah 1
7. Di Browser Principal buka `Activity Log > Session` milik Admin Console dan cari entri untuk `Ayu Firmansyah` yang dibuat sesudah langkah 2 dimulai
8. Verifikasi Entri `Session ended` (Activity `Session`) tampil di `Activity Log > Session` milik Admin Console [DEFERRED]
9. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Ayu Firmansyah` dan cari entri yang dibuat sesudah langkah 2 dimulai
10. Verifikasi Entri `Session ended` tampil di User Log sebagai `Session ended (Admin Console)`

### TC-AUTH-SES-330: End Product Global Settings mengakhiri sesi-produk tanpa melepas seat dan dicatat Session ended

11. Tutup konteks Browser A sebelumnya, buka konteks baru Browser A, lalu login di `Auth > Login with Password` dengan email `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD` → halaman Portal — Product Hub tampil
12. Di Browser A klik card Global Settings → Global Settings tampil (sesi-produk Global Settings Active)
13. Di Browser License muat ulang daftar License > Concurrent User dan catat hitungan seat aktif
14. Di Browser A klik App Switcher (ikon kembali ke Portal) di header Global Settings
15. Verifikasi Tidak ada dialog yang tampil di Browser A
16. Verifikasi Sesi-produk Global Settings akun `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (dibuka pada langkah 12) berstatus Ended
17. Di Browser License muat ulang daftar License > Concurrent User
18. Verifikasi Tidak ada perubahan kuota atau seat: hitungan seat aktif sama dengan catatan langkah 13
19. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` yang dibuat sesudah langkah 14 dimulai
20. Verifikasi Entri `Session ended` tampil di `Global Settings > Activity Log > Session`
21. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik akun `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan cari entri yang dibuat sesudah langkah 14 dimulai
22. Verifikasi Entri `Session ended` tampil di User Log sebagai `Session ended (Global Settings)`

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: dua TC End Product untuk produk exempt (tanpa `subscriptionId`) lewat App Switcher dengan harness yang sama (web, baca seat dan log); keluar eksplisit dari produk berlisensi (TC-AUTH-SES-132) ada di spec `TC-AUTH-SES-E2E-041-sesi-produk-keluar-eksplisit-dan-daftar-concurrent-user`.
- Urutan mengikuti TC sumber (329, 330); tidak ada penyimpangan (S-10).
- Expected c TC-AUTH-SES-329 untuk surface `Activity Log > Session` milik Admin Console adalah forward-dependency bertanda `[DEFERRED]` (NC-15, PRD §12 #3) seperti TC-AUTH-SES-318 di spec `TC-AUTH-SES-E2E-058`; asersi User Log tidak bertanda.
- Baseline log (S-12): asersi mencari entri yang dibuat sesudah aksi App Switcher dimulai (langkah 2 dan 14), berdasarkan Note dan email, bukan posisi teratas. Browser Admin dibuka sesudah langkah 14, sehingga pembukaan Global Settings oleh Browser Admin sendiri tidak memengaruhi entri `Session ended` yang dicari.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): mencatat dan memuat ulang hitungan seat aktif di Browser License (langkah 1, 5, 13, 17) sebagai pembanding "tidak ada perubahan seat" (S-14); membuka konteks baru Browser A, login akun aktor, dan membuka card Global Settings (langkah 11 dan 12); membuka halaman log.
- Temuan untuk QA: (1) TC-AUTH-SES-330 memakai akun aktor `totalControlGlobalSettings` (Pre-setup #1) sebagai subjek uji sekaligus akun yang membaca log; spec membuka akun itu di dua konteks browser (Browser A dan Browser Admin). TC dan PRD tidak menyebut apakah dua sesi web akun yang sama memicu Duplicate Login; bila memicu, Browser Admin harus login ulang sesudah langkah 18. (2) Expected b TC-AUTH-SES-329 dan 330 "tidak ada perubahan kuota atau seat" tidak menyebut permukaan baca; spec membandingkan hitungan seat aktif Fixed Asset di License > Concurrent User sebelum dan sesudah App Switcher (Supply Asset tidak dibaca karena akun Admin License hanya untuk Fixed Asset). (3) Expected a "sesi-produk berstatus Ended" tidak menyebut cara membaca; spec memakai pembacaan status dari backend yang disediakan tim FE/BE tanpa endpoint karangan (S-13). (4) TC-AUTH-SES-329 menulis "User Log `Ayu Firmansyah`" untuk user Principal staff tanpa lokasi; spec memakai `Global Settings > User > Detail > User Log` yang dibaca akun Total Control seperti TC-AUTH-SES-318.
