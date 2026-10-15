---
id: TC-AUTH-SES-E2E-076-product-session-sweep-and-time-travel
title: "Sesi-Produk: Tab Ditutup, Kedaluwarsa Sesi Platform, dan Sweep Dinonaktifkan (Time-Travel)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-130
  - TC-AUTH-SES-131
coverage:
  web: automated
---

# Sesi-Produk: Tab Ditutup, Kedaluwarsa Sesi Platform, dan Sweep Dinonaktifkan (Time-Travel)

## Prerequisites

- Mode: FE+BE.
- Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; batas idle 15 menit. Tidak ada kuota yang diubah spec ini.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) milik Client Q2 dengan App Access Fixed Asset dan Supply Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-131: `Putri Ramadhan` (`putriramadhan+{runId}-076@qwertysystem.net`); sesi platform web dan sesi-produk Fixed Asset Active di Browser A (seat terpakai 1), dibuat di `before` lewat login API dan pembukaan Fixed Asset.
  - TC-AUTH-SES-130: `Dimas Pratama` (`dimaspratama+{runId}-076@qwertysystem.net`; hanya akun, login dilakukan di langkah spec) serta user seat seed (Tabel Data Uji Pre-setup #7) `Gunawan Prakoso` (`gunawanprakoso+{runId}-076@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-076@qwertysystem.net`; hanya akun, sesi dibuat di langkah "Siapkan state").
  - Browser A pada TC-AUTH-SES-131 = konteks browser yang memuat sesi platform `Putri Ramadhan` (dibuat di `before`); Browser A pada TC-AUTH-SES-130 = konteks browser baru tanpa sesi untuk `Dimas Pratama`.
- Akun aktor lain (login di hook `before`, satu konteks browser):
  - Browser License: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #33, Global Role Manage Global License dengan scope Client Q2 dan Client Alpha), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat uji (dimajukan bersama pada TC-AUTH-SES-131 dan TC-AUTH-SES-130, dipulihkan ke waktu nyata di akhir tiap TC dan di hook `after`) serta sweep penandaan sesi kedaluwarsa (nonaktif pada TC-AUTH-SES-130, diaktifkan kembali di akhir TC dan di hook `after`).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): kembalikan jam server uji dan jam browser/perangkat uji ke waktu nyata, aktifkan kembali sweep penandaan sesi kedaluwarsa, akhiri semua sesi seed dan sesi-produk, tutup semua konteks browser, hapus keempat user.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan background job), disediakan tim FE/BE: jam server uji dan jam browser/perangkat uji dapat dimajukan bersama dengan presisi menit dan dipulihkan ke waktu nyata, serta sweep penandaan sesi kedaluwarsa dapat dinonaktifkan dan diaktifkan kembali (kendali sweep: Tabel Data Uji Pre-setup #18); API Open Product Session dan End Product Session (Auth - Session Management) oleh sesi platform user seed; pembacaan hitungan seat aktif dan baris sesi-produk di License > Concurrent User; reCAPTCHA mode uji di environment (halaman Login with Password).
- Penyimpangan konteks: memajukan jam server membuat semua sesi platform yang tidak aktif melewati batas idle (termasuk sesi Browser License), jadi setelah jam dimajukan Browser License login ulang lewat langkah eksplisit (langkah 7 dan 18).
- Akun yang dipakai: user uji pada Browser A; Browser License memakai akun aktor di atas.

## Test Steps

### TC-AUTH-SES-131: Menutup tab atau browser tidak memanggil End Product dan seat baru lepas saat sesi platform berakhir

1. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), muat ulang daftar, dan catat hitungan seat aktif serta baris `Putri Ramadhan`
2. Di Browser A (sesi `Putri Ramadhan`) tutup tab Fixed Asset (browser tetap terbuka)
3. Di Browser License muat ulang daftar License > Concurrent User
4. Verifikasi Sesi-produk Fixed Asset `Putri Ramadhan` tetap Active setelah tab ditutup
5. Verifikasi Seat tetap terpakai setelah tab ditutup (hitungan seat aktif tidak berubah)
6. Majukan jam server uji dan jam browser/perangkat uji bersama 16 menit sampai sesi platform `Putri Ramadhan` expired
7. Di Browser License buka `Auth > Login with Password`, ketik email `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_MGL_PASSWORD`, lalu klik [Log in] (sesi Browser License sebelumnya melewati batas idle)
8. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
9. Verifikasi Sesi-produk Fixed Asset `Putri Ramadhan` berakhir setelah sesi platform expired
10. Verifikasi Seat dilepas setelah sesi platform expired
11. Pulihkan jam server uji dan jam browser/perangkat uji ke waktu nyata

