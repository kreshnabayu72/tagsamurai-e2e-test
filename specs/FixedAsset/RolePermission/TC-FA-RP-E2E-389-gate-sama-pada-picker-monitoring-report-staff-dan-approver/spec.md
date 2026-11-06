---
id: TC-FA-RP-E2E-389-gate-sama-pada-picker-monitoring-report-staff-dan-approver
title: "Gate Home Group yang sama berlaku pada picker Monitoring & Report, Staff, dan Approver"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1228
coverage:
  web: automated
---

# Gate Home Group yang sama berlaku pada picker Monitoring & Report, Staff, dan Approver

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Hesti Rahma, Home Group `Logistics Warehouse`; Active, Activated), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`), dan #19 (penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal`).
- Kemampuan teknis (disediakan tim FE/BE lewat fixture BE, tanpa endpoint karangan): seed bersih precondition TC di hook `before` berupa Hesti Rahma tanpa penugasan Role Transaksi pada node mana pun (dipakai sebagai precondition TC, tidak diasersi), serta pemulihan Pre-setup #17 dan #19 ke kondisi Tabel Data Uji Pre-setup TC di hook `after` sebagai cadangan.
- Data Dinamis: tidak ada data yang dibuat spec. Spec tidak menyimpan penugasan apa pun (tanpa klik `[Assign]`); tidak ada state yang berubah selain pembukaan dan penutupan popup.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture. Spec ini tidak login sebagai Hesti Rahma.

## Test Steps

### TC-FA-RP-1228: Gate Home Group yang sama berlaku pada picker Monitoring & Report, Staff, dan Approver

1. Klik Tab `Transaction Role`, klik node `Dock 1` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Monitoring & Report
3. Ketik Search `Hesti Rahma`, tekan Enter
4. Verifikasi Hesti Rahma ada di daftar picker section Monitoring & Report `Dock 1` (descendant constraint)
5. Tutup popup Assign lewat `[×]`
6. Klik `[+ Assign]` pada section Staff
7. Ketik Search `Hesti Rahma`, tekan Enter
8. Verifikasi Hesti Rahma ada di daftar picker section Staff `Dock 1` (descendant constraint)
9. Tutup popup Assign lewat `[×]`
10. Klik `[+ Assign]` pada section Approver
11. Ketik Search `Hesti Rahma`, tekan Enter
12. Verifikasi Hesti Rahma ada di daftar picker section Approver `Dock 1` (descendant constraint)
13. Tutup popup Assign lewat `[×]`
14. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
15. Klik `[+ Assign]` pada section Monitoring & Report
16. Ketik Search `Hesti Rahma`, tekan Enter
17. Verifikasi empty state `No results found` tampil sehingga Hesti Rahma tidak ada di daftar picker section Monitoring & Report `Data Center` (di luar constraint)
18. Tutup popup Assign lewat `[×]`
19. Klik `[+ Assign]` pada section Staff
20. Ketik Search `Hesti Rahma`, tekan Enter
21. Verifikasi empty state `No results found` tampil sehingga Hesti Rahma tidak ada di daftar picker section Staff `Data Center` (di luar constraint)
22. Tutup popup Assign lewat `[×]`
23. Klik `[+ Assign]` pada section Approver
24. Ketik Search `Hesti Rahma`, tekan Enter
25. Verifikasi empty state `No results found` tampil sehingga Hesti Rahma tidak ada di daftar picker section Approver `Data Center` (di luar constraint)
26. Tutup popup Assign lewat `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 26 langkah.
- Langkah penghubung (S-03): langkah 1 dan 14 (navigasi Tab, node, sub-tab), langkah 2, 6, 10, 15, 19, dan 23 (membuka popup Assign pada tiap section), dan langkah 5, 9, 13, 18, 22, dan 26 (menutup popup, S-09). Langkah 3, 7, 11, 16, 20, dan 24 adalah Search nama kandidat di Table User Picker yang dapat memuat lebih dari satu halaman (R-16, R-22).
- Expected a dan b TC ("ketiga section") dipecah satu `Verifikasi` per section (langkah 4, 8, 12 untuk `Dock 1`; langkah 17, 21, 25 untuk `Data Center`) agar tiap section dapat gagal sendiri (S-01).
- Asersi absence langkah 17, 21, dan 25 memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); langkah 4, 8, dan 12 membuktikan pada sesi dan user yang sama bahwa Hesti Rahma muncul di picker ketiga section bila node memenuhi constraint, sehingga hasil kosong bukan karena user tidak dimuat. Spec tidak menyimpan penugasan, tanpa asersi log (S-05).
- Spec ini 26 langkah, di bawah smell 35 langkah.
- Temuan untuk QA:
  - NC-20 / Open Item #9 (menunggu PM): arah gate Home Group sebagai constraint belum dikonfirmasi PM; bila PM menetapkan lain, Expected 1228.a dan 1228.b usang.
  - TC-FA-RP-1228 tidak memuat asersi preview scope popup dan PRD tidak memuat locator preview scope; spec tidak mengasersinya. Teks empty state `No results found` mengikuti pola picker pada spec lain di suite ini; TC hanya menyebut "tidak ada di daftar picker".
  - Email Hesti Rahma tidak tertulis di Pre-setup #17; spec ini tidak login sebagai Hesti Rahma. Bila spec lain memakai sesinya, kredensial lewat env `FA_HESTI_PASSWORD` (terdaftar di `suite.md`), tanpa password di spec atau fixture.
  - Precondition TC-FA-RP-1228 ("tanpa penugasan Role Transaksi") tidak menyebut cara membentuknya; spec menetapkannya lewat fixture BE yang disediakan tim FE/BE (kemampuan seeding dan pemulihan Pre-setup #17 belum punya nama di Pre-setup).
  - Picker Approver pada TC-FA-RP-315 menyaring user bukan Active dan Activated serta Read Only; Hesti Rahma Active, Activated (Pre-setup #17) sehingga tidak bentrok dengan Expected 1228.a.
  - Post Condition TC-FA-RP-1228 kosong ("-").
