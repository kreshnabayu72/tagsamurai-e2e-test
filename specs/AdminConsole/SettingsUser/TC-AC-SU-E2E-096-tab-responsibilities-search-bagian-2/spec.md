---
id: TC-AC-SU-E2E-096-tab-responsibilities-search-bagian-2
title: "Tab Responsibilities Search: Kolom Non-Searchable, Trim Query, dan Kolom Hidden"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-343
  - TC-AC-SU-344
  - TC-AC-SU-345
coverage:
  web: automated
---

# Tab Responsibilities Search: Kolom Non-Searchable, Trim Query, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-096`): target `Jane Smith {runId}-096` dengan 3 Pending Approval; requester `Budi Santoso {runId}-096`, `Rina Putri {runId}-096`, dan `PT Maju Bersama {runId}-096` (teks `PT Maju` hanya ada di kolom Requester).
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-096` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-096` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-096` | 05 Jun 2026 |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-096`, tekan Enter
3. Klik Name `Jane Smith {runId}-096` untuk membuka Detail User

### TC-AC-SU-343: Search kolom non-searchable tidak ikut dicari

4. Klik tab `Responsibilities (3)`
5. Klik icon Search
6. Ketik Search `02 Jun 2026`, tekan Enter
7. Verifikasi empty state dengan judul `No results found`
8. Klik icon Filter
9. Verifikasi field `Submission Date` tersedia di Filter Panel
10. Klik icon Filter untuk menutup Filter Panel
11. Klik `(←)` pada kotak Search

### TC-AC-SU-344: Search query di-trim saat Enter

12. Klik icon Search
13. Ketik Search `  ID-HALC  ` (spasi di awal dan akhir), tekan Enter
14. Verifikasi baris `ID-HALC` tampil (hasil sama dengan pencarian tanpa spasi)
15. Verifikasi baris `ID-WLT` tidak tampil
16. Verifikasi isi search box tidak berubah (spasi tetap terlihat)
17. Klik `(←)` pada kotak Search

### TC-AC-SU-345: Kolom yang di-hide tidak ikut dicari, lalu kembali searchable saat di-unhide

18. Klik header `⋯`
19. Hapus centang kolom `Requester` pada overlay Column Visibility
20. Klik icon Search
21. Ketik Search `PT Maju`, tekan Enter
22. Verifikasi empty state dengan judul `No results found`
23. Klik header `⋯`
24. Centang kolom `Requester` pada overlay Column Visibility
25. Ganti isi kotak search dengan `PT Maju`, tekan Enter
26. Verifikasi baris `ID-WLT` (Requester `PT Maju Bersama {runId}-096`) tampil kembali
27. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); `(←)` menutup Search; icon Filter pada TC-343 hanya memastikan field `Submission Date` tersedia (Expected b TC-343, "bila Filterable").
- Kolom `Requester` dipulihkan ke tampil pada TC-345 sehingga tidak ada konfigurasi kolom yang tersisa.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-096` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-343 Expected (b) menulis "(bila Filterable)"; TC-346 menyatakan `Submission Date` filterable sehingga spec mengasersi field itu ada.
