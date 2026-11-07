---
id: TC-FA-SU-E2E-144-sub-tab-borrowed-assets-setup-column-bagian-1
title: "Sub-tab Borrowed Assets: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-430
  - TC-FA-SU-431
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Tabel "Kolom Hideable" (satu kolom per iterasi langkah berulang; kolom PIC dibahas di luar tabel karena menjadi satu-satunya kolom visible):

  | Kolom |
  |---|
  | Photo |
  | Name |
  | Asset ID |
  | Transaction ID |
  | Brand |
  | Model / Type |
  | Due Return Date |
- Tabel "Geser kolom" (satu kolom per iterasi; tiap kolom diseret satu posisi, urutan dihitung berurutan dari urutan awal Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC):

  | Kolom | Arah | Urutan sesudah diseret | Posisi akhir |
  |---|---|---|---|
  | Photo | ke bawah | Name, Photo, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC | 1 |
  | Name | ke bawah | Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC | 2 |
  | Asset ID | ke bawah | Photo, Name, Transaction ID, Asset ID, Brand, Model / Type, Due Return Date, PIC | 3 |
  | Transaction ID | ke bawah | Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC | 4 |
  | Brand | ke bawah | Photo, Name, Asset ID, Transaction ID, Model / Type, Brand, Due Return Date, PIC | 5 |
  | Model / Type | ke bawah | Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC | 7 |
  | Due Return Date | ke bawah | Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, PIC, Due Return Date | 8 |
  | PIC | ke atas | Photo, Name, Asset ID, Transaction ID, Brand, PIC, Model / Type, Due Return Date | 6 |
- State yang diubah: preferensi kolom tabel tersimpan per perangkat setelah `[Save]`. Dipulihkan dengan menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi), bukan `[Reset to Default]`; langkah pemulihan ada di akhir blok yang menyimpan, dan hook `after` mengulangnya sebagai cadangan. Spec tidak mengubah data backend.

## Test Steps

### TC-FA-SU-430: Ceklis dan unceklis Setup Column Sub-tab Borrowed Assets kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Klik header kolom Column Visibility (⋯)
4. Klik `Setup Column...`
5. Untuk setiap baris tabel "Kolom Hideable" di Prerequisites (langkah 5 sampai 6): hapus centang kolom pada baris itu
6. Verifikasi perubahan kolom tersebut tampil di Live Preview: kolom tidak lagi tampil
7. Arahkan kursor ke checkbox kolom PIC (satu-satunya kolom visible)
8. Verifikasi checkbox kolom PIC disabled dengan tooltip `At least one column must remain visible.`
9. Klik `[Save]`
10. Verifikasi kolom PIC tetap tampil di tabel
11. Untuk setiap baris tabel "Kolom Hideable" di Prerequisites (langkah 11): verifikasi kolom pada baris itu tidak tampil di tabel
12. Tekan F5
13. Verifikasi kolom PIC tetap tampil setelah refresh (F5)
14. Untuk setiap baris tabel "Kolom Hideable" di Prerequisites (langkah 14): verifikasi kolom pada baris itu tetap tidak tampil setelah refresh (F5)
15. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

### TC-FA-SU-431: Geser (drag reorder) Setup Column Sub-tab Borrowed Assets kelas Hideable (default tampil)

16. Klik header kolom Column Visibility (⋯)
17. Klik `Setup Column...`
18. Untuk setiap baris tabel "Geser kolom" di Prerequisites (langkah 18 sampai 19): drag kolom pada baris itu satu posisi sesuai kolom Arah
19. Verifikasi urutan Live Preview sesuai kolom Urutan sesudah diseret pada baris itu
20. Klik `[Save]`
21. Untuk setiap baris tabel "Geser kolom" di Prerequisites (langkah 21): verifikasi posisi kolom pada baris itu di tabel sama dengan kolom Posisi akhir
22. Tekan F5
23. Untuk setiap baris tabel "Geser kolom" di Prerequisites (langkah 23): verifikasi posisi kolom pada baris itu bertahan setelah F5 sesuai kolom Posisi akhir
24. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Rentang langkah 5 sampai 6, langkah 11, dan langkah 14 masing-masing diulang untuk tujuh kolom pada tabel "Kolom Hideable" (Prerequisites).
- Rentang langkah 18 sampai 19, langkah 21, dan langkah 23 masing-masing diulang untuk delapan kolom pada tabel "Geser kolom" (Prerequisites).
- Pemulihan konfigurasi kolom: preferensi kolom yang disimpan spec dihapus di browser pada akhir blok dan di hook `after` (Prerequisites); `[Reset to Default]` tidak dipakai sebagai pemulihan.
- Alasan melewati sekitar 35 langkah (24 langkah tertulis, 76 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-430: butir a sampai h meminta kedelapan kolom diubah centangnya, sedangkan butir i menyatakan kolom terakhir tidak dapat di-uncheck; spec meng-uncheck tujuh kolom pertama dan mengasersi kolom PIC lewat butir i (perubahan PIC di Live Preview tidak dapat terjadi). Post Condition (preferensi tersimpan per perangkat) tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-SU-431: arah seret dipilih penulis (satu posisi ke bawah, kecuali PIC ke atas) dan urutan sesudah tiap seretan dihitung berurutan dari urutan awal; TC hanya menyebut "satu posisi". Post Condition tidak diasersi.
