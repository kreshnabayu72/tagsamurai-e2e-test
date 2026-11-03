---
id: TC-AC-ACTS-E2E-194-tab-in-use-state
title: "Detail SKU Tab In Use: State Kosong, Empty-Filtered, Error Load, dan Loading"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-464
  - TC-AC-ACTS-465
  - TC-AC-ACTS-466
  - TC-AC-ACTS-467
coverage:
  web: automated
---

# Detail SKU Tab In Use: State Kosong, Empty-Filtered, Error Load, dan Loading

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan intercept (disediakan tim FE): intercept respons 5xx dan penahan respons (delay jaringan) pada request daftar data Tab In Use, di atas backend nyata; endpoint tidak disebut TC dan tidak dikarang di spec. Intercept dilepas segera setelah dipakai (S-09).
- Data TC-AC-ACTS-464: SKU `RFID-SEAL-DELTA-R1` (Pre-setup #16, SKU tanpa unit) dipakai sebagai "SKU baru tanpa unit In Use".
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-465: Empty-filtered

2. Ketik Search `zzz-tidak-ada`, tekan Enter
3. Verifikasi ilustrasi empty state dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
4. Verifikasi tampilan bukan error
5. Klik `(←)` pada kotak Search

### TC-AC-ACTS-466: Error load fetch gagal bukan empty state

6. Aktifkan intercept respons 5xx pada request daftar data tabel
7. Muat ulang tampilan (F5)
8. Verifikasi copy `Unable to load this data.` dan tombol `[Try Again]` tampil di area tabel
9. Verifikasi tab bar, Summary bar, dan toolbar tetap tampil
10. Verifikasi tampilan bukan empty state
11. Lepas intercept respons 5xx
12. Klik `[Try Again]`
13. Verifikasi tabel memuat ulang data (sedikitnya satu baris tampil)

### TC-AC-ACTS-467: Loading state

14. Aktifkan penahan respons daftar data (delay jaringan)
15. Muat ulang tampilan (F5)
16. Verifikasi komponen loading tampil selama data diambil
17. Lepas penahan respons
18. Verifikasi tabel menggantikan komponen loading

### TC-AC-ACTS-464: Empty state genuine

19. Klik menu sidebar TAG > Stock, klik row action `Detail` pada SKU `RFID-SEAL-DELTA-R1`, klik Tab `In Use`
20. Verifikasi ilustrasi empty state dengan judul `No TAGs in use` dan deskripsi `TAGs currently registered to assets or users will appear here.`
21. Verifikasi tidak ada baris data

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Perubahan urutan TC (S-05): TC-AC-ACTS-465, 466, 467 dikerjakan pada SKU `RFID-ASSET-CORE-R5` dan TC-AC-ACTS-464 di akhir pada SKU `RFID-SEAL-DELTA-R1`, agar perpindahan SKU hanya sekali.
- P-5 (butir b): TC-AC-ACTS-466 adalah objek uji ringan kelas b (satu kegagalan 5xx) pada permukaan yang sama dengan spec ini; intercept 5xx di atas backend nyata dan tidak ada TC kelas b lain di spec ini.
- Langkah penghubung (S-03): klik `(←)` pada kotak Search, melepas intercept dan penahan respons (S-09). Penahan respons pada TC-AC-ACTS-467 hanya untuk mengamati state Loading (bagian 3 prinsip 13b), diasersi sebelum dilepas (bagian 8b butir 5).
- Temuan untuk QA: TC-AC-ACTS-464 langkah 4 "Gunakan SKU baru tanpa unit In Use" bertentangan dengan precondition b (SKU `RFID-ASSET-CORE-R5` memiliki unit In Use); spec memakai SKU Pre-setup #16 (tanpa unit). Endpoint daftar untuk intercept (TC-AC-ACTS-466, 467) tidak disebut TC, PRD, atau LLD.
