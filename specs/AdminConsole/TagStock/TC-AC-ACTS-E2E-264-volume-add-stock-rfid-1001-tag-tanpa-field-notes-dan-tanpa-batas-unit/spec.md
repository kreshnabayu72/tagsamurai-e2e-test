---
id: TC-AC-ACTS-E2E-264-volume-add-stock-rfid-1001-tag-tanpa-field-notes-dan-tanpa-batas-unit
title: "Volume Add Stock RFID 1.001 TAG dalam Satu Sesi Scan: Tanpa Field Notes dan Tanpa Batas Jumlah Unit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-732
coverage:
  web: automated
---

# Volume Add Stock RFID 1.001 TAG dalam Satu Sesi Scan: Tanpa Field Notes dan Tanpa Batas Jumlah Unit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data Pre-setup (dibaca saja): SKU `Fixture.tagStock.skuRfid` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Data volume (kelas e): 1.001 TAG RFID unik (EPC dan UID berbeda, belum terdaftar) dari `Fixture.tagStock.volume1001`, dibangkitkan simulator reader RFID dalam satu sesi scan, bukan seeding. Seluruh unit hasil Submit dihapus fixture BE di hook `after` sehingga SKU Pre-setup kembali ke jumlah unit awal.
- Kemampuan teknis: simulator pemindai RFID (scan banyak TAG dalam satu sesi) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec), pembacaan state BE yang tidak terlihat di UI, dan sesi API aktor, disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`); simulator reader bersama.

## Test Steps

1. Catat baseline: Total Registered SKU `Fixture.tagStock.skuRfid` (lewat kemampuan baca BE)
2. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
3. Klik (⋯) baris SKU `Fixture.tagStock.skuRfid`, klik `Add Stock`
4. Verifikasi tidak ada field Notes di halaman Idle
5. Klik `[Add by Scan]`
6. Scan 1.001 TAG unik (EPC dan UID berbeda) dari fixture "TAG volume" lewat simulator reader RFID
7. Klik `[Stop]`
8. Verifikasi Scanned TAG List memuat 1.001 baris tanpa pesan batas jumlah unit
9. Verifikasi counter widget menampilkan `[N] TAGs scanned` dengan N = 1.001
10. Klik `[Submit]`
11. Verifikasi toast sukses `Success, TAG has been registered.`
12. Klik icon `[Event Log]` di toolbar Tab Available pada halaman Detail SKU `Fixture.tagStock.skuRfid` (Tab Add Stock)
13. Verifikasi sesi Add Stock terbaru di Event Log memuat Success `1.001`
14. Tutup modal Event Log dengan klik (X)
15. Verifikasi Total Registered SKU `Fixture.tagStock.skuRfid` bertambah 1.001 dari baseline langkah 1

## Notes

- Spec ini kelas e (volume 1.001 unit dalam satu sesi scan, di atas ambang 100 baris). Simulator reader RFID hanya membangkitkan volume sebagai pembentuk state (precondition); objek uji adalah halaman Add Stock yang tanpa field Notes dan tanpa batas jumlah unit, bukan perangkat scan.
- TC-AC-ACTS-732 ada di spec ini; spec 056 memuat TC Add Stock RFID lainnya.
- Langkah penghubung (S-03): langkah 1 (mencatat baseline Total Registered sebelum scan, S-12), langkah 2 dan 3 (Search SKU untuk menemukan baris target, R-16, dan membuka halaman Add Stock), langkah 5 sampai 7 (sesi scan), langkah 12 (membuka modal Event Log), dan langkah 14 (menutup modal Event Log, S-09).
- Asersi tambahan di luar Expected TC (S-03): langkah 15 (Total Registered bertambah 1.001) mengonfirmasi unit tercatat sejumlah Success `1.001` di Event Log (Expected c) dengan baseline langkah 1; langkah 9 (counter) adalah Expected b TC.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun perlu dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-732 langkah 4 menyebut membuka Detail SKU > `[Event Log]` (Tab Add Stock) tanpa menyebut cara; spec memakai icon `[Event Log]` di toolbar Tab Available setelah Submit sukses kembali ke Detail SKU. Format angka `1.001` di counter widget mengikuti TC.
