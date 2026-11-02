---
id: TC-AC-RP-E2E-019-mobile-selection-mode-android
title: "Mobile Android: Selection Mode Role Detail, Checkbox CRUD Inert dan Ketuk Card"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-427
coverage:
  mobile: automated
---

# Mobile Android: Selection Mode Role Detail, Checkbox CRUD Inert dan Ketuk Card

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6). Spec hanya membaca dan memilih card secara lokal; tidak ada checkbox CRUD yang diubah dan tidak ada perubahan state server.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang (Tabel Data Uji Pre-setup #22), serta kemampuan tap, long press, dan mengetuk elemen UI. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Principal `Siti Nurhaliza`, `totalControlRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_TC_PASSWORD`. Login di aplikasi Android dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_RP_TC_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Data Pre-setup (identitas dirujuk lewat fixture `acRolePermission`, belum ada, dibuat pada tahap script): #11 (tree group Principal), #12 (user Standard `John Dohan`, `Maya Putri`), #15 (penugasan `Manage device master data` John Dohan C/R/U dan Maya Putri R), #22.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `+{runId}-019`, maupun cleanup.
- Kemampuan teknis (disediakan tim FE/BE; mekanismenya tidak tertulis di TC, PRD, atau LLD): membaca jumlah entri Changelog `Manage device master data` sebelum dan sesudah aksi (baseline, bagian 8b butir 10), dan memantau request jaringan yang dikirim aplikasi Android selama langkah 9 dan 10.
- Hook suite web (`beforeEach` pembuka halaman) berlaku untuk sesi browser; pada sesi aplikasi Android halaman dibuka lewat langkah spec ini, dan flag Guided Tooltip `guided_tooltip_seen_role-permission` untuk akun aktor disetel `true` oleh hook `before` suite (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-AC-RP-427: Baris checkbox CRUD inert selama selection mode dan ketuk card memilih atau melepas card

1. Buka halaman `Settings > Role & Permission` di aplikasi Android
2. Klik tab `System`
3. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
4. Catat jumlah entri Changelog `Manage device master data` sebagai baseline
5. Long press card `John Dohan`
6. Verifikasi mode checkbox aktif
7. Verifikasi card `John Dohan` tercentang
8. Verifikasi counter "1 Selected"
9. Ketuk checkbox U pada card `John Dohan`
10. Ketuk checkbox D pada card `Maya Putri`
11. Verifikasi nilai U pada card `John Dohan` tidak berubah
12. Verifikasi nilai D pada card `Maya Putri` tidak berubah
13. Verifikasi tidak ada request, dialog, maupun toast setelah langkah 9 dan 10
14. Verifikasi jumlah entri Changelog `Manage device master data` sama dengan baseline langkah 4
15. Ketuk card `Maya Putri`
16. Verifikasi card `Maya Putri` tercentang
17. Verifikasi counter "2 Selected"
18. Ketuk card `Maya Putri` sekali lagi
19. Verifikasi card `Maya Putri` terlepas
20. Verifikasi counter "1 Selected"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03, S-14): langkah 4 (baseline Changelog, aksi tanpa `Verifikasi`). Langkah 1 membuka halaman secara eksplisit karena hook `beforeEach` suite membuka halaman pada sesi web.
- Pembagian TC lintas spec: TC-AC-RP-426 (Pagination card list dan Select All, volume 105 user) ada di spec 139.
- Asersi TC-AC-RP-427 Expected b ("tidak ada request, dialog, toast, maupun entry baru di Changelog") adalah asersi state dengan baseline (S-12), bukan asersi absence pencatatan log kelas g; tidak ada spec absence untuk TC ini. Nilai U dan D yang tidak berubah (langkah 11 dan 12) menjadi anchor bahwa halaman Role Detail termuat sebelum absence dialog, toast, dan request (langkah 13) diasersi.
- Temuan untuk QA:
  - TC-AC-RP-427 Expected b tidak menyebut cara memantau "tidak ada request" di aplikasi native; spec memakainya sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint (S-13).
  - Post Condition TC-AC-RP-427 bernilai "-" sehingga tidak ada yang diasersi.
