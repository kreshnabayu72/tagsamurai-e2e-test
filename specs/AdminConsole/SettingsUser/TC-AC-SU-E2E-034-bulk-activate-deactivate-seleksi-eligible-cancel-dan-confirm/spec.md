---
id: TC-AC-SU-E2E-034-bulk-activate-deactivate-seleksi-eligible-cancel-dan-confirm
title: "Bulk Activate dan Bulk Deactivate: Seleksi Semua Eligible, Dialog, Cancel Mempertahankan Seleksi, dan Confirm"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-117
  - TC-AC-SU-118
  - TC-AC-SU-119
  - TC-AC-SU-120
  - TC-AC-SU-121
coverage:
  web: automated
---

# Bulk Activate dan Bulk Deactivate: Seleksi Semua Eligible, Dialog, Cancel Mempertahankan Seleksi, dan Confirm

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-117, 118, 121 | `John Doe` | `John Doe {runId}-034` | `johndoe+{runId}-034@qwertysystem.net` | Activated, Active |
| TC-AC-SU-117, 118, 121 | `Rina Putri` | `Rina Putri {runId}-034` | `rinaputri+{runId}-034@qwertysystem.net` | Activated, Active |
| TC-AC-SU-119, 120 | `Jane Smith` | `Jane Smith {runId}-034` | `janesmith+{runId}-034@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-119, 120 | `Budi Santoso` | `Budi Santoso {runId}-034` | `budisantoso+{runId}-034@qwertysystem.net` | Activated, Inactive |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-117: Screening dialog Bulk Deactivate Users (2 baris, semua eligible)

1. Ketik Search `{runId}-034`, tekan Enter
2. Centang `John Doe {runId}-034` dan `Rina Putri {runId}-034`
3. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
4. Verifikasi Title `Deactivate Users` dengan `[×]`
5. Verifikasi dialog muncul: Title `Deactivate Users` dengan icon `[×]`; Body bullet `John Doe {runId}-034` dan `Rina Putri {runId}-034`, `These users will lose portal access.`, `Are you sure you want to deactivate them?`
6. Verifikasi tombol `[Cancel]` dan `[Deactivate]`
7. Verifikasi dialog `severity="danger"`
8. Verifikasi container bullet scrollable

### TC-AC-SU-121: Dialog bulk di-Cancel, seleksi tidak di-reset

9. Klik `[Cancel]` pada dialog Deactivate Users
10. Verifikasi dialog tertutup
11. Verifikasi tidak ada toast
12. Verifikasi Bulk Action Bar tetap tampil `2 Users selected`

### TC-AC-SU-118: Bulk Deactivate semua eligible, Confirm

13. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
14. Klik `[Deactivate]` pada dialog Deactivate Users
15. Verifikasi toast sukses: "Success, user has been deactivated."
16. Verifikasi switch `John Doe {runId}-034` dan `Rina Putri {runId}-034` OFF
17. Verifikasi Bulk Action Bar hilang
18. Verifikasi seleksi di-reset ke 0

### TC-AC-SU-119: Screening dialog Bulk Activate Users (2 baris, semua eligible)

19. Centang `Jane Smith {runId}-034` dan `Budi Santoso {runId}-034`
20. Klik `[Bulk Action ▾]` lalu pilih `Activate`
21. Verifikasi Title `Activate Users` dengan `[×]`
22. Verifikasi dialog muncul: Title `Activate Users` dengan icon `[×]`; Body bullet `Jane Smith {runId}-034` dan `Budi Santoso {runId}-034`, `These users will regain access to the portal.`, `Are you sure you want to activate them?`
23. Verifikasi tombol `[Cancel]` dan `[Activate]`
24. Verifikasi dialog `severity="info"`

### TC-AC-SU-120: Bulk Activate semua eligible, Confirm

25. Klik `[Activate]` pada dialog Activate Users
26. Verifikasi toast sukses: "Success, user has been activated."
27. Verifikasi switch `Jane Smith {runId}-034` dan `Budi Santoso {runId}-034` ON
28. Verifikasi seleksi di-reset
29. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 29 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Urutan TC dalam spec (S-05 dan S-10): 117, 121, 118, 119, 120. TC-AC-SU-121 memakai dialog dan seleksi yang masih terbuka dari TC-AC-SU-117; TC-AC-SU-118 memakai seleksi yang dipertahankan TC-AC-SU-121; TC-AC-SU-120 memakai dialog yang masih terbuka dari TC-AC-SU-119 (langkah "centang" dan "Bulk Action" TC-AC-SU-118 dan TC-AC-SU-120 dipenuhi oleh seleksi dan dialog dari blok sebelumnya agar tidak membuka dialog yang sama dua kali).
- Temuan untuk QA:
  - TC-AC-SU-118 dan TC-AC-SU-120 Post Condition "entri log Deactivate/Activate per user" tidak punya langkah observasi di TC ini dan tidak diasersi (S-01; "Section 5" dirujuk).
  - TC-AC-SU-120 butir a: toast "Success, user has been activated." memakai bentuk singular untuk dua user sesuai teks TC.
  - Nama user TC (`John Doe`, `Rina Putri`, `Jane Smith`, `Budi Santoso`) dipakai sebagai nama bersuffix `{runId}-034` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
