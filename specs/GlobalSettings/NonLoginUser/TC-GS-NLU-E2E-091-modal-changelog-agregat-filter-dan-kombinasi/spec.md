---
id: TC-GS-NLU-E2E-091-modal-changelog-agregat-filter-dan-kombinasi
title: "Modal Changelog Agregat: Filter dan Kombinasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-316
  - TC-GS-NLU-317
  - TC-GS-NLU-318
  - TC-GS-NLU-319
coverage:
  web: automated
---

# Modal Changelog Agregat: Filter dan Kombinasi

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor Total Control, kemampuan disediakan tim FE/BE; dihapus di hook `after`), semua dibuat dan diubah oleh `Siti N` pada hari yang sama:
  - `Budi Kurniawan {runId}-091` (Division Operations): entri Create (Field `Name`), lalu Edit Division `Operations` ke `Logistics` (entri Edit, Field `Division`).
  - `Hapus Uji {runId}-091`: dibuat lalu di-Delete (entri Create dan entri Delete, Field `Name`).
  - `Tanpa Riwayat {runId}-091`: Non-Login User yang di-seed tanpa menulis entri Changelog (kemampuan seeding tanpa audit trail disediakan tim FE/BE; lihat Temuan untuk QA).
- Tanggal hari seeding dicatat di hook `before` dan dipakai langkah 19 sebagai rentang Date satu hari.
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Kemampuan teknis: memilih beberapa opsi pada dropdown Filter, memilih rentang Date, membaca opsi dropdown.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-316: Screening Filter Panel Modal Changelog agregat

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
2. Klik icon Filter
3. Verifikasi field Filter Panel: `Date` (date range, `"Select date"`), `Action` (`"All actions"`), `User Name` (`"All users"`), `Field` (`"All fields"`), `Modified By` (`"All users"`)
4. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-NLU-317: Filter Action, User Name, Field, dan Modified By pada Modal Changelog agregat

5. Verifikasi tabel sebelum Filter memuat sedikitnya satu baris (pembanding generik)
6. Pilih Action `Create` dan `Delete`, klik `[Apply]`
7. Verifikasi baris Create `Budi Kurniawan {runId}-091` dan baris Delete `Hapus Uji {runId}-091` tampil
8. Verifikasi setiap baris yang tampil ber-Action `Create` atau `Delete` (OR dalam field)
9. Pilih User Name `Budi Kurniawan {runId}-091`, klik `[Apply]`
10. Verifikasi setiap baris yang tampil ber-User Name `Budi Kurniawan {runId}-091`
11. Pilih Field `Name`, klik `[Apply]`
12. Verifikasi setiap baris yang tampil ber-Field `Name` (baris Create atau Delete)
13. Pilih Modified By `Siti N`, klik `[Apply]`
14. Verifikasi setiap baris yang tampil berasal dari aksi `Siti N`
15. Buka dropdown User Name pada Filter Panel
16. Verifikasi opsi dropdown User Name memuat `Budi Kurniawan {runId}-091` (nilai yang ada di log)
17. Verifikasi opsi dropdown User Name tidak memuat `Tanpa Riwayat {runId}-091` (entitas tanpa entri)

### TC-GS-NLU-318: Filter Date rentang inklusif pada Modal Changelog agregat

18. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
19. Pilih rentang Date satu hari, yaitu tanggal hari seeding riwayat, klik `[Apply]`
20. Verifikasi baris Create `Budi Kurniawan {runId}-091` tampil
21. Verifikasi setiap baris yang tampil bertanggal pada hari yang dipilih

### TC-GS-NLU-319: Kombinasi Search dan Filter pada Modal Changelog agregat beririsan

22. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
23. Ketik Search `Budi`, tekan Enter
24. Pilih Action `Edit` pada Filter Panel, klik `[Apply]`
25. Verifikasi baris Edit `Budi Kurniawan {runId}-091` tampil
26. Verifikasi setiap baris yang tampil ber-Action `Edit` dan memuat `Budi` (irisan Search dan Filter)
27. Kosongkan isi kotak search, tekan Enter
28. Verifikasi setiap baris yang tampil tetap ber-Action `Edit` (Filter tetap aktif)
29. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (316, 317, 318, 319) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (membuka Modal Changelog dan Filter Panel); langkah 15 (membuka dropdown User Name untuk memeriksa opsi); langkah 18, 22, dan 29 (mengosongkan Filter sebelum TC berikutnya dan di akhir spec, S-09); langkah 23 dan 27 dijalankan oleh TC-GS-NLU-319 sendiri.
- Asersi tambahan (konkretisasi Expected): hasil Filter ditulis sebagai asersi universal ("setiap baris ...") yang didahului pembanding positif (baris seeding spec tampil) agar hasil kosong tidak meloloskan asersi (bagian 8b butir 2); "opsi dropdown hanya nilai yang ada di log; entitas tanpa entri tidak muncul" (TC-GS-NLU-317 e) ditulis memakai `Tanpa Riwayat {runId}-091` sebagai entitas tanpa entri.
- Pembagian TC lintas spec: Search ada di spec 090; Sort, Pagination, Download ada di spec 092 dan 135; Setup Column ada di spec 093 dan 094.
- Temuan untuk QA:
  - TC-GS-NLU-317: TC tidak menyebut entitas mana yang tanpa entri Changelog dan cara menyediakannya pada audit trail permanen; spec memakai record yang di-seed tanpa menulis log (mekanisme disediakan tim FE/BE, R-19).
  - TC-GS-NLU-317 dan 319: TC tidak menyatakan apakah Filter Panel tetap terbuka sesudah `[Apply]` dan apakah Filter berikutnya bersifat kumulatif; spec mengikuti urutan TC (Filter ditambahkan kumulatif dan dikosongkan dengan `[Clear Field]` di antara TC) tanpa membuka ulang Filter Panel.
  - TC-GS-NLU-318: TC tidak menyebut rentang tanggal konkret; spec memakai hari seeding riwayat. TC-GS-NLU-319: TC tidak menyatakan cara "Kosongkan Search" yang dipakai; spec memakai mengosongkan isi kotak search lalu Enter agar Filter tidak ikut ter-reset.
