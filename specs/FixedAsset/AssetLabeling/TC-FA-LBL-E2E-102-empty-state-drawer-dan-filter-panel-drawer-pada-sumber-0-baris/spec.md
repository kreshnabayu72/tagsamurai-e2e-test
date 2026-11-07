---
id: TC-FA-LBL-E2E-102-empty-state-drawer-dan-filter-panel-drawer-pada-sumber-0-baris
title: "Empty State Drawer dan Filter Panel Drawer pada Sumber 0 Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-335
  - TC-FA-LBL-532
coverage:
  web: automated
---

# Empty State Drawer dan Filter Panel Drawer pada Sumber 0 Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (hanya dibaca): label `Seasonal Event` (`#EC4899`, Total Asset 0) tanpa aset; Company Alpha memiliki dua buku Asset Value tetap `Commercial` dan `Fiscal` (precondition TC-FA-LBL-532). Fixture label: `Fixture.assetLabeling.labelSeasonalEvent` (`Seasonal Event`).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-335: Empty state genuinely Drawer untuk label tanpa aset

1. Klik chip `Seasonal Event` di kolom Label
2. Verifikasi Drawer menampilkan Illustration dengan Title `No assets tagged` dan Description `No assets are assigned this label yet.`

### TC-FA-LBL-532: Filter Panel Drawer Tagged Asset pada sumber 0 baris: dropdown menampilkan No options available

3. Verifikasi empty state `No assets tagged` tampil sebelum Filter Panel dibuka
4. Klik icon Filter di toolbar Drawer
5. Verifikasi Filter Panel terbuka dengan field `Asset Name`, `TAG`, `Brand`, `Model/Type`, `Measurement`, `Category`, `Group`, `Label`, `Status`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Warranty Expiry`, dan `Last Updated`
6. Buka dropdown `Asset Name`
7. Verifikasi dropdown `Asset Name` menampilkan teks `No options available`
8. Tutup dropdown lalu buka dropdown `Brand`
9. Verifikasi dropdown `Brand` menampilkan teks `No options available`
10. Tutup dropdown lalu buka dropdown `Model/Type`
11. Verifikasi dropdown `Model/Type` menampilkan teks `No options available`
12. Tutup dropdown lalu buka dropdown `Group`
13. Verifikasi dropdown `Group` menampilkan teks `No options available`
14. Tutup dropdown lalu buka dropdown `Status`
15. Verifikasi dropdown `Status` menampilkan teks `No options available`
16. Tutup dropdown lalu buka dropdown `Label`
17. Verifikasi dropdown `Label` menampilkan teks `No options available`
18. Verifikasi tidak ada pesan error pada keenam dropdown
19. Tutup dropdown `Label`, lalu tutup Drawer dengan `[✕]`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-FA-LBL-532 dilanjutkan pada Drawer yang sama dengan TC-FA-LBL-335 (satu pembukaan; TC tanpa perubahan state data). `Verifikasi` empty state sebelum Filter Panel dibuka adalah Expected TC-FA-LBL-532 butir a ('Setelah langkah 1'), diasersi pada keadaan yang sama dengan TC-FA-LBL-335.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup dropdown dan Drawer di langkah terakhir.
- Pembagian TC lintas spec: TC-FA-LBL-327 sampai TC-FA-LBL-331 ada di spec 087; TC-FA-LBL-334, TC-FA-LBL-336, TC-FA-LBL-373, TC-FA-LBL-374, dan TC-FA-LBL-509 ada di spec 088.
