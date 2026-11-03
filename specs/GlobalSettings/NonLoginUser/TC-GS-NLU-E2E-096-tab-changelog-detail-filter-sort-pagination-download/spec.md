---
id: TC-GS-NLU-E2E-096-tab-changelog-detail-filter-sort-pagination-download
title: "Tab Changelog Detail: Filter, Sort, Pagination, dan Download"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-338
  - TC-GS-NLU-339
  - TC-GS-NLU-351
  - TC-GS-NLU-352
coverage:
  web: automated
---

# Tab Changelog Detail: Filter, Sort, Pagination, dan Download

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor Total Control, kemampuan disediakan tim FE/BE; dihapus di hook `after`): `Budi Kurniawan {runId}-096` (Division Operations) dengan riwayat 12 entri oleh `Siti N` pada hari yang sama: Create (Field `Name`) dan 11 kali Edit Division bergantian `Logistics` dan `Operations` (Field `Division`). Tanggal hari seeding dicatat di hook `before`. Riwayat lebih dari 10 entri dipakai TC-GS-NLU-352.
- Non-Login User Pre-setup `Budi Kurniawan` (No. 11) dipakai hanya dibaca oleh TC-GS-NLU-351 (nama berkas bergantung pada nama record Pre-setup).
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Kemampuan teknis: memilih rentang Date pada Filter Panel, membaca opsi dropdown Filter, menerima unduhan berkas XLSX dan membaca nama berkasnya.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-338: Screening Filter Panel Tab Changelog Detail

1. Ketik Search `Budi Kurniawan {runId}-096`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan {runId}-096`
3. Klik tab `Changelog`
4. Klik icon Filter
5. Verifikasi field Filter Panel: `Date` (`"Select date"`), `Action` (`"All actions"`), `Field` (`"All fields"`), `Modified By` (`"All users"`)
6. Verifikasi Filter Panel tidak memuat field Name

### TC-GS-NLU-339: Filter Date, Action, Field, dan Modified By pada Tab Changelog Detail

7. Verifikasi opsi dropdown Action hanya `Create` dan `Edit` (nilai yang ada di log)
8. Pilih Action `Edit`, klik `[Apply]`
9. Verifikasi baris Edit tampil di Tab Changelog (pembanding generik)
10. Verifikasi setiap baris yang tampil ber-Action `Edit`
11. Verifikasi opsi dropdown Field hanya `Name` dan `Division` (nilai yang ada di log)
12. Pilih Field `Division`, klik `[Apply]`
13. Verifikasi setiap baris yang tampil ber-Field `Division`
14. Verifikasi opsi dropdown Modified By hanya `Siti N` (nilai yang ada di log)
15. Pilih Modified By `Siti N`, klik `[Apply]`
16. Verifikasi setiap baris yang tampil berasal dari aksi `Siti N`
17. Pilih rentang Date satu hari, yaitu tanggal hari seeding riwayat, klik `[Apply]`
18. Verifikasi setiap baris yang tampil bertanggal pada hari yang dipilih
19. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`

### TC-GS-NLU-352: Pagination Tab Changelog Detail

20. Verifikasi footer tab: default 10 baris per halaman
21. Klik halaman 2
22. Verifikasi halaman 2 menampilkan entri berikutnya (sedikitnya satu baris yang berbeda dari baris halaman 1)

### TC-GS-NLU-351: Download Tab Changelog Detail

23. Kembali ke daftar Non-Login User (Global Settings > User > User List > sub-tab Non-Login User)
24. Ketik Search `Budi Kurniawan`, tekan Enter
25. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
26. Klik tab `Changelog`
27. Klik Download > `Download as XLSX`
28. Verifikasi tidak ada toast sukses
29. Verifikasi berkas `Changelog-Non-Login-User-Budi-Kurniawan.xlsx` terunduh

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber diubah: TC-GS-NLU-352 (Pagination) ditaruh sebelum TC-GS-NLU-351 (Download) karena TC-GS-NLU-351 memakai Detail record Pre-setup `Budi Kurniawan` dan menutup spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Budi Kurniawan {runId}-096`, membuka Detail, dan tab `Changelog`; R-16); langkah 4 (membuka Filter Panel); langkah 19 (mengosongkan Filter sebelum TC-GS-NLU-352, S-09); langkah 23, 24, 25, 26 (kembali ke daftar dan membuka Detail record Pre-setup).
- Asersi tambahan (konkretisasi Expected): "opsi dropdown hanya nilai yang ada di log Budi Kurniawan" (TC-GS-NLU-339) ditulis sebagai daftar opsi dari riwayat seeding; hasil Filter ditulis sebagai asersi universal yang didahului pembanding (baris Edit tampil).
- Pembagian TC lintas spec: TC-GS-NLU-340, 341, 342 (Sort) ada di spec 136; Screening, Search ada di spec 095; Setup Column ada di spec 097 dan 098.
- Temuan untuk QA:
  - TC-GS-NLU-351: Expected "berkas .xlsx berisi entri Budi Kurniawan" adalah isi berkas (kelas f); spec mengasersi nama berkas dan tidak adanya toast sukses, isi sel tidak diasersi. Belum ada spec kelas f untuk isi berkas Changelog Detail.
  - TC-GS-NLU-339: TC tidak menyatakan apakah Filter Panel tetap terbuka dan Filter berikutnya bersifat kumulatif; spec mengikuti urutan TC tanpa membuka ulang Filter Panel dan menyusun data seeding supaya kombinasi kumulatif tetap menghasilkan baris. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