### TC-AUTH-SES-130: Sesi-produk yang semua sesi platform induknya sudah lewat batas idle tidak dihitung walau sweep belum menandai

12. Siapkan state Client Q2: sesi platform dan sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan `Melati Anggun` (seat aktif 2)
13. Nonaktifkan sweep penandaan sesi kedaluwarsa
14. Majukan jam server uji dan jam browser/perangkat uji bersama 16 menit sehingga sesi platform induk sesi-produk `Gunawan Prakoso` dan `Melati Anggun` melewati waktu kedaluwarsa tetapi belum ditandai sweep
15. Tutup konteks Browser A milik `Putri Ramadhan` dan hapus sesi login browser terkait, lalu di Browser A (konteks baru) buka `Auth > Login with Password`, ketik email `dimaspratama+{runId}-076@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, klik [Log in], lalu tunggu Portal — Product Hub terbuka
16. Di Browser A klik card Fixed Asset
17. Verifikasi Browser A masuk Fixed Asset tanpa popup karena kedua sesi-produk seed tidak dihitung
18. Di Browser License buka `Auth > Login with Password`, ketik email `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_MGL_PASSWORD`, lalu klik [Log in] (sesi Browser License sebelumnya melewati batas idle)
19. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
20. Verifikasi Seat aktif yang dihitung hanya milik `Dimas Pratama`
21. Pulihkan jam server uji dan jam browser/perangkat uji ke waktu nyata, lalu aktifkan kembali sweep penandaan sesi kedaluwarsa

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-SES-130 dan 131 (sweep dinonaktifkan sebagai background job dan time-travel sebagai objek uji, kelas d) ada di spec ini; TC-AUTH-SES-132 dan 270 ada di spec `TC-AUTH-SES-E2E-041-sesi-produk-keluar-eksplisit-dan-daftar-concurrent-user`.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-131, 130 (urutan TC sumber 130, 131). TC 131 ditaruh lebih dulu karena sesi seed-nya dibuat di hook `before` pada waktu nyata, sedangkan TC 130 memajukan jam dan membentuk sendiri sesi seed-nya pada langkah 12. Jam dipulihkan di langkah 11 sebelum TC 130 dimulai, sehingga TC 130 tidak mewarisi pergeseran jam dari TC 131. Seat Client Q2 (kuota 2) dijaga: pada TC 131 hanya `Putri Ramadhan` (1 seat) yang memegang seat, dan seat itu sudah dilepas sebelum TC 130 membuat dua seat seed.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "catat hitungan seat aktif" dan "muat ulang daftar" di Browser License (langkah 1 dan 3) membentuk keadaan yang dibandingkan asersi seat (S-14); langkah 7 dan 18 login ulang Browser License setelah jam dimajukan; langkah 11 dan 21 memulihkan jam (dan sweep) sebelum TC berikutnya atau akhir spec (S-09); langkah 12 "Siapkan state Client Q2" membentuk seat seed lewat API (S-04); langkah 15 menutup konteks Browser A TC sebelumnya dan menghapus sesi login browser terkait sebelum konteks baru dibuka (S-09).
- Spec ini tidak membuka Activity Log atau User Log; asersi seat memakai baseline hitungan seat aktif yang dicatat sebelum aksi (S-12), dan jam dipulihkan sebelum bagian berikutnya yang memakai jam bersama (bagian 6).
- Cara membaca daftar License > Concurrent User mengikuti `fixed-asset/license/PRD/license.md` §3.2.
- Temuan untuk QA: (1) TC-AUTH-SES-130 Langkah Uji tidak menyebut cara membuat sesi platform induk kedaluwarsa tanpa sweep; spec memajukan jam server uji dan jam browser/perangkat uji bersama 16 menit setelah seat seed dibuka. (2) TC-AUTH-SES-130 Expected b ("seat aktif yang dihitung hanya milik Dimas Pratama") dibaca di License > Concurrent User sebagai Admin License (Pre-setup #33); bila daftar menampilkan sesi-produk seed berstatus Active yang belum ditandai sweep, cara membedakannya dari sesi yang dihitung perlu dipastikan QA. (3) TC-AUTH-SES-131 Langkah 2 memajukan jam 16 menit tanpa menyebut sesi Browser License yang ikut kedaluwarsa; spec menambah langkah login ulang Browser License (langkah 7 dan 18). (4) TC-AUTH-SES-131 tidak menyebut cara menutup tab tanpa menutup browser; spec menutup tab Fixed Asset saja. (5) TC-AUTH-SES-130 dan 131 menyebut "periksa seat aktif" tanpa nilai awal; spec mencatat hitungan awal sebelum aksi.
