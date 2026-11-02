---
id: TC-AC-SU-E2E-190-badge-status-header-detail-user-dan-field-email-pending
title: "Detail User: Badge Status Header per Kondisi dan Field Email saat Pending Email Confirmation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-39
  - TC-AC-SU-41
coverage:
  web: automated
---

# Detail User: Badge Status Header per Kondisi dan Field Email saat Pending Email Confirmation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-39 | `Jane Smith` | `Jane Smith {runId}-190` | `janesmith+{runId}-190@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-39 | `Mike Tan` | `Mike Tan {runId}-190` | `miketan+{runId}-190@qwertysystem.net` | Pending Activation, Active |
| TC-AC-SU-39, 41 | `Rina Putri` | `Rina Putri {runId}-190` | `rina+{runId}-190@qwertysystem.net` | Pending Email Confirmation, Active; email baru pending `rinaputri+{runId}-190@qwertysystem.net` |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-39: Badge status di header Detail User per kondisi

1. Ketik Search `Jane Smith {runId}-190`, tekan Enter
2. Klik Name `Jane Smith {runId}-190`
3. Verifikasi header `Jane Smith {runId}-190`: badge `Inactive` (danger)
4. Verifikasi header `Jane Smith {runId}-190`: switch berlabel `Inactive`
5. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
6. Ganti isi kotak search dengan `Mike Tan {runId}-190`, tekan Enter
7. Klik Name `Mike Tan {runId}-190`
8. Verifikasi header `Mike Tan {runId}-190`: badge `Active` (success)
9. Verifikasi header `Mike Tan {runId}-190`: badge `Pending Activation` (warning)
10. Verifikasi header `Mike Tan {runId}-190`: tombol `Resend Activation Email`
11. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
12. Ganti isi kotak search dengan `Rina Putri {runId}-190`, tekan Enter
13. Klik Name `Rina Putri {runId}-190`
14. Verifikasi header `Rina Putri {runId}-190`: badge `Active` (success)
15. Verifikasi header `Rina Putri {runId}-190`: badge `Pending Email Confirmation` (warning)
16. Verifikasi header `Rina Putri {runId}-190`: tombol `Resend Confirmation Email`

### TC-AC-SU-41: Field Email Detail User saat Pending Email Confirmation

17. Amati field Email pada General Information `Rina Putri {runId}-190`
18. Verifikasi field Email bernilai `rina+{runId}-190@qwertysystem.net`
19. Verifikasi di sebelah nilai Email tampil teks `Pending email change to rinaputri+{runId}-190@qwertysystem.net`
20. Verifikasi teks pending berwarna on-surface/neutral
21. Verifikasi tidak ada tombol Cancel/Confirm pada field Email
22. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
23. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk Search sesudahnya), langkah 5, 11, dan 22 (kembali ke daftar), langkah 23 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Detail `Rina Putri {runId}-190` dipakai bersama oleh TC-AC-SU-39 dan TC-AC-SU-41 (kunjungan yang sama, tanpa membuka ulang).
- Temuan untuk QA:
  - TC-AC-SU-41 memakai email literal `rina@qwertysystem.net` dan `rinaputri@qwertysystem.net`; spec memakai email bersuffix `{runId}-190` sesuai S-12.
  - Nama user TC (`Jane Smith`, `Mike Tan`, `Rina Putri`) dipakai sebagai nama bersuffix `{runId}-190` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
