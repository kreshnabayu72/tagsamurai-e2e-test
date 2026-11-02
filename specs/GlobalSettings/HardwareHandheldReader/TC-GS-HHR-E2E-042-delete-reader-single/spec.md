---
id: TC-GS-HHR-E2E-042-delete-reader-single
title: "Delete Reader Tunggal: Dialog, Cancel, Delete Jalur A dan B pada Status Available, Damaged, Missing, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-149
  - TC-GS-HHR-150
  - TC-GS-HHR-151
  - TC-GS-HHR-152
  - TC-GS-HHR-153
  - TC-GS-HHR-154
  - TC-GS-HHR-458
coverage:
  web: automated
---

# Delete Reader Tunggal: Dialog, Cancel, Delete Jalur A dan B pada Status Available, Damaged, Missing, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini menghapus reader Seed Reader A dan memulihkannya (lihat butir pemulihan); aksi Delete berada di akhir spec.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman).
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SN-HHR-00101, SKU-HHR-01, Jalur A, Long Range, Available), DD-07 (`Honeywell CK65 - 1`, SN-HHR-00108, Jalur B, Long Range, Available), DD-03 (`Zebra Mobile Reader - 1`, Jalur A, Long Range, Damaged), dan DD-04 (`Gudang Reader - 2`, Jalur A, Short Range, Missing). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR).
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya, dan nilai Expected tiap TC (pagination `Showing 1 - 9 of 9 readers`, kartu kuota) mengasumsikan hanya satu reader yang dihapus. Spec memulihkan Seed Reader A pada langkah pertama tiap iterasi hapus dan sebelum TC-GS-HHR-458 lewat kemampuan "pulihkan Seed Reader A lewat fixture backend" yang disediakan tim FE/BE tanpa endpoint yang dikarang, lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Tabel "Kasus dialog Delete Reader" (parameter langkah 1 sampai 7):

| TC | Reader | Bullet Body baris 1 | Kalimat dampak Body baris 2 |
|---|---|---|---|
| TC-GS-HHR-149 | DD-01 | `Zebra RFID Reader - 1 (SN-HHR-00101)` | `Its license quota will be returned and the unit will be available again in Hardware Stock.` |
| TC-GS-HHR-150 | DD-07 | `Honeywell CK65 - 1 (SN-HHR-00108)` | `Its license quota will be returned.` |

- Tabel "Kasus Delete berhasil" (parameter langkah 8 sampai 15):

| TC | Reader | Device Name | Kartu kuota sesudah |
|---|---|---|---|
| TC-GS-HHR-151 | DD-01 (Jalur A, Available) | `Zebra RFID Reader - 1` | `Long Range` `4 of 6`, `2 remaining` |
| TC-GS-HHR-152 | DD-07 (Jalur B, Available) | `Honeywell CK65 - 1` | `Long Range` `4 of 6`, `2 remaining` |
| TC-GS-HHR-153 | DD-03 (Damaged) | `Zebra Mobile Reader - 1` | `Long Range` `4 of 6`, `2 remaining` |
| TC-GS-HHR-154 | DD-04 (Missing) | `Gudang Reader - 2` | `Short Range` `4 of 8`, `4 remaining` |

- Kemampuan teknis: klik ganda cepat pada `[Delete]` (TC-GS-HHR-458); pembacaan teks pagination, kartu kuota, dan Modal Changelog; pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-149 dan TC-GS-HHR-150: Screening dialog Delete Reader dan Cancel tidak menghapus

Untuk setiap baris tabel "Kasus dialog Delete Reader" (langkah 1 sampai 7):

1. Buka Overlay row action baris {Reader}
2. Klik `Delete`
3. Verifikasi dialog tampil utuh: Judul `Delete Reader`, Body baris 1 bullet `{Bullet Body baris 1}`, Body baris 2 `{Kalimat dampak Body baris 2}`, Body baris 3 `Are you sure you want to delete it? This action cannot be undone.`, Footer `[Cancel]` dan `[Delete]` (`[Delete]` `severity="danger"`)
4. Klik `[Cancel]`
5. Verifikasi tidak ada toast
6. Verifikasi dialog tertutup
7. Verifikasi baris {Reader} tetap ada

### TC-GS-HHR-151, 152, 153, 154: Delete reader berhasil

Untuk setiap baris tabel "Kasus Delete berhasil" (langkah 8 sampai 15):

8. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
9. Buka Overlay row action baris {Reader}
10. Klik `Delete`
11. Klik `[Delete]` pada dialog
12. Verifikasi muncul toast sukses: "Success, {Device Name} has been deleted."
13. Verifikasi baris {Reader} hilang dari tabel
14. Verifikasi pagination menampilkan `Showing 1 - 9 of 9 readers`
15. Verifikasi kartu kuota menampilkan {Kartu kuota sesudah}

### TC-GS-HHR-458: Klik ganda cepat pada konfirmasi Delete hanya menghapus satu kali

16. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
17. Buka ikon Changelog (Modal Changelog), catat jumlah entri sebagai baseline
18. Tutup Modal Changelog dengan `✕`
19. Buka Overlay row action baris DD-01 (`Zebra RFID Reader - 1`)
20. Klik `Delete`
21. Tunggu toast lama hilang otomatis
22. Klik ganda cepat `[Delete]` pada dialog
23. Verifikasi hanya satu toast sukses yang tampil: "Success, Zebra RFID Reader - 1 has been deleted."
24. Verifikasi tidak ada toast `This device is no longer available.`
25. Buka ikon Changelog
26. Verifikasi jumlah entri Changelog bertambah tepat 1 dibanding baseline langkah 17
27. Verifikasi entri baru: Action `Delete` untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
28. Tutup Modal Changelog dengan `✕`
29. Verifikasi kartu `Long Range` menjadi `4 of 6`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3e).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 1 sampai 7 diulang dua kali dan langkah 8 sampai 15 diulang empat kali, sehingga ekspansi spec 14 + 32 + 14 = 60 langkah.
- Urutan TC di spec: 149 dan 150 (dialog dengan `[Cancel]`, tidak menghapus), lalu 151, 152, 153, 154 (Delete berhasil), lalu 458 paling akhir. Aksi yang menghapus data berada sesudah semua kasus yang membutuhkan baris tetap ada (prinsip 5); TC-GS-HHR-458 memakai DD-01 yang sudah dihapus oleh TC-GS-HHR-151 sehingga Seed Reader A dipulihkan sebelumnya. Menyimpang dari urutan nomor TC sumber (458 berada di section yang sama sesudah 155).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 dan 16 (pemulihan dan muat ulang), langkah 17 dan 18 (baseline Changelog sebelum aksi pemicu; S-12), langkah 21 (menunggu toast lama hilang agar hitungan satu toast bermakna), dan langkah 28 (menutup Modal Changelog).
- Pada TC-GS-HHR-458 langkah 23 dan 24 diletakkan segera sesudah klik ganda karena toast adalah state sementara; hitungan "satu toast" didahului muat ulang halaman pada langkah 16 dan langkah 21. Baris DD-01 hilang diasersi oleh toast sukses sebagai anchor (langkah 13 pada iterasi hapus).
- Pengecualian alasan di atas sekitar 35 langkah (ekspansi 60): seluruh blok satu kelas (Delete reader tunggal), tiap iterasi hapus berdiri sendiri dengan pemulihan Seed Reader A sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, langkah diulang hanya per baris data, dan seluruh aksi Delete berada di akhir.
- Pengecualian S-12 Population Seed Reader A HHR (A-5) berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Bulk Delete (TC-GS-HHR-214 sampai 217, 220) ada di spec 046; resilience Delete 5xx (TC-GS-HHR-155) ada di spec 027.
- Temuan untuk QA:
  - Post Condition TC-GS-HHR-151, 152, 153, dan 154 ("Record reader dihapus, kuota dikembalikan" teramati lewat baris hilang dan kartu kuota; "Tiga surface log (TC section 5)"; "Unit di Hardware Stock kembali `Available` (TC section 7)"; "Reader Jalur B tidak mengubah stok Admin Console") tidak punya langkah observasi untuk tiga surface log dan Hardware Stock di TC ini, sehingga tidak diasersi di spec ini.
  - TC-GS-HHR-151 s.d. 154 menulis pagination `Showing 1 - 9 of 9 readers` dan kartu kuota yang mengasumsikan hanya satu reader dihapus per TC; spec memulihkan Seed Reader A antar-iterasi agar nilai Expected TC tetap berlaku.
  - TC-GS-HHR-458 Expected b ("satu entri `Delete` untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`") tidak menyebut cara menemukan entri di Changelog kumulatif; spec memakai selisih jumlah entri terhadap baseline dan entri baru pada urutan default.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend hanya disebut "fixture backend" di Catatan TC dan tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
