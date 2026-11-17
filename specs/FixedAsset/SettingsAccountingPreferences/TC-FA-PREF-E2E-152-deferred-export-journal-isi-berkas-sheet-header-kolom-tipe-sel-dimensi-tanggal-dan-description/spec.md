---
id: TC-FA-PREF-E2E-152-deferred-export-journal-isi-berkas-sheet-header-kolom-tipe-sel-dimensi-tanggal-dan-description
title: "[DEFERRED] Export Journal isi berkas (1): sheet, header, kolom, tipe sel, dimensi, tanggal, dan Description"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-493
  - TC-FA-PREF-494
  - TC-FA-PREF-495
  - TC-FA-PREF-496
  - TC-FA-PREF-497
  - TC-FA-PREF-498
sourceRules: ["FAPREF-LOGIC-09q", "FAPREF-LOGIC-09r", "FAPREF-LOGIC-09s", "FAPREF-LOGIC-09u", "FAPREF-LOGIC-09v", "FAPREF-LOGIC-09e", "FAPREF-LOGIC-09t", "FAPREF-LOGIC-09p"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-09q": [4, 5]
  "FAPREF-LOGIC-09r": 6
  "FAPREF-LOGIC-09s": 7
  "FAPREF-LOGIC-09u": 8
  "FAPREF-LOGIC-09v": 9
  "FAPREF-LOGIC-09e": 9
  "FAPREF-LOGIC-09t": 13
  "FAPREF-LOGIC-09p": 13
coverage:
  web: automated
---

# [DEFERRED] Export Journal isi berkas (1): sheet, header, kolom, tipe sel, dimensi, tanggal, dan Description

## Prerequisites

- Mode: FE+BE.
- Kelas harness: f (binary buffer; isi berkas XLSX hasil ekspor Export Journal).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (bulan berjalan Oktober 2026); data aset Export Journal PC-17: enam aset menyusut dengan akun Beban Penyusutan yang sama (dua laptop dan satu printer di Group Indonesia > Jakarta, IT Equipment, Category Elektronik > Laptop dan Elektronik > Printer; satu laptop di Group Indonesia > Bandung, IT Equipment; dua mobil di Group Indonesia > Jakarta, Vehicles, Category Kendaraan > Mobil). Data modul Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Journal Grouping (dibentuk lewat seed): "Group" untuk TC-FA-PREF-493, 494, 495, 497, dan 498; "Group", "Category", dan "Asset Class" untuk TC-FA-PREF-496.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan enam aset PC-17; ekspor jurnal penyusutan bulan ini lewat UI Export Journal; pembaca berkas XLSX (jumlah sheet, baris header, tipe dan format sel, urutan kolom), disediakan tim FE.
- State global yang diubah: Journal Grouping company; dikembalikan ke nilai awal PC-1 ("Group") oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Berkas ekspor Journal Grouping "Group" (TC-FA-PREF-493, 494, 495, 497, dan 498)

1. Seed Journal Grouping tersimpan "Group" dan enam aset menyusut PC-1 dan PC-17 hingga tersimpan
2. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
3. Buka file ekspor XLSX

### TC-FA-PREF-493: File ekspor memiliki satu sheet dan satu baris header

4. Verifikasi file ekspor memiliki tepat 1 sheet
5. Verifikasi sheet memiliki tepat 1 baris header

### TC-FA-PREF-494: Kolom Debit dan Credit berupa sel numerik dengan dua desimal

6. Verifikasi sel kolom Debit dan Credit bertipe numerik dengan dua desimal

### TC-FA-PREF-495: File ekspor memiliki kolom tetap berurutan

7. Verifikasi kolom tetap berurutan: Transaction Number, Date, Account Code, Account Name, Description, Debit, Credit

### TC-FA-PREF-497: Kolom Date berupa sel tanggal yang ditampilkan yyyy-mm-dd

8. Verifikasi sel kolom Date bernilai tanggal dan ditampilkan dengan format yyyy-mm-dd

### TC-FA-PREF-498: Kolom Description mengikuti aturan tetap Export Journal

9. Verifikasi kolom Description terisi menurut aturan tetap Export Journal, bukan dari Preferences

### TC-FA-PREF-496: Kolom dimensi Journal Grouping ditulis setelah kolom tetap sesuai urutan Group, Category, Asset Class

10. Seed Journal Grouping tersimpan "Group", "Category", dan "Asset Class" dan enam aset menyusut PC-1 dan PC-17 hingga tersimpan
11. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
12. Buka file ekspor XLSX
13. Verifikasi setelah kolom Credit terdapat kolom Group, Category, Asset Class berurutan berisi path penuh Group Assignable dan Category serta nama Asset Class
14. Pulihkan Journal Grouping ke "Group" lewat seed hingga tersimpan

## Notes

- Satu berkas ekspor Journal Grouping "Group" (langkah 2 dan 3) dipakai bersama TC-FA-PREF-493, 494, 495, 497, dan 498: kelima TC memiliki Precondition dan langkah ekspor yang identik (Journal Grouping "Group", enam aset PC-17, ekspor jurnal penyusutan bulan ini, buka file XLSX) dan hanya berbeda pada klausa isi berkas yang diasersi. TC-FA-PREF-496 memakai Journal Grouping lain sehingga ekspor sendiri (langkah 10 sampai 12). Urutan TC di spec berbeda dari urutan nomor (496 sesudah 498) agar berkas "Group" dipakai bersama sebelum seed diganti.
- Langkah penghubung (S-03): langkah 14 (pemulihan state, S-09, R-08).
- Spec kelas f hanya memuat asersi isi berkas; pemicu ekspor adalah langkah Export Journal tanpa asersi UI.
- Temuan untuk QA:
  - TC-FA-PREF-493 sampai 498 menyebut "ekspor jurnal penyusutan bulan ini" tanpa nama berkas, format pilihan ekspor, atau label tombol; spec memakai teks TC.
  - TC-FA-PREF-494 dan 497 menyebut tipe sel tanpa aturan format sel (mis. format angka Excel); spec mengasersi teks Expected apa adanya.
  - TC-FA-PREF-498 menyebut "aturan tetap Export Journal" tanpa merincinya; spec tidak dapat mengasersi isi Description yang spesifik.
  - TC-FA-PREF-496 Expected tidak menyebut nilai path Group, Category, dan nama Asset Class per baris; spec mengasersi teks Expected apa adanya.
  - Post Condition TC-FA-PREF-493 sampai 498 tidak ada (bernilai `-`).
