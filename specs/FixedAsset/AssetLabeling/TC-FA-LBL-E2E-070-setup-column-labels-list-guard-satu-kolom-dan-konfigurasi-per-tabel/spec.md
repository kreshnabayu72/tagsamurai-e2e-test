---
id: TC-FA-LBL-E2E-070-setup-column-labels-list-guard-satu-kolom-dan-konfigurasi-per-tabel
title: "Setup Column Labels List: Guard Satu Kolom Tersisa dan Konfigurasi per Tabel"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-263
  - TC-FA-LBL-264
coverage:
  web: automated
---

# Setup Column Labels List: Guard Satu Kolom Tersisa dan Konfigurasi per Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Color Hex |
  |---|---|
  | `High Priority` | `#EF4444` |
  | `Finance Department` | `#3B82F6` |
  | `Audit Ready` | `#10B981` |
  | `Executive Asset` | `#8B5CF6` |
  | `Maintenance Due` | `#F59E0B` |
  | `Seasonal Event` | `#EC4899` |
  | `Night Shift` | `#1E3A8A` |
  | `Warehouse Priority` | `#0EA5E9` |
  | `Field Kit` | `#84CC16` |

- Data Pre-setup #13 (aset berlabel `Finance Department` untuk Drawer Tagged Asset; hanya dibaca).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Labels List (diubah dan dipulihkan oleh langkah spec); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).

## Test Steps

### TC-FA-LBL-263: Guard satu kolom tersisa: checkbox kolom terakhir disabled

1. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
2. Hapus centang `Color Hex`, `Total Asset`, `Modified By`, dan `Last Updated` sehingga hanya `Label` tersisa
3. Hover checkbox `Label`
4. Verifikasi checkbox `Label` disabled dan tidak dapat di-uncheck
5. Verifikasi tooltip `At least one column must remain visible.` tampil
6. Klik icon `[✕]` pada popup Setup Column (menutup tanpa menyimpan)

### TC-FA-LBL-264: Konfigurasi kolom Labels List tidak memengaruhi tabel Changelog dan Drawer

7. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
8. Hapus centang `Color Hex`
9. Klik `[Save]`
10. Klik icon Changelog di Table Tools
11. Verifikasi Modal Changelog menampilkan ketujuh kolomnya: `Date`, `Action`, `Label Name`, `Field`, `Old Value`, `New Value`, `Modified By`
12. Tutup Modal Changelog
13. Klik `⋯` pada baris `Finance Department`, lalu klik `Detail`
14. Verifikasi Drawer Tagged Asset menampilkan delapan kolom default: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
15. Tutup Drawer Tagged Asset
16. Verifikasi tabel Labels List tetap tanpa kolom `Color Hex` (konfigurasi tersimpan per tabel)
17. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
18. Centang `Color Hex`
19. Klik `[Save]`

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6 menutup popup tanpa menyimpan agar TC-FA-LBL-264 mulai dari lima kolom; langkah 12 dan 15 menutup Modal Changelog dan Drawer; langkah 17 sampai 19 memulihkan kolom `Color Hex` (S-09).
- Drawer dibuka lewat row action `Detail` (NC-02), karena TC-FA-LBL-264 hanya menyebut "buka ... Drawer Tagged Asset `Finance Department`".
- Temuan untuk QA:
  - TC-FA-LBL-264 tidak menyebut cara membuka Drawer dan Modal Changelog; spec memakai icon Changelog di Table Tools dan row action `Detail`.
  - TC-FA-LBL-264 Expected "konfigurasi tersimpan per tabel" adalah kesimpulan dari dua butir sebelumnya; spec mengasersi sisi Labels List (tanpa `Color Hex`) di langkah 16.
