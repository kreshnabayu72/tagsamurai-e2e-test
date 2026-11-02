---
id: TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role
title: "Defense-in-depth: Request Langsung oleh Read Only dan Manage user and role Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-371
  - TC-AC-RP-372
  - TC-AC-RP-373
  - TC-AC-RP-374
  - TC-AC-RP-375
  - TC-AC-RP-376
  - TC-AC-RP-377
  - TC-AC-RP-443
coverage:
  web: automated
---

# Defense-in-depth: Request Langsung oleh Read Only dan Manage user and role Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata; request langsung ke endpoint modul lewat klien HTTP, tanpa browser)
- Akun aktor (urutan eksekusi; aktor pertama login di hook `before` spec ini, sisanya lewat langkah Ganti akun):

| Urutan | Aktor | Akun | Env password | TC |
|---|---|---|---|---|
| 1 | `Dewi Anggraini` (Read Only, Pre-setup #3) | `readOnlyRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_RO_PASSWORD` | TC-AC-RP-371, TC-AC-RP-443 |
| 2 | `Indra Kusuma` (Manage user and role R saja, Pre-setup #5) | `manageUserRoleR_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_R_PASSWORD` | TC-AC-RP-372, TC-AC-RP-375 |
| 3 | `Hendra Wijaya` (Manage user and role R+U, Pre-setup #4) | `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_MUR_U_PASSWORD` | TC-AC-RP-373, TC-AC-RP-374, TC-AC-RP-376, TC-AC-RP-377 |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal; `Region A`, `Region Jawa`, `Sumatera`), #12 (user Standard `Alex Tan`, `John Dohan`), #13 (pemegang Total Control `Rina Wijaya`), #14 (penugasan Group Manager), #15 (peran individual `John Dohan` pada `Manage device master data`; `Manage language`; `Manage hardware stock`), #17 (toggle `Manage allocation`: `Sumatera` OFF tersimpan), dan #25 (klien HTTP). Seluruh request spec ini ditolak server dan target aksi adalah data Pre-setup bernama literal sesuai TC; tidak ada Data Dinamis bersuffix `+{runId}-113` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): klien HTTP untuk request langsung ke endpoint modul (Pre-setup #25); sesi API aktor (dinyatakan di `suite.md`) untuk tiap akun pada tabel di atas; kemampuan membaca state data (nilai C/R/U/D peran individual user, tingkat akses user, nilai toggle `Require Approval`) lewat fixture BE untuk asersi "data tidak berubah".
- Pemulihan baseline: seluruh request ditolak sehingga data Pre-setup tidak diubah; kemampuan reset data Pre-setup yang disediakan tim FE/BE (dinyatakan di `suite.md`) dijalankan di hook `before` dan `after` spec ini sebagai jaring pengaman. Last Updated dan Modified By data Pre-setup tidak berubah.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_RP_RO_PASSWORD`, `AC_RP_MUR_R_PASSWORD`, `AC_RP_MUR_U_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Catat lewat fixture BE sebagai baseline: nilai Create `John Dohan` pada `Manage device master data`, nilai toggle `Manage allocation` `Sumatera`, tingkat akses `Alex Tan`, dan tingkat akses `Rina Wijaya`

### TC-AC-RP-371: Read Only mengirim Edit CRUD langsung

2. Sesi API `Dewi Anggraini`: kirim request Edit CRUD Create=true untuk `John Dohan` pada `Manage device master data`
3. Verifikasi respons request ditolak dengan status 403
4. Verifikasi pesan respons "You don't have permission to do this."
5. Verifikasi lewat fixture BE bahwa data peran `John Dohan` pada `Manage device master data` sama dengan baseline langkah 1

### TC-AC-RP-443: Read Only mengirim Toggle Require Approval langsung

6. Sesi API `Dewi Anggraini`: kirim request toggle `Manage allocation` `Sumatera` ON
7. Verifikasi respons request ditolak dengan status 403
8. Verifikasi pesan respons "You don't have permission to do this."
9. Verifikasi lewat fixture BE bahwa nilai toggle `Manage allocation` `Sumatera` tetap OFF

10. Ganti akun: login sesi API sebagai `Indra Kusuma` (`Spectra.env.AC_RP_MUR_R_PASSWORD`)

### TC-AC-RP-372: Manage user and role tanpa Update mengirim Assign User to Role langsung

11. Sesi API `Indra Kusuma`: kirim request Assign `Alex Tan` ke `Manage language`
12. Verifikasi respons request ditolak dengan status 403
13. Verifikasi pesan respons "You don't have permission to do this."

### TC-AC-RP-375: Manage user and role tanpa Update mengirim Toggle Require Approval langsung

14. Sesi API `Indra Kusuma`: kirim request toggle `Manage allocation` `Sumatera` ON
15. Verifikasi respons request ditolak dengan status 403
16. Verifikasi pesan respons "You don't have permission to do this."
17. Verifikasi lewat fixture BE bahwa nilai toggle `Manage allocation` `Sumatera` tetap OFF

18. Ganti akun: login sesi API sebagai `Hendra Wijaya` (`Spectra.env.AC_RP_MUR_U_PASSWORD`)

### TC-AC-RP-373: Manage user and role mengirim Assign Group Manager langsung

19. Sesi API `Hendra Wijaya`: kirim request Assign GM `John Dohan` di `Region A`
20. Verifikasi respons request ditolak dengan status 403
21. Verifikasi pesan respons "Only Default User or Total Control can assign Group Manager."

### TC-AC-RP-374: Manage user and role mengirim Assign Total Control langsung

22. Sesi API `Hendra Wijaya`: kirim request Assign Total Control `Alex Tan`
23. Verifikasi respons request ditolak dengan status 403
24. Verifikasi pesan respons "You don't have permission to do this."
25. Verifikasi lewat fixture BE bahwa tingkat akses `Alex Tan` sama dengan baseline langkah 1

### TC-AC-RP-376: Manage user and role mengirim Edit CRUD target TC langsung

26. Sesi API `Hendra Wijaya`: kirim request Edit CRUD Delete=false untuk `Rina Wijaya` pada `Manage preload`
27. Verifikasi respons request ditolak dengan status 403
28. Verifikasi pesan respons "You don't have permission to edit."
29. Verifikasi lewat fixture BE bahwa tingkat akses `Rina Wijaya` sama dengan baseline langkah 1

### TC-AC-RP-377: Manage user and role mengirim Edit CRUD GM-target langsung

30. Sesi API `Hendra Wijaya`: kirim request Edit CRUD Update=false untuk `Fajar Nugroho` pada `Manage partner` di `Region Jawa`
31. Verifikasi respons request ditolak dengan status 403
32. Verifikasi pesan respons "You don't have permission to edit."

## Notes

- K-1: TC-AC-RP-371 sampai TC-AC-RP-377 dan TC-AC-RP-443 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap berada di spec FE+BE karena TC granular adalah sumber dan tiap TC tepat satu spec, walau isinya tumpang tindih dengan `tc-settings-role-permission-backend.md`; BE mencatatnya pada tingkat endpoint.
- Asersi hanya status respons, pesan respons, dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (S-03, S-07): langkah 1 (baseline state), langkah 10 dan 18 (Ganti akun sesi API, S-07). Urutan TC mengelompokkan TC per aktor agar ganti akun hanya dua kali (S-10): Read Only (TC-AC-RP-371, 443), Indra Kusuma (TC-AC-RP-372, 375), Hendra Wijaya (TC-AC-RP-373, 374, 376, 377).
- Temuan untuk QA:
  - TC-AC-RP-371: request Edit CRUD Create=true untuk `John Dohan` pada `Manage device master data`, sedangkan Pre-setup #15 sudah memberi `John Dohan` C/R/U; nilai Create sudah aktif sehingga "data tidak berubah" tidak membedakan penolakan dari no-op. Spec mengasersi dengan baseline langkah 1; QA diminta menentukan payload yang membedakan (mis. Delete=true).
  - TC-AC-RP-376: peran `Manage preload` tidak tercantum di Pre-setup #15 maupun daftar Global Role; spec mengikuti TC. Mohon konfirmasi nama peran.
  - TC-AC-RP-373, 372, 377 tidak menyatakan state data pada Expected; spec hanya mengasersi status dan pesan (S-02).
  - TC-AC-RP-372 sampai 377 dan 443 tidak menyatakan endpoint, method, atau body request; spec menulis aksi seperti di TC tanpa mengarang endpoint (S-13).
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
