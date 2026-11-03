---
id: TC-GS-NLU-E2E-107-assigned-assets-setup-column-bagian-2
title: "Assigned Assets: Setup Column Bagian 2"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-387
  - TC-GS-NLU-388
  - TC-GS-NLU-389
  - TC-GS-NLU-390
coverage:
  web: automated
---

# Assigned Assets: Setup Column Bagian 2

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Halaman awal spec: Detail Non-Login User `Budi Kurniawan` (Pre-setup No. 11, hanya dibaca), dibuka oleh langkah 1 dan 2 dari daftar sub-tab Non-Login User.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13; Non-Login User `Budi Kurniawan` (No. 11). Data FAMS Budi Kurniawan (No. 14) dibaca lewat rute modul aset FAMS (LLD §4).
- Spec tidak membuat atau mengubah data Non-Login User; satu-satunya state yang berubah adalah preferensi kolom tabel di browser.
- Pemulihan Setup Column: konfigurasi kolom yang disimpan spec ini dipulihkan hook `after` dengan menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; spec terdaftar di bagian Hook suite `suite.md`).
- Tiap `[Save]` Setup Column adalah aksi sisi klien tanpa toast; langkah berikutnya tidak menunggu respons server.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan state yang diubah spec ini (preferensi kolom di browser).
- Urutan kolom default Assigned Assets: `Photo`, `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `PIC`.
- Tabel `Cara menutup Setup Column` (dipakai langkah 20 sampai 25):

  | Cara menutup |
  |---|
  | Tombol `✕` pada popup Setup Column |
  | Tombol keyboard `Esc` |
- Kemampuan teknis: drag and drop baris kolom, scroll horizontal tabel, hover tooltip checkbox, menekan `Esc`, muat ulang halaman, dan menghapus preferensi kolom di browser (disediakan tim FE).

## Test Steps

### TC-GS-NLU-387: Pin dan Unpin kolom pada Setup Column Assigned Assets

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Responsibilities`, sub-tab `Assigned Assets`
4. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
5. Pin kolom pertama (`Photo`), klik `[Save]`
6. Scroll tabel secara horizontal
7. Verifikasi kolom `Photo` membeku saat scroll horizontal
8. Buka Setup Column, Unpin kolom pertama (`Photo`), klik `[Save]`
9. Scroll tabel secara horizontal
10. Verifikasi kolom `Photo` kembali ikut bergeser

### TC-GS-NLU-388: Reset to Default pada Setup Column Assigned Assets

11. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
12. Ubah visibilitas dan urutan kolom: hapus centang kolom pertama (`Photo`) dan drag kolom terakhir (`PIC`) ke posisi pertama
13. Klik `[Reset to Default]`
14. Verifikasi Live Preview kembali ke default modul
15. Klik `[Save]`
16. Verifikasi tabel mengikuti default
17. Muat ulang halaman
18. Klik tab `Responsibilities`, sub-tab `Assigned Assets`
19. Verifikasi tabel tetap mengikuti default setelah refresh

### TC-GS-NLU-389: Menutup Setup Column Assigned Assets tanpa Save membuang perubahan

20. Untuk setiap baris tabel `Cara menutup Setup Column` di `## Prerequisites` (langkah 20 sampai 25)
21. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
22. Hapus centang kolom pertama (`Photo`)
23. Tutup popup Setup Column dengan cara pada baris tabel (tombol `✕` atau tombol keyboard `Esc`)
24. Verifikasi popup Setup Column tertutup
25. Verifikasi kolom `Photo` kembali tampil seperti konfigurasi tersimpan

### TC-GS-NLU-390: Kolom visible terakhir pada Setup Column Assigned Assets tidak dapat dihapus centang

26. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
27. Hapus centang semua kolom kecuali satu (`PIC`)
28. Arahkan kursor ke checkbox kolom tersisa
29. Verifikasi checkbox kolom tersisa disabled
30. Verifikasi tooltip checkbox `"At least one column must remain visible."`
31. Tutup popup Setup Column dengan tombol `✕` tanpa menyimpan

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (TC-GS-NLU-387, TC-GS-NLU-388, TC-GS-NLU-389, TC-GS-NLU-390) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (Search `Budi Kurniawan` dan membuka Detail, langkah penghubung menuju layar awal spec; Search di daftar mengikuti bagian 8b butir 9); langkah 3 (membuka Assigned Assets); tiap langkah pembuka Setup Column dan langkah terakhir di blok kolom visible terakhir (menutup popup dengan `✕` tanpa menyimpan, agar tidak ada form dirty tersisa).
- Asersi tambahan (konkretisasi Expected): kolom yang di-Pin pada TC-GS-NLU-387 adalah `Photo`; perubahan pada TC-GS-NLU-388 adalah menghapus centang `Photo` dan drag `PIC` ke posisi pertama; langkah 20 sampai 25 diulang untuk `✕` dan `Esc` (parameter di tabel Prerequisites, langkah yang diulang dituliskan sekali). Langkah muat ulang diikuti membuka kembali Assigned Assets.
- Pembagian TC lintas spec: Setup Column Assigned Assets dibagi dua spec; TC separuh lainnya ada di spec 106.
- Hook `after` suite memulihkan konfigurasi kolom (menghapus preferensi kolom di browser), sehingga spec berikutnya mulai dari urutan default.
- Spec melewati sekitar 35 langkah (31 langkah nominal, 37 dengan ekspansi blok `✕` dan `Esc`). Alasan: keempat TC satu kelas harness (fungsional), satu layar, satu dataset, dan masing-masing berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memisahkannya mengulang login, pembukaan layar, dan pembentukan state yang sama.
- Temuan untuk QA:
  - TC-GS-NLU-387: TC tidak menyatakan bahwa tabel cukup lebar untuk scroll horizontal; kebutuhan itu (lebar viewport atau jumlah kolom) disediakan tim FE.
  - TC-GS-NLU-388: TC tidak menyebut perubahan konkret sebelum `[Reset to Default]`; spec memilih menghapus centang kolom pertama dan memindahkan kolom terakhir.
  - TC-GS-NLU-389: TC menulis "(ulangi dengan `Esc`)" tanpa menyatakan apakah `Esc` menutup hanya popup Setup Column atau juga Assigned Assets; spec mengasersi popup Setup Column tertutup dan kolom kembali seperti konfigurasi tersimpan.
  - TC tidak menyebut cara memulihkan konfigurasi kolom yang disimpan; spec memakai kemampuan "disediakan tim FE" untuk menghapus preferensi kolom di browser (S-13).
