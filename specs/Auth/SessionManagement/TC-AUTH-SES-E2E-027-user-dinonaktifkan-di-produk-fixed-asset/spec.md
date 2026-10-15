---
id: TC-AUTH-SES-E2E-027-user-dinonaktifkan-di-produk-fixed-asset
title: "User Dinonaktifkan di Produk Fixed Asset: Pemutusan Sesi-Produk"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-326
  - TC-AUTH-SES-327
coverage:
  web: automated
---

# User Dinonaktifkan di Produk Fixed Asset: Pemutusan Sesi-Produk

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: subscription Fixed Asset dan Supply Asset Active, kuota 5), Activated, Active ON di Global Settings dan di produk Fixed Asset, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`:
  - TC-AUTH-SES-326 dan TC-AUTH-SES-327: `Lestari Maulana` (`lestarimaulana+{runId}-027@qwertysystem.net`)
- Sesi uji (hook `before`, lewat login API pada konteks Browser A, Chrome on Windows): sesi web Active di Browser A; sesi-produk Fixed Asset Active (seat terpakai) dan sesi-produk Supply Asset Active milik `Lestari Maulana`.
- Akun lain yang dipakai di langkah: `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, `Spectra.env.FA_MGL_PASSWORD`) di Browser License (konteks browser baru, langkah ganti akun eksplisit) untuk membaca `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) pada TC-AUTH-SES-327. Browser Admin = akun Total Control (Global Settings), sudah login dari hook `before`.
- Hook `after`: aktifkan kembali `Lestari Maulana` di produk Fixed Asset bila masih nonaktif, akhiri semua sesi seed, logout Browser License, kembalikan sesi Browser Admin ke akun default suite, hapus user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: beberapa konteks browser bersamaan (Browser A, Browser Admin, Browser License); pembacaan status sesi platform dan sesi-produk (Active, Ended), hitungan seat, dan daftar sesi aktif dari BE; pengaturan status user per produk (Fixed Asset) terpisah dari status Global Settings di `Global Settings > User > Detail`; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- State global yang diubah: status `Lestari Maulana` di produk Fixed Asset (nonaktif lalu aktif kembali). Pemulihan di hook `after`.

## Test Steps

### TC-AUTH-SES-326: User dinonaktifkan di produk Fixed Asset saat punya sesi-produk Fixed Asset memutus sesi-produk tanpa dialog dan sesi platform tetap aktif

1. Di Browser Admin catat baseline: jumlah entri Note `Session ended` dengan email `lestarimaulana+{runId}-027@qwertysystem.net` di Activity Log Session Fixed Asset dan di `Global Settings > User > Detail > User Log` milik `Lestari Maulana`
2. Di Browser Admin buka `Global Settings > User`, cari `Lestari Maulana`, buka Detail dan nonaktifkan status di produk Fixed Asset saja (status Global Settings tetap Active)
3. Verifikasi Sesi-produk Fixed Asset `Lestari Maulana` berstatus Ended
4. Verifikasi Seat sesi-produk Fixed Asset `Lestari Maulana` dilepas
5. Di Browser A amati halaman Portal — Product Hub
6. Verifikasi Sesi platform tetap Active
7. Verifikasi Tidak ada dialog apa pun
8. Di Browser A buka card Supply Asset
9. Verifikasi Sesi-produk Supply Asset tetap Active
10. Verifikasi Card Supply Asset dapat dibuka
11. Di Browser Admin buka Activity Log Session Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Lestari Maulana`, cari entri berdasarkan Note `Session ended` dan email `lestarimaulana+{runId}-027@qwertysystem.net`
12. Verifikasi Jumlah entri Note `Session ended` di Session Fixed Asset bertambah 1 terhadap baseline
13. Verifikasi Jumlah entri Note `Session ended` di User Log `Lestari Maulana` bertambah 1 terhadap baseline

### TC-AUTH-SES-327: Mengaktifkan kembali user di produk Fixed Asset tidak menghidupkan sesi-produk yang sudah berakhir

14. Di Browser Admin buka `Global Settings > User`, cari `Lestari Maulana`, buka Detail dan aktifkan kembali status di produk Fixed Asset
15. Di Browser Admin buka Activity Log Session Fixed Asset
16. Buka Browser License (konteks browser baru), login dengan `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_MGL_PASSWORD` → Portal — Product Hub tampil
17. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi
18. Verifikasi Sesi-produk Fixed Asset `Lestari Maulana` yang Ended tetap Ended
19. Verifikasi Sesi-produk itu tidak muncul di daftar sesi aktif
20. Di Browser A amati layar
21. Verifikasi Tidak ada dialog di Browser A

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan mengikuti TC sumber (326 lalu 327); tidak ada penyimpangan (S-05, S-10). TC-AUTH-SES-327 berdependensi pada TC-AUTH-SES-326 (sesi-produk Fixed Asset sudah Ended akibat penonaktifan); langkah 2 disalin secara utuh sebagai bagian TC-AUTH-SES-326 dalam spec yang sama sehingga TC-AUTH-SES-327 berjalan di atas keadaan itu tanpa menumpang spec lain (S-04, S-06).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah mencatat baseline entri log (1), langkah mengamati Browser A (5, 20), langkah membuka Activity Log Session Fixed Asset (15) dan ganti akun ke Browser License (16). Asersi "entri baru" memakai selisih jumlah entri terhadap baseline dan entri dicari berdasarkan Note dan email (S-12).
- Expected butir b TC-AUTH-SES-327 bagian "tidak ada entri log baru akibat pengaktifan kembali" adalah asersi absence dan tidak diasersikan di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin` (S-05). Bagian "tidak ada dialog" diasersikan pada langkah 21.
- Temuan untuk QA: (1) TC-AUTH-SES-326 dan 327 menyebut "Activity Log Session Fixed Asset" tanpa akun yang membacanya; spec memakai akun Total Control (Global Settings). (2) TC-AUTH-SES-327 langkah 2 menyebut `PLATFORM SETTINGS > License > Concurrent User` tanpa menyebut akun; spec memakai akun `manageGlobalLicenseFixedAsset` seperti TC-AUTH-SES-72. (4) TC-AUTH-SES-326 a dan TC-AUTH-SES-327 a tidak menyebut permukaan pembacaan status sesi-produk, seat, dan daftar sesi aktif; spec memakai kemampuan BE yang disediakan tim FE/BE. (3) TC-AUTH-SES-326 tidak menyebut cara membuat sesi-produk Fixed Asset dan Supply Asset yang Active; spec mengandalkan seeding sesi di hook `before` tanpa endpoint.
