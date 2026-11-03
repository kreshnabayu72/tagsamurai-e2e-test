---
id: TC-FA-SU-E2E-140-sub-tab-borrowed-assets-sort
title: "Sub-tab Borrowed Assets: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-417
  - TC-FA-SU-418
  - TC-FA-SU-419
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Tabel "Sort kolom teks" (urutan baris sesudah klik header; kelima baris selalu dipakai):

  | Kolom | Ascending | Descending |
  |---|---|---|
  | Name | `Kamera DSLR`, `Kendaraan Operasional`, `Laptop - 1`, `Laptop - 2`, `Proyektor Portable` | `Proyektor Portable`, `Laptop - 2`, `Laptop - 1`, `Kendaraan Operasional`, `Kamera DSLR` |
  | Asset ID | `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional` | `Kendaraan Operasional`, `Proyektor Portable`, `Kamera DSLR`, `Laptop - 2`, `Laptop - 1` |
  | Transaction ID | `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional` | `Kendaraan Operasional`, `Proyektor Portable`, `Kamera DSLR`, `Laptop - 1`, `Laptop - 2` |
  | Brand | `Kamera DSLR`, `Laptop - 1`, `Proyektor Portable`, `Kendaraan Operasional`, `Laptop - 2` | `Laptop - 2`, `Kendaraan Operasional`, `Proyektor Portable`, `Laptop - 1`, `Kamera DSLR` |
  | Model / Type | `Laptop - 2`, `Proyektor Portable`, `Kamera DSLR`, `Laptop - 1`, `Kendaraan Operasional` | `Kendaraan Operasional`, `Laptop - 1`, `Kamera DSLR`, `Proyektor Portable`, `Laptop - 2` |
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-417: Sort Sub-tab Borrowed Assets kelas teks: Name, Asset ID, Transaction ID, Brand, Model / Type

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Untuk setiap baris tabel "Sort kolom teks" di Prerequisites (langkah 2 sampai 7): klik header kolom pada baris itu satu kali
3. Verifikasi klik 1 ascending (↑): urutan baris sesuai kolom Ascending pada baris itu
4. Klik header kolom yang sama kedua kali
5. Verifikasi klik 2 descending (↓): urutan baris sesuai kolom Descending pada baris itu
6. Klik header kolom yang sama ketiga kali
7. Verifikasi klik 3 netral kembali ke default: `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional`

### TC-FA-SU-418: Sort Sub-tab Borrowed Assets kelas date: Due Return Date

8. Klik header kolom Due Return Date satu kali
9. Verifikasi Due Return Date klik 1 ascending (↑): `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional`
10. Klik header kolom Due Return Date kedua kali
11. Verifikasi Due Return Date klik 2 descending (↓): `Kendaraan Operasional`, `Proyektor Portable`, `Kamera DSLR`, `Laptop - 1`, `Laptop - 2`
12. Klik header kolom Due Return Date ketiga kali
13. Verifikasi Due Return Date klik 3 netral kembali ke default: `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional`

### TC-FA-SU-419: Sort Sub-tab Borrowed Assets kelas user: PIC

14. Klik header kolom PIC satu kali
15. Verifikasi PIC klik 1 ascending (↑): `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional`
16. Klik header kolom PIC kedua kali
17. Verifikasi PIC klik 2 descending (↓): `Kendaraan Operasional`, `Kamera DSLR`, `Proyektor Portable`, `Laptop - 1`, `Laptop - 2`
18. Klik header kolom PIC ketiga kali
19. Verifikasi PIC klik 3 netral kembali ke default: `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Rentang langkah 2 sampai 7 diulang untuk lima kolom pada tabel "Sort kolom teks" (Prerequisites).
- Alasan melewati sekitar 35 langkah (19 langkah tertulis, 43 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-417: baris dengan nilai kolom sama (mis. Transaction ID `BRW-20260610` pada `Laptop - 1` dan `Laptop - 2`) berurutan seperti tertulis di TC; TC tidak menyebut aturan urutan sekunder.
  - TC-FA-SU-418: klik 1 ascending menghasilkan urutan yang sama dengan default, sehingga klik 3 netral tidak terbedakan dari klik 1 hanya lewat urutan baris; spec mengasersi urutan sesuai TC.
  - TC-FA-SU-419: dua baris ber-PIC sama (`Ahmad D`) berurutan seperti tertulis di TC; TC tidak menyebut aturan urutan sekunder.
