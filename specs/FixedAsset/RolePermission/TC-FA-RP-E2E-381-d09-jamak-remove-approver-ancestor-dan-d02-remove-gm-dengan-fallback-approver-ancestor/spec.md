---
id: TC-FA-RP-E2E-381-d09-jamak-remove-approver-ancestor-dan-d02-remove-gm-dengan-fallback-approver-ancestor
title: "Remove Approver di ancestor menampilkan D-09 jamak berisi group terdampak, dan Remove Group Manager dengan fallback Approver ancestor memakai D-02"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1217
  - TC-FA-RP-1218
  - TC-FA-RP-1221
coverage:
  web: automated
---

# Remove Approver di ancestor menampilkan D-09 jamak berisi group terdampak, dan Remove Group Manager dengan fallback Approver ancestor memakai D-02

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, bagian "Hook suite".
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #15 (Ahmad Fauzi), #18 (struktur group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`), dan #35 (`Company Isolated`: struktur group sama dengan #18; tanpa Group Manager; Pandu Wijaya (Active, Activated) Approver sub-tab `Disposal` di `IT Infrastructure`, yang mencakup `Data Center`, `Helpdesk`, dan `Rack A1`; Require Approval transaksi OFF di semua node).
- Kondisi awal yang di-seed di hook `before` (precondition TC-FA-RP-1217, dipakai sebagai precondition, tidak diasersi): toggle `Require Approval for Disposal` ON di `IT Infrastructure`, `Data Center`, dan `Rack A1`, OFF di `Helpdesk`; Pandu Wijaya satu-satunya Approver sub-tab `Disposal` yang mencakup node-node itu; tanpa Group Manager. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Seed antar TC (langkah "Siapkan state", precondition TC, tidak diasersi): langkah 19 untuk TC-FA-RP-1218 dan langkah 27 untuk TC-FA-RP-1221, ditulis `hingga tersimpan`. Seed ini tambahan di atas Pre-setup #35 dan bukan asumsi fixture global; khusus TC-FA-RP-1221 menambah Kevin Susanto Group Manager di `Data Center` (Pre-setup #35 menyebut tanpa Group Manager; lihat Temuan untuk QA).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: spec hanya membuka dialog dan menekan `[Cancel]` (tanpa penghapusan sungguhan); yang berubah adalah seed state (toggle `Require Approval for Disposal` dan `Require Approval for Damaged`, penugasan Ahmad Fauzi Approver `Data Center`, Pandu Wijaya Approver `Damaged` di `IT Infrastructure`, Kevin Susanto Group Manager di `Data Center`). Hook `after` memulihkan seluruhnya ke Pre-setup #35 (toggle OFF di semua node dan sub-tab, penugasan tambahan dicabut), dijamin fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_ISOLATED_TC_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1217: Remove Approver ancestor, D-09 jamak berisi tiga group

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` pada Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`
4. Verifikasi dialog D-09 severity danger: Title `Remove Last Approver`; Body baris `• Pandu W`
5. Verifikasi kalimat group terdampak memuat nama group `IT Infrastructure`, `Data Center`, dan `Rack A1` dipisah koma, diikuti `will have no approver other than Total Control while approval is required.`
6. Verifikasi `Helpdesk` tidak disebut pada kalimat group terdampak
7. Verifikasi penutup dialog `Are you sure you want to remove it?`
8. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
9. Verifikasi dialog `Remove Approver` biasa tidak tampil
10. Klik `[Cancel]`
11. Verifikasi baris Pandu Wijaya tetap ada pada section Approver
12. Verifikasi toggle `Require Approval for Disposal` pada `IT Infrastructure` tetap ON
13. Klik node `Data Center`, lalu klik sub-tab `Disposal`
14. Verifikasi toggle `Require Approval for Disposal` pada `Data Center` tetap ON
15. Klik node `Rack A1`, lalu klik sub-tab `Disposal`
16. Verifikasi toggle `Require Approval for Disposal` pada `Rack A1` tetap ON
17. Klik node `Helpdesk`, lalu klik sub-tab `Disposal`
18. Verifikasi toggle `Require Approval for Disposal` pada `Helpdesk` tetap OFF

### TC-FA-RP-1218: group dengan Approver lain tidak disebut pada D-09

