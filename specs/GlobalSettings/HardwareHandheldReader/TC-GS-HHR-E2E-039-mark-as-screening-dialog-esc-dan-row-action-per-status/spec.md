---
id: TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status
title: "Mark as Damaged, Missing, dan Available: Screening Dialog, Cancel, Esc, dan Row Action per Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-138
  - TC-GS-HHR-140
  - TC-GS-HHR-142
  - TC-GS-HHR-144
  - TC-GS-HHR-146
  - TC-GS-HHR-148
coverage:
  web: automated
---

# Mark as Damaged, Missing, dan Available: Screening Dialog, Cancel, Esc, dan Row Action per Status

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini tidak mengubah data: seluruh dialog ditutup lewat `[Cancel]` atau `Esc`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend; dibaca saja, tidak diubah spec ini): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), 10 reader DD-01 s.d. DD-10, plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, Long Range, Available), DD-03 (`Zebra Mobile Reader - 1`, Long Range, Damaged), dan DD-04 (`Gudang Reader - 2`, Short Range, Missing). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR); pemulihan Seed Reader A oleh fixture backend disediakan tim FE/BE (lihat Temuan untuk QA).
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Tabel "Kasus dialog Mark as" (parameter langkah 11 sampai 17):

| TC | Reader | Device Name | Status awal | Aksi (Judul dialog) | Kalimat penutup Body |
|---|---|---|---|---|---|
| TC-GS-HHR-138 | DD-01 | `Zebra RFID Reader - 1` | `Available` | `Mark as Damaged` | `Are you sure you want to mark it as damaged?` |
| TC-GS-HHR-140 | DD-01 | `Zebra RFID Reader - 1` | `Available` | `Mark as Missing` | `Are you sure you want to mark it as missing?` |
| TC-GS-HHR-142 | DD-03 | `Zebra Mobile Reader - 1` | `Damaged` | `Mark as Available` | `Are you sure you want to mark it as available?` |
| TC-GS-HHR-144 | DD-04 | `Gudang Reader - 2` | `Missing` | `Mark as Available` | `Are you sure you want to mark it as available?` |

- Kemampuan teknis: pembacaan Overlay row action beserta urutan dan severity item; penekanan tombol `Esc`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-148: Row action per status, Damaged dan Missing tidak menawarkan transisi langsung antar keduanya

1. Buka Overlay row action baris DD-03 (`Zebra Mobile Reader - 1`, Damaged)
2. Verifikasi Overlay memuat aksi berurutan `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Available`, `Delete`
3. Verifikasi Overlay tidak memuat `Mark as Missing`
4. Verifikasi urutan aksi: aksi severity dark lebih dulu, lalu danger (`Delete`)
5. Tutup Overlay dengan klik di luar Overlay
6. Buka Overlay row action baris DD-04 (`Gudang Reader - 2`, Missing)
7. Verifikasi Overlay memuat aksi berurutan `Detail`, `Edit Alias Name`, `Mark as Available`, `Delete`
8. Verifikasi Overlay tidak memuat `Mark as Damaged`
9. Verifikasi urutan aksi: aksi severity dark lebih dulu, lalu danger (`Delete`)
10. Tutup Overlay dengan klik di luar Overlay

### TC-GS-HHR-138, 140, 142, 144: Screening dialog Mark as dan Cancel tidak mengubah status

Untuk setiap baris tabel "Kasus dialog Mark as" (langkah 11 sampai 17):

11. Buka Overlay row action baris {Reader}
12. Klik `{Aksi}`
13. Verifikasi dialog tampil utuh: Judul `{Aksi}`, Body berisi bullet `{Device Name}` lalu `{Kalimat penutup Body}`, Footer `[Cancel]` dan `[{Aksi}]`
14. Klik `[Cancel]`
15. Verifikasi tidak ada toast
16. Verifikasi dialog tertutup
17. Verifikasi `Status` {Reader} tetap `{Status awal}`

### TC-GS-HHR-146: Esc pada dialog Mark as Damaged setara tombol Cancel

18. Buka Overlay row action baris DD-01
19. Klik `Mark as Damaged`
20. Tekan `Esc`
21. Verifikasi tidak ada toast
22. Verifikasi dialog tertutup
23. Verifikasi `Status` DD-01 tetap `Available`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3d).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 11 sampai 17 diulang empat kali (satu kali per baris tabel "Kasus dialog Mark as"), sehingga ekspansi spec 10 + 28 + 6 = 44 langkah.
- Urutan TC di spec: 148, 138, 140, 142, 144, 146. Row action per status (tanpa dialog) dipasang lebih dulu sebagai screening, dialog dengan `[Cancel]` sesudahnya, dan `Esc` terakhir. Menyimpang dari urutan nomor TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 10 (menutup Overlay).
- Pengecualian alasan di atas sekitar 35 langkah (ekspansi 44): seluruh blok satu kelas (screening tanpa perubahan data), memakai reader Seed Reader A yang hanya dibaca, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Langkah 11 sampai 17 hanya diulang per baris data.
- Dialog konfirmasi diasersi utuh dalam satu `Verifikasi` (judul, isi, dan tombol footer) sesuai S-01 untuk dialog konfirmasi satu elemen.
- Mark as Damaged, Missing, dan Available yang berhasil (TC-GS-HHR-139, 141, 143, 145, 459) ada di spec 040.
- Pengecualian S-12 Population Seed Reader A HHR (A-5) berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Temuan untuk QA:
  - TC-GS-HHR-142 dan 144 berjudul identik ("Screening dialog Mark as Available dan Cancel tidak mengubah status"); keduanya dibedakan oleh Data Uji (DD-03 Damaged versus DD-04 Missing), jadi bukan duplikat dan keduanya ditulis sebagai baris tabel. TC-GS-HHR-143 dan 145 (spec 040) berjudul identik pula.
  - TC-GS-HHR-148 Expected b tidak menyebut `Edit Reader Power` untuk DD-04 (Short Range); PRD §4.2d menyatakan `Edit Reader Power` khusus Long Range. Spec mengikuti daftar TC dan tidak mengasersi ketidakhadiran `Edit Reader Power` pada DD-04.
  - TC-GS-HHR-138, 140, 142, 144, dan 146 tidak mencantumkan Post Condition; tidak ada yang tidak diasersi.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-HHR-146 Expected a tidak menyebut cara menutup selain `Esc`; spec mengikuti TC.
