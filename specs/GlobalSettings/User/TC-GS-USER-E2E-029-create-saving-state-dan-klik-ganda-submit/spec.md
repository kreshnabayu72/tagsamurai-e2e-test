---
id: TC-GS-USER-E2E-029-create-saving-state-dan-klik-ganda-submit
title: "Create: saving state tombol [Submit] dan klik ganda"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-144
  - TC-GS-USER-145
coverage:
  web: automated
---

# Create: saving state tombol [Submit] dan klik ganda

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk TC-GS-USER-144).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Layar awal: hook `beforeEach` mengembalikan layar ke Global Settings > User > User List, sub-tab Login User.
- Data Pre-setup (hanya dibaca): Division `Finance` (No. 23); opsi Access `Fixed Asset` (No. 26).
- Data Dinamis (dibuat oleh TC lewat UI; tidak ada seeding), semua bersuffix `{runId}-029`, Division `Finance`, Access `Fixed Asset`:
  - Emergency Phone (No. 24) diisi pada kedua Create mengikuti TC: Country Code `🇮🇩 +62`, Number `81234567890`.
  - U-144: First Name `Budi`, Last Name `Santoso 144 {runId}-029`, Email `budisantoso144+{runId}-029@qwertysystem.net`.
  - U-145: First Name `Budi`, Last Name `Santoso 145 {runId}-029`, Email `budisantoso145+{runId}-029@qwertysystem.net`.
- Kebutuhan intercept (`Spectra.intercept()`) untuk TC-GS-USER-144: respons Create user ditahan (tidak dijawab) sampai dilepas lewat langkah eksplisit. Nama endpoint ditentukan tim FE di tahap script. Intercept dilepas segera setelah state saving diamati; hook `after` melepas intercept walau spec gagal di tengah.
- Kemampuan teknis: hover elemen; membaca state tombol (loading, disabled); menghitung request Create user dan toast "Success, user has been created." yang muncul selama double-click (disediakan tim FE).
- Cleanup di hook `after` (tidak berasumsi alur berhasil penuh): hapus lewat API user bersuffix `{runId}-029`.
- State global yang diubah: Custom Field `Emergency Phone` tidak Required selama spec ini (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158 dan 349, TC Create dan Edit lain dijalankan saat Required nonaktif). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah. Spec membuat data dalam suite serial; form Create dibuka dua kali.

## Test Steps

### TC-GS-USER-144: Tombol [Submit] masuk saving state saat request berjalan

1. Klik `[+ User]` di Table Tools
2. Isi First Name `Budi`, Last Name `Santoso 144 {runId}-029`, Division `Finance`, Email `budisantoso144+{runId}-029@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
3. Pasang intercept: tahan respons Create user
4. Hover `[Submit]`
5. Verifikasi tombol `[Submit]` menampilkan state hover
6. Klik `[Submit]`
7. Verifikasi tombol `[Submit]` dalam state loading
8. Verifikasi tombol `[Submit]` disabled
9. Lepas intercept dan teruskan respons Create user
10. Tunggu aksi selesai

### TC-GS-USER-145: Klik [Submit] ganda cepat hanya membuat satu user

11. Klik `[+ User]` di Table Tools
12. Isi First Name `Budi`, Last Name `Santoso 145 {runId}-029`, Division `Finance`, Email `budisantoso145+{runId}-029@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
13. Tunggu toast lama hilang otomatis (toast sukses Create TC-GS-USER-144)
14. Mulai hitung request Create user dan toast sukses
15. Double-click `[Submit]` dengan cepat
16. Verifikasi hanya 1 request Create user terkirim
17. Verifikasi hanya 1 toast sukses: "Success, user has been created."
18. Klik icon Search, ketik `Budi Santoso 145 {runId}-029`, tekan Enter
19. Verifikasi hanya 1 baris `Budi Santoso 145 {runId}-029` di User List

## Notes

- Mode: FE+BE. Intercept hanya menahan respons untuk mengamati state saving sehingga bukan kelas b; seluruh state data tetap dari backend nyata.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan (144, lalu 145). Pembukaan form dilakukan dua kali (langkah 1 dan 11) karena Submit sukses pada kedua TC menutup Popup.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 3 dan 9 (pasang dan lepas intercept), 10 (menunggu Create selesai sebelum membuka form berikutnya; hasil Submit TC-GS-USER-144 tidak diasersi karena Expected hanya mengatur state saving), 13 (menunggu toast sukses TC-GS-USER-144 hilang sebelum toast TC-GS-USER-145 dihitung, R-12), 14 (memulai penghitungan request dan toast untuk TC-GS-USER-145).
- State sementara (hover, loading, disabled) diasersi pada langkah 5, 7, dan 8 sebelum intercept dilepas (8b butir 5, 8).
- Pembagian TC: TC-GS-USER-146 dan TC-GS-USER-147 (Create gagal 5xx dan timeout) diverifikasi di spec 066; spec ini tidak memaksa kegagalan.
- Temuan untuk QA:
  - TC-GS-USER-144 precondition c "Response Create ditahan (network throttle)" tidak menyebut cara menahan respons ataupun durasi; spec menahan respons lewat intercept sampai dilepas lewat langkah 9. Nama endpoint ditentukan tim FE.
  - TC-GS-USER-144 Expected a "state hover tombol" tidak menyebut perubahan visual yang diharapkan; spec mengasersi tombol dalam state hover sebagaimana dibaca runner.
  - TC-GS-USER-144 Expected b "loading dan disabled sampai response diterima" tidak punya observasi sesudah response diterima (Popup menutup); spec tidak mengasersi akhir state saving (8b butir 8).
  - TC-GS-USER-144 dan 145 mengisi Emergency Phone (Pre-setup No. 24; Required nonaktif untuk TC ini) dengan Country Code `🇮🇩 +62` dan Number `81234567890`; spec mengikuti TC.
  - TC-GS-USER-145 tidak menyebut cara menghitung request dan toast; kemampuan disediakan tim FE.
