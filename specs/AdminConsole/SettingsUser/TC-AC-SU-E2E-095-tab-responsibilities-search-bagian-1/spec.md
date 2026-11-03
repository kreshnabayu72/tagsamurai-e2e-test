---
id: TC-AC-SU-E2E-095-tab-responsibilities-search-bagian-1
title: "Tab Responsibilities Search: Siklus Interaksi Search Box dan Search Kelas Teks dan Badge"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-340
  - TC-AC-SU-341
  - TC-AC-SU-342
coverage:
  web: automated
---

# Tab Responsibilities Search: Siklus Interaksi Search Box dan Search Kelas Teks dan Badge

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-095`): target `Jane Smith {runId}-095` dengan 3 Pending Approval; requester `Budi Santoso {runId}-095`, `Rina Putri {runId}-095`, dan `PT Maju Bersama {runId}-095`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-095` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-095` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-095` | 05 Jun 2026 |
- Tabel Search TC-341 dan TC-342 (parameter langkah 27 sampai 32):
| No | Kolom | Keyword substring | Keyword huruf kapital | Baris yang tampil |
|---|---|---|---|---|
| 1 | ID | `alc-2026` | `ALC-2026` | `ID-HALC` |
| 2 | Requester | `budi` | `BUDI` | `ID-HALC` (Requester `Budi Santoso {runId}-095`) |
| 3 | Transaction | `wallet top` | `WALLET TOP` | `ID-WLT` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-095`, tekan Enter
3. Klik Name `Jane Smith {runId}-095` untuk membuka Detail User

### TC-AC-SU-340: Siklus interaksi Search box Tab Responsibilities

4. Klik tab `Responsibilities (3)`
5. Hover icon Search
6. Verifikasi tooltip `Search` tampil
7. Klik icon Search
8. Verifikasi input melebar dengan kursor auto-focus
9. Verifikasi placeholder `Search ID or requester...`
10. Ketik `ALC-2026` tanpa menekan Enter
11. Verifikasi icon `(✕)` muncul
12. Verifikasi tabel belum tersaring: baris `ID-WLT` masih tampil
13. Tekan Enter
14. Verifikasi baris `ID-HALC` dan `ID-LALC` tampil
15. Verifikasi baris `ID-WLT` tidak tampil
16. Klik icon `(✕)`
17. Verifikasi input kosong
18. Verifikasi search bar tetap terbuka
19. Verifikasi tabel tetap menampilkan hasil search terakhir (baris `ID-WLT` tidak tampil)
20. Tekan Enter pada input kosong
21. Verifikasi tabel kembali ke semua data (baris `ID-WLT` tampil)
22. Ketik Search `ALC-2026`, tekan Enter
23. Klik icon `(←)`
24. Verifikasi search bar collapse ke icon Search dengan keyword kosong
25. Verifikasi tabel langsung kembali ke semua data (baris `ID-WLT` tampil)

### TC-AC-SU-341 dan TC-AC-SU-342: Search per kolom kelas teks dan kelas badge

26. Klik icon Search
27. Ketik Search keyword substring pada kolom "Keyword substring" tabel Search TC-341 dan TC-342, tekan Enter
28. Verifikasi baris pada kolom "Baris yang tampil" tampil
29. Klik `✕` pada Search
30. Ketik Search keyword huruf kapital pada kolom "Keyword huruf kapital", tekan Enter
31. Verifikasi baris pada kolom "Baris yang tampil" tampil
32. Klik `✕` pada Search, tekan Enter
33. Klik `(←)` pada kotak Search

## Notes

- Langkah 27 sampai 32 diulang untuk tiap baris tabel Search TC-341 dan TC-342 (8b butir 7); parameter ada di Prerequisites. Baris 1 dan 2 adalah TC-341, baris 3 adalah TC-342; TC-341 dan TC-342 memiliki Expected yang sama bentuknya sehingga langkahnya satu blok.
- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); `(←)` menutup Search.
- Alasan di atas ±35 langkah: ketiga TC adalah Search Tab Responsibilities dengan dataset sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-095` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-341 mengasersi keyword `alc-2026` menampilkan baris `HALC-2026-0012` tanpa menyebut bahwa baris `LALC-2026-0044` ikut cocok; spec hanya mengasersi baris `ID-HALC` tampil.
