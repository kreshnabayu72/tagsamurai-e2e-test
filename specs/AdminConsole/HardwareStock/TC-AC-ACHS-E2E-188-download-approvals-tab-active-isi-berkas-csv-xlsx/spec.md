---
id: TC-AC-ACHS-E2E-188-download-approvals-tab-active-isi-berkas-csv-xlsx
title: "Download Approvals Tab Active Isi Berkas XLSX Transformasi Sel"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-414
coverage:
  web: automated
---

# Download Approvals Tab Active Isi Berkas XLSX Transformasi Sel

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Baris dirujuk lewat nomor baris Tabel C: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel C (`Fixture.hardwareStock.p21.c[n]`). Urutan default FIFO (Requested At terlama di atas) sama dengan urutan Tabel C (#1 teratas, #12 terbawah). Nilai sel tidak ditulis di spec ini; penulis script membaca nilainya dari fixture lewat kunci pada tabel Parameter Pre-setup (R-06).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #21 Tabel C | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
  | Device Name (SKU) baris #n (n = 1 sampai 12) | #21 Tabel C | Device Name diikuti kode SKU dalam kurung; #9 adalah Subject BYO tanpa SKU (Device Name (SKU) tanpa kode SKU, Category `—`) | `Fixture.hardwareStock.p21.c[n].deviceName` |
  | Category baris #n (n = 1 sampai 12) | #21 Tabel C | Long Range pada #1 dan #10; Short Range pada #2, #3, #5, #6, #7, #8, #11; Smart Fixed Reader pada #4; BLE Gateway pada #12; `—` pada #9 | `Fixture.hardwareStock.p21.c[n].category` |
  | Requested At baris #n (n = 1 sampai 12) | #21 Tabel C | naik menurut n (FIFO); bulan dan tahun sama pada seluruh baris | `Fixture.hardwareStock.p21.c[n].requestedAt` |
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan di browser dan membaca isi sel berkas XLSX (nilai sel dan tipe sel).
- Format tanggal dan jam: pengaturan General Settings akun aktor (dibaca lewat kemampuan baca state, disediakan tim FE/BE); sel Requested At di berkas dibandingkan dengan teks sel yang sama di layar.
- Subject BYO tanpa SKU: baris Matched Identifier #9 (Device Name (SKU) tanpa kode SKU, Category `—`, Pre-setup #21).

## Test Steps

### Transformasi isi sel per tipe kolom (TC-AC-ACHS-414)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Klik icon Download, pilih `Download as XLSX`
4. Buka berkas XLSX terunduh
5. Verifikasi kolom Type ditulis label teks (`Activation Collision` atau `Register Duplicate`) tanpa warna badge
6. Verifikasi sel Device Name (SKU) dan Category pada baris Matched Identifier #9 (Subject BYO tanpa SKU, bernilai `—` di layar) ditulis `-`
7. Verifikasi kolom Requested At mengikuti format tanggal dan jam General Settings, sama dengan teks sel di layar

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-414). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Kelas f (binary buffer): isi sel berkas XLSX (nilai dan tipe sel) dipisah dari spec fungsional download (spec 187).
- Langkah 2 (klik Tab `Active`) dan langkah 4 (membuka berkas lewat kemampuan baca berkas) adalah langkah penghubung dari langkah 2 dan 4 TC.
- Temuan untuk QA:
  - TC-414 Expected b menyebut Device Name (SKU) dan Category bernilai `—` untuk Subject BYO tanpa SKU; pada Tabel C hanya satu baris (Matched Identifier #9) yang demikian, sedangkan Device Name (SKU) tampil sebagai nama tanpa kode SKU (bukan `—` saja) dan opsi Filter Category TC-377 tidak memuat `—`; spec mengikuti TC pada baris itu.
  - TC-414 Expected c tidak menyebut format konkret; spec membandingkan dengan teks sel di layar.
  - TC-414 tidak menyebut tipe sel tanggal di XLSX; spec tidak mengasersi tipe tersebut.
