---
id: TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status
title: "Bulk Action: Opsi yang Tampil Mengikuti Status Seluruh Reader Terpilih"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-196
  - TC-GS-HHR-197
  - TC-GS-HHR-198
  - TC-GS-HHR-199
  - TC-GS-HHR-200
coverage:
  web: automated
---

# Bulk Action: Opsi yang Tampil Mengikuti Status Seluruh Reader Terpilih

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini tidak mengubah data reader: opsi Bulk Action hanya dibuka dan dibaca, tidak ada yang dipilih.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend; dibaca saja): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), 10 reader DD-01 s.d. DD-10, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Status yang dipakai: DD-01, DD-02, DD-06, DD-07 `Available`; DD-03 `Damaged`; DD-04 `Missing`. Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Tabel "Kasus eligibility bulk" (parameter langkah 1 sampai 7):

| TC | Reader terpilih | Opsi yang tampil (urut) | Opsi yang tidak ada |
|---|---|---|---|
| TC-GS-HHR-196 | DD-01 (Available), DD-07 (Available) | `Mark as Damaged`, `Mark as Missing`, `Delete` (masing-masing severity danger) | `Mark as Available` |
| TC-GS-HHR-197 | DD-03 (Damaged), DD-04 (Missing) | `Mark as Available` (dark), `Delete` (danger) | `Mark as Damaged` dan `Mark as Missing` |
| TC-GS-HHR-198 | DD-01 (Available), DD-03 (Damaged) | `Delete` | `Mark as Damaged`, `Mark as Missing`, dan `Mark as Available` |

- Kemampuan teknis: pembacaan daftar opsi Bulk Action beserta urutan, severity, dan keadaan tampil (Hidden, bukan disabled).
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-196, 197, 198: Seleksi dengan status seragam atau campuran menentukan opsi Bulk Action

Untuk setiap baris tabel "Kasus eligibility bulk" (langkah 1 sampai 7):

1. Centang checkbox baris reader terpilih pertama pada kolom "Reader terpilih"
2. Centang checkbox baris reader terpilih kedua pada kolom "Reader terpilih"
3. Klik tombol `Bulk Action`
4. Verifikasi daftar opsi tampil berurutan: {Opsi yang tampil}
5. Verifikasi opsi {Opsi yang tidak ada} tidak ada di daftar (disembunyikan, bukan disabled)
6. Klik tombol `Bulk Action` sekali lagi untuk menutup daftar opsi
7. Klik ikon `×`

### TC-GS-HHR-199: Seleksi campuran Available dan Missing hanya menampilkan Delete

8. Centang checkbox baris DD-02 (Available)
9. Centang checkbox baris DD-04 (Missing)
10. Klik tombol `Bulk Action`
11. Verifikasi hanya opsi `Delete` yang tampil
12. Klik tombol `Bulk Action` sekali lagi untuk menutup daftar opsi
13. Klik ikon `×`

### TC-GS-HHR-200: Seleksi satu baris menampilkan opsi sesuai status baris itu

14. Centang checkbox baris DD-03 (Damaged)
15. Klik tombol `Bulk Action`
16. Verifikasi opsi tampil: `Mark as Available` dan `Delete`
17. Klik tombol `Bulk Action` sekali lagi untuk menutup daftar opsi
18. Lepas centang checkbox baris DD-03
19. Centang checkbox baris DD-06 (Available)
20. Klik tombol `Bulk Action`
21. Verifikasi opsi tampil: `Mark as Damaged`, `Mark as Missing`, dan `Delete`
22. Klik tombol `Bulk Action` sekali lagi untuk menutup daftar opsi
23. Klik ikon `×`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 1 sampai 7 diulang tiga kali (satu kali per baris tabel "Kasus eligibility bulk"), sehingga ekspansi spec 21 + 6 + 10 = 37 langkah, sedikit di atas sekitar 35 langkah; alasan: seluruh blok satu kelas (membaca opsi Bulk Action tanpa mengubah data), tiap blok memakai seleksi sendiri yang dikosongkan sebelum blok berikutnya, dan langkah diulang hanya per baris data.
- Urutan TC di spec: 196, 197, 198, 199, 200 (sama dengan urutan nomor TC sumber). Tidak ada aksi yang mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 12, 17, dan 22 (menutup daftar opsi dengan klik `Bulk Action` kedua kali), langkah 7, 13, dan 23 (mengosongkan seleksi lewat `×`), dan langkah 18 (melepas centang DD-03 sebagai bagian aksi TC-GS-HHR-200).
- Asersi tidak ada (langkah 5) didahului langkah 4 yang membuktikan daftar opsi pada surface yang sama sudah tampil dan memuat opsi lain (anchor positif; 8b butir 2).
- Aturan hak aktor per level capability (TC-GS-HHR-201 sampai 203) ada di spec 008.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): spec memakai nama literal tanpa suffix reader Pre-setup DD-01, DD-02, DD-03, DD-04, DD-06, dan DD-07 Client A karena asersi bergantung pada nama dan status persis; pemulihan Seed Reader A dijamin fixture backend yang disediakan tim FE/BE dan dinyatakan di `suite.md` dan Prerequisites; spec ini hanya membaca daftar opsi sehingga tidak ada langkah pemulihan; suite serial.
- Temuan untuk QA:
  - TC-GS-HHR-196 Expected a menulis "masing-masing severity danger" sedangkan TC-GS-HHR-197 menulis `Mark as Available` (dark) dan `Delete` (danger); TC-GS-HHR-198, 199, dan 200 tidak menyebut severity. Spec mengasersi severity hanya pada kasus yang menyebutnya.
  - TC-GS-HHR-200 tidak menyebut cara melepas centang DD-03 sebelum mencentang DD-06 selain "Lepas centang DD-03"; spec memakai klik checkbox baris DD-03.
  - TC-GS-HHR-196 sampai 200 tidak mencantumkan Post Condition.
