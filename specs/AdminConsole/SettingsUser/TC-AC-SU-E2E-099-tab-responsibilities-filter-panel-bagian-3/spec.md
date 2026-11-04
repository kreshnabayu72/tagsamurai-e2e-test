---
id: TC-AC-SU-E2E-099-tab-responsibilities-filter-panel-bagian-3
title: "Tab Responsibilities Filter Panel: Search di Dropdown, Search lalu Filter, dan Filter lalu Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-353
  - TC-AC-SU-354
  - TC-AC-SU-355
coverage:
  web: automated
---

# Tab Responsibilities Filter Panel: Search di Dropdown, Search lalu Filter, dan Filter lalu Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-099`): target `Jane Smith {runId}-099` dengan 4 Pending Approval; requester `Budi Santoso {runId}-099`, `Rina Putri {runId}-099`, `PT Maju Bersama {runId}-099`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-099` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-099` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-099` | 05 Jun 2026 |
| `ID-TAG` | TAG Stock | (tanpa pemohon) | 09 Jun 2026 |
- Opsi `Transaction` berjumlah empat (lebih dari 3 nilai), dua di antaranya memuat `alloc`; semua ID memuat `2026`.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-099`, tekan Enter
3. Klik Name `Jane Smith {runId}-099` untuk membuka Detail User

### TC-AC-SU-353: Search di dalam dropdown `Transaction`

4. Klik tab `Responsibilities (4)`
5. Klik icon Filter
6. Buka dropdown `Transaction`
7. Ketik `alloc` di kotak search dropdown
8. Verifikasi opsi `Device Allocation` dan `License Allocation` tampil (case-insensitive)
9. Verifikasi opsi `Wallet Top-Up` dan `TAG Stock` tidak tampil
10. Ganti ketikan dengan `zzqx`
11. Verifikasi dropdown menampilkan state tidak ada opsi cocok
12. Tutup dropdown
13. Klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-354: Search lalu Filter, hasil irisan

14. Klik icon Search
15. Ketik Search `2026`, tekan Enter
16. Klik icon Filter
17. Pilih `Device Allocation` di field `Transaction`
18. Klik `[Apply]`
19. Verifikasi baris `ID-HALC` (memuat `2026`, Device Allocation) tampil
20. Verifikasi baris `ID-LALC` dan `ID-WLT` tidak tampil
21. Verifikasi keyword Search `2026` tetap terisi
22. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
23. Klik `(←)` pada kotak Search

### TC-AC-SU-355: Filter lalu Search, hasil irisan

24. Klik icon Filter
25. Pilih `Device Allocation` di field `Transaction`
26. Klik `[Apply]`
27. Klik icon Search
28. Ketik Search `2026`, tekan Enter
29. Verifikasi baris `ID-HALC` (Device Allocation, memuat `2026`) tampil
30. Verifikasi baris `ID-LALC` dan `ID-WLT` tidak tampil
31. Klik `(←)` pada kotak Search
32. Verifikasi baris `ID-HALC` tampil (filter Transaction `Device Allocation` tetap aktif)
33. Verifikasi baris `ID-LALC` dan `ID-WLT` tidak tampil
34. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); Filter Panel ditutup sesudah TC-353 (toggle icon Filter) agar `Klik icon Filter` berikutnya membukanya; `[Apply]` menutup panel, sehingga `[Clear Field]` sesudah Apply diawali `Klik icon Filter`; `[Clear Field]` lalu `[Apply]` dan `(←)` di akhir tiap TC mereset state (S-09).
- Spec ini memakai empat Pending Approval (satu `TAG Stock` tambahan) agar opsi `Transaction` lebih dari 3 nilai sesuai precondition TC-353.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-099` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-353 precondition menyebut opsi `Transaction` lebih dari 3 nilai tanpa menyebut nilai keempat; spec memakai `TAG Stock` (label sub-menu Approvals) sebagai Transaction keempat.
