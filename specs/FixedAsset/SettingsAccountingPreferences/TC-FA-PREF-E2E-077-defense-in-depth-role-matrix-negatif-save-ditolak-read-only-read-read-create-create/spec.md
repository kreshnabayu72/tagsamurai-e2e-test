---
id: TC-FA-PREF-E2E-077-defense-in-depth-role-matrix-negatif-save-ditolak-read-only-read-read-create-create
title: "Defense-in-Depth Role Matrix Negatif: Request Langsung Save Preferences Ditolak Server 403 untuk Read Only, Manage accounting - Read, Read + Create, dan Create"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-230
  - TC-FA-PREF-511
  - TC-FA-PREF-512
  - TC-FA-PREF-513
  - TC-FA-PREF-514
coverage:
  web: automated
---

# Defense-in-Depth Role Matrix Negatif: Request Langsung Save Preferences Ditolak Server 403 untuk Read Only, Manage accounting - Read, Read + Create, dan Create

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI (hook `before`, dipakai membaca ulang nilai di TC-230): Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Aktor request langsung (sesi API, tanpa UI; lihat butir "Sesi API aktor" di `suite.md`), email dan password:

  | Role (Precondition) | Email pre-setup | Password | TC |
  |---|---|---|---|
  | Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-PREF-230, TC-FA-PREF-512 |
  | Manage accounting - Read | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAR_PASSWORD` | TC-FA-PREF-511 |
  | Manage accounting - Read + Create | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MARC_PASSWORD` | TC-FA-PREF-513 |
  | Manage accounting - Create | `manageAccountingCreateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAC_PASSWORD` | TC-FA-PREF-514 |

- Env var `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_MAR_PASSWORD`, `FA_MARC_PASSWORD`, dan `FA_MAC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-230 memakai PB-1 (Preferences nilai awal; In-service Date Source "Activation date") dan PB-2 (akun Chart of Accounts tersedia); TC-511 sampai 514 memakai PC-1 (In-service Date Source tersimpan "Activation date"). Nilai awal PB-1 dan PC-1 setara; spec ini tidak menyimpan perubahan sehingga tidak ada seed ulang di antara TC.
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP memakai sesi API aktor, dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-230: Permintaan langsung Save oleh Read Only ditolak server Forbidden

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
2. Kirim request langsung Save Preferences (fixture BE) dengan In-service Date Source = Manual by Accounting memakai sesi API Read Only
3. Verifikasi server menolak permintaan dengan Forbidden (403)
4. Buka kembali Settings > Accounting > Preferences pada sesi Total Control
5. Verifikasi In-service Date Source tetap "Activation date" pada tab Preferences
6. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
7. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada baris log baru)

### TC-FA-PREF-511: Request langsung Save Preferences ditolak server untuk aktor Manage accounting - Read

8. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
9. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Manage accounting - Read, mengubah In-service Date Source menjadi Manual by Accounting
10. Verifikasi respons server 403 Forbidden
11. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
12. Verifikasi In-service Date Source tetap Activation date
13. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
14. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-512: Request langsung Save Preferences ditolak server untuk aktor Read Only

15. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
16. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Read Only, mengubah In-service Date Source menjadi Manual by Accounting
17. Verifikasi respons server 403 Forbidden
18. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
19. Verifikasi In-service Date Source tetap Activation date
20. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
21. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-513: Request langsung Save Preferences ditolak server untuk aktor Manage accounting - Read + Create

22. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
23. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Manage accounting - Read + Create, mengubah In-service Date Source menjadi Manual by Accounting
24. Verifikasi respons server 403 Forbidden
25. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
26. Verifikasi In-service Date Source tetap Activation date
27. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
28. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-514: Request langsung Save Preferences ditolak server untuk aktor Manage accounting - Create

29. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS
30. Kirim request langsung Save Preferences dengan klien HTTP memakai sesi API Manage accounting - Create, mengubah In-service Date Source menjadi Manual by Accounting
31. Verifikasi respons server 403 Forbidden
32. Baca ulang nilai Preferences tersimpan memakai sesi API Total Control Rina Anggraini
33. Verifikasi In-service Date Source tetap Activation date
34. Hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
35. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API; Role Matrix negatif dengan polaritas seragam (semua aktor ditolak). Request langsung memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`) dan tidak melewati browser; asersi 403 ada pada langkah Verifikasi respons.
- Pelaku kedua (sesi API Total Control untuk membaca ulang nilai pada TC-511 sampai 514) hanya mengamati state; bukan konteks kedua kelas c (bagian 3 P-2).
- Post Condition semua TC ("tidak ada perubahan data maupun log") dicakup Expected butir b dan diasersi pada langkah nilai tersimpan dan jumlah baris log.
- Temuan untuk QA:
  - TC-FA-PREF-230 dan TC-FA-PREF-512 menguji aktor dan Expected yang sama (Read Only, In-service Date Source = Manual by Accounting); perbedaannya hanya seri fixture (PB-1 dan PC-1) dan cara membaca ulang (UI atau API).
  - TC-FA-PREF-511 sampai 514 tidak menyebut nama env var password aktor; nama `FA_RO_PASSWORD`, `FA_MAR_PASSWORD`, `FA_MARC_PASSWORD`, dan `FA_MAC_PASSWORD` diusulkan spec dan perlu keputusan tim.
  - TC-FA-PREF-511 sampai 514 menyebut "klien HTTP dengan sesi aktor" tanpa endpoint; endpoint disediakan tim FE/BE (S-13).
