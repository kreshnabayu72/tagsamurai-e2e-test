---
id: TC-FA-PREF-E2E-078-defense-in-depth-role-matrix-negatif-save-ditolak-delete-update-group-manager-role-lain
title: "Defense-in-Depth Role Matrix Negatif: Request Langsung Save Preferences Ditolak Server 403 untuk Delete saja, Update saja, Group Manager, dan Role Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-515
  - TC-FA-PREF-516
  - TC-FA-PREF-517
  - TC-FA-PREF-518
coverage:
  web: automated
---

# Defense-in-Depth Role Matrix Negatif: Request Langsung Save Preferences Ditolak Server 403 untuk Delete saja, Update saja, Group Manager, dan Role Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI (hook `before`): Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Aktor request langsung (sesi API, tanpa UI; lihat butir "Sesi API aktor" di `suite.md`), email dan password:

  | Role (Precondition) | Email pre-setup | Password | TC |
  |---|---|---|---|
  | Manage accounting - Delete | `manageAccountingDeleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAD_PASSWORD` | TC-FA-PREF-515 |
  | Manage accounting - Update | `manageAccountingUpdateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAU_PASSWORD` | TC-FA-PREF-516 |
  | Group Manager (tanpa Manage accounting) | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | TC-FA-PREF-517 |
  | Role lain (tanpa Manage accounting) | `otherRoleFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_OT_PASSWORD` | TC-FA-PREF-518 |

- Env var `FA_TC_PASSWORD`, `FA_MAD_PASSWORD`, `FA_MAU_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_OT_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PC-1 (In-service Date Source tersimpan "Activation date"). Spec ini tidak menyimpan perubahan sehingga tidak ada seed ulang di antara TC.
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP memakai sesi API aktor, dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-515: Request langsung Save Preferences ditolak server untuk aktor Manage accounting - Delete

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
2. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Manage accounting - Delete, mengubah In-service Date Source menjadi Manual by Accounting
3. Verifikasi respons server 403 Forbidden
4. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
5. Verifikasi In-service Date Source tetap Activation date
6. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
7. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-516: Request langsung Save Preferences ditolak server untuk aktor Manage accounting - Update

8. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
9. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Manage accounting - Update, mengubah In-service Date Source menjadi Manual by Accounting
10. Verifikasi respons server 403 Forbidden
11. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
12. Verifikasi In-service Date Source tetap Activation date
13. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
14. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-517: Request langsung Save Preferences ditolak server untuk aktor Group Manager (tanpa Manage accounting)

15. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
16. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Group Manager, mengubah In-service Date Source menjadi Manual by Accounting
17. Verifikasi respons server 403 Forbidden
18. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
19. Verifikasi In-service Date Source tetap Activation date
20. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
21. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-518: Request langsung Save Preferences ditolak server untuk aktor Role lain (tanpa Manage accounting)

22. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
23. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Role lain, mengubah In-service Date Source menjadi Manual by Accounting
24. Verifikasi respons server 403 Forbidden
25. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
26. Verifikasi In-service Date Source tetap Activation date
27. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
28. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API; Role Matrix negatif dengan polaritas seragam (semua aktor ditolak). Request langsung memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`) dan tidak melewati browser; asersi 403 ada pada langkah Verifikasi respons.
- Sesi API Total Control untuk membaca ulang nilai hanya mengamati state; bukan konteks kedua kelas c (bagian 3 P-2).
- Post Condition semua TC ("tidak ada perubahan data maupun log") dicakup Expected butir b dan diasersi pada langkah nilai tersimpan dan jumlah baris log.
- Temuan untuk QA:
  - TC-FA-PREF-515 sampai 518 tidak menyebut nama env var password aktor; nama `FA_MAD_PASSWORD`, `FA_MAU_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_OT_PASSWORD` diusulkan spec dan perlu keputusan tim.
  - TC-FA-PREF-515 sampai 518 menyebut "klien HTTP dengan sesi aktor" tanpa endpoint; endpoint disediakan tim FE/BE (S-13).
  - TC-FA-PREF-516 menyebut aktor Update tanpa Read; kemampuan aktor itu login lewat API perlu dikonfirmasi tim FE/BE.
