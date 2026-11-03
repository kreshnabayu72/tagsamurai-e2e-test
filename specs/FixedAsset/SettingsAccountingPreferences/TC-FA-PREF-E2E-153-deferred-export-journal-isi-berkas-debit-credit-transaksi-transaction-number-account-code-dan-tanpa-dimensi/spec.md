---
id: TC-FA-PREF-E2E-153-deferred-export-journal-isi-berkas-debit-credit-transaksi-transaction-number-account-code-dan-tanpa-dimensi
title: "[DEFERRED] Export Journal isi berkas (2): Debit dan Credit, minimal 2 baris, Transaction Number, Account Code, dan tanpa dimensi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-499
  - TC-FA-PREF-500
  - TC-FA-PREF-501
  - TC-FA-PREF-502
  - TC-FA-PREF-503
coverage:
  web: automated
---

# [DEFERRED] Export Journal isi berkas (2): Debit dan Credit, minimal 2 baris, Transaction Number, Account Code, dan tanpa dimensi

## Prerequisites

- Mode: FE+BE.
- Kelas harness: f (binary buffer; isi berkas XLSX hasil ekspor Export Journal).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1 (bulan berjalan Oktober 2026); data aset Export Journal PC-17: enam aset menyusut dengan akun Beban Penyusutan yang sama (dua laptop dan satu printer di Group Indonesia > Jakarta, IT Equipment, Category Elektronik > Laptop dan Elektronik > Printer; satu laptop di Group Indonesia > Bandung, IT Equipment; dua mobil di Group Indonesia > Jakarta, Vehicles, Category Kendaraan > Mobil); Chart of Accounts PC-5. Data modul Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Journal Grouping (dibentuk lewat seed): "Group" untuk TC-FA-PREF-499, 500, 501, dan 502; kosong untuk TC-FA-PREF-503.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences dan enam aset PC-17; ekspor jurnal penyusutan bulan ini lewat UI Export Journal; pembaca berkas XLSX (nilai sel per baris, pengelompokan Transaction Number, kolom setelah Credit), disediakan tim FE; pembacaan Account Code dan Account Name di Chart of Accounts.
- State global yang diubah: Journal Grouping company; dikembalikan ke nilai awal PC-1 ("Group") oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Berkas ekspor Journal Grouping "Group" (TC-FA-PREF-499, 500, 501, dan 502)

1. Seed Journal Grouping tersimpan "Group" dan enam aset menyusut PC-1 dan PC-17 hingga tersimpan
2. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
3. Buka file ekspor XLSX

### TC-FA-PREF-499: Pada tiap baris salah satu dari Debit dan Credit bernilai 0

4. Verifikasi pada setiap baris tepat salah satu kolom Debit atau Credit bernilai 0

### TC-FA-PREF-500: Tiap transaksi memiliki minimal 2 baris dan total Debit sama dengan total Credit

5. Verifikasi setiap transaksi memiliki minimal 2 baris
6. Verifikasi total Debit sama dengan total Credit pada setiap transaksi

### TC-FA-PREF-501: Baris dengan Transaction Number sama menjadi satu transaksi

7. Verifikasi baris-baris dengan Transaction Number yang sama membentuk satu transaksi

### TC-FA-PREF-502: Kolom Account Code dan Account Name berasal dari Chart of Accounts

8. Verifikasi Account Code dan Account Name pada file ekspor sama dengan Account Code dan Account Name di Chart of Accounts

### TC-FA-PREF-503: File ekspor tanpa kolom dimensi saat Journal Grouping kosong

9. Seed Journal Grouping tersimpan kosong dan enam aset menyusut PC-1 dan PC-17 hingga tersimpan
10. Buka Export Journal dan ekspor jurnal penyusutan bulan ini
11. Buka file ekspor XLSX
12. Verifikasi kolom Credit tampil pada file ekspor
13. Verifikasi tidak ada kolom Group, Category, maupun Asset Class setelah kolom Credit
14. Pulihkan Journal Grouping ke "Group" lewat seed hingga tersimpan

## Notes

- Satu berkas ekspor Journal Grouping "Group" (langkah 2 dan 3) dipakai bersama TC-FA-PREF-499, 500, 501, dan 502: keempat TC memiliki Precondition dan langkah ekspor yang identik (Journal Grouping "Group", enam aset PC-17, ekspor jurnal penyusutan bulan ini, buka file XLSX) dan hanya berbeda pada klausa isi berkas yang diasersi. TC-FA-PREF-503 memakai Journal Grouping kosong sehingga ekspor sendiri (langkah 10 sampai 12).
- Langkah 12 adalah anchor positif untuk asersi absence pada langkah 13 (bagian 8b butir 2): kolom Credit pada berkas yang sama tampil; langkah ini adalah asersi tambahan di luar Expected TC.
- Langkah penghubung (S-03): langkah 14 (pemulihan state, S-09, R-08).
- Spec kelas f hanya memuat asersi isi berkas; pemicu ekspor adalah langkah Export Journal tanpa asersi UI.
- Temuan untuk QA:
  - TC-FA-PREF-499 sampai 503 menyebut "ekspor jurnal penyusutan bulan ini" tanpa nama berkas atau label tombol ekspor; spec memakai teks TC.
  - TC-FA-PREF-500 Expected a dan b dituliskan dua `Verifikasi` (langkah 5 dan 6, S-01).
  - TC-FA-PREF-502 menyebut kesamaan dengan Chart of Accounts tanpa menyebut akun yang dibandingkan; spec membandingkan seluruh baris berkas dengan Chart of Accounts PC-5.
  - Post Condition TC-FA-PREF-499 sampai 503 tidak ada (bernilai `-`).
