---
id: TC-GS-NLU-E2E-098-tab-changelog-detail-setup-column-bagian-2
title: "Tab Changelog Detail: Setup Column Bagian 2"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-347
  - TC-GS-NLU-348
  - TC-GS-NLU-349
  - TC-GS-NLU-350
coverage:
  web: automated
---

# Tab Changelog Detail: Setup Column Bagian 2

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
- Tabel `Cara menutup Setup Column` (dipakai langkah 20 sampai 25):

  | Cara menutup |
  |---|
  | Tombol `✕` pada popup Setup Column |
  | Tombol keyboard `Esc` |
- Kemampuan teknis: drag and drop baris kolom, scroll horizontal tabel, hover tooltip checkbox, menekan `Esc`, muat ulang halaman, dan menghapus preferensi kolom di browser (disediakan tim FE).

## Test Steps

### TC-GS-NLU-347: Pin dan Unpin kolom pada Setup Column Tab Changelog Detail

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Changelog`
4. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
5. Pin kolom pertama (`Date`), klik `[Save]`
6. Scroll tabel secara horizontal
7. Verifikasi kolom `Date` membeku saat scroll horizontal
8. Buka Setup Column, Unpin kolom pertama (`Date`), klik `[Save]`
9. Scroll tabel secara horizontal
10. Verifikasi kolom `Date` kembali ikut bergeser

### TC-GS-NLU-348: Reset to Default pada Setup Column Tab Changelog Detail

11. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
12. Ubah visibilitas dan urutan kolom: hapus centang kolom pertama (`Date`) dan drag kolom terakhir (`Modified By`) ke posisi pertama
13. Klik `[Reset to Default]`
14. Verifikasi Live Preview kembali ke default modul
15. Klik `[Save]`
16. Verifikasi tabel mengikuti default
17. Muat ulang halaman
18. Klik tab `Changelog`
19. Verifikasi tabel tetap mengikuti default setelah refresh

### TC-GS-NLU-349: Menutup Setup Column Tab Changelog Detail tanpa Save membuang perubahan

20. Untuk setiap baris tabel `Cara menutup Setup Column` di `## Prerequisites` (langkah 20 sampai 25)
21. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
22. Hapus centang kolom pertama (`Date`)
23. Tutup popup Setup Column dengan cara pada baris tabel (tombol `✕` atau tombol keyboard `Esc`)
24. Verifikasi popup Setup Column tertutup
25. Verifikasi kolom `Date` kembali tampil seperti konfigurasi tersimpan

### TC-GS-NLU-350: Kolom visible terakhir pada Setup Column Tab Changelog Detail tidak dapat dihapus centang

26. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
27. Hapus centang semua kolom kecuali satu (`Modified By`)
28. Arahkan kursor ke checkbox kolom tersisa
29. Verifikasi checkbox kolom tersisa disabled
30. Verifikasi tooltip checkbox `"At least one column must remain visible."`
31. Tutup popup Setup Column dengan tombol `✕` tanpa menyimpan

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (TC-GS-NLU-347, TC-GS-NLU-348, TC-GS-NLU-349, TC-GS-NLU-350) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (Search `Budi Kurniawan` dan membuka Detail, langkah penghubung menuju layar awal spec; Search di daftar mengikuti bagian 8b butir 9); langkah 3 (membuka Tab Changelog Detail); tiap langkah pembuka Setup Column dan langkah terakhir di blok kolom visible terakhir (menutup popup dengan `✕` tanpa menyimpan, agar tidak ada form dirty tersisa).
- Asersi tambahan (konkretisasi Expected): kolom yang di-Pin pada TC-GS-NLU-347 adalah `Date`; perubahan pada TC-GS-NLU-348 adalah menghapus centang `Date` dan drag `Modified By` ke posisi pertama; langkah 20 sampai 25 diulang untuk `✕` dan `Esc` (parameter di tabel Prerequisites, langkah yang diulang dituliskan sekali). Langkah muat ulang diikuti membuka kembali Tab Changelog Detail.
- Pembagian TC lintas spec: Setup Column Tab Changelog Detail dibagi dua spec; TC separuh lainnya ada di spec 097.
- Hook `after` suite memulihkan konfigurasi kolom (menghapus preferensi kolom di browser), sehingga spec berikutnya mulai dari urutan default.
- Spec melewati sekitar 35 langkah (31 langkah nominal, 37 dengan ekspansi blok `✕` dan `Esc`). Alasan: keempat TC satu kelas harness (fungsional), satu layar, satu dataset, dan masing-masing berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memisahkannya mengulang login, pembukaan layar, dan pembentukan state yang sama.
- Temuan untuk QA:
  - TC-GS-NLU-347: TC tidak menyatakan bahwa tabel cukup lebar untuk scroll horizontal; kebutuhan itu (lebar viewport atau jumlah kolom) disediakan tim FE.
  - TC-GS-NLU-348: TC tidak menyebut perubahan konkret sebelum `[Reset to Default]`; spec memilih menghapus centang kolom pertama dan memindahkan kolom terakhir.
  - TC-GS-NLU-349: TC menulis "(ulangi dengan `Esc`)" tanpa menyatakan apakah `Esc` menutup hanya popup Setup Column atau juga Tab Changelog Detail; spec mengasersi popup Setup Column tertutup dan kolom kembali seperti konfigurasi tersimpan.
  - TC tidak menyebut cara memulihkan konfigurasi kolom yang disimpan; spec memakai kemampuan "disediakan tim FE" untuk menghapus preferensi kolom di browser (S-13).