19. Siapkan state: Pandu Wijaya Approver di `IT Infrastructure` dan Ahmad Fauzi Approver di `Data Center` sub-tab `Disposal`; toggle `Require Approval for Disposal` ON di `IT Infrastructure`, `Data Center`, dan `Helpdesk`, OFF di `Rack A1`; tanpa Group Manager, hingga tersimpan.
20. Muat ulang halaman (F5), buka Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
21. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`
22. Verifikasi dialog D-09 `Remove Last Approver` tampil
23. Verifikasi kalimat group terdampak memuat nama group `IT Infrastructure` dan `Helpdesk` dipisah koma, diikuti `will have no approver other than Total Control while approval is required.`
24. Verifikasi `Data Center` tidak disebut pada kalimat group terdampak
25. Verifikasi `Rack A1` tidak disebut pada kalimat group terdampak
26. Klik `[Cancel]`

### TC-FA-RP-1221: Remove Group Manager dengan fallback Approver ancestor memakai D-02

27. Siapkan state: pulihkan seed TC-FA-RP-1218 (toggle `Require Approval for Disposal` OFF di semua node, Ahmad Fauzi dilepas dari Approver `Data Center`); Kevin Susanto Group Manager di `Data Center`; toggle `Require Approval for Damaged` ON di `Data Center`; Pandu Wijaya Approver di `IT Infrastructure` sub-tab `Damaged`; tanpa pemegang Update dan tanpa Group Manager lain, hingga tersimpan.
28. Muat ulang halaman (F5), buka Tab `Group Manager`, lalu klik node `Data Center`
29. Klik `[⋯]` pada baris Kevin Susanto, lalu pilih `Remove`
30. Verifikasi dialog D-02 `Remove Group Manager` tampil
31. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil
32. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): navigasi Tab, node, dan sub-tab (langkah 1, 2, 13, 15, 17, 20, 28), seeding antar TC (langkah 19 dan 27), dan penutupan dialog lewat `[Cancel]` (langkah 10, 26, 32; langkah 10 disebut TC langkah 4, dua lainnya menutup dialog supaya blok berikutnya tidak mewarisi dialog terbuka, S-09). Muat ulang (F5) sesudah seeding API memastikan UI membaca state terbaru. Tabel Approver `IT Infrastructure` memuat kurang dari 10 baris (Pre-setup #19), sehingga baris Pandu Wijaya tidak dicari lewat Search.
- Asersi absence atas dialog sementara (bagian 8b butir 2, 11): langkah 9 didahului langkah 4 sampai 8 (dialog D-09 tampil), langkah 31 didahului langkah 30 (dialog D-02 tampil), dan langkah 6, 24, 25 didahului asersi kalimat group terdampak (langkah 5 dan 23). Langkah 11 dan 12 sampai 18 dilakukan sesudah dialog tertutup (langkah 10).
- Langkah 12 sampai 18 menerjemahkan "seluruh toggle tidak berubah" (1217 Expected d) menjadi satu `Verifikasi` per node, dengan nilai awal sesuai seed (ON di `IT Infrastructure`, `Data Center`, `Rack A1`; OFF di `Helpdesk`).
- Pembagian TC lintas spec: TC-FA-RP-1217, TC-FA-RP-1218, dan TC-FA-RP-1221 hanya ada di spec ini. Varian Remove sungguhan (D-08 dan Remove Approver descendant) ada di spec 382 (TC-FA-RP-1219 dan TC-FA-RP-1220).
- Temuan untuk QA:
  - NC-19 / Open Item #8 (menunggu PM): copy jamak D-09 bertanda `copy usulan, PRD 12 #8`. Expected TC-FA-RP-1217 dan TC-FA-RP-1218 ditulis sesuai TC; bila PM mengubah copy, spec ini usang (langkah 5 dan 23). Urutan nama group pada `[Group Names]` tidak ditetapkan PRD, sehingga spec hanya meng-assert kehadiran nama (langkah 5, 6, 23, 24, 25), bukan urutannya.
  - Pre-setup #35 menyebut `Company Isolated` tanpa Group Manager, sedangkan TC-FA-RP-1221 Precondition d menugaskan Kevin Susanto Group Manager di `Data Center` (Pre-setup #13 dan #43 menyebut Kevin Susanto Group Manager hanya di `Data Center`, tanpa menyebut company). Spec men-seed kondisi precondition d lewat langkah 27; keberadaan Kevin Susanto pada `Company Isolated` perlu direkonsiliasi.
  - TC-FA-RP-1221 Expected hanya menyebut "Dialog D-02 `Remove Group Manager` tampil tanpa D-09" dan tidak memuat Title atau Body D-02. Spec mengasersi dialog D-02 tampil (langkah 30) dan ketiadaan D-09 setelah anchor itu (langkah 31); Body D-02 tidak diasersi di spec ini dan mengikuti TC-FA-RP-456 (spec 132).
  - NC-11: hak efektif pada modul konsumen tidak teramati di surface ini; spec hanya meng-assert dialog dan toggle.
  - TC-FA-RP-1217 Expected d dan TC-FA-RP-1218 Expected a/b tidak merinci langkah observasi per node; langkah 12 sampai 18 dan langkah 22 sampai 25 adalah pemecahan per klausa (S-01).
  - Akun login Total Control `Company Isolated` tidak tertulis di Pre-setup TC; akun disediakan tim FE.
