---
id: TC-AC-ACHS-E2E-208-download-approvals-tab-history-isi-berkas-csv-xlsx
title: "Download Approvals > Hardware Stock Tab History: Isi Berkas XLSX per Tipe Kolom"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-464
coverage:
  web: automated
---

# Download Approvals > Hardware Stock Tab History: Isi Berkas XLSX per Tipe Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini. Baris yang diasersi: Canceled #1 dan #8 (Approver `—`), Approved oleh System #7, dan baris dengan Approver akun Pre-setup #1 (nama singkat `Fixture.hardwareStock.account.p01.totalControl.shortName`).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama singkat akun Total Control Principal #1 | #1 | Total Control Principal; nama depan + inisial belakang seperti tampil di UI | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | Nama lengkap akun Total Control Principal #1 | #1 | Total Control Principal; nama lengkap akun | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #22 Tabel D | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #5 dan #8 berformat MAC dengan awalan yang sama | `Fixture.hardwareStock.p22.d[n].matchedIdentifier` |
  | Approval baris #n (n = 1 sampai 12) | #22 Tabel D | Canceled pada #1, #8; Approved pada #2, #5, #6, #7, #11, #12; Rejected pada #3, #4, #9, #10 | `Fixture.hardwareStock.p22.d[n].approval` |
  | Approver baris #n (n = 1 sampai 12) | #22 Tabel D | `—` pada #1 dan #8 (Canceled); `System` pada #7; nama singkat akun Pre-setup #1 pada #2, #3, #9, #11, akun #2 pada #4, #5, #12, akun #6 pada #6, #10 | `Fixture.hardwareStock.p22.d[n].approver` |
  | Requested At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Requested At tiap baris, format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p22.d[n].requestedAt` |
  | Resolved At baris #n (n = 1 sampai 12) | #22 Tabel D | tanggal Resolved At tiap baris, menurun menurut n (Resolved At terbaru lebih dulu) | `Fixture.hardwareStock.p22.d[n].resolvedAt` |
- Format tanggal dan jam General Settings: bawaan environment, tidak diubah spec; Requested At dan Resolved At di berkas dibandingkan dengan nilai yang tampil di tabel.
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser dan membaca isi berkas XLSX per sel (nilai, tipe sel, pengisian warna sel).
- State global: tidak ada yang diubah. Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`
3. Klik icon Download
4. Pilih `Download as XLSX`
5. Buka berkas XLSX dan bandingkan dengan tabel di layar
6. Verifikasi kolom Type dan Approval ditulis label teks (`Approved`, `Rejected`, `Canceled`) tanpa warna badge
7. Verifikasi kolom Approver pada baris Canceled (#1, #8) ditulis `-` untuk `—`
8. Verifikasi kolom Approver pada baris #7 ditulis `System`
9. Verifikasi kolom Requested At dan Resolved At mengikuti format tanggal dan jam General Settings
10. Verifikasi kolom Approver ditulis nama lengkap user (nama singkat `Fixture.hardwareStock.account.p01.totalControl.shortName` ditulis `Fixture.hardwareStock.account.p01.totalControl.fullName`), bukan format singkat

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-464). Tidak ada TC hanya-BE di spec ini. Kelas binary buffer (prinsip 13f): nilai sel dan tipe sel berkas dipisah dari nama berkas, kolom, dan jumlah baris yang ada di spec 207.
- Temuan untuk QA:
  - TC-464 judul menyebut CSV dan XLSX, tetapi langkah dan Expected hanya memakai XLSX; spec mengikuti langkah TC.
  - Butir a ("tanpa warna badge") tidak menyebut cara mengamati pada berkas; spec membaca pengisian warna sel.
  - Nama lengkap user selain akun Pre-setup #1 tidak ada di Pre-setup TC; spec hanya mengasersi nama lengkap yang tercantum.
  - Populasi Pre-setup #22 dirujuk lewat nomor baris Tabel D (`#n` = `Fixture.hardwareStock.p22.d[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nama literal Pre-setup di spec dan tanpa pengecualian S-12. Literal yang tetap ada adalah teks UI nyata (placeholder, nilai Type, Approval, Category, `System`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
