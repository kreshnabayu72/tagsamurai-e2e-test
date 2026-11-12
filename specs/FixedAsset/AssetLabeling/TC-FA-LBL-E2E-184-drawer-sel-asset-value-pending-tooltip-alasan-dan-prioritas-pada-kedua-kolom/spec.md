---
id: TC-FA-LBL-E2E-184-drawer-sel-asset-value-pending-tooltip-alasan-dan-prioritas-pada-kedua-kolom
title: "Drawer Tagged Asset: Sel Asset Value Pending pada Kedua Kolom, Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi, dan Prioritas Alasan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-596
coverage:
  web: automated
---

# Drawer Tagged Asset: Sel Asset Value Pending pada Kedua Kolom, Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi, dan Prioritas Alasan

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Pending Reason` (pengguna `Total Control Pend`) (Pre-setup #58), `Fixture.assetLabeling.akun.totalControlPend` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net` pada company itu), `Spectra.env.FA_PEND_TC_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlPend` (email akun) dan `Fixture.assetLabeling.pendingReason` (data Pre-setup #58, kunci usulan).
- Data Pre-setup #58 (`Company Pending Reason`; fixture baru, hanya dibaca): General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal); Group `Pend HQ`; Asset Name `Pend Item` tanpa Asset Class; label `Pend Label` terpasang pada aset Active `Pend Asset - 91` (Group `Pend HQ`; Purchase Cost 150000; Asset Value `Pending`, tooltip `Asset class has not been set.`) dan `Pend Asset - 92` (Group `Pend HQ`; tanpa Purchase Cost; Asset Value `Pending`, tooltip `Purchase cost has not been set.` karena prioritas alasan Purchase mengalahkan Asset Class).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah.
- Env var: `Spectra.env.FA_PEND_TC_PASSWORD` dan `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after`.

## Test Steps

### TC-FA-LBL-596: Sel Asset Value Pending pada kedua kolom: tooltip alasan Purchase cost belum diisi atau Asset class belum diisi, dan prioritas alasan

1. Klik chip `Pend Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
3. Verifikasi `Pend Asset - 91` dan `Pend Asset - 92` menampilkan teks `Pending` pada `Asset Value (Commercial)` dan `Asset Value (Fiscal)` (bukan `—`, bukan `Rp 0,00`, bukan `No access`)
4. Hover sel `Pending` `Pend Asset - 91` pada kolom `Asset Value (Commercial)`
5. Verifikasi tooltip `Pend Asset - 91` pada kolom `Asset Value (Commercial)`: `Asset class has not been set.` (Purchase Cost sudah ada)
6. Hover sel `Pending` `Pend Asset - 91` pada kolom `Asset Value (Fiscal)`
7. Verifikasi tooltip `Pend Asset - 91` pada kolom `Asset Value (Fiscal)`: `Asset class has not been set.`
8. Hover sel `Pending` `Pend Asset - 92` pada kolom `Asset Value (Commercial)`
9. Verifikasi tooltip `Pend Asset - 92` pada kolom `Asset Value (Commercial)`: `Purchase cost has not been set.` (prioritas alasan Purchase mengalahkan Asset Class)
10. Hover sel `Pending` `Pend Asset - 92` pada kolom `Asset Value (Fiscal)`
11. Verifikasi tooltip `Pend Asset - 92` pada kolom `Asset Value (Fiscal)`: `Purchase cost has not been set.`
12. Verifikasi tooltip sel `Pending` tidak memuat metode atau masa manfaat
13. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
14. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 13 dan 14 (pemulihan kolom dan tutup Drawer). Hover `Pending` pada langkah TC 4 dipecah per sel dan per kolom (langkah 4, 6, 8, 10) agar tooltip tiap sel diverifikasi.
- Temuan untuk QA:
  - TC-FA-LBL-596 Expected e (pemanggil tanpa hak melihat `No access`, bukan `Pending`) merujuk TC-FA-LBL-547 dan tidak diasersi di spec ini; asersi itu ada di spec TC-FA-LBL-E2E-122.
  - Pre-setup #58 (`Company Pending Reason`) adalah fixture baru; email akun `Total Control Pend`, nama env password, dan kunci fixture belum ada dan disediakan tim FE (nama env usulan).
  - Post Condition TC tidak disebut; tidak diasersi.
