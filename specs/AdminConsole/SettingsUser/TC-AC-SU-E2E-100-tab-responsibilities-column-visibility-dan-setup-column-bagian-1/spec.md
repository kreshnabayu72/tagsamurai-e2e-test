---
id: TC-AC-SU-E2E-100-tab-responsibilities-column-visibility-dan-setup-column-bagian-1
title: "Tab Responsibilities Column Visibility dan Setup Column: Screening, Ceklis, dan Drag Reorder"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-356
  - TC-AC-SU-357
  - TC-AC-SU-358
  - TC-AC-SU-359
coverage:
  web: automated
---

# Tab Responsibilities Column Visibility dan Setup Column: Screening, Ceklis, dan Drag Reorder

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-100`): target `Jane Smith {runId}-100` dengan 3 Pending Approval; requester `Budi Santoso {runId}-100`, `Rina Putri {runId}-100`, `PT Maju Bersama {runId}-100`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-100` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-100` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-100` | 05 Jun 2026 |
- Konfigurasi kolom Tab Responsibilities awal adalah default (tidak ada preferensi kolom tersimpan).
- Tabel kolom TC-358 (parameter langkah 23 sampai 26): ID, Transaction, Requester.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-100`, tekan Enter
3. Klik Name `Jane Smith {runId}-100` untuk membuka Detail User

### TC-AC-SU-356: Screening Overlay Column Visibility Tab Responsibilities

4. Klik tab `Responsibilities (3)`
5. Hover header kolom Actions `⋯`
6. Verifikasi tooltip `Column Visibility` tampil
7. Klik header `⋯`
8. Verifikasi overlay terbuka dengan tombol `[Setup Column]` di atas
9. Verifikasi daftar kolom urutan default: ID | Transaction | Requester | Submission Date
10. Verifikasi tiap kolom berupa checkbox checked dan enabled
11. Verifikasi drag handle tersedia pada tiap kolom
12. Tekan Esc untuk menutup overlay

### TC-AC-SU-357: Screening Popup Setup Column Tab Responsibilities

13. Klik header `⋯`
14. Klik `[Setup Column]`
15. Verifikasi header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon `(X)`
16. Verifikasi body popup: daftar ID | Transaction | Requester | Submission Date dengan checkbox checked dan enabled, drag handle, dan icon Pin
17. Verifikasi Live Preview menampilkan header dan isi sel sesuai tabel asli
18. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
19. Verifikasi footer tanpa `[Cancel]`
20. Klik icon `(X)` pada popup

### TC-AC-SU-358: Setup Column unceklis dan ceklis kolom lalu Save

21. Klik header `⋯`
22. Klik `[Setup Column]`
23. Hapus centang kolom pada tabel kolom TC-358
24. Verifikasi Live Preview menyembunyikan kolom tersebut
25. Centang kembali kolom tersebut
26. Verifikasi Live Preview menampilkan kembali kolom tersebut
27. Hapus centang kolom `Transaction`
28. Klik `[Save]`
29. Verifikasi kolom `Transaction` tidak tampil di tabel
30. Tekan F5
31. Klik tab `Responsibilities (3)`
32. Verifikasi kolom `Transaction` tetap tersembunyi
33. Klik header `⋯`, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-SU-359: Setup Column drag reorder kolom lalu Save

34. Klik header `⋯`
35. Klik `[Setup Column]`
36. Drag `Submission Date` ke posisi pertama
37. Drag `ID` ke posisi terakhir
38. Verifikasi Live Preview memuat `Submission Date` di posisi pertama
39. Verifikasi Live Preview memuat `ID` di posisi terakhir
40. Klik `[Save]`
41. Verifikasi tabel memakai urutan baru
42. Tekan F5
43. Klik tab `Responsibilities (3)`
44. Verifikasi tabel tetap memakai urutan baru
45. Klik header `⋯`, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

## Notes

- Langkah 23 sampai 26 diulang untuk tiap kolom pada tabel kolom TC-358 (8b butir 7); parameter ada di Prerequisites.
- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); Esc menutup overlay Column Visibility; `[Reset to Default]` lalu `[Save]` di akhir TC-358 dan TC-359 memulihkan konfigurasi (S-09); hook `after` memulihkan juga; langkah 31 dan 43 (klik tab `Responsibilities (3)` sesudah F5, karena PRD tidak menyatakan tab Detail yang aktif sesudah muat ulang).
- Alasan di atas ±35 langkah: keempat TC adalah Column Visibility dan Setup Column Tab Responsibilities dengan dataset sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-100` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-358 langkah 3 menyebut ID, Transaction, Requester tetapi tidak Submission Date; spec mengikuti TC.
  - PRD tidak menyatakan tab Detail User mana yang aktif sesudah F5; spec mengklik tab `Responsibilities (3)` sesudah tiap F5 sebelum asersi tabel.
