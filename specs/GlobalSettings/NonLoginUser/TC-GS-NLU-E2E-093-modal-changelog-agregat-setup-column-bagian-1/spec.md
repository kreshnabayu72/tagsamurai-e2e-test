---
id: TC-GS-NLU-E2E-093-modal-changelog-agregat-setup-column-bagian-1
title: "Modal Changelog Agregat: Setup Column Bagian 1"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-323
  - TC-GS-NLU-324
  - TC-GS-NLU-325
  - TC-GS-NLU-326
coverage:
  web: automated
---

# Modal Changelog Agregat: Setup Column Bagian 1

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13; Non-Login User `Budi Kurniawan` (No. 11).
- Spec tidak membuat atau mengubah data Non-Login User; satu-satunya state yang berubah adalah preferensi kolom tabel di browser.
- Pemulihan Setup Column: konfigurasi kolom yang disimpan spec ini dipulihkan hook `after` dengan menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; spec terdaftar di bagian Hook suite `suite.md`).
- Tiap `[Save]` Setup Column adalah aksi sisi klien tanpa toast; langkah berikutnya tidak menunggu respons server.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan state yang diubah spec ini (preferensi kolom di browser).
- Urutan kolom default Modal Changelog agregat: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Kemampuan teknis: drag and drop baris kolom, scroll horizontal tabel, hover tooltip checkbox, menekan `Esc`, muat ulang halaman, dan menghapus preferensi kolom di browser (disediakan tim FE).

## Test Steps

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka

### TC-GS-NLU-323: Screening overlay Column Visibility Modal Changelog agregat

2. Klik ikon `⋯` pada header kolom Actions
3. Verifikasi overlay memuat kolom `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi setiap kolom pada overlay punya checkbox ☑ checked dan enabled
5. Verifikasi setiap kolom pada overlay punya drag handle
6. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-NLU-324: Screening popup Setup Column Modal Changelog agregat

7. Klik item `Setup Column...` pada overlay
8. Verifikasi header popup: Title `Setup Column`, deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.", dan tombol `✕`
9. Verifikasi body popup memuat daftar kolom dengan status centang default
10. Verifikasi setiap kolom pada popup punya drag handle
11. Verifikasi setiap kolom pada popup punya ikon Pin
12. Verifikasi body popup memuat Live Preview tabel
13. Verifikasi footer popup memuat `[Reset to Default]` dan `[Save]`
14. Verifikasi footer popup tanpa `[Cancel]`

### TC-GS-NLU-325: Hapus centang kolom Hideable pada Setup Column Modal Changelog agregat lalu Save persisten setelah refresh

15. Hapus centang dua kolom pertama (`Date` dan `Action`)
16. Verifikasi Live Preview mengikuti perubahan sebelum Save
17. Klik `[Save]`
18. Verifikasi kolom `Date` dan `Action` hilang dari tabel
19. Muat ulang halaman
20. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
21. Verifikasi kolom `Date` dan `Action` tetap hilang dari tabel (pengaturan tetap setelah refresh)
22. Hapus preferensi kolom di browser (kemampuan disediakan tim FE), lalu muat ulang halaman
23. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka

### TC-GS-NLU-326: Drag reorder kolom pada Setup Column Modal Changelog agregat

24. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
25. Drag kolom terakhir (`Modified By`) ke posisi pertama
26. Verifikasi Live Preview mengikuti urutan baru
27. Klik `[Save]`
28. Verifikasi tabel mengikuti urutan baru dengan kolom `Modified By` di posisi pertama
29. Muat ulang halaman
30. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
31. Verifikasi urutan baru tetap setelah refresh (kolom `Modified By` di posisi pertama)

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (TC-GS-NLU-323, TC-GS-NLU-324, TC-GS-NLU-325, TC-GS-NLU-326) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog agregat); langkah 22 dan 23 (menghapus preferensi kolom yang disimpan TC-GS-NLU-325 sebelum TC-GS-NLU-326 mengandalkan urutan default, lalu membuka kembali Modal Changelog agregat).
- Asersi tambahan (konkretisasi Expected): daftar kolom pada TC-GS-NLU-323 dan TC-GS-NLU-324 ditulis dari kolom default Modal Changelog agregat pada Prerequisites; "dua kolom pertama" pada TC-GS-NLU-325 ditulis `Date` dan `Action`; "kolom terakhir" pada TC-GS-NLU-326 ditulis `Modified By`. Langkah muat ulang diikuti membuka kembali Modal Changelog agregat supaya pengaturan tersimpan teramati.
- Pembagian TC lintas spec: Setup Column Modal Changelog agregat dibagi dua spec; TC separuh lainnya ada di spec 094.
- Hook `after` suite memulihkan konfigurasi kolom (menghapus preferensi kolom di browser), sehingga spec berikutnya mulai dari urutan default.
- Temuan untuk QA:
  - TC-GS-NLU-325: "dua kolom pertama selain kolom terakhir" ambigu (apakah "selain kolom terakhir" membatasi kolom yang boleh dihapus centang atau memaksudkan kolom visible terakhir); spec menghapus centang dua kolom pertama pada urutan Setup Column.
  - TC-GS-NLU-326: TC tidak menyebut apakah kolom hasil drag harus tampil di posisi pertama pada Live Preview dan tabel sekaligus; spec mengasersi keduanya sebagai dua klausa dan urutan setelah muat ulang.
  - TC tidak menyebut cara memulihkan konfigurasi kolom yang disimpan; spec memakai kemampuan "disediakan tim FE" untuk menghapus preferensi kolom di browser (S-13).
