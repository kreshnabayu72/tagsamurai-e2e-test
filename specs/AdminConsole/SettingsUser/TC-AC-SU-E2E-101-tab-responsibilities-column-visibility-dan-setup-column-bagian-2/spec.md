---
id: TC-AC-SU-E2E-101-tab-responsibilities-column-visibility-dan-setup-column-bagian-2
title: "Tab Responsibilities Column Visibility dan Setup Column: Pin, Reset to Default, Discard, dan Guard Satu Kolom"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-360
  - TC-AC-SU-361
  - TC-AC-SU-362
  - TC-AC-SU-363
coverage:
  web: automated
---

# Tab Responsibilities Column Visibility dan Setup Column: Pin, Reset to Default, Discard, dan Guard Satu Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-101`): target `Jane Smith {runId}-101` dengan 3 Pending Approval; requester `Budi Santoso {runId}-101`, `Rina Putri {runId}-101`, `PT Maju Bersama {runId}-101`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-101` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-101` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-101` | 05 Jun 2026 |
- Viewport 1280px sehingga tabel dapat di-scroll horizontal (TC-360).
- Konfigurasi kolom Tab Responsibilities awal adalah default (tidak ada preferensi kolom tersimpan).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-101`, tekan Enter
3. Klik Name `Jane Smith {runId}-101` untuk membuka Detail User

### TC-AC-SU-360: Setup Column pin dan unpin kolom

4. Klik tab `Responsibilities (3)`
5. Klik header `⋯`
6. Klik `[Setup Column]`
7. Klik icon Pin `ID`
8. Klik `[Save]`
9. Scroll tabel secara horizontal
10. Verifikasi kolom `ID` tetap terlihat (sticky) saat scroll horizontal
11. Tekan F5
12. Scroll tabel secara horizontal
13. Verifikasi kolom `ID` tetap terlihat (sticky) setelah F5
14. Klik header `⋯`, klik `[Setup Column]`
15. Klik icon Pin `ID` (unpin), klik `[Save]`
16. Scroll tabel secara horizontal
17. Verifikasi kolom `ID` ikut ter-scroll setelah unpin

### TC-AC-SU-361: Setup Column Reset to Default

18. Klik header `⋯`, klik `[Setup Column]`
19. Hapus centang `Transaction`, drag `Submission Date` ke posisi pertama, dan klik icon Pin `ID`
20. Klik `[Save]`
21. Klik header `⋯`, klik `[Setup Column]`
22. Klik `[Reset to Default]`
23. Verifikasi Live Preview kembali ke urutan default ID | Transaction | Requester | Submission Date, tiap kolom tampil dan tanpa pin
24. Klik `[Save]`
25. Verifikasi tabel memakai konfigurasi default
26. Tekan F5
27. Verifikasi tabel tetap memakai konfigurasi default

### TC-AC-SU-362: Tutup popup tanpa Save membuang perubahan

28. Klik header `⋯`, klik `[Setup Column]`
29. Hapus centang `Transaction` dan drag `Submission Date` ke posisi awal
30. Klik icon `(X)`
31. Verifikasi popup tertutup tanpa dialog
32. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default)
33. Klik header `⋯`, klik `[Setup Column]`
34. Hapus centang `Requester`
35. Tekan Esc
36. Verifikasi popup tertutup tanpa dialog
37. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default)

### TC-AC-SU-363: Satu kolom tersisa tidak bisa di-unceklis

38. Klik header `⋯`, klik `[Setup Column]`
39. Hapus centang `Transaction`, `Requester`, dan `Submission Date`
40. Hover checkbox `ID`
41. Verifikasi checkbox `ID` tetap tampil dan checked
42. Verifikasi checkbox `ID` berstatus disabled
43. Verifikasi tooltip `At least one column must remain visible.`
44. Klik icon `(X)` pada popup

## Notes

- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); menyimpan konfigurasi pada TC-361 memenuhi precondition ("konfigurasi sudah diubah"); icon `(X)` menutup popup tanpa menyimpan.
- Alasan di atas ±35 langkah: keempat TC adalah Setup Column Tab Responsibilities dengan dataset sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-101` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-361 precondition c menyebut konfigurasi sudah diubah (kolom tersembunyi, urutan berubah, pin aktif) tanpa nilai; spec mengubah Transaction disembunyikan, Submission Date diseret ke awal, dan ID di-pin.
