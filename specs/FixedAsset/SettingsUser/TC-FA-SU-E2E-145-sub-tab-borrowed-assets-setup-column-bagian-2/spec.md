---
id: TC-FA-SU-E2E-145-sub-tab-borrowed-assets-setup-column-bagian-2
title: "Sub-tab Borrowed Assets: Setup Column (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-433
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Setup Column (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- State yang diubah: preferensi kolom tabel tersimpan per perangkat setelah `[Save]`. Dipulihkan dengan menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi), bukan `[Reset to Default]`; langkah pemulihan ada di akhir blok yang menyimpan, dan hook `after` mengulangnya sebagai cadangan. Spec tidak mengubah data backend.

## Test Steps

### TC-FA-SU-433: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column Sub-tab Borrowed Assets

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Klik header kolom Column Visibility (⋯)
3. Klik `Setup Column...`
4. Hapus centang kolom Name
5. Drag kolom PIC satu posisi ke atas
6. Klik icon Pin pada kolom Photo
7. Klik `[Reset to Default]`
8. Verifikasi `[Reset to Default]` mengembalikan visibility ke default pada preview: seluruh kolom (Photo sampai PIC) tampil
9. Verifikasi `[Reset to Default]` mengembalikan urutan ke default pada preview: Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC
10. Verifikasi `[Reset to Default]` mengembalikan pin ke default pada preview: tidak ada kolom ter-pin
11. Klik `[Save]`
12. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`: tabel menampilkan seluruh kolom tanpa kolom ter-pin
13. Klik header kolom Column Visibility (⋯)
14. Klik `Setup Column...`
15. Hapus centang kolom Name
16. Tutup popup Setup Column dengan ✕
17. Verifikasi menutup lewat ✕ tanpa Save membuang perubahan preview: tabel tetap menampilkan Name
18. Klik header kolom Column Visibility (⋯)
19. Klik `Setup Column...`
20. Hapus centang kolom Name
21. Tutup popup Setup Column dengan Esc
22. Verifikasi menutup lewat Esc tanpa Save membuang perubahan preview: tabel tetap menampilkan Name
23. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Assigned Assets
24. Verifikasi konfigurasi kolom Sub-tab Assigned Assets tidak terpengaruh oleh perubahan konfigurasi Sub-tab Borrowed Assets (cache per tabel)
25. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-432 ada di spec 148.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Pemulihan konfigurasi kolom: preferensi kolom yang disimpan spec dihapus di browser pada akhir blok dan di hook `after` (Prerequisites); `[Reset to Default]` tidak dipakai sebagai pemulihan.
- Temuan untuk QA (S-15):
  - TC-FA-SU-433: "beberapa pengaturan" dan "tabel lain yang punya Setup Column" tidak dirinci; spec memilih sendiri (Name di-uncheck, PIC digeser, Photo di-pin; tabel lain = Sub-tab Assigned Assets). Perubahan yang disimpan berupa konfigurasi default, sehingga independensi cache diasersi sebagai konfigurasi tabel lain tidak berubah. Post Condition tidak diasersi.
