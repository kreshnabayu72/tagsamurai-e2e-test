---
id: TC-GS-NLU-E2E-094-modal-changelog-agregat-setup-column-bagian-2
title: "Modal Changelog Agregat: Setup Column Bagian 2"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-327
  - TC-GS-NLU-328
  - TC-GS-NLU-329
  - TC-GS-NLU-330
coverage:
  web: automated
---

# Modal Changelog Agregat: Setup Column Bagian 2

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
- Tabel `Cara menutup Setup Column` (dipakai langkah 18 sampai 23):

  | Cara menutup |
  |---|
  | Tombol `✕` pada popup Setup Column |
  | Tombol keyboard `Esc` |
- Kemampuan teknis: drag and drop baris kolom, scroll horizontal tabel, hover tooltip checkbox, menekan `Esc`, muat ulang halaman, dan menghapus preferensi kolom di browser (disediakan tim FE).

## Test Steps

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka

### TC-GS-NLU-327: Pin dan Unpin kolom pada Setup Column Modal Changelog agregat

2. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
3. Pin kolom pertama (`Date`), klik `[Save]`
4. Scroll tabel secara horizontal
5. Verifikasi kolom `Date` membeku saat scroll horizontal
6. Buka Setup Column, Unpin kolom pertama (`Date`), klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi kolom `Date` kembali ikut bergeser

### TC-GS-NLU-328: Reset to Default pada Setup Column Modal Changelog agregat

9. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
10. Ubah visibilitas dan urutan kolom: hapus centang kolom pertama (`Date`) dan drag kolom terakhir (`Modified By`) ke posisi pertama
11. Klik `[Reset to Default]`
12. Verifikasi Live Preview kembali ke default modul
13. Klik `[Save]`
14. Verifikasi tabel mengikuti default
15. Muat ulang halaman
16. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
17. Verifikasi tabel tetap mengikuti default setelah refresh

### TC-GS-NLU-329: Menutup Setup Column Modal Changelog agregat tanpa Save membuang perubahan

18. Untuk setiap baris tabel `Cara menutup Setup Column` di `## Prerequisites` (langkah 18 sampai 23)
19. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
20. Hapus centang kolom pertama (`Date`)
21. Tutup popup Setup Column dengan cara pada baris tabel (tombol `✕` atau tombol keyboard `Esc`)
22. Verifikasi popup Setup Column tertutup
23. Verifikasi kolom `Date` kembali tampil seperti konfigurasi tersimpan

### TC-GS-NLU-330: Kolom visible terakhir pada Setup Column Modal Changelog agregat tidak dapat dihapus centang

24. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
25. Hapus centang semua kolom kecuali satu (`Modified By`)
26. Arahkan kursor ke checkbox kolom tersisa
27. Verifikasi checkbox kolom tersisa disabled
28. Verifikasi tooltip checkbox `"At least one column must remain visible."`
29. Tutup popup Setup Column dengan tombol `✕` tanpa menyimpan

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (TC-GS-NLU-327, TC-GS-NLU-328, TC-GS-NLU-329, TC-GS-NLU-330) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog agregat); tiap langkah pembuka Setup Column dan langkah terakhir di blok kolom visible terakhir (menutup popup dengan `✕` tanpa menyimpan, agar tidak ada form dirty tersisa).
- Asersi tambahan (konkretisasi Expected): kolom yang di-Pin pada TC-GS-NLU-327 adalah `Date`; perubahan pada TC-GS-NLU-328 adalah menghapus centang `Date` dan drag `Modified By` ke posisi pertama; langkah 18 sampai 23 diulang untuk `✕` dan `Esc` (parameter di tabel Prerequisites, langkah yang diulang dituliskan sekali). Langkah muat ulang diikuti membuka kembali Modal Changelog agregat.
- Pembagian TC lintas spec: Setup Column Modal Changelog agregat dibagi dua spec; TC separuh lainnya ada di spec 093.
- Hook `after` suite memulihkan konfigurasi kolom (menghapus preferensi kolom di browser), sehingga spec berikutnya mulai dari urutan default.
- Temuan untuk QA:
  - TC-GS-NLU-327: TC tidak menyatakan bahwa tabel cukup lebar untuk scroll horizontal; kebutuhan itu (lebar viewport atau jumlah kolom) disediakan tim FE.
  - TC-GS-NLU-328: TC tidak menyebut perubahan konkret sebelum `[Reset to Default]`; spec memilih menghapus centang kolom pertama dan memindahkan kolom terakhir.
  - TC-GS-NLU-329: TC menulis "(ulangi dengan `Esc`)" tanpa menyatakan apakah `Esc` menutup hanya popup Setup Column atau juga Modal Changelog agregat; spec mengasersi popup Setup Column tertutup dan kolom kembali seperti konfigurasi tersimpan.
  - TC tidak menyebut cara memulihkan konfigurasi kolom yang disimpan; spec memakai kemampuan "disediakan tim FE" untuk menghapus preferensi kolom di browser (S-13).
