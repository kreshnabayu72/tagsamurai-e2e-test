---
id: TC-AC-ACHS-E2E-138-download-tab-available-isi-berkas-csv-xlsx
title: "Download Stock Detail Tab Available: Isi Berkas XLSX (Transformasi Sel per Tipe Kolom)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-314
coverage:
  web: automated
---

# Download Stock Detail Tab Available: Isi Berkas XLSX (Transformasi Sel per Tipe Kolom)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | Device Name unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | Registered At unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered At unit 10 Tabel E (#17), format General Settings #15 | `Fixture.hardwareStock.p17.e[10].registeredAt` |
  | Registered By unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered By unit 10 Tabel E (#17); pendaftar yang sama untuk unit 13, 16, 19, 22, 25 | `Fixture.hardwareStock.p17.e[10].registeredBy` |
  | Device Name unit 12 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 12, Tabel E (#17) | `Fixture.hardwareStock.p17.e[12].deviceName` |
  | Registered By unit 12 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered By unit 12 Tabel E (#17); pendaftar yang sama untuk unit 15, 18, 21, 24, 27 | `Fixture.hardwareStock.p17.e[12].registeredBy` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | Serial Number unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Serial Number unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].serialNumber` |
  | Nilai turunan registeredByU12FullName | turunan dari `Fixture.hardwareStock.p17.e[12].registeredBy` | nama lengkap pendaftar unit 12 menurut Expected TC-AC-ACHS-314 (`Budi Santoso`; sumber nama lengkap dicatat di Temuan untuk QA) | `Fixture.hardwareStock.derived.registeredByU12FullName` |
- Kemampuan teknis (disediakan tim FE): membaca isi berkas CSV dan XLSX yang terunduh (jumlah baris, header kolom, isi sel) dari lokasi unduhan unik per langkah unduh sehingga nama berkas yang sama tidak bertabrakan.
- Baris contoh (Pre-setup #17, Tabel E): `Fixture.hardwareStock.p17.e[28].deviceName` (Serial Number `Fixture.hardwareStock.p17.e[28].serialNumber`, Status `Waiting for Approval`, Current Power `—`) untuk Status dan Current Power kosong; `Fixture.hardwareStock.p17.e[10].deviceName` (Status `Available`, Registered By `Fixture.hardwareStock.p17.e[10].registeredBy`, Registered At `Fixture.hardwareStock.p17.e[10].registeredAt`, Min Power `-20 dBm`, Max Power `30 dBm`, Current Power `21 dBm`) untuk tanggal, angka, dan Registered By; `Fixture.hardwareStock.p17.e[12].deviceName` (Registered By `Fixture.hardwareStock.p17.e[12].registeredBy`) untuk nama lengkap. Nama lengkap `Fixture.hardwareStock.p17.e[12].registeredBy` adalah `Fixture.hardwareStock.derived.registeredByU12FullName` menurut TC.
- State global yang diubah: tidak ada.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif
3. Klik icon Download, pilih `Download as XLSX`
4. Buka berkas XLSX dan bandingkan dengan tabel di layar
5. Verifikasi Status baris `Fixture.hardwareStock.p17.e[10].deviceName` ditulis label teks `Available` tanpa warna badge
6. Verifikasi Status baris `Fixture.hardwareStock.p17.e[28].deviceName` ditulis label teks `Waiting for Approval` tanpa warna badge
7. Verifikasi Registered At baris `Fixture.hardwareStock.p17.e[10].deviceName` mengikuti format tanggal dan jam General Settings (`Fixture.hardwareStock.p17.e[10].registeredAt`)
8. Verifikasi Min Power, Max Power, dan Current Power baris `Fixture.hardwareStock.p17.e[10].deviceName` ditulis angka asli tanpa satuan (`-20`, `30`, `21`)
9. Verifikasi Current Power baris `Fixture.hardwareStock.p17.e[28].deviceName` yang gagal terbaca (`—` di tabel) ditulis `-`
10. Verifikasi Registered By baris `Fixture.hardwareStock.p17.e[12].deviceName` ditulis nama lengkap `Fixture.hardwareStock.derived.registeredByU12FullName`, bukan format singkat `Fixture.hardwareStock.p17.e[12].registeredBy`

## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini. Spec kelas binary buffer (bagian 3 prinsip 13f): nilai sel dan tipe sel dipisah dari nama berkas dan kolom yang diasersi di spec lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif" dan pembukaan berkas (membaca isi lewat kemampuan pembaca XLSX).
- Spec memiliki 10 langkah dan tidak melewati smell 35 langkah.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-314 Expected a sampai d tidak menyebut baris contoh; spec memilih `Fixture.hardwareStock.p17.e[10].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName`, dan `Fixture.hardwareStock.p17.e[28].deviceName` dari Tabel E (pilihan spec).
  - TC-AC-ACHS-314 Expected d menulis Registered By `Fixture.hardwareStock.p17.e[12].registeredBy` sebagai `Fixture.hardwareStock.derived.registeredByU12FullName` (nama lengkap), sedangkan NC-14 dalam TC menyatakan ketidakpastian format nama pada berkas; spec mengikuti Expected TC. Nama lengkap `Fixture.hardwareStock.derived.registeredByU12FullName` hanya tertulis di Pre-setup #10 untuk akun Distributor, bukan sebagai Registered By unit; sumber nama lengkap perlu dikonfirmasi QA.
  - TC-AC-ACHS-314 tidak menyebut cara membaca berkas XLSX; dicatat sebagai kemampuan pembaca XLSX yang disediakan tim FE.
