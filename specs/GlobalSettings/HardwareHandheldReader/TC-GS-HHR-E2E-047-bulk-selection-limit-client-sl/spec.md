---
id: TC-GS-HHR-E2E-047-bulk-selection-limit-client-sl
title: "Selection Limit Bulk Reader Client SL: Checkbox ke-(Limit+1) Disabled dan Select All Dipotong ke Limit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-221
  - TC-GS-HHR-222
coverage:
  web: automated
---

# Selection Limit Bulk Reader Client SL: Checkbox ke-(Limit+1) Disabled dan Select All Dipotong ke Limit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini tidak mengubah data reader: seleksi dikosongkan lewat ikon `×`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka.
- Akun aktor: Total Control Client SL. Email mengikuti pola Pre-setup TC `totalControl_automated_{namaClient}@qwertysystem.net` dengan `{namaClient}` = Client SL; email persisnya disediakan tim FE. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTSL_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (kondisi Client SL dari Tabel Data Uji Pre-setup TC; fixture baru `Fixture.hardwareHandheldReader.clientSL`): 12 reader berstatus Available; `Selection Limit` System Limits Client SL diubah menjadi 5. Kondisi ini disediakan tim FE sebagai Pre-setup dan tidak diubah spec ini; aktor dan mekanisme pengubahan Selection Limit tidak disebut TC, PRD, atau LLD (lihat Temuan untuk QA). Rows per page default 10 sehingga baris keenam berada di halaman 1.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor (Client SL) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover pada checkbox disabled dan pembacaan tooltip; pembacaan state checkbox, teks Bulk Action Bar, tombol `Bulk Action`, dan toast error.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-221: Seleksi manual berhenti pada Selection Limit dengan checkbox tambahan disabled

1. Centang lima baris pertama tabel satu per satu
2. Verifikasi counter `5 Readers selected`
3. Arahkan kursor ke checkbox baris keenam
4. Verifikasi checkbox baris keenam disabled dengan tooltip `You've reached the maximum selection of 5 rows.`
5. Klik checkbox baris keenam
6. Verifikasi baris keenam tidak tercentang
7. Verifikasi counter tetap `5 Readers selected`
8. Verifikasi Bulk Action Bar tetap tampil
9. Verifikasi tombol `Bulk Action` aktif untuk lima baris terpilih
10. Klik ikon `×`

### TC-GS-HHR-222: Select All melebihi Selection Limit memotong seleksi ke limit dan menampilkan toast error

11. Klik tombol `Select All (12 records)`
12. Verifikasi muncul toast error: "Error, only the first 5 of 12 rows were selected. Narrow your filter to include the rest."
13. Verifikasi seleksi dipotong menjadi 5 baris pertama
14. Verifikasi counter `5 Readers selected`
15. Verifikasi Bulk Action Bar tetap tampil
16. Verifikasi tombol `Bulk Action` aktif untuk lima baris terpilih
17. Klik ikon `×`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k). Kelas e (volume data: batas Selection Limit), berdiri sebagai spec sendiri sesuai prinsip 12.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: 221, 222. Seleksi dikosongkan lewat `×` antar-TC (langkah 10 dan 17).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 dan 17 (mengosongkan seleksi lewat `×`).
- Pada TC-GS-HHR-222 langkah 12 (toast error) diletakkan segera sesudah klik `Select All` karena toast adalah state sementara; urutan ini menyimpang dari urutan Expected TC (a lalu b).
- Langkah 2, 6, 7, 13, dan 14 hanya mengasersi keadaan checkbox atau counter sehingga tidak butuh baris pembanding (8b butir 2). Langkah 6 adalah klausa b Expected TC-GS-HHR-221 ("Klik pada checkbox disabled tidak menambah seleksi") dan langkah 7 klausa counter tetap.
- Temuan untuk QA:
  - Precondition TC-GS-HHR-221 dan 222 ("`Selection Limit` System Limits Client SL diubah menjadi 5") tidak menyebut aktor atau mekanisme pengubahan; Pre-setup TC memasukkan kondisi itu sebagai kondisi Client SL. Spec menuliskannya sebagai kondisi Pre-setup yang disediakan tim FE tanpa mengarang akun atau endpoint (S-13).
  - Email akun Total Control Client SL tidak tertulis di Pre-setup TC (hanya pola `totalControl_automated_{namaClient}@qwertysystem.net`) dan env var passwordnya belum terdaftar di `spectra.config.ts` maupun `.env.example`; spec memakai `GS_CLIENTSL_TC_PASSWORD` (env baru).
  - TC-GS-HHR-221 langkah 1 tidak menyebut baris mana yang dicentang selain "lima baris pertama"; spec memakai lima baris pertama pada urutan default.
  - TC-GS-HHR-222 Expected a ("5 baris pertama") tidak menyebut urutan; spec mengasersi lima baris pertama tabel pada urutan default.
  - TC-GS-HHR-221 dan 222 tidak mencantumkan Post Condition.
