---
id: TC-FA-RP-E2E-379-approver-ancestor-dihitung-aktivasi-toggle-descendant-dan-descendant-tidak-dihitung-bagi-ancestor
title: "Approver di ancestor dihitung untuk aktivasi toggle Require Approval node descendant, sedangkan Approver di descendant tidak dihitung bagi ancestor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1214
  - TC-FA-RP-1215
coverage:
  web: automated
---

# Approver di ancestor dihitung untuk aktivasi toggle Require Approval node descendant, sedangkan Approver di descendant tidak dihitung bagi ancestor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, bagian "Hook suite".
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #18 (struktur group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`) dan #35 (`Company Isolated`: struktur group sama dengan #18; tanpa Group Manager; Pandu Wijaya (Active, Activated) Approver sub-tab `Disposal` di `IT Infrastructure`, yang mencakup `Data Center`, `Helpdesk`, dan `Rack A1`; Require Approval transaksi OFF di semua node).
- Kondisi awal yang di-seed di hook `before` (precondition TC-FA-RP-1215, dipakai sebagai precondition, tidak diasersi): Pandu Wijaya Approver sub-tab `Damaged` hanya di `Data Center`; `IT Infrastructure` sub-tab `Damaged` tanpa Approver manual dan tanpa Group Manager. Pre-setup #35 tidak memuat penugasan itu, sehingga seed ini tambahan dan bukan asumsi fixture global. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: toggle `Require Approval for Disposal` di `Data Center` diaktifkan oleh langkah 3 dan toggle `Require Approval for Damaged` di `Data Center` diaktifkan oleh langkah 20. Hook `after` mengembalikan kedua toggle ke OFF dan mencabut penugasan Pandu Wijaya Approver `Damaged` di `Data Center`, sehingga state kembali ke Pre-setup #35; dijamin fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_ISOLATED_TC_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1214: Approver di ancestor dihitung bagi aktivasi toggle node descendant

1. Klik Tab `Transaction Role`
2. Klik node `Data Center` pada Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Aktifkan toggle `Require Approval for Disposal`
4. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
5. Verifikasi dialog blok `Cannot Require Approval` tidak tampil
6. Verifikasi toggle `Require Approval for Disposal` ON dan RadioGroup tampil dengan `Any approver (OR)` terpilih
7. Verifikasi section Approver `Data Center` tidak memuat baris Pandu Wijaya
8. Klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
9. Verifikasi toggle `Require Approval for Disposal` pada `IT Infrastructure` tetap OFF
10. Klik node `Helpdesk`, lalu klik sub-tab `Disposal`
11. Verifikasi toggle `Require Approval for Disposal` pada `Helpdesk` tetap OFF
12. Klik node `Rack A1`, lalu klik sub-tab `Disposal`
13. Verifikasi toggle `Require Approval for Disposal` pada `Rack A1` tetap OFF

### TC-FA-RP-1215: Approver di node descendant tidak dihitung bagi ancestor

14. Klik node `IT Infrastructure`, lalu klik sub-tab `Damaged`
15. Aktifkan toggle `Require Approval for Damaged`
16. Verifikasi dialog blok severity warning: Title `Cannot Require Approval`; Body `Add at least one approver, or assign a Group Manager, to this group or its parent group before enabling approval.`; satu tombol `[OK]`
17. Klik `[OK]`
18. Verifikasi toggle `Require Approval for Damaged` pada `IT Infrastructure` kembali OFF
19. Klik node `Data Center`, lalu klik sub-tab `Damaged`
20. Aktifkan toggle `Require Approval for Damaged`
21. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
22. Verifikasi toggle `Require Approval for Damaged` pada `Data Center` ON
23. Verifikasi dialog blok `Cannot Require Approval` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 23 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): navigasi Tab, node, dan sub-tab (langkah 1, 2, 8, 10, 12, 14, 19) dan penutupan dialog blok lewat `[OK]` (langkah 17; `[OK]` disebut TC langkah 3). Pemulihan toggle dan seed hanya di hook `after` (Prerequisites).
- Asersi absence: langkah 5 dan 23 didahului langkah 4 dan 21 (toast sukses dari server, anchor positif, bagian 8b butir 2); langkah 7 didahului langkah 6 (RadioGroup dan toggle `Data Center` termuat); langkah 9, 11, 13 adalah asersi keadaan toggle OFF yang tampil pada kartu Approval Rule node itu (bukan absence elemen).
- Pembagian TC lintas spec: TC-FA-RP-1214 dan TC-FA-RP-1215 hanya ada di spec ini. Kedua TC tidak memuat asersi log.
- Temuan untuk QA:
  - NC-19 / Open Item #8 (menunggu PM): pelebaran penugasan, Approver ancestor dihitung, dan copy jamak D-09. TC-FA-RP-1214 dan TC-FA-RP-1215 meng-assert perilaku PRD saat ini (21b, D-11); bila PM menetapkan lain, spec ini perlu diubah.
  - Akun login Total Control `Company Isolated` tidak tertulis di Pre-setup TC (#35 hanya menyebut "Total Control tersedia"); akun disediakan tim FE.
  - Seed tambahan TC-FA-RP-1215 (Pandu Wijaya Approver `Damaged` hanya di `Data Center`) tidak ada di Pre-setup #35 dan di-seed di hook `before`.
  - NC-11: hak efektif pada modul konsumen tidak teramati di surface ini; spec hanya meng-assert toggle, dialog blok, toast, dan section Approver.
  - TC-FA-RP-1214 Expected c ditulis satu butir untuk tiga node; spec memecahnya satu `Verifikasi` per node (langkah 9, 11, 13). Expected a "tanpa dialog `Cannot Require Approval`" diasersi pada langkah 5 setelah toast.
