---
id: TC-FA-SU-E2E-103-popup-select-home-group-bulk-dan-aksesibilitas-popup-select-home-group
title: "Popup Select Home Group Bulk dan Aksesibilitas Popup Select Home Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-908
  - TC-FA-SU-1047
coverage:
  web: automated
---

# Popup Select Home Group Bulk dan Aksesibilitas Popup Select Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21). Pengguna: Gita Permata, Budi Santoso (dua baris bulk), dan Hana Kusuma (popup singular untuk aksesibilitas). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis: pembacaan label aksesibel (accessible name) elemen dan pengamatan urutan fokus keyboard disediakan tim FE.
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-908: Popup Select Home Group varian bulk

1. Ketik Search `Gita Permata`, tekan Enter
2. Centang Gita Permata
3. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
4. Centang Budi Santoso
5. Klik Bulk Action > `Edit Home Group`
6. Ketik Search `Surabaya`, tekan Enter
7. Verifikasi pohon memfilter node dan node Branch Surabaya tampil
8. Klik node Branch Surabaya
9. Verifikasi tepat satu node terpilih
10. Kosongkan isi kotak search popup, tekan Enter
11. Klik node lain (hasil Search sesudah mengosongkan Search)
12. Verifikasi node lain menggantikan pilihan sebelumnya
13. Ketik Search `zzz`, tekan Enter
14. Verifikasi empty state `No results found` tampil
15. Klik `[Cancel]` lalu klik Unselect All

### TC-FA-SU-1047: Aksesibilitas popup Select Home Group

16. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
17. Klik ⋯ pada baris Hana Kusuma lalu klik `Edit Home Group`
18. Tekan Tab berulang
19. Verifikasi fokus keyboard terkunci di dalam popup `Select Home Group` (Tab dan Shift+Tab berputar di dalam popup)
20. Tekan Esc
21. Verifikasi popup tertutup tanpa menyimpan
22. Klik ⋯ pada baris Hana Kusuma
23. Verifikasi ikon aksi baris (Detail, Edit Home Group, Resend) memiliki label deskriptif untuk screen reader

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): `[Cancel]` dan Unselect All, langkah 10 (mengosongkan Search popup supaya pohon penuh tampil sebelum klik node lain), langkah 1, 3, dan 16 (Search untuk menemukan baris target, R-16 dan butir 8b.13), dan langkah 22 (membuka kembali menu ⋯ yang tertutup sesudah popup ditutup, supaya ikon aksi baris teramati). TC-FA-SU-908 langkah 3 "klik node lain" ditulis sebagai klik node pada hasil sesudah Search dikosongkan; urutan Search mengikuti TC.
- Temuan untuk QA (S-15): (1) TC-FA-SU-908 tidak menyebut dua baris yang dicentang dan node "lain"; spec memakai Gita Permata dan Budi Santoso, serta node lain yang tampil pada hasil Search. (2) TC-FA-SU-908 tidak menyebut node "lain"; spec mengosongkan Search lebih dulu (langkah 10) lalu memilih node lain pada pohon penuh. (3) TC-FA-SU-1047 Expected c (label ikon aksi baris Detail, Edit Home Group, Resend) tidak punya langkah yang membuka baris yang menampilkan ketiga ikon; spec mengamati ikon pada baris Hana Kusuma (Pending Activation). (4) Post Condition tidak ada. (5) TC-FA-SU-908 mencentang dua pengguna sekaligus tanpa menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti; mohon konfirmasi.
