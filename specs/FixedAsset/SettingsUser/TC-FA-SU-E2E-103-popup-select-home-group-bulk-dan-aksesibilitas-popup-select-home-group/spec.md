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

1. Centang Gita Permata dan Budi Santoso lalu klik Bulk Action > `Edit Home Group`
2. Ketik Search `Surabaya`, tekan Enter
3. Verifikasi pohon memfilter node dan node Branch Surabaya tampil
4. Klik node Branch Surabaya
5. Verifikasi tepat satu node terpilih
6. Klik node lain (hasil Search sesudah mengosongkan Search)
7. Verifikasi node lain menggantikan pilihan sebelumnya
8. Ganti isi kotak Search dengan `zzz`, tekan Enter
9. Verifikasi empty state `No results found` tampil
10. Klik `[Cancel]` lalu klik Unselect All

### TC-FA-SU-1047: Aksesibilitas popup Select Home Group

11. Klik ⋯ pada baris Hana Kusuma lalu klik `Edit Home Group`
12. Tekan Tab berulang
13. Verifikasi fokus keyboard terkunci di dalam popup `Select Home Group` (Tab dan Shift+Tab berputar di dalam popup)
14. Tekan Esc
15. Verifikasi popup tertutup tanpa menyimpan
16. Verifikasi ikon aksi baris (Detail, Edit Home Group, Resend) memiliki label deskriptif untuk screen reader

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): `[Cancel]` dan Unselect All. TC-FA-SU-908 langkah 3 "klik node lain" ditulis sebagai klik node pada hasil sesudah Search dikosongkan; urutan Search mengikuti TC.
- Temuan untuk QA (S-15): (1) TC-FA-SU-908 tidak menyebut dua baris yang dicentang dan node "lain"; spec memakai Gita Permata dan Budi Santoso, serta node lain yang tampil pada hasil Search. (2) Klik node lain pada hasil Search `Surabaya` hanya mengamati node yang tampil; bila hanya Branch Surabaya tampil, node lain tidak terpilih sehingga langkah itu bergantung pada hasil Search. (3) TC-FA-SU-1047 Expected c (label ikon aksi baris Detail, Edit Home Group, Resend) tidak punya langkah yang membuka baris yang menampilkan ketiga ikon; spec mengamati ikon pada baris Hana Kusuma (Pending Activation). (4) Post Condition tidak ada.
