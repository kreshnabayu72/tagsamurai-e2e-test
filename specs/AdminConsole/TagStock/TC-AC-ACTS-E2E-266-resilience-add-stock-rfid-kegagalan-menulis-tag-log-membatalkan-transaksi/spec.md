---
id: TC-AC-ACTS-E2E-266-resilience-add-stock-rfid-kegagalan-menulis-tag-log-membatalkan-transaksi
title: "Resilience Add Stock RFID: Kegagalan Menulis Entri TAG Log Membatalkan Transaksi Kejadiannya"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-981
coverage:
  web: automated
---

# Resilience Add Stock RFID: Kegagalan Menulis Entri TAG Log Membatalkan Transaksi Kejadiannya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data Pre-setup (dibaca saja): SKU `Fixture.tagStock.skuRfid` (Pre-setup #12). Dua TAG RFID unik yang belum terdaftar (`Fixture.tagStock.rfidFail1` dan `Fixture.tagStock.rfidFail2`, EPC dan UID ditetapkan fixture) dibangkitkan simulator reader RFID; transaksi dibatalkan sehingga keduanya tetap belum terdaftar.
- Kemampuan teknis: injeksi kegagalan penulisan TAG Log di sisi server (dan pelepasannya) lewat fixture BE, disediakan tim FE/BE tanpa endpoint karangan; hook `after` melepas kegagalan itu bila spec berhenti sebelum langkah 9.
- Kemampuan teknis: simulator pemindai RFID (`[Add by Scan]`, scan, `[Stop]`) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec. Kemampuan baca BE untuk jumlah unit Available SKU dan jumlah baris Event Log SKU disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec), pembacaan state BE yang tidak terlihat di UI, dan sesi API aktor, disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`); simulator reader bersama.

## Test Steps

1. Catat baseline: jumlah unit Available SKU `Fixture.tagStock.skuRfid` dan jumlah baris Event Log Tab Add Stock SKU itu (lewat kemampuan baca BE)
2. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
3. Klik (⋯) baris SKU `Fixture.tagStock.skuRfid`, klik `Add Stock`
4. Atur penulisan TAG Log gagal di sisi server (fixture BE)

### TC-AC-ACTS-981: Kegagalan menulis entri TAG Log membatalkan transaksi kejadiannya

5. Klik `[Add by Scan]`, scan dua TAG RFID unik (`Fixture.tagStock.rfidFail1` dan `Fixture.tagStock.rfidFail2`) lewat simulator reader RFID, klik `[Stop]`
6. Klik `[Submit]`
7. Verifikasi toast error "Error, failed to register TAGs."
8. Verifikasi tidak ada unit, receipt, atau entri log yang tersimpan (jumlah unit Available SKU dan jumlah baris Event Log SKU sama dengan baseline)
9. Lepas kegagalan penulisan TAG Log (fixture BE)

## Notes

- Spec resilience kelas b (kegagalan penulisan TAG Log yang dipaksa di sisi server pada backend nyata, mode FE+BE) dengan simulator reader RFID kelas d.
- P-5 butir (b): TC-AC-ACTS-981 adalah satu-satunya TC objek-uji ringan kelas b di spec ini (satu kegagalan yang dipaksa, tanpa harness eksternal sendiri); objek ujinya rollback transaksi Add Stock, bukan perangkat scan.
- Simulator reader RFID hanya membentuk state sebelum Submit (precondition) dan bukan objek uji. Spec ini adalah spec resilience kelas b untuk TC-AC-ACTS-981, sehingga tidak memakai `P-9` (ketahanan terhadap kegagalan tulis masuk spec resilience menurut konvensi); spec hanya memuat satu blok.
- Langkah penghubung (S-03): langkah 1 (baseline sebelum aksi, S-12), langkah 2 dan 3 (Search SKU untuk menemukan baris target, R-16, dan membuka halaman Add Stock), langkah 4 (menyetel kegagalan penulisan TAG Log), dan langkah 9 (melepas kegagalan, S-09).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun perlu dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-981 menyebut toast `T-03` sebagai kode pesan; spec memakai teks "Error, failed to register TAGs." dari PRD bagian 7. TC tidak menyebut cara membaca "receipt"; spec memakai kemampuan baca BE.
  - TC-AC-ACTS-981 Precondition b menyebut halaman Add Stock dibuka dari Stock List > Add Stock; spec membuka lewat row action `Add Stock` setelah baseline.
