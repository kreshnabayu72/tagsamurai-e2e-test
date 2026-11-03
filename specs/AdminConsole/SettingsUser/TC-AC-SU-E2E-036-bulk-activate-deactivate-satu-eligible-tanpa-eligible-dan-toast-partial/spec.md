---
id: TC-AC-SU-E2E-036-bulk-activate-deactivate-satu-eligible-tanpa-eligible-dan-toast-partial
title: "Bulk Activate dan Bulk Deactivate: Satu Baris Eligible, Tanpa Baris Eligible (Dialog Blok), dan Toast Partial"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-123
  - TC-AC-SU-129
  - TC-AC-SU-652
coverage:
  web: automated
---

# Bulk Activate dan Bulk Deactivate: Satu Baris Eligible, Tanpa Baris Eligible (Dialog Blok), dan Toast Partial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis tambahan: pengamatan request jaringan yang keluar dari browser (ada atau tidaknya request ke server) disediakan tim FE; endpoint tidak dikarang di spec (S-13).
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-123, 129, 652 | `John Doe` | `John Doe {runId}-036` | `johndoe+{runId}-036@qwertysystem.net` | Activated, Active |
| TC-AC-SU-123 | `Rina Putri` | `Rina Putri {runId}-036` | `rinaputri+{runId}-036@qwertysystem.net` | Activated, Active |
| TC-AC-SU-123, 129 | `Jane Smith` | `Jane Smith {runId}-036` | `janesmith+{runId}-036@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-652 | `Rudi Hartono` | `Rudi Hartono {runId}-036` | `rudihartono+{runId}-036@qwertysystem.net` | switch per-produk OFF dan nonaktif di Global Settings |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-129: Bulk Deactivate seleksi 2 baris dengan hanya 1 baris eligible, tetap varian dua kelompok

1. Ketik Search `{runId}-036`, tekan Enter
2. Centang `John Doe {runId}-036` dan `Jane Smith {runId}-036`
3. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
4. Verifikasi dialog tidak collapse ke single: Title `Deactivate Users`
5. Verifikasi kelompok diproses berisi bullet `John Doe {runId}-036`
6. Verifikasi kelompok skipped (`already inactive`) berisi bullet `Jane Smith {runId}-036`
7. Verifikasi penutup `Are you sure you want to continue?` dengan tombol `[Cancel]` dan `[Continue]`
8. Klik `[Cancel]` pada dialog, lalu klik icon `×` pada bulk action bar untuk membatalkan seleksi

### TC-AC-SU-652: Bulk Activate tanpa baris eligible, dialog blok, seleksi dipertahankan

9. Centang `John Doe {runId}-036` dan `Rudi Hartono {runId}-036`
10. Klik `[Bulk Action ▾]` lalu pilih `Activate`
11. Verifikasi dialog blok Title `Cannot Activate Users` dengan `[×]`
12. Verifikasi body `None of the selected users can be activated (already active, inactive in Global Settings, or no permission):` dengan bullet `John Doe {runId}-036` dan bullet `Rudi Hartono {runId}-036`
13. Verifikasi tombol tunggal `[OK]`
14. Verifikasi tidak ada dialog konfirmasi `Activate Users`
15. Verifikasi tidak ada request ke server
16. Verifikasi tidak ada toast
17. Klik `[OK]`
18. Verifikasi dialog tertutup
19. Verifikasi Bulk Action Bar tetap tampil `2 Users selected`
20. Batalkan centang `John Doe {runId}-036`
21. Klik `[Bulk Action ▾]` lalu pilih `Activate`
22. Verifikasi dialog blok Title `Cannot Activate User` (singular)
23. Verifikasi body `This user cannot be activated (already active, inactive in Global Settings, or no permission):` dengan bullet `Rudi Hartono {runId}-036`
24. Verifikasi tombol `[OK]`
25. Klik `[OK]`, lalu klik icon `×` pada bulk action bar untuk membatalkan seleksi

### TC-AC-SU-123: Bulk Deactivate seleksi campuran, Continue, toast partial

26. Centang `John Doe {runId}-036`, `Rina Putri {runId}-036`, dan `Jane Smith {runId}-036`
27. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
28. Klik `[Continue]`
29. Verifikasi toast sukses: "Success, user has been deactivated. Some items were skipped."
30. Verifikasi switch `John Doe {runId}-036` dan `Rina Putri {runId}-036` OFF
31. Verifikasi switch `Jane Smith {runId}-036` tetap OFF
32. Verifikasi seleksi di-reset termasuk baris yang di-skip
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 8 dan 25 (tutup dialog dan batalkan seleksi sebelum TC berikutnya, S-09), langkah 33 (reset Search).
- Urutan TC dalam spec (S-10): 129 dan 652 (tanpa mengubah status), lalu 123 (Continue mengubah status).
- Temuan untuk QA:
  - TC-AC-SU-652 butir b "tidak ada request ke server" butuh pengamatan request jaringan yang tidak disebut TC; disediakan tim FE (lihat Prerequisites).
  - TC-AC-SU-652 mensyaratkan `Rudi Hartono` "Inactive per-produk dan nonaktif di Global Settings"; spec men-seed sebagai user milik spec.
  - TC-AC-SU-123 dan TC-AC-SU-129 Post Condition (entri log, status akhir) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Nama user TC (`John Doe`, `Rina Putri`, `Jane Smith`, `Rudi Hartono`) dipakai sebagai nama bersuffix `{runId}-036` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
