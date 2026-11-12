---
id: TC-FA-CAT-E2E-205-sel-asset-value-pending-tooltip-alasan-dan-prioritas
title: "Sel Asset Value Pending Tabel Assets: Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi dan Prioritas Alasan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-702
coverage:
  web: automated
---

# Sel Asset Value Pending Tabel Assets: Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi dan Prioritas Alasan

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori), #21 (Asset Name), #22 (aset), #50 (akun), #55, dan #58 tersedia (disediakan tim FE).
- Data Pre-setup #60 (CatMain, node `Furniture`, seed API; baru, disediakan tim FE/BE): Asset Name `Office Chair` tanpa Asset Class; `Office Chair - 1` Purchase Cost 500000.00 (Asset Value Commercial dan Fiscal `Pending`, tooltip `Asset class has not been set.`); `Office Chair - 2` tanpa Purchase Cost (Asset Value Commercial dan Fiscal `Pending`, tooltip `Purchase cost has not been set.` karena prioritas alasan Purchase mengalahkan Asset Class).
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-702: Sel Asset Value Pending: tooltip alasan Purchase cost belum diisi atau Asset class belum diisi, dan prioritas alasan

1. Klik elipsis (⋯) pada baris `Furniture` > `Detail`
2. Klik header Actions (⋯) > `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
3. Verifikasi `Office Chair - 1` dan `Office Chair - 2` menampilkan teks `Pending` pada kedua kolom (bukan `—`, bukan currency nol, bukan `No access`)
4. Hover sel `Pending` pada `Office Chair - 1` di kolom `Asset Value (Commercial)`
5. Verifikasi tooltip `Office Chair - 1` pada kolom `Asset Value (Commercial)`: `Asset class has not been set.` (Purchase Cost sudah ada)
6. Hover sel `Pending` pada `Office Chair - 1` di kolom `Asset Value (Fiscal)`
7. Verifikasi tooltip `Office Chair - 1` pada kolom `Asset Value (Fiscal)`: `Asset class has not been set.`
8. Hover sel `Pending` pada `Office Chair - 2` di kolom `Asset Value (Commercial)`
9. Verifikasi tooltip `Office Chair - 2` pada kolom `Asset Value (Commercial)`: `Purchase cost has not been set.` (prioritas alasan Purchase mengalahkan Asset Class)
10. Hover sel `Pending` pada `Office Chair - 2` di kolom `Asset Value (Fiscal)`
11. Verifikasi tooltip `Office Chair - 2` pada kolom `Asset Value (Fiscal)`: `Purchase cost has not been set.`
12. Verifikasi tooltip sel `Pending` tidak memuat metode atau masa manfaat

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 1 (membuka Popup Detail node `Furniture`); hover `Pending` pada langkah TC 4 dipecah per sel dan per kolom (langkah 4, 6, 8, 10) agar tooltip tiap sel diverifikasi.
- Temuan untuk QA:
  - TC-FA-CAT-702 membuka Popup Detail dari baris `Furniture` tanpa menyebut langkah memilih node induk di Sidebar Category Tree; spec mengikuti TC (baris `Furniture` diasumsikan tampil pada tabel Categories List).
  - TC-FA-CAT-702 menyebut Pre-setup #58 tanpa penjelasan; spec memakainya sebagai prasyarat tanpa mengasersinya.
  - Pre-setup #60 (Asset Name `Office Chair`) adalah fixture baru; kunci fixture belum ada dan disediakan tim FE/BE.
  - Post Condition TC ("Konfigurasi kolom dikembalikan lewat `[Reset to Default]` lalu `[Save]`") tidak punya langkah observasi di TC; pemulihan lewat hook `after`.
