---
id: TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri
title: "Defense-in-depth: Request Langsung atas Default User, Diri Sendiri, dan oleh Aktor Default User Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-378
  - TC-AC-RP-379
  - TC-AC-RP-380
  - TC-AC-RP-381
  - TC-AC-RP-382
  - TC-AC-RP-383
  - TC-AC-RP-434
  - TC-AC-RP-438
coverage:
  web: automated
---

# Defense-in-depth: Request Langsung atas Default User, Diri Sendiri, dan oleh Aktor Default User Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata; request langsung ke endpoint modul lewat klien HTTP, tanpa browser)
- Akun aktor (urutan eksekusi; aktor pertama login di hook `before` spec ini, aktor kedua lewat langkah Ganti akun):

| Urutan | Aktor | Akun | Env password | TC |
|---|---|---|---|---|
| 1 | `Siti Nurhaliza` (Total Control Principal, Pre-setup #1) | `totalControlRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_TC_PASSWORD` | TC-AC-RP-378, 379, 380, 381, 382, 434, 438 |
| 2 | `Bambang Hartono` (Default User Principal, Pre-setup #2) | `defaultUserRP_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RP_DU_PASSWORD` | TC-AC-RP-383 |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #2 dan #13 (`Bambang Hartono`, Default User sekaligus pemegang Total Control), #11 (tree group Principal; `Region A`), #12 (user Standard), #14 (penugasan Group Manager), #17 (approver `Manage TAG stock`: `Sarah Kimura`), dan #25 (klien HTTP). Seluruh request spec ini ditolak server dan target aksi adalah data Pre-setup bernama literal sesuai TC; tidak ada Data Dinamis bersuffix `+{runId}-114` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): klien HTTP untuk request langsung (Pre-setup #25); sesi API aktor (dinyatakan di `suite.md`) untuk kedua akun; kemampuan membaca state data lewat fixture BE (tingkat akses `Siti Nurhaliza`, penugasan Group Manager `Siti Nurhaliza`, daftar approver `Manage TAG stock`).
- Pemulihan baseline: seluruh request ditolak sehingga data Pre-setup tidak diubah; kemampuan reset data Pre-setup yang disediakan tim FE/BE (dinyatakan di `suite.md`) dijalankan di hook `before` dan `after` spec ini sebagai jaring pengaman. Last Updated dan Modified By data Pre-setup tidak berubah.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_DU_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Catat lewat fixture BE sebagai baseline: tingkat akses `Siti Nurhaliza`, penugasan Group Manager `Siti Nurhaliza`, dan daftar approver `Manage TAG stock`

### TC-AC-RP-378: Edit CRUD target Default User langsung

2. Sesi API `Siti Nurhaliza`: kirim request Edit CRUD untuk `Bambang Hartono`
3. Verifikasi respons request ditolak dengan status 403
4. Verifikasi pesan respons "Default User cannot be modified."

### TC-AC-RP-379: Remove Total Control Default User langsung

5. Sesi API `Siti Nurhaliza`: kirim request Remove Total Control `Bambang Hartono`
6. Verifikasi respons request ditolak dengan status 403
7. Verifikasi pesan respons "Default User cannot be modified."

### TC-AC-RP-380: Assign User to Role memuat aktor sendiri langsung

8. Sesi API `Siti Nurhaliza`: kirim request Assign `Siti Nurhaliza` ke `Manage language`
9. Verifikasi respons request ditolak dengan status 403
10. Verifikasi pesan respons "You can't manage your own account from here."

### TC-AC-RP-381: Assign Total Control memuat aktor sendiri langsung

11. Sesi API `Siti Nurhaliza`: kirim request Assign Total Control yang memuat `Siti Nurhaliza` (aktor sendiri)
12. Verifikasi respons request ditolak dengan status 403
13. Verifikasi pesan respons "You can't manage your own account from here."
14. Verifikasi lewat fixture BE bahwa tingkat akses `Siti Nurhaliza` sama dengan baseline langkah 1

### TC-AC-RP-382: Edit CRUD diri sendiri langsung

15. Sesi API `Siti Nurhaliza`: kirim request Edit CRUD untuk `Siti Nurhaliza`
16. Verifikasi respons request ditolak dengan status 403
17. Verifikasi pesan respons "You can't manage your own account from here."

### TC-AC-RP-434: Assign GM ke diri sendiri oleh aktor Total Control langsung

18. Sesi API `Siti Nurhaliza`: kirim request Assign GM `Siti Nurhaliza` di `Region A`
19. Verifikasi respons request ditolak dengan status 403
20. Verifikasi pesan respons "You can't manage your own account from here."
21. Verifikasi lewat fixture BE bahwa penugasan Group Manager `Siti Nurhaliza` sama dengan baseline langkah 1 (`Siti Nurhaliza` tidak menjadi GM)

### TC-AC-RP-438: Assign Approver memuat aktor sendiri langsung

22. Sesi API `Siti Nurhaliza`: kirim request Assign Approver yang memuat `Siti Nurhaliza` pada `Manage TAG stock`
23. Verifikasi respons request ditolak dengan status 403
24. Verifikasi pesan respons "You can't manage your own account from here."
25. Verifikasi lewat fixture BE bahwa daftar approver `Manage TAG stock` sama dengan baseline langkah 1 (`Siti Nurhaliza` tidak menjadi approver)

26. Ganti akun: login sesi API sebagai `Bambang Hartono` (`Spectra.env.AC_RP_DU_PASSWORD`)

### TC-AC-RP-383: Assign GM ke diri sendiri langsung oleh aktor Default User

27. Sesi API `Bambang Hartono`: kirim request Assign GM `Bambang Hartono` di `Region A`
28. Verifikasi respons request ditolak dengan status 403
29. Verifikasi pesan respons "Default User cannot be modified."

## Notes

- K-1: TC-AC-RP-378 sampai TC-AC-RP-383, TC-AC-RP-434, dan TC-AC-RP-438 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap berada di spec FE+BE karena TC granular adalah sumber dan tiap TC tepat satu spec, walau isinya tumpang tindih dengan `tc-settings-role-permission-backend.md`; BE mencatatnya pada tingkat endpoint.
- Asersi hanya status respons, pesan respons, dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (S-03, S-07): langkah 1 (baseline state) dan langkah 26 (Ganti akun sesi API, S-07). TC-AC-RP-383 (aktor Default User) diletakkan di akhir agar ganti akun hanya sekali (S-10).
- Temuan untuk QA:
  - TC-AC-RP-383: Expected memuat penjelasan dalam kurung tentang urutan `ACRP-LOGIC-11b`; spec hanya mengasersi status dan pesan, penjelasan tidak diasersi.
  - TC-AC-RP-434 dan TC-AC-RP-383: Expected menyatakan urutan prioritas pesan, bukan state tambahan; spec mengikuti pesan persis TC.
  - TC-AC-RP-378, 379, 380, 382, dan 383 tidak menyatakan state data pada Expected; spec tidak menambah asersi state (S-02).
  - TC-AC-RP-378 dan 382 tidak menyebut nilai CRUD yang dikirim ("Kirim request Edit CRUD untuk ..."), dan TC-AC-RP-380, 381, 438 tidak menyebut body request lain; spec mengikuti TC tanpa mengarang payload (S-13).
  - TC-AC-RP-381, 434, dan 438: Expected "tidak ada perubahan tingkat akses", "tidak menjadi GM", dan "tidak menjadi approver" tidak menyebut keadaan awal; spec membandingkannya dengan baseline langkah 1.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
