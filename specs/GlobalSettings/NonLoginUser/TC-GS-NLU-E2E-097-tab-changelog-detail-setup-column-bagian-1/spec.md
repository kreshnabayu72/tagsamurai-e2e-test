---
id: TC-GS-NLU-E2E-097-tab-changelog-detail-setup-column-bagian-1
title: "Tab Changelog Detail: Setup Column Bagian 1"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-343
  - TC-GS-NLU-344
  - TC-GS-NLU-345
  - TC-GS-NLU-346
coverage:
  web: automated
---

# Tab Changelog Detail: Setup Column Bagian 1

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Halaman awal spec: Detail Non-Login User `Budi Kurniawan` (Pre-setup No. 11, hanya dibaca), dibuka oleh langkah 1 dan 2 dari daftar sub-tab Non-Login User.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13; Non-Login User `Budi Kurniawan` (No. 11).
- Spec tidak membuat atau mengubah data Non-Login User; satu-satunya state yang berubah adalah preferensi kolom tabel di browser.
- Pemulihan Setup Column: konfigurasi kolom yang disimpan spec ini dipulihkan hook `after` dengan menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; spec terdaftar di bagian Hook suite `suite.md`).
- Tiap `[Save]` Setup Column adalah aksi sisi klien tanpa toast; langkah berikutnya tidak menunggu respons server.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan state yang diubah spec ini (preferensi kolom di browser).
- Urutan kolom default Tab Changelog Detail: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Kemampuan teknis: drag and drop baris kolom, scroll horizontal tabel, hover tooltip checkbox, menekan `Esc`, muat ulang halaman, dan menghapus preferensi kolom di browser (disediakan tim FE).

## Test Steps

### TC-GS-NLU-343: Screening overlay Column Visibility Tab Changelog Detail

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Changelog`
4. Klik ikon `⋯` pada header kolom Actions
5. Verifikasi overlay memuat kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
6. Verifikasi setiap kolom pada overlay punya checkbox ☑ checked dan enabled
7. Verifikasi setiap kolom pada overlay punya drag handle
8. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-NLU-344: Screening popup Setup Column Tab Changelog Detail

9. Klik item `Setup Column...` pada overlay
10. Verifikasi header popup: Title `Setup Column`, deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.", dan tombol `✕`
11. Verifikasi body popup memuat daftar kolom dengan status centang default
12. Verifikasi setiap kolom pada popup punya drag handle
13. Verifikasi setiap kolom pada popup punya ikon Pin
14. Verifikasi body popup memuat Live Preview tabel
15. Verifikasi footer popup memuat `[Reset to Default]` dan `[Save]`
16. Verifikasi footer popup tanpa `[Cancel]`

### TC-GS-NLU-345: Hapus centang kolom Hideable pada Setup Column Tab Changelog Detail lalu Save persisten setelah refresh

17. Hapus centang dua kolom pertama (`Date` dan `Action`)
18. Verifikasi Live Preview mengikuti perubahan sebelum Save
19. Klik `[Save]`
20. Verifikasi kolom `Date` dan `Action` hilang dari tabel
21. Muat ulang halaman
22. Klik tab `Changelog`
23. Verifikasi kolom `Date` dan `Action` tetap hilang dari tabel (pengaturan tetap setelah refresh)
24. Hapus preferensi kolom di browser (kemampuan disediakan tim FE), lalu muat ulang halaman
25. Klik tab `Changelog`

### TC-GS-NLU-346: Drag reorder kolom pada Setup Column Tab Changelog Detail

26. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
27. Drag kolom terakhir (`Modified By`) ke posisi pertama
28. Verifikasi Live Preview mengikuti urutan baru
29. Klik `[Save]`
30. Verifikasi tabel mengikuti urutan baru dengan kolom `Modified By` di posisi pertama
31. Muat ulang halaman
32. Klik tab `Changelog`
33. Verifikasi urutan baru tetap setelah refresh (kolom `Modified By` di posisi pertama)

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (TC-GS-NLU-343, TC-GS-NLU-344, TC-GS-NLU-345, TC-GS-NLU-346) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (Search `Budi Kurniawan` dan membuka Detail, langkah penghubung menuju layar awal spec; Search di daftar mengikuti bagian 8b butir 9); langkah 3 (membuka Tab Changelog Detail); langkah 24 dan 25 (menghapus preferensi kolom yang disimpan TC-GS-NLU-345 sebelum TC-GS-NLU-346 mengandalkan urutan default, lalu membuka kembali Tab Changelog Detail).
- Asersi tambahan (konkretisasi Expected): daftar kolom pada TC-GS-NLU-343 dan TC-GS-NLU-344 ditulis dari kolom default Tab Changelog Detail pada Prerequisites; "dua kolom pertama" pada TC-GS-NLU-345 ditulis `Date` dan `Action`; "kolom terakhir" pada TC-GS-NLU-346 ditulis `Modified By`. Langkah muat ulang diikuti membuka kembali Tab Changelog Detail supaya pengaturan tersimpan teramati.
- Pembagian TC lintas spec: Setup Column Tab Changelog Detail dibagi dua spec; TC separuh lainnya ada di spec 098.
- Hook `after` suite memulihkan konfigurasi kolom (menghapus preferensi kolom di browser), sehingga spec berikutnya mulai dari urutan default.
- Temuan untuk QA:
  - TC-GS-NLU-345: "dua kolom pertama selain kolom terakhir" ambigu (apakah "selain kolom terakhir" membatasi kolom yang boleh dihapus centang atau memaksudkan kolom visible terakhir); spec menghapus centang dua kolom pertama pada urutan Setup Column.
  - TC-GS-NLU-346: TC tidak menyebut apakah kolom hasil drag harus tampil di posisi pertama pada Live Preview dan tabel sekaligus; spec mengasersi keduanya sebagai dua klausa dan urutan setelah muat ulang.
  - TC tidak menyebut cara memulihkan konfigurasi kolom yang disimpan; spec memakai kemampuan "disediakan tim FE" untuk menghapus preferensi kolom di browser (S-13).
