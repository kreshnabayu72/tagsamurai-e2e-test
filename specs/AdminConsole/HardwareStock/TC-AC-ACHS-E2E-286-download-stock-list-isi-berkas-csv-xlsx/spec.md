---
id: TC-AC-ACHS-E2E-286-download-stock-list-isi-berkas-csv-xlsx
title: "Download Stock List: Isi Berkas CSV dan XLSX (Transformasi Sel per Tipe Kolom dan Aturan Teknis Berkas)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-255
  - TC-AC-ACHS-261
coverage:
  web: automated
---

# Download Stock List: Isi Berkas CSV dan XLSX (Transformasi Sel per Tipe Kolom dan Aturan Teknis Berkas)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List (lihat `suite.md`).
- Data Pre-setup (read-only): #16 Katalog SKU 30 baris Stock List (Tabel A) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Baris contoh TC-AC-ACHS-255: `Fixture.hardwareStock.p16.a[4].sku` (Type `Handheld Reader`, Brand `Fixture.hardwareStock.p16.a[4].brand`, Model/Type `Fixture.hardwareStock.p16.a[4].modelType`, Total Registered 25, Available 18, In Use 7, Last Updated `Fixture.hardwareStock.p16.a[4].lastUpdated`) dan `Fixture.hardwareStock.p16.a[6].sku` (Range Type `—`, Last Updated `—`).
- Baseline Pre-setup (S-06): spec ini membaca baseline Katalog SKU 30 baris Stock List (Pre-setup #16, Tabel A) beserta hitungan unit dari Pre-setup #17, #18, #19, #24, dan #27 tanpa mengubahnya, sedangkan nomor spec ini sesudah spec penulis (240 sampai 284). Syarat: baseline Pre-setup dipulihkan fixture environment automation ke keadaan awal sebelum spec ini dimulai (`suite.md`, bagian "Urutan jalan" dan "Seeding ulang Pre-setup"); fixture dan skrip pemulihannya disediakan tim FE/BE dan belum ada. Spec ini tidak menumpang hasil spec lain.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

| Parameter | Pre-setup | Peran dan atribut penentu | Kunci fixture |
|---|---|---|---|
| `brand_a1` | #16 (Tabel A baris ke-4) | Brand baris 4 Tabel A (#16): Handheld Reader Long Range; baris yang diasersi pada langkah 4 | `Fixture.hardwareStock.p16.a[4].brand` |
| `updated_a4` | #16 (Tabel A baris ke-4) | Last Updated baris 4 Tabel A (#16), format General Settings #15 | `Fixture.hardwareStock.p16.a[4].lastUpdated` |
| `model_a4` | #16 (Tabel A baris ke-4) | Model/Type baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].modelType` |
| `sku_a4` | #16 (Tabel A baris ke-4) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
| `sku_a6` | #16 (Tabel A baris ke-6) | kode SKU baris 6 Tabel A (#16): Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated kosong) | `Fixture.hardwareStock.p16.a[6].sku` |
| `brand_16e` | #16e (seed sesaat) | Brand SKU seed sesaat 16e (#16) | `Fixture.hardwareStock.p16e.brand` |
| `name_16e` | #16e (seed sesaat) | Device Name SKU 16e (#16): mengandung tanda koma dan tanda kutip ganda | `Fixture.hardwareStock.p16e.deviceName` |
| `sku_16e` | #16e (seed sesaat) | kode SKU seed sesaat 16e (#16): Smart Fixed Reader, dimuat tepat sebelum TC pemakainya dan dihapus setelahnya | `Fixture.hardwareStock.p16e.sku` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email` |

- Data Dinamis (hanya TC-AC-ACHS-261; Pre-setup #16e, dimuat tepat sebelum TC itu dan dihapus setelahnya): SKU `Fixture.hardwareStock.p16e.sku` (Smart Fixed Reader, Brand `Fixture.hardwareStock.p16e.brand`, Device Name `Fixture.hardwareStock.p16e.deviceName`). Penghapusan dilakukan di langkah 22; hook `after` spec ini menghapusnya lewat sesi API bila masih ada.
- Kemampuan teknis (disediakan tim FE): membaca isi berkas CSV mentah (byte BOM, pemisah, escaping) dan XLSX (daftar sheet, tipe dan nilai sel) dari lokasi unduhan unik per langkah unduh; seed dan hapus SKU sementara lewat sesi API aktor (suite.md).
- State global yang diubah: seed dan penghapusan SKU `Fixture.hardwareStock.p16e.sku` (langkah 9 sampai 22) dan sort SKU Ascending yang dipulihkan ke netral. Preferensi kolom tidak diubah.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-255: Transformasi isi sel per tipe kolom

1. Klik icon Download, pilih `Download as XLSX`
2. Buka berkas XLSX dan bandingkan dengan tabel di layar
3. Verifikasi kolom Photo tidak ikut berkas
4. Verifikasi nilai Type, Brand, dan Model/Type baris `Fixture.hardwareStock.p16.a[4].sku` ditulis label teks apa adanya (`Handheld Reader`, `Fixture.hardwareStock.p16.a[4].brand`, `Fixture.hardwareStock.p16.a[4].modelType`) tanpa warna badge
5. Verifikasi nilai Total Registered, Available, dan In Use baris `Fixture.hardwareStock.p16.a[4].sku` ditulis angka asli (sel angka di XLSX: 25, 18, 7)
6. Verifikasi Last Updated baris `Fixture.hardwareStock.p16.a[4].sku` mengikuti format tanggal dan jam General Settings (`Fixture.hardwareStock.p16.a[4].lastUpdated`)
7. Verifikasi Last Updated baris `Fixture.hardwareStock.p16.a[6].sku` ditulis `-`
8. Verifikasi Range Type kosong baris `Fixture.hardwareStock.p16.a[6].sku` ditulis `-`

### TC-AC-ACHS-261: Aturan teknis berkas

9. Muat SKU sementara `Fixture.hardwareStock.p16e.sku` (Pre-setup #16e) lewat seed API, lalu muat ulang halaman Hardware > Stock (F5)
10. Klik header SKU (Ascending)
11. Klik icon Download, pilih `Download as CSV`
12. Buka berkas CSV dengan editor teks
13. Verifikasi CSV berenkode UTF-8 dengan BOM
14. Verifikasi CSV memakai pemisah koma
15. Verifikasi nilai Device Name `Fixture.hardwareStock.p16e.deviceName` dibungkus tanda kutip ganda dan tanda kutip di dalamnya digandakan (`"Reader, ""Pro"""`)
16. Klik icon Download, pilih `Download as XLSX`
17. Buka berkas XLSX
18. Verifikasi XLSX berisi satu sheet bernama `Sheet1`
19. Verifikasi urutan baris berkas CSV mengikuti sort SKU Ascending yang aktif
20. Verifikasi urutan baris berkas XLSX mengikuti sort SKU Ascending yang aktif
21. Klik header SKU dua kali sampai netral
22. Hapus SKU `Fixture.hardwareStock.p16e.sku` lewat sesi API aktor hingga penghapusan tersimpan

## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini. Spec kelas binary buffer (bagian 3 prinsip 13f): nilai sel, BOM, dan tipe sel dipisah dari nama berkas dan kolom yang diasersi di spec lain.
- Urutan TC: TC-AC-ACHS-255 pada baseline 30 baris, lalu TC-AC-ACHS-261 yang menambah SKU sementara dan menghapusnya di akhir spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan berkas (membaca isi lewat kemampuan pembaca CSV dan XLSX), pemulihan sort SKU ke netral, dan penghapusan SKU sementara (langkah 22, hook `after` sebagai cadangan).
- Spec memiliki 22 langkah dan tidak melewati smell 35 langkah.
- Temuan untuk QA:
  - Nomor spec ini (286) sesudah spec penulis (240 sampai 284), padahal spec membaca baseline Pre-setup dan `suite.md` bagian "Urutan jalan" menempatkan spec baca di bawah nomor 240. Spec tidak direnumber; syarat pemulihan baseline ditulis di `## Prerequisites`, dan keputusan penomoran (folder baru di bawah 240) menunggu keputusan di luar spec ini.
  - TC-AC-ACHS-255 Expected a sampai d tidak menyebut baris contoh; spec memilih `Fixture.hardwareStock.p16.a[4].sku` untuk badge, angka, dan tanggal, dan `Fixture.hardwareStock.p16.a[6].sku` untuk nilai kosong (pilihan spec).
  - TC-AC-ACHS-261 tidak menyebut cara membaca byte berkas; dicatat sebagai kemampuan pembaca CSV dan XLSX yang disediakan tim FE.
  - TC-AC-ACHS-261 Expected d mengasersi urutan baris berkas untuk dua format (CSV dan XLSX) walau Langkah hanya menyebut sort Ascending; spec mengasersi keduanya.
