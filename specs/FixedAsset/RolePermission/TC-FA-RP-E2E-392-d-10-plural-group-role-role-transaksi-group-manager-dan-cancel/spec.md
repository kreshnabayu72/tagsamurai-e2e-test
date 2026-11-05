---
id: TC-FA-RP-E2E-392-d-10-plural-group-role-role-transaksi-group-manager-dan-cancel
title: "Dialog D-10 bentuk jamak memuat Group Role, Role Transaksi, dan Group Manager sekaligus, dan Cancel mempertahankan penugasan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1231
  - TC-FA-RP-1232
coverage:
  web: automated
---

# Dialog D-10 bentuk jamak memuat Group Role, Role Transaksi, dan Group Manager sekaligus, dan Cancel mempertahankan penugasan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage global user & role dengan Update (Hendra Wijaya, Pre-setup #6) `murGlobal_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MUR_GLOBAL_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group: `Helpdesk`, `Logistics Warehouse`, `Dock 1`, `Data Center`), dan #19 (penugasan Role Transaksi bersama; latar, tidak diasersi).
- Seeding precondition (hook `before`, dipakai sebagai precondition TC, tidak diasersi; kemampuan seeding penugasan disediakan tim FE/BE, tanpa endpoint karangan): Gunawan Halim (Pre-setup #17) diatur tanpa Home Group, lalu diberi empat penugasan: Group Role `Manage files` di `Helpdesk`; Asset Admin sub-tab `Disposal` di `Helpdesk`; Staff sub-tab `Damaged` di `Logistics Warehouse`; Group Manager di `Dock 1`. Seed ini memuat precondition kedua TC (penugasan Asset Admin `Helpdesk` sub-tab `Disposal` dipakai TC-FA-RP-1232).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: spec tidak menetapkan Home Group (kedua TC berakhir dengan `[Cancel]`), tetapi seeding mengubah Home Group dan penugasan Gunawan Halim. Hook `after` (tidak berasumsi langkah spec berhasil penuh) mencabut empat penugasan seed lewat fixture BE dan memulihkan Home Group Gunawan Halim ke `Data Center` (Pre-setup #17). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1231: D-10 memuat bullet Group Role, Role Transaksi, dan Group Manager sekaligus, bentuk jamak

1. Buka Settings > User lewat sidebar
2. Ketik Search `Gunawan Halim`, tekan Enter
3. Klik Name `Gunawan Halim`
4. Klik field Home Group lalu pilih `Data Center` dan klik `[Select]`
5. Verifikasi dialog severity danger dengan Title `Role Outside Constraint Will Be Revoked`
6. Verifikasi Body dialog memuat bullet `• Manage files — Helpdesk`, `• Asset Admin — Disposal — Helpdesk`, `• Staff — Damaged — Logistics Warehouse`, dan `• Group Manager — Dock 1` (urutan bullet tidak di-assert)
7. Verifikasi Body dialog memuat kalimat `Setting the Home Group constraint to Data Center for Gunawan Halim will revoke these assignments outside this group.`
8. Verifikasi Body dialog memuat kalimat `Are you sure you want to revoke them?`
9. Verifikasi tombol `[Cancel]` dan `[Revoke]` tampil pada dialog
10. Klik `[Cancel]`

### TC-FA-RP-1232: Cancel D-10 yang memuat Role Transaksi: constraint tidak tersimpan dan penugasan Role Transaksi tetap

11. Buka Settings > User lewat sidebar
12. Ketik Search `Gunawan Halim`, tekan Enter
13. Klik Name `Gunawan Halim`
14. Klik field Home Group, pilih `Data Center`, klik `[Select]`
15. Klik `[Cancel]` pada dialog D-10
16. Verifikasi Home Group Gunawan Halim tidak berubah (tanpa constraint)
17. Buka Fixed Asset > Settings > Role & Permission, klik Tab `Transaction Role`, klik node `Helpdesk`, lalu klik sub-tab `Disposal`
18. Verifikasi Gunawan Halim tetap tampil di section Asset Admin `Helpdesk`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 18 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 sampai 3 dan 11 sampai 13 (membuka Detail User; Search pada langkah 2 dan 12 menemukan baris target, R-16 dan bagian 8b butir 13); langkah 10 (`[Cancel]` menutup dialog karena TC-FA-RP-1231 hanya mengasersi dialog); langkah 17 (navigasi ke sub-tab Role Transaksi untuk mengamati hasil).
- Seed bersama: empat penugasan Gunawan Halim di-seed satu kali di hook `before` dan dipakai kedua TC. Precondition TC-FA-RP-1232 (hanya Asset Admin `Helpdesk` sub-tab `Disposal`) adalah himpunan bagian seed itu, dan `[Cancel]` pada langkah 10 dan 15 tidak mengubah state, sehingga TC-FA-RP-1232 tidak membutuhkan seeding ulang.
- Teks bertanda `copy usulan, PRD 12 #1` (bullet Role Transaksi dan kalimat jamak Body dialog) diasersi literal sesuai TC dan bergantung pada persetujuan PM (NC-20, Open Item #9).
- Temuan untuk QA:
  - NC-20 (PRD Open Item #9) masih menunggu PM: arah gate Home Group, tanpa migrasi, pencabutan silent, dan copy bullet D-10 Role Transaksi (`copy usulan`). Asersi langkah 6 sampai 8 berubah bila copy final berbeda.
  - Precondition TC-FA-RP-1231 dan 1232 menyebut Gunawan Halim "tanpa Home Group", sedangkan Pre-setup #17 menyatakan Home Group `Data Center`; spec mengatur Home Group ke kosong lewat seeding di hook `before` dan memulihkannya di hook `after`.
  - Penugasan Group Role `Manage files` di `Helpdesk`, Staff `Damaged` di `Logistics Warehouse`, dan Group Manager di `Dock 1` tidak termasuk Pre-setup #19; spec membentuknya lewat seeding precondition (kemampuan disediakan tim FE/BE).
  - Email akun Gunawan Halim tidak tertulis di Pre-setup #17; spec ini tidak login sebagai Gunawan Halim sehingga tidak membutuhkannya.
  - TC-FA-RP-1232 tidak menyebut keadaan form Detail User sesudah `[Cancel]` (field Home Group kembali kosong atau tetap berisi nilai yang belum disimpan, dan apakah navigasi berikutnya memicu dialog `Unsaved Changes`). Spec mengasersi bahwa Home Group tampil tidak berubah (langkah 16) dan berpindah halaman lewat sidebar tanpa langkah bersyarat (S-08); bila produk menampilkan dialog `Unsaved Changes`, TC perlu menyebut langkah `[Leave]`.
  - Post Condition kedua TC kosong ("-").
