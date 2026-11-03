---
id: TC-AC-SU-E2E-189-row-action-menu-per-status-aktivasi-dan-ikon-severity
title: "User List: Isi Row Action Menu per Status Aktivasi serta Ikon dan Severity Row Actions"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-10
  - TC-AC-SU-663
coverage:
  web: automated
---

# User List: Isi Row Action Menu per Status Aktivasi serta Ikon dan Severity Row Actions

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-10, 663 | `Mike Tan` | `Mike Tan {runId}-189` | `miketan+{runId}-189@qwertysystem.net` | Pending Activation, Active |
| TC-AC-SU-10 | `Sarah Lee` | `Sarah Lee {runId}-189` | `sarahlee+{runId}-189@qwertysystem.net` | Pending Activation, Inactive |
| TC-AC-SU-10 | `John Doe` | `John Doe {runId}-189` | `johndoe+{runId}-189@qwertysystem.net` | Activated, Active |
| TC-AC-SU-10 | `Jane Smith` | `Jane Smith {runId}-189` | `janesmith+{runId}-189@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-10 | `Rina Putri` | `Rina Putri {runId}-189` | `rinaputri+{runId}-189@qwertysystem.net` | Pending Email Confirmation, Active |
| TC-AC-SU-10 | `Budi Santoso` | `Budi Santoso {runId}-189` | `budisantoso+{runId}-189@qwertysystem.net` | Pending Email Confirmation, Inactive |

- Aktor Total Control bukan target. Data TC-AC-SU-10 "sama dengan TC-AC-SU-9" di-seed ulang oleh spec ini (tanpa menumpang spec 005).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-10: Isi row action menu per kondisi status aktivasi

1. Ketik Search `{runId}-189`, tekan Enter
2. Klik (⋯) baris `Mike Tan {runId}-189`
3. Verifikasi menu `Mike Tan {runId}-189` (Pending Activation + Active): `Detail | Resend Activation Email`
4. Verifikasi menu `Mike Tan {runId}-189` tidak berisi opsi Activate/Deactivate, Edit, maupun Delete
5. Tutup menu row action dengan Esc
6. Klik (⋯) baris `Sarah Lee {runId}-189`
7. Verifikasi menu `Sarah Lee {runId}-189` (Pending Activation + Inactive): `Detail | Resend Activation Email`
8. Verifikasi menu `Sarah Lee {runId}-189` tidak berisi opsi Activate/Deactivate, Edit, maupun Delete
9. Tutup menu row action dengan Esc
10. Klik (⋯) baris `John Doe {runId}-189`
11. Verifikasi menu `John Doe {runId}-189` (Activated + Active): `Detail`
12. Verifikasi menu `John Doe {runId}-189` tidak berisi opsi Activate/Deactivate, Edit, maupun Delete
13. Tutup menu row action dengan Esc
14. Klik (⋯) baris `Jane Smith {runId}-189`
15. Verifikasi menu `Jane Smith {runId}-189` (Activated + Inactive): `Detail`
16. Verifikasi menu `Jane Smith {runId}-189` tidak berisi opsi Activate/Deactivate, Edit, maupun Delete
17. Tutup menu row action dengan Esc
18. Klik (⋯) baris `Rina Putri {runId}-189`
19. Verifikasi menu `Rina Putri {runId}-189` (Pending Email Confirmation + Active): `Detail | Resend Confirmation Email`
20. Verifikasi menu `Rina Putri {runId}-189` tidak berisi opsi Activate/Deactivate, Edit, maupun Delete
21. Tutup menu row action dengan Esc
22. Klik (⋯) baris `Budi Santoso {runId}-189`
23. Verifikasi menu `Budi Santoso {runId}-189` (Pending Email Confirmation + Inactive): `Detail | Resend Confirmation Email`
24. Verifikasi menu `Budi Santoso {runId}-189` tidak berisi opsi Activate/Deactivate, Edit, maupun Delete
25. Tutup menu row action dengan Esc

### TC-AC-SU-663: Ikon dan severity Row Actions User List

26. Buka row actions baris `Mike Tan {runId}-189`
27. Amati ikon dan warna tiap aksi
28. Verifikasi `Detail`: ikon `FileInfoLine`
29. Verifikasi `Detail`: severity dark
30. Verifikasi `Resend Activation Email`: ikon `MailSendLine`
31. Verifikasi `Resend Activation Email`: severity dark (bukan danger)
32. Tutup menu row action dengan Esc
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 5 dan 32 serta enam langkah tutup menu lain dengan Esc, langkah 33 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Temuan untuk QA:
  - TC-AC-SU-10 butir g ("tidak ada opsi Activate/Deactivate, Edit, maupun Delete di menu mana pun") diasersi pada tiap dari enam menu (satu `Verifikasi` per menu).
  - Nama user TC (`Mike Tan`, `Sarah Lee`, `John Doe`, `Jane Smith`, `Rina Putri`, `Budi Santoso`) dipakai sebagai nama bersuffix `{runId}-189` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
