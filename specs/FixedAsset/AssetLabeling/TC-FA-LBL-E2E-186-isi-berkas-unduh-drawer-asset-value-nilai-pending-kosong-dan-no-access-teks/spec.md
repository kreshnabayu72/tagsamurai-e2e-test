---
id: TC-FA-LBL-E2E-186-isi-berkas-unduh-drawer-asset-value-nilai-pending-kosong-dan-no-access-teks
title: "Isi Berkas Unduh Drawer Tagged Asset: Sel Asset Value Bernilai, Pending Kosong, dan No access Teks pada CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-598
coverage:
  web: automated
---

# Isi Berkas Unduh Drawer Tagged Asset: Sel Asset Value Bernilai, Pending Kosong, dan No access Teks pada CSV dan XLSX

## Prerequisites

- Mode: FE+BE. Backend nyata; berkas diunduh dan dibaca.
- Akun aktor: Gate-Value (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value pada `Gate HQ`) (Pre-setup #40), `Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateValue` (email akun) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Data Pre-setup `Company Gate` (#38) dan #40 (hanya dibaca): General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; label `Gate Label` pada `Gate Item - 51` (`Gate HQ`; Commercial `Rp 1.500.000,00`), `Gate Item - 52` (`Gate HQ > Gate Branch A`; Commercial `Rp 0,00`), `Gate Plain - 54` (`Gate HQ`; Asset Value `Pending` karena belum ada Purchase Cost), dan `Gate Item - 53` (`Gate Other`; di luar hak sehingga `No access`).
- Kemampuan teknis (disediakan tim FE): direktori unduhan uji untuk menangkap berkas; pembaca CSV dan XLSX (header, tipe sel, dan isi sel); hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (dipulihkan pada langkah 11); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).
- Suite berjalan serial (`parallel: false`).
- Env var: `Spectra.env.FA_GATE_VALUE_PASSWORD` dan `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after`.

## Test Steps

### TC-FA-LBL-598: Download Drawer pada pemanggil berhak sebagian: sel Asset Value bernilai, Pending, dan No access

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
3. Klik icon Download di toolbar Drawer
4. Klik `Download as CSV`
5. Verifikasi berkas CSV memuat kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, Fiscal tepat setelah Commercial
6. Verifikasi berkas CSV: `Gate Item - 51` dan `Gate Item - 52` menulis nilai asli Commercial (`1.500.000,00` dan `0,00`, nol tidak dikosongkan)
7. Verifikasi berkas CSV: `Gate Plain - 54` menulis sel kosong pada kedua kolom (bukan teks `Pending`, bukan `—`)
8. Verifikasi berkas CSV: `Gate Item - 53` menulis teks `No access` pada kedua kolom dan tidak memuat nilai asli aset tersebut
9. Klik icon Download di toolbar Drawer
10. Klik `Download as XLSX`
11. Verifikasi berkas XLSX memuat kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, Fiscal tepat setelah Commercial
12. Verifikasi berkas XLSX: `Gate Item - 51` dan `Gate Item - 52` menulis nilai asli Commercial (`1.500.000,00` dan `0,00`, nol tidak dikosongkan)
13. Verifikasi berkas XLSX: `Gate Plain - 54` menulis sel kosong pada kedua kolom (bukan teks `Pending`, bukan `—`)
14. Verifikasi berkas XLSX: `Gate Item - 53` menulis teks `No access` pada kedua kolom dan tidak memuat nilai asli aset tersebut
15. Verifikasi isi CSV dan XLSX identik untuk sel-sel Asset Value di atas
16. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
17. Tutup Drawer Tagged Asset

## Notes

- Mode: FE+BE (backend nyata; berkas diunduh dan dibaca). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Kelas harness binary buffer (bagian 3 prinsip 13f): spec ini hanya memuat asersi isi berkas hasil unduh Drawer.
- Urutan `Verifikasi` mengikuti berkas: Expected a sampai d untuk CSV (langkah 5 sampai 8), lalu untuk XLSX (langkah 11 sampai 14), supaya tiap berkas dibaca tepat setelah diunduh (urutan state, bagian 8b butir 5); Expected e menjadi langkah 15.
- Langkah penghubung (S-03): langkah 16 dan 17 (pemulihan kolom dan tutup Drawer).
- Temuan untuk QA:
  - TC-FA-LBL-598 menyebut nilai Commercial dalam format `1.500.000,00` dan `0,00` tanpa awalan `Rp`; spec mengasersi teks persis itu seperti di Expected b dan tidak menebak format sel angka pada XLSX.
  - TC-FA-LBL-598 tidak menyebut nilai Fiscal untuk `Gate Item - 51` dan `Gate Item - 52`; spec tidak mengasersinya.
  - TC-FA-LBL-598 tidak menyebut nama berkas unduhan; tidak diasersi (nama berkas diasersi di TC-FA-LBL-594).
  - Post Condition TC tidak disebut; tidak diasersi.
