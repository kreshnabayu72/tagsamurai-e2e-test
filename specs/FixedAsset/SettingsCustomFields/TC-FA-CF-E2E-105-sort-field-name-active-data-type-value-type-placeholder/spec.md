---
id: TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder
title: "Sort: Field Name, Active, Data Type, Value Type, dan Placeholder"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-394
  - TC-FA-CF-395
  - TC-FA-CF-396
  - TC-FA-CF-397
  - TC-FA-CF-398
  - TC-FA-CF-406
coverage:
  web: automated
---

# Sort: Field Name, Active, Data Type, Value Type, dan Placeholder

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi urutan bergantung pada nama dan nilai kolom seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field:
  - `Asset Serial Tag`: Text; Active; Value Type Specific; Placeholder kosong.
  - `Storage Capacity`: Numeric; Active; Value Type Specific; Placeholder `Capacity in GB`.
  - `Equipment Class`: Dropdown; Active; Value Type Specific.
  - `Operating Voltage`: Text; Active; Value Type Global.
  - `Total Cost`: Formula; Active; Value Type `—`; Placeholder `—`.
  - `Depreciated Ratio`: Percentage; Inactive; Value Type Specific.
  - `Compliance File`: Document; Active; Value Type Specific.
  - `Legacy Tag`: Text; Active; Value Type Specific.
  Placeholder selain `Storage Capacity` dikosongkan sehingga nilai efektif memakai default tipe.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan ikon sort per header kolom (naik, turun, netral) dan urutan baris tabel pada halaman teramati (delapan baris tampil pada satu halaman, ukuran halaman bawaan 10).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-406: Kolom Checkbox dan Actions tidak memiliki ikon sort

1. Verifikasi ikon sort tampil pada header kolom `Field Name`
2. Verifikasi tidak ada ikon sort pada kolom Checkbox dan Actions `(⋯)`

### TC-FA-CF-394: Urutan awal Field Name A-Z dan siklus tiga klik kembali ke default

3. Klik header `Field Name` sekali
4. Verifikasi ikon naik aktif pada header `Field Name`
5. Verifikasi urutan A-Z (default)
6. Klik header `Field Name` sekali lagi
7. Verifikasi ikon turun aktif pada header `Field Name`
8. Verifikasi urutan Z-A (`Total Cost` di atas)
9. Klik header `Field Name` sekali lagi
10. Verifikasi ikon sort netral pada header `Field Name`
11. Verifikasi urutan kembali ke default A-Z

### TC-FA-CF-395: Sort kolom Active mengikuti Active First lalu Inactive First

12. Klik header `Active` sekali
13. Verifikasi urutan menaik (Active First): tujuh baris ON dalam urutan Field Name A-Z (`Asset Serial Tag`, `Compliance File`, `Equipment Class`, `Legacy Tag`, `Operating Voltage`, `Storage Capacity`, `Total Cost`) lalu `Depreciated Ratio` (OFF)
14. Klik header `Active` sekali lagi
15. Verifikasi urutan menurun (Inactive First): `Depreciated Ratio` di atas lalu baris ON

### TC-FA-CF-396: Sort kolom Data Type alfabetis A-Z dengan tie-breaker default sort

16. Klik header `Data Type` sekali
17. Verifikasi urutan menaik: `Document` (`Compliance File`), `Dropdown` (`Equipment Class`), `Formula` (`Total Cost`), `Numeric` (`Storage Capacity`), `Percentage` (`Depreciated Ratio`), lalu `Text` (tiga baris Text: `Asset Serial Tag`, `Legacy Tag`, `Operating Voltage`)
18. Klik header `Data Type` sekali lagi
19. Verifikasi urutan menurun: urutan tipe terbalik (`Text` lebih dulu hingga `Document` terakhir) dan tiga baris Text tetap A-Z menurut default sort (`Asset Serial Tag`, `Legacy Tag`, `Operating Voltage`)

### TC-FA-CF-397: Sort kolom Value Type menempatkan nilai kosong Formula di akhir saat menaik dan di awal saat menurun

20. Klik header `Value Type` sekali
21. Verifikasi urutan menaik: `Global` (`Operating Voltage`), enam baris `Specific`, lalu `—` (`Total Cost`) di akhir
22. Klik header `Value Type` sekali lagi
23. Verifikasi urutan menurun: `—` (`Total Cost`) di awal, enam baris `Specific`, lalu `Global` (`Operating Voltage`) di akhir

### TC-FA-CF-398: Sort kolom Placeholder berdasarkan nilai efektif

24. Klik header `Placeholder` sekali
25. Verifikasi urutan menaik berdasarkan nilai efektif: `Storage Capacity` (`Capacity in GB`), `Asset Serial Tag`, `Legacy Tag`, `Operating Voltage`, `Depreciated Ratio`, `Equipment Class`, `Compliance File`, lalu `Total Cost` (`—`) di akhir

## Notes

- Spec memuat 25 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Sort tabel utama), satu dataset, satu akun.
- Urutan TC berbeda dari urutan TC sumber: TC-FA-CF-406 ditaruh paling awal (screening, S-10). Langkah 1 adalah `Verifikasi` tambahan di luar Expected TC (S-03): ikon sort pada header `Field Name` tampil sebagai anchor positif bagi asersi absence langkah 2 (bagian 8b butir 2).
- Tidak ada langkah penghubung: mengklik header kolom lain mereset sort kolom sebelumnya (TC-FA-CF-405), sehingga tiap TC mulai dari klik pertama kolomnya; TC-FA-CF-394 berakhir pada sort netral.
- Daftar nama baris pada langkah 13 dan 17 diturunkan dari data baseline Pre-setup #12 (Field Name A-Z dan Data Type tiap field) dan sesuai Expected TC.
- Temuan untuk QA:
  - TC-FA-CF-395 Expected a menyebut "tujuh baris ON dalam urutan Field Name A-Z" tanpa nama; spec menyebut nama berdasarkan baseline Pre-setup #12.
  - TC-FA-CF-397 dan TC-FA-CF-398 mengasersi urutan lengkap; urutan enam baris `Specific` mengikuti default sort (Field Name A-Z) tanpa disebut nama pada Expected TC-FA-CF-397.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
