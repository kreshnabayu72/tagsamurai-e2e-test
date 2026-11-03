---
id: TC-AC-ACHS-E2E-228-download-popup-event-log-isi-berkas-csv-xlsx
title: "Download Popup Event Log: Isi Berkas XLSX per Tipe Kolom"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-512
coverage:
  web: automated
---

# Download Popup Event Log: Isi Berkas XLSX per Tipe Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki tepat 12 sesi Event Log; baseline read-only yang tidak diubah spec ini. Baris yang diasersi: sesi Add Stock (Activity `Add Stock`), sesi Delete Stock dengan Success `1` dan Waiting for Approval `—`, serta sesi user Distributor Pre-setup #11 (nama lengkap `Fixture.hardwareStock.account.p11.distributorMitra.fullName`). Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
  | Date baris #n (n = 1 sampai 12) | #20 Tabel B | identitas baris hasil; urutan default Date terbaru lebih dulu; format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p20.b[n].date` |
  | Waiting for Approval baris #n (n = 1 sampai 12) | #20 Tabel B | jumlah unit Waiting for Approval tiap sesi; `—` pada baris Delete Stock (#1, #5, #9) | `Fixture.hardwareStock.p20.b[n].waitingForApproval` |
  | Nama singkat akun user Distributor #11 | #11 | user Distributor; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
  | Nama lengkap akun user Distributor #11 | #11 | user Distributor; nama lengkap akun | `Fixture.hardwareStock.account.p11.distributorMitra.fullName` |
- Format tanggal dan jam General Settings: bawaan environment, tidak diubah spec; kolom Date di berkas dibandingkan dengan nilai yang tampil di tabel.
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser dan membaca isi berkas XLSX per sel (nilai dan tipe sel).
- State global: tidak ada yang diubah. Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab `Available` aktif
3. Klik icon `[Event Log]` di toolbar
4. Klik icon Download
5. Pilih `Download as XLSX`
6. Buka berkas XLSX dan bandingkan dengan tabel di layar
7. Verifikasi kolom Date mengikuti format tanggal dan jam General Settings
8. Verifikasi kolom Activity ditulis teks `Add Stock` atau `Delete Stock`
9. Verifikasi kolom Success dan Waiting for Approval ditulis angka asli
10. Verifikasi sel `—` pada baris Delete Stock ditulis `-`
11. Verifikasi kolom Modified By ditulis nama lengkap user (nama singkat `Fixture.hardwareStock.account.p11.distributorMitra.shortName` ditulis `Fixture.hardwareStock.account.p11.distributorMitra.fullName`), bukan format singkat

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-512). Tidak ada TC hanya-BE di spec ini. Kelas binary buffer (prinsip 13f): nilai sel dan tipe sel berkas dipisah dari nama berkas, kolom, dan jumlah baris yang ada di spec 227.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite).
- Temuan untuk QA:
  - TC-512 butir c merujuk sel `—` pada baris Delete Stock tanpa menyebut kolomnya; pada Tabel B sel `—` ada di kolom Waiting for Approval, dan spec mengasersi isi sel `-` pada kolom itu.
  - Nama lengkap user selain user Pre-setup #11 tidak ada di Pre-setup TC; spec hanya mengasersi nama lengkap yang tercantum.
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Total 12 sesi hanya berlaku sebelum spec lain menambah sesi pada SKU ini (audit trail permanen, lihat suite.md). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
