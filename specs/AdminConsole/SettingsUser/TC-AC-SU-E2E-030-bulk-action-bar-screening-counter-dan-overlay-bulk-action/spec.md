---
id: TC-AC-SU-E2E-030-bulk-action-bar-screening-counter-dan-overlay-bulk-action
title: "Bulk Action Bar: Screening, Overlay Bulk Action per Komposisi Seleksi, dan Counter Realtime"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-105
  - TC-AC-SU-106
  - TC-AC-SU-107
  - TC-AC-SU-108
  - TC-AC-SU-109
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Overlay Bulk Action per Komposisi Seleksi, dan Counter Realtime

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-105, 106, 107, 109 | `John Doe` | `John Doe {runId}-030` | `johndoe+{runId}-030@qwertysystem.net` | Activated, Active |
| TC-AC-SU-106, 108, 109 | `Jane Smith` | `Jane Smith {runId}-030` | `janesmith+{runId}-030@qwertysystem.net` | Activated, Inactive |
| TC-AC-SU-106 | `Mike Tan` | `Mike Tan {runId}-030` | `miketan+{runId}-030@qwertysystem.net` | Pending Activation, Active |
| TC-AC-SU-107 | `Rina Putri` | `Rina Putri {runId}-030` | `rinaputri+{runId}-030@qwertysystem.net` | Activated, Active (bukan Pending Activation) |
| TC-AC-SU-108 | `Budi Santoso` | `Budi Santoso {runId}-030` | `budisantoso+{runId}-030@qwertysystem.net` | Activated, Inactive |

- Total baris hasil Search atas suffix spec adalah 5 (N = 5 dari seeding, bagian 8b butir 10); Default User dan aktor tidak ikut karena tidak memuat suffix.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-105: Screening Bulk Action Bar saat 1 baris dicentang

1. Ketik Search `{runId}-030`, tekan Enter
2. Centang checkbox baris `John Doe {runId}-030`
3. Verifikasi Bulk Action Bar muncul di atas tabel
4. Verifikasi Bulk Action Bar rata kiri
5. Verifikasi Bulk Action Bar sejajar TableTools
6. Verifikasi urutan elemen Bulk Action Bar: `[Bulk Action ▾]` | `1 User selected` | `[Select All (5 records)]` | icon `×`
7. Verifikasi `[N]` = 5, total baris match filter aktif tanpa baris checkbox Disabled
8. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-106: Screening overlay Bulk Action, seleksi campuran Active, Inactive, Pending Activation

9. Centang `John Doe {runId}-030`, `Jane Smith {runId}-030`, dan `Mike Tan {runId}-030`
10. Klik `[Bulk Action ▾]`
11. Verifikasi overlay menampilkan `Activate` (icon CloseLine)
12. Verifikasi overlay menampilkan `Deactivate` (icon CheckLine)
13. Verifikasi overlay tidak berisi `Resend Activation Email` maupun `Resend Confirmation Email`
14. Tutup overlay dengan Esc, lalu klik icon `×` pada Bulk Action Bar

### TC-AC-SU-107: Overlay Bulk Action, seleksi semua Active menyembunyikan Activate

15. Centang `John Doe {runId}-030` dan `Rina Putri {runId}-030`
16. Klik `[Bulk Action ▾]`
17. Verifikasi hanya `Deactivate` tampil
18. Verifikasi `Activate` Hidden
19. Verifikasi `Resend Activation Email` Hidden
20. Tutup overlay dengan Esc, lalu klik icon `×` pada Bulk Action Bar

### TC-AC-SU-108: Overlay Bulk Action, seleksi semua Inactive menyembunyikan Deactivate

21. Centang `Jane Smith {runId}-030` dan `Budi Santoso {runId}-030`
22. Klik `[Bulk Action ▾]`
23. Verifikasi `Activate` tampil
24. Verifikasi `Deactivate` Hidden
25. Tutup overlay dengan Esc, lalu klik icon `×` pada Bulk Action Bar

### TC-AC-SU-109: Counter Bulk Action Bar realtime singular/plural dan dismiss via ×

26. Centang `John Doe {runId}-030`
27. Verifikasi counter `1 User selected`
28. Centang `Jane Smith {runId}-030`
29. Verifikasi counter `2 Users selected`
30. Batalkan centang `Jane Smith {runId}-030`
31. Verifikasi counter `1 User selected`
32. Klik icon `×` pada Bulk Action Bar
33. Verifikasi seleksi dibatalkan
34. Verifikasi Bulk Action Bar hilang
35. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 8, 14, dan langkah tutup overlay dan batalkan seleksi lainnya (pemulihan state sebelum TC berikutnya, S-09), langkah 35 (reset Search).
- Temuan untuk QA:
  - TC-AC-SU-105 butir c: "[N] = total baris match filter aktif" diasersi sebagai N = 5 dari seeding (Search atas suffix); TC tidak menyebut filter yang dipakai.
  - TC-AC-SU-106 butir a menyebut `Activate` berikon CloseLine dan `Deactivate` berikon CheckLine (ikon tampak tertukar terhadap makna); spec mengasersi persis seperti TC.
  - Nama user TC (`John Doe`, `Jane Smith`, `Mike Tan`, `Rina Putri`, `Budi Santoso`) dipakai sebagai nama bersuffix `{runId}-030` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
