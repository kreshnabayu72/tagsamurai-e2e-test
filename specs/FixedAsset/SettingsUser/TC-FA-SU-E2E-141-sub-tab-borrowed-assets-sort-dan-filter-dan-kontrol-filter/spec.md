---
id: TC-FA-SU-E2E-141-sub-tab-borrowed-assets-sort-dan-filter-dan-kontrol-filter
title: "Sub-tab Borrowed Assets: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-420
  - TC-FA-SU-421
  - TC-FA-SU-422
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Tabel "Filter kolom fk" (satu field per iterasi langkah berulang):

  | Field | Opsi | Pilihan | Hasil |
  |---|---|---|---|
  | Name | `Kamera DSLR`, `Kendaraan Operasional`, `Laptop - 1`, `Laptop - 2`, `Proyektor Portable` | `Kamera DSLR` | `Kamera DSLR` (1 baris) |
  | Brand | `Canon`, `Dell`, `Epson`, `Honda`, `LG` | `Canon` | `Kamera DSLR` (1 baris) |
  | Model / Type | `24MK430H`, `EB-X41`, `EOS 90D`, `Latitude 5420`, `Vario 125` | `24MK430H` | `Laptop - 2` (1 baris) |
  | PIC | `Ahmad D`, `Citra L`, `Eka W` | `Ahmad D` | `Laptop - 1`, `Laptop - 2` (2 baris) |
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-420: Guard kolom non-sortable Sub-tab Borrowed Assets: Photo

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Hover header kolom Photo
4. Klik header kolom Photo
5. Verifikasi header Photo tidak memiliki icon sort
6. Verifikasi klik header Photo tidak mengubah urutan

### TC-FA-SU-421: Screening Filter Panel Sub-tab Borrowed Assets: field, label, placeholder, dan tombol

7. Klik icon Filter
8. Verifikasi panel Filter terbuka di bawah Table Tools
9. Verifikasi icon Filter menjadi gelap
10. Hover icon Filter
11. Verifikasi tooltip `Filter`
12. Verifikasi field pertama Name berupa multi-select searchable dengan placeholder `All assets`
13. Verifikasi field kedua Brand berupa multi-select searchable dengan placeholder `All brands`
14. Verifikasi field ketiga Model / Type berupa multi-select searchable dengan placeholder `All models/types`
15. Verifikasi field keempat Due Return Date berupa date range picker dengan placeholder `Select date`
16. Verifikasi field kelima PIC berupa multi-select searchable dengan placeholder `All PICs`
17. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
18. Verifikasi icon Filter tanpa badge titik selama belum ada filter ter-Apply
19. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-422: Filter Sub-tab Borrowed Assets kelas fk: Name, Brand, Model / Type, PIC

20. Klik icon Filter
21. Untuk setiap baris tabel "Filter kolom fk" di Prerequisites (langkah 21 sampai 28): buka dropdown pada field baris itu
22. Verifikasi opsi dropdown sama dengan DISTINCT data tabel sesuai kolom Opsi pada baris itu
23. Centang opsi pada kolom Pilihan baris itu
24. Klik `[Apply]`
25. Verifikasi memilih opsi tersebut menyisakan baris pada kolom Hasil baris itu
26. Verifikasi chip opsi yang dipilih tampil di dalam field
27. Klik `[Clear Field]` pada field tersebut
28. Klik `[Apply]`
29. Tutup panel Filter dengan klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Rentang langkah 21 sampai 28 diulang untuk empat field pada tabel "Filter kolom fk" (Prerequisites).
- Alasan melewati sekitar 35 langkah (29 langkah tertulis, 53 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-422 langkah 5, 8, dan 11: `[Clear Field]` disebut "pada field tersebut", sedangkan footer Filter Panel (TC-FA-SU-421) hanya punya satu `[Clear Field]`; spec mengklik `[Clear Field]` footer.
