---
id: TC-FA-RP-E2E-382-remove-approver-ancestor-d08-dan-remove-approver-descendant-tanpa-d09
title: "Remove Approver di ancestor tanpa group terdampak memakai D-08, dan Remove Approver di descendant dengan Approver ancestor tanpa D-09"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1219
  - TC-FA-RP-1220
coverage:
  web: automated
---

# Remove Approver di ancestor tanpa group terdampak memakai D-08, dan Remove Approver di descendant dengan Approver ancestor tanpa D-09

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, bagian "Hook suite".
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #15 (Ahmad Fauzi), #18 (struktur group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`), dan #35 (`Company Isolated`: struktur group sama dengan #18; tanpa Group Manager; Pandu Wijaya (Active, Activated) Approver sub-tab `Disposal` di `IT Infrastructure`, yang mencakup `Data Center`, `Helpdesk`, dan `Rack A1`; Require Approval transaksi OFF di semua node).
- Kondisi awal yang di-seed di hook `before` (precondition TC-FA-RP-1219 dan TC-FA-RP-1220, dipakai sebagai precondition, tidak diasersi): Ahmad Fauzi satu-satunya Approver manual di `Data Center` sub-tab `Disposal`; toggle `Require Approval for Disposal` ON hanya di `Data Center`; tanpa Group Manager. Seed ini tambahan di atas Pre-setup #35 dan bukan asumsi fixture global. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya (spec destruktif, `[Remove]` sungguhan): Pandu Wijaya dilepas dari Approver `IT Infrastructure` sub-tab `Disposal` oleh langkah 6 dan dipasang kembali oleh seed pada langkah 10; Ahmad Fauzi dilepas dari Approver `Data Center` oleh langkah 15. Hook `after` memulihkan Pandu Wijaya Approver `IT Infrastructure` sub-tab `Disposal` (Pre-setup #35), mencabut penugasan tambahan Ahmad Fauzi, dan mengembalikan toggle `Require Approval for Disposal` `Data Center` ke OFF, dijamin fixture backend yang disediakan tim FE/BE dan tidak berasumsi langkah spec berhasil penuh. Efek pada Last Updated baris dan Changelog: entri `Remove` ditambahkan oleh aksi spec dan tidak dihapus. Suite berjalan serial (`parallel: false`); spec ini dijalankan paling akhir di antara spec penugasan Approver `Company Isolated`.
- Env var yang dipakai: `FA_ISOLATED_TC_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1219: Remove Approver ancestor tanpa group terdampak memakai D-08 biasa

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` pada Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`
4. Verifikasi dialog `Remove Approver` biasa tampil dengan Body `• Pandu W` lalu `This user will no longer be assigned to this role for IT Infrastructure.`
5. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil
6. Klik `[Remove]`
7. Verifikasi muncul toast sukses: `Success, Approver has been removed.`
8. Klik node `Data Center`, lalu klik sub-tab `Disposal`
9. Verifikasi toggle `Require Approval for Disposal` pada `Data Center` tetap ON

### TC-FA-RP-1220: Remove Approver descendant dengan Approver ancestor tanpa D-09

10. Siapkan state: Pandu Wijaya dipasang kembali sebagai Approver di `IT Infrastructure` sub-tab `Disposal`, hingga tersimpan.
11. Muat ulang halaman (F5), buka Tab `Transaction Role`, klik node `Data Center`, lalu klik sub-tab `Disposal`
12. Klik `[⋯]` pada baris Ahmad Fauzi, lalu pilih `Remove`
13. Verifikasi dialog `Remove Approver` biasa tampil dengan Body `• Ahmad F` lalu `This user will no longer be assigned to this role for Data Center.`
14. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil
15. Klik `[Remove]`
16. Verifikasi muncul toast sukses: `Success, Approver has been removed.`
17. Verifikasi toggle `Require Approval for Disposal` pada `Data Center` tetap ON

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 17 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): navigasi Tab, node, dan sub-tab (langkah 1, 2, 8, 11), seeding antar TC (langkah 10, memulihkan Pandu Wijaya yang dilepas langkah 6 sebagai precondition TC-FA-RP-1220), dan muat ulang (F5) sesudah seeding API (langkah 11). Tabel Approver `IT Infrastructure` dan `Data Center` memuat kurang dari 10 baris (Pre-setup #19), sehingga baris target tidak dicari lewat Search.
- Asersi absence D-09 (langkah 5 dan 14) didahului asersi dialog `Remove Approver` biasa tampil (langkah 4 dan 13) sebagai anchor positif dialog sementara (bagian 8b butir 2). Kedua dialog diasersi sebelum `[Remove]` ditekan (bagian 8b butir 5).
- Pembagian TC lintas spec: TC-FA-RP-1219 dan TC-FA-RP-1220 hanya ada di spec ini. Varian yang hanya membuka dialog (D-09 jamak dan D-02) ada di spec 381.
- Temuan untuk QA:
  - NC-19 / Open Item #8 (menunggu PM): Approver ancestor dihitung dan pelebaran penugasan; TC-FA-RP-1219 dan TC-FA-RP-1220 meng-assert perilaku PRD saat ini (21b, 21h). Bila PM menetapkan lain, spec ini perlu diubah.
  - TC-FA-RP-1219 Expected a menyebut "D-08" hanya pada judul; asersi mengikuti Body dialog `Remove Approver` biasa yang ditulis TC. Keduanya TC tidak menulis Title dialog `Remove Approver`, sehingga spec tidak mengasersi Title.
  - TC-FA-RP-1219 tidak menyatakan state Pandu Wijaya sesudah Remove; spec memulihkannya lewat seed (langkah 10) karena TC-FA-RP-1220 mensyaratkan Approver manual di ancestor.
  - NC-11: hak efektif pada modul konsumen tidak teramati di surface ini; spec hanya meng-assert dialog, toast, dan toggle.
  - Akun login Total Control `Company Isolated` tidak tertulis di Pre-setup TC; akun disediakan tim FE.
