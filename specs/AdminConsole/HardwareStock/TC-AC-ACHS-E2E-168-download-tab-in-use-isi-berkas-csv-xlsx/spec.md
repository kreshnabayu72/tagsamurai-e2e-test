---
id: TC-AC-ACHS-E2E-168-download-tab-in-use-isi-berkas-csv-xlsx
title: "Download Tab In Use Isi Berkas XLSX Transformasi Sel"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-366
coverage:
  web: automated
---

# Download Tab In Use Isi Berkas XLSX Transformasi Sel

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` dengan 7 unit In Use (Pre-setup #18, Tabel F TC); baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya. Status unit 1 sampai 7: Damaged, Active, Missing, Active, Active, Damaged, Active (label UI). Pendaftar baris 3 dan 6 sama (`Fixture.hardwareStock.p18.f[3].registeredBy`, format singkat); nama lengkapnya adalah nama tampil akun Pre-setup #1 (`Fixture.hardwareStock.account.p01.totalControl.fullName`). Min Power dan Max Power sama pada seluruh unit (`Fixture.hardwareStock.p18.f[1].minPower`, `Fixture.hardwareStock.p18.f[1].maxPower`), Current Power berbeda per unit (`Fixture.hardwareStock.p18.f[n].currentPower`).
- Format tanggal dan jam: pengaturan General Settings akun aktor (dibaca lewat kemampuan baca state, disediakan tim FE/BE); sel Registered At dan Activated At di berkas dibandingkan dengan teks sel yang sama di layar.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan di browser dan membaca isi sel berkas XLSX (nilai sel dan tipe sel).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Max Power baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Max Power unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].maxPower` |
  | Min Power baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Min Power unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].minPower` |
  | Registered By baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 3, Tabel F (#18) | `Fixture.hardwareStock.p18.f[3].registeredBy` |

## Test Steps

### Transformasi isi sel per tipe kolom (TC-AC-ACHS-366)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Klik icon Download, pilih `Download as XLSX`
4. Buka berkas XLSX terunduh
5. Verifikasi kolom Status ditulis label teks `Active`, `Damaged`, atau `Missing` tanpa warna badge
6. Verifikasi kolom Registered At dan Activated At mengikuti format tanggal dan jam General Settings, sama dengan teks sel di layar
7. Verifikasi kolom Min Power, Max Power, dan Current Power ditulis angka asli tanpa satuan
8. Verifikasi kolom Registered By ditulis nama lengkap user (nilai format singkat `Fixture.hardwareStock.p18.f[3].registeredBy` ditulis `Fixture.hardwareStock.account.p01.totalControl.fullName`), bukan format singkat

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-366). Tidak ada TC hanya-BE di spec ini.
- Kelas f (binary buffer): isi sel berkas XLSX (nilai dan tipe sel) dipisah dari spec fungsional download (spec 167).
- Langkah 4 (membuka berkas lewat kemampuan baca berkas) adalah langkah penghubung dari langkah 5 TC.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state, label Status) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-366 Expected b ("mengikuti format tanggal dan jam General Settings") tidak menyebut format konkret; spec membandingkan dengan teks sel di layar.
  - TC-366 tidak menyebut tipe sel tanggal di XLSX (teks atau tanggal Excel); spec tidak mengasersi tipe tersebut.
