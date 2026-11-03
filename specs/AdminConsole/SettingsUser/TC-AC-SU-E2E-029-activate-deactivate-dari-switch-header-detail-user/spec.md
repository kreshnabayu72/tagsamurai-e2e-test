---
id: TC-AC-SU-E2E-029-activate-deactivate-dari-switch-header-detail-user
title: "Activate dan Deactivate dari Switch Header Detail User: Dialog, Toast, Label, Badge, dan Sinkron ke User List"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-90
  - TC-AC-SU-91
coverage:
  web: automated
---

# Activate dan Deactivate dari Switch Header Detail User: Dialog, Toast, Label, Badge, dan Sinkron ke User List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-90 | `Mike Tan` | `Mike Tan {runId}-029` | `miketan+{runId}-029@qwertysystem.net` | Activated, Active |
| TC-AC-SU-91 | `Jane Smith` | `Jane Smith {runId}-029` | `janesmith+{runId}-029@qwertysystem.net` | Activated, Inactive |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-90: Deactivate dari switch header Detail User, dialog dan hasil simetris dengan User List

1. Ketik Search `Mike Tan {runId}-029`, tekan Enter
2. Klik Name `Mike Tan {runId}-029`
3. Klik switch Active di header Detail (label `Active`)
4. Verifikasi dialog konfirmasi muncul: Title `Deactivate User` dengan icon `[×]`; Body bullet `Mike Tan {runId}-029`, `This user will lose portal access.`, `Are you sure you want to deactivate it?`; tombol `[Cancel]` (Text, Contrast) dan `[Deactivate]` (filled, danger)
5. Klik `[Deactivate]` pada dialog Deactivate User
6. Verifikasi toast sukses: "Success, user has been deactivated."
7. Verifikasi switch header OFF dengan label `Inactive`
8. Verifikasi status badge header `Inactive` (severity danger)
9. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
10. Verifikasi switch baris `Mike Tan {runId}-029` OFF di User List

### TC-AC-SU-91: Activate dari switch header Detail User

11. Ganti isi kotak search dengan `Jane Smith {runId}-029`, tekan Enter
12. Klik Name `Jane Smith {runId}-029`
13. Klik switch Active di header Detail
14. Verifikasi dialog muncul: Title `Activate User` dengan icon `[×]`; Body bullet `Jane Smith {runId}-029`, `This user will regain access to the portal.`, `Are you sure you want to activate it?`; tombol `[Cancel]` (Text, Contrast) dan `[Activate]` (filled, primary)
15. Klik `[Activate]` pada dialog Activate User
16. Verifikasi toast sukses: "Success, user has been activated."
17. Verifikasi switch header ON dengan label `Active`
18. Verifikasi badge `Active` (severity success)
19. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
20. Verifikasi switch baris `Jane Smith {runId}-029` ON di User List
21. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk Search sesudahnya), langkah 9 dan langkah kembali ke daftar berikutnya (kembali ke Settings > User untuk observasi Post Condition yang diberikan TC), langkah 21 (reset Search).
- Temuan untuk QA:
  - TC-AC-SU-90 langkah 2 ("Verifikasi dialog") dan butir a menyebut dialog "sama dengan dialog dari User List"; spec mengasersi isi dialog secara utuh sebagai satu elemen komposit (S-01).
  - Nama user TC (`Mike Tan`, `Jane Smith`) dipakai sebagai nama bersuffix `{runId}-029` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
