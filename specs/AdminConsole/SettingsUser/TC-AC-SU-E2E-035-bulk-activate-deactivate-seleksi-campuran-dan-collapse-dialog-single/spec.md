---
id: TC-AC-SU-E2E-035-bulk-activate-deactivate-seleksi-campuran-dan-collapse-dialog-single
title: "Bulk Activate dan Bulk Deactivate: Dialog Dua Kelompok untuk Seleksi Campuran, Skipped, dan Collapse ke Dialog Single"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-122
  - TC-AC-SU-124
  - TC-AC-SU-126
  - TC-AC-SU-127
  - TC-AC-SU-128
coverage:
  web: automated
---

# Bulk Activate dan Bulk Deactivate: Dialog Dua Kelompok untuk Seleksi Campuran, Skipped, dan Collapse ke Dialog Single

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-122, 124, 127 | `John Doe` | `John Doe {runId}-035` | `johndoe+{runId}-035@qwertysystem.net` | Activated, Active |
| TC-AC-SU-122 | `Rina Putri` | `Rina Putri {runId}-035` | `rinaputri+{runId}-035@qwertysystem.net` | Activated, Active |
| TC-AC-SU-122, 124, 128 | `Jane Smith` | `Jane Smith {runId}-035` | `janesmith+{runId}-035@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-124 | `Budi Santoso` | `Budi Santoso {runId}-035` | `budisantoso+{runId}-035@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-126 | `Rudi Hartono` | `Rudi Hartono {runId}-035` | `rudihartono+{runId}-035@qwertysystem.net` | switch per-produk OFF dan nonaktif di Global Settings |
| TC-AC-SU-126 | `Jane Smith` | `Jane Smith {runId}-035-T126` | `janesmith+{runId}-035-T126@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-126 | `Budi Santoso` | `Budi Santoso {runId}-035-T126` | `budisantoso+{runId}-035-T126@qwertysystem.net` | Activated, Inactive |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-127: Bulk Deactivate dengan seleksi 1 baris, dialog collapse ke versi single

1. Ketik Search `{runId}-035`, tekan Enter
2. Centang `John Doe {runId}-035` saja
3. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
4. Verifikasi Title `Deactivate User` (singular)
5. Verifikasi Body bullet `John Doe {runId}-035`, `This user will lose portal access.`, `Are you sure you want to deactivate it?`
6. Verifikasi tombol `[Cancel]` dan `[Deactivate]`
7. Klik `[Cancel]` pada dialog, lalu klik icon `×` pada bulk action bar untuk membatalkan seleksi

### TC-AC-SU-128: Bulk Activate dengan seleksi 1 baris, dialog collapse ke versi single

8. Centang `Jane Smith {runId}-035` saja
9. Klik `[Bulk Action ▾]` lalu pilih `Activate`
10. Verifikasi Title `Activate User` (singular)
11. Verifikasi Body bullet `Jane Smith {runId}-035`, `This user will regain access to the portal.`, `Are you sure you want to activate it?`
12. Verifikasi tombol `[Cancel]` dan `[Activate]`
13. Klik `[Cancel]` pada dialog, lalu klik icon `×` pada bulk action bar untuk membatalkan seleksi

### TC-AC-SU-122: Bulk Deactivate seleksi campuran, dialog dua kelompok

14. Centang `John Doe {runId}-035`, `Rina Putri {runId}-035`, dan `Jane Smith {runId}-035`
15. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
16. Verifikasi Title `Deactivate Users`
17. Verifikasi Body: `The following will be deactivated:`, bullet `John Doe {runId}-035`, bullet `Rina Putri {runId}-035`, `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`, bullet `Jane Smith {runId}-035`, `Are you sure you want to continue?`
18. Verifikasi tombol `[Cancel]` dan `[Continue]`
19. Klik `[Cancel]` pada dialog, lalu klik icon `×` pada bulk action bar untuk membatalkan seleksi

### TC-AC-SU-124: Bulk Activate seleksi campuran, dialog dua kelompok dan Continue

20. Centang `Jane Smith {runId}-035`, `Budi Santoso {runId}-035`, dan `John Doe {runId}-035`
21. Klik `[Bulk Action ▾]` lalu pilih `Activate`
22. Verifikasi Body: `The following will be activated:`, bullet `Jane Smith {runId}-035`, bullet `Budi Santoso {runId}-035`, `The following will be skipped (already active, inactive in Global Settings, or no permission):`, bullet `John Doe {runId}-035`, `Are you sure you want to continue?`
23. Verifikasi tombol `[Cancel]` dan `[Continue]`
24. Klik `[Continue]`
25. Verifikasi toast sukses: "Success, user has been activated. Some items were skipped."

### TC-AC-SU-126: Bulk Activate, target nonaktif di Global Settings masuk kelompok skipped

26. Ganti isi kotak search dengan `{runId}-035`, tekan Enter
27. Centang `Rudi Hartono {runId}-035`, `Jane Smith {runId}-035-T126`, dan `Budi Santoso {runId}-035-T126`
28. Klik `[Bulk Action ▾]` lalu pilih `Activate`
29. Verifikasi kelompok skipped berisi `Rudi Hartono {runId}-035`
30. Klik `[Continue]`
31. Verifikasi toast sukses: "Success, user has been activated. Some items were skipped."
32. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16; berlaku juga untuk Search sesudahnya), langkah 7 dan langkah tutup dialog serta batalkan seleksi lainnya (pemulihan state sebelum TC berikutnya, S-09), langkah 32 (reset Search).
- Urutan TC dalam spec (S-10): 127, 128, 122 (hanya dialog), lalu 124 dan 126 (Continue mengubah status). Dialog dan seleksi tiap TC dibersihkan sebelum TC berikutnya.
- Temuan untuk QA:
  - TC-AC-SU-124 langkah 3 "Verifikasi dialog" dan TC-AC-SU-126 langkah 3 diperlakukan sebagai bagian aksi dan diasersi lewat Expected (isi dialog, kelompok skipped).
  - TC-AC-SU-122, 124, 126: Post Condition (log, status akhir) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-AC-SU-126 memakai `Jane Smith` dan `Budi Santoso` yang sudah Active setelah TC-AC-SU-124; spec memakai seed terpisah (suffix `-T126`).
  - Nama user TC (`John Doe`, `Rina Putri`, `Jane Smith`, `Budi Santoso`, `Rudi Hartono`) dipakai sebagai nama bersuffix `{runId}-035` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
