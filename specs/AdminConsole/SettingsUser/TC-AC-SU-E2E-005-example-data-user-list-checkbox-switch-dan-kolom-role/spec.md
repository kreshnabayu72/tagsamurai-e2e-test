---
id: TC-AC-SU-E2E-005-example-data-user-list-checkbox-switch-dan-kolom-role
title: "Example Data User List: Checkbox, Switch Active, dan Kolom Role per Kondisi Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-9
coverage:
  web: automated
---

# Example Data User List: Checkbox, Switch Active, dan Kolom Role per Kondisi Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-9 | `John Doe` | `John Doe {runId}-005` | `johndoe+{runId}-005@qwertysystem.net` | Activated, Active, 3 role aktif |
| TC-AC-SU-9 | `Jane Smith` | `Jane Smith {runId}-005` | `janesmith+{runId}-005@qwertysystem.net` | Activated, Inactive, 2 role aktif |
| TC-AC-SU-9 | `Mike Tan` | `Mike Tan {runId}-005` | `miketan+{runId}-005@qwertysystem.net` | Pending Activation, Active, 1 role aktif |
| TC-AC-SU-9 | `Sarah Lee` | `Sarah Lee {runId}-005` | `sarahlee+{runId}-005@qwertysystem.net` | Pending Activation, Inactive, 0 role aktif |
| TC-AC-SU-9 | `Rina Putri` | `Rina Putri {runId}-005` | `rinaputri+{runId}-005@qwertysystem.net` | Pending Email Confirmation, Active, Total Control |
| TC-AC-SU-9 | `Budi Santoso` | `Budi Santoso {runId}-005` | `budisantoso+{runId}-005@qwertysystem.net` | Pending Email Confirmation, Inactive, 1 role aktif |

- Baris Default User entitas (Pre-setup #1, TC permanen) dicari lewat Search atas emailnya dan tidak diubah. Aktor Total Control bukan Default User.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-9: Example Data User List: checkbox, switch, kolom Role per kondisi

1. Ketik Search `{runId}-005`, tekan Enter
2. Amati kolom Checkbox, Active, dan Role pada tiap baris seed
3. Verifikasi `John Doe {runId}-005`: checkbox enabled
4. Verifikasi `John Doe {runId}-005`: switch ON enabled
5. Verifikasi `John Doe {runId}-005`: kolom Role `3 roles`
6. Verifikasi `Jane Smith {runId}-005`: checkbox enabled
7. Verifikasi `Jane Smith {runId}-005`: switch OFF enabled
8. Verifikasi `Jane Smith {runId}-005`: kolom Role `2 roles`
9. Verifikasi `Mike Tan {runId}-005`: checkbox enabled
10. Verifikasi `Mike Tan {runId}-005`: switch ON enabled
11. Verifikasi `Mike Tan {runId}-005`: kolom Role `1 role`
12. Verifikasi `Sarah Lee {runId}-005`: checkbox enabled
13. Verifikasi `Sarah Lee {runId}-005`: switch OFF enabled
14. Verifikasi `Sarah Lee {runId}-005`: kolom Role `0 roles`
15. Verifikasi `Rina Putri {runId}-005`: checkbox enabled
16. Verifikasi `Rina Putri {runId}-005`: switch ON enabled
17. Verifikasi `Rina Putri {runId}-005`: kolom Role badge `Total Control`
18. Verifikasi `Budi Santoso {runId}-005`: checkbox enabled
19. Verifikasi `Budi Santoso {runId}-005`: switch OFF enabled
20. Verifikasi `Budi Santoso {runId}-005`: kolom Role `1 role`
21. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
22. Verifikasi Default User: checkbox tampil namun disabled
23. Verifikasi Default User: switch ON tampil namun disabled
24. Verifikasi Default User: kolom Role badge `Total Control`
25. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec agar tabel berisi user seed, R-16), langkah 21 (Search untuk menemukan baris Default User lewat email Pre-setup #1, R-16), langkah 25 (reset Search). Layar awal dibuka hook `beforeEach` suite sehingga langkah "Buka Settings > User" TC tidak diulang.
- Temuan untuk QA:
  - TC-AC-SU-9 menulis Default User sebagai "TC permanen" tanpa email; spec menemukannya lewat email Pre-setup #1 dan mengasumsikan itu baris Default User yang dimaksud.
  - Nama user TC (`John Doe`, `Jane Smith`, `Mike Tan`, `Sarah Lee`, `Rina Putri`, `Budi Santoso`) dipakai sebagai nama bersuffix `{runId}-005` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
  - Jumlah role (`3 roles`, `2 roles`, `1 role`, `0 roles`) dan jenis role yang di-seed tidak disebut TC; nilai seed ditentukan tim FE/BE sehingga label jumlah sesuai.
