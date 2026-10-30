---
id: TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available
title: "Mark as Damaged, Missing, dan Available Berhasil Mengubah Status, Row Action Mengikuti Status Baru, dan Klik Ganda Hanya Sekali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-139
  - TC-GS-HHR-141
  - TC-GS-HHR-143
  - TC-GS-HHR-145
  - TC-GS-HHR-459
coverage:
  web: automated
---

# Mark as Damaged, Missing, dan Available Berhasil Mengubah Status, Row Action Mengikuti Status Baru, dan Klik Ganda Hanya Sekali

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini mengubah status reader Seed Reader A dan memulihkannya (lihat butir pemulihan).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman).
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, Long Range, Available), DD-03 (`Zebra Mobile Reader - 1`, Long Range, Damaged), dan DD-04 (`Gudang Reader - 2`, Short Range, Missing). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR).
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya. Spec memulihkannya pada langkah pertama tiap iterasi dan sebelum TC-GS-HHR-459 (kemampuan "pulihkan Seed Reader A lewat fixture backend" disediakan tim FE/BE, tanpa endpoint yang dikarang), lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Tabel "Kasus Mark as berhasil" (parameter langkah 1 sampai 11):

| TC | Reader | Device Name | Status awal | Aksi | Toast sukses | Status baru | Row action sesudah (urut) | Tidak tampil |
|---|---|---|---|---|---|---|---|---|
| TC-GS-HHR-139 | DD-01 | `Zebra RFID Reader - 1` | `Available` | `Mark as Damaged` | "Success, Zebra RFID Reader - 1 has been marked as damaged." | `Damaged` | `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Available`, `Delete` | `Mark as Damaged`, `Mark as Missing` |
| TC-GS-HHR-141 | DD-01 | `Zebra RFID Reader - 1` | `Available` | `Mark as Missing` | "Success, Zebra RFID Reader - 1 has been marked as missing." | `Missing` | `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Available`, `Delete` | `Mark as Damaged`, `Mark as Missing` |
| TC-GS-HHR-143 | DD-03 | `Zebra Mobile Reader - 1` | `Damaged` | `Mark as Available` | "Success, Zebra Mobile Reader - 1 has been marked as available." | `Available` | `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`, `Delete` | `Mark as Available` |
| TC-GS-HHR-145 | DD-04 | `Gudang Reader - 2` | `Missing` | `Mark as Available` | "Success, Gudang Reader - 2 has been marked as available." | `Available` | `Detail`, `Edit Alias Name`, `Mark as Damaged`, `Mark as Missing`, `Delete` | `Edit Reader Power` (khusus `Long Range`), `Mark as Available` |

- Kemampuan teknis: klik ganda cepat pada `[Mark as Damaged]` (TC-GS-HHR-459); pembacaan Overlay row action, kartu kuota, dan Modal Changelog (jumlah entri dan isi entri); pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain status Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-139, 141, 143, 145: Mark as berhasil mengubah status

Untuk setiap baris tabel "Kasus Mark as berhasil" (langkah 1 sampai 11):

1. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
2. Buka Overlay row action baris {Reader} (`{Device Name}`, {Status awal})
3. Klik `{Aksi}`
4. Klik `[{Aksi}]` pada dialog
5. Verifikasi muncul toast sukses: "{Toast sukses}"
6. Verifikasi Badge `Status` baris {Reader} menjadi `{Status baru}`
7. Buka kembali Overlay row action baris {Reader} dan amati daftar opsi
8. Verifikasi Overlay memuat aksi berurutan {Row action sesudah}
9. Verifikasi {Tidak tampil} tidak tampil pada Overlay
10. Tutup Overlay dengan klik di luar Overlay
11. Verifikasi kartu kuota tidak berubah: `Short Range` `5 of 8` dan `Long Range` `5 of 6`

### TC-GS-HHR-459: Klik ganda cepat pada konfirmasi Mark as Damaged hanya mengubah status satu kali

12. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
13. Buka ikon Changelog (Modal Changelog), catat jumlah entri sebagai baseline
14. Tutup Modal Changelog dengan `✕`
15. Buka Overlay row action baris DD-01 (`Zebra RFID Reader - 1`, Available)
16. Klik `Mark as Damaged`
17. Klik ganda cepat `[Mark as Damaged]` pada dialog
18. Verifikasi hanya satu toast sukses yang tampil: "Success, Zebra RFID Reader - 1 has been marked as damaged."
19. Verifikasi tidak ada toast `This device was changed by someone else. Please review.`
20. Buka ikon Changelog
21. Verifikasi jumlah entri Changelog bertambah tepat 1 dibanding baseline langkah 13
22. Verifikasi entri baru: Action `Edit`, Field `Status`, Old Value `Available`, New Value `Damaged`, untuk `Zebra RFID Reader - 1 (SKU-HHR-01)`
23. Tutup Modal Changelog dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3d).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 1 sampai 11 diulang empat kali (satu kali per baris tabel "Kasus Mark as berhasil"), sehingga ekspansi spec 44 + 12 = 56 langkah.
- Urutan TC di spec: 139, 141, 143, 145, 459. TC-GS-HHR-139, 141, 459 memakai DD-01 yang berstatus Available pada precondition TC, sehingga Seed Reader A dipulihkan di awal tiap iterasi dan sebelum TC-GS-HHR-459 (tiap TC dalam sumber berdiri atas Seed Reader A yang dipulihkan). Langkah pemulihan pada iterasi pertama tidak mengubah apa pun dan dipertahankan agar iterasi seragam tanpa langkah bersyarat.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 12 (pemulihan dan muat ulang), langkah 7 (membuka kembali Overlay agar Overlay diasersi, sesuai Langkah Uji 4 TC), langkah 10 (menutup Overlay), langkah 13 dan 14 (mencatat baseline Changelog sebelum aksi pemicu; S-12), dan langkah 23 (menutup Modal Changelog).
- Pada TC-GS-HHR-459 langkah 18 dan 19 diletakkan segera sesudah klik ganda dan sebelum membuka Changelog, karena toast adalah state sementara (8b butir 5). Hitungan "satu toast" didahului muat ulang halaman pada langkah 12 sehingga tidak ada toast lama.
- Row action sesudah perubahan (Expected c TC-GS-HHR-139, 141, 143, 145) ditulis sesuai TC: urutan opsi yang tampil dan opsi yang tidak tampil; `Edit Reader Power` khusus Long Range (DD-01 dan DD-03 Long Range, DD-04 Short Range).
- Pengecualian alasan di atas sekitar 35 langkah (ekspansi 56): seluruh blok satu kelas (Mark as tunggal berhasil), tiap blok memakai reader dan pemulihan Seed Reader A sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan langkah 1 sampai 11 hanya diulang per baris data.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Screening dialog Mark as dan row action per status (TC-GS-HHR-138, 140, 142, 144, 146, 148) ada di spec 039.
- Temuan untuk QA:
  - Post Condition TC-GS-HHR-139, 141, 143, dan 145 ("Status = ..." teramati lewat Badge `Status`; "Tiga surface log (TC section 5)" dan "Hardware Stock Jalur A (TC section 7)") tidak punya langkah observasi untuk tiga surface log dan Hardware Stock di TC ini, sehingga tidak diasersi di spec ini.
  - TC-GS-HHR-143 dan 145 berjudul identik ("Mark as Available berhasil mengubah status menjadi Available"); keduanya dibedakan oleh Data Uji (DD-03 versus DD-04), bukan duplikat.
  - TC-GS-HHR-459 Expected b ("satu entri `Edit` `Status` `Available` ke `Damaged` untuk DD-01") tidak menyebut cara menemukan entri di Changelog kumulatif; spec memakai selisih jumlah entri terhadap baseline dan entri baru pada urutan default.
