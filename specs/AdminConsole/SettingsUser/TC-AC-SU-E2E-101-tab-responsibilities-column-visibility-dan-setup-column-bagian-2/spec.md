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
- Kemampuan teknis (disediakan tim FE): mengatur lebar viewport menjadi 1280px sehingga tabel dapat di-scroll horizontal (TC-360 Precondition c) dan memulihkannya ke ukuran awal.
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
5. Atur lebar viewport menjadi 1280px
6. Klik header `⋯`
7. Klik `[Setup Column]`
8. Klik icon Pin `ID`
9. Klik `[Save]`
10. Scroll tabel secara horizontal
11. Verifikasi kolom `ID` tetap terlihat (sticky) saat scroll horizontal
12. Tekan F5
13. Klik tab `Responsibilities (3)`
14. Scroll tabel secara horizontal
15. Verifikasi kolom `ID` tetap terlihat (sticky) setelah F5
16. Klik header `⋯`, klik `[Setup Column]`
17. Klik icon Pin `ID` (unpin), klik `[Save]`
18. Scroll tabel secara horizontal
19. Verifikasi kolom `ID` ikut ter-scroll setelah unpin
20. Pulihkan lebar viewport ke ukuran awal

### TC-AC-SU-361: Setup Column Reset to Default

21. Klik header `⋯`, klik `[Setup Column]`
22. Hapus centang `Transaction`, drag `Submission Date` ke posisi pertama, dan klik icon Pin `ID`
23. Klik `[Save]`
24. Klik header `⋯`, klik `[Setup Column]`
25. Klik `[Reset to Default]`
26. Verifikasi Live Preview kembali ke urutan default ID | Transaction | Requester | Submission Date, tiap kolom tampil dan tanpa pin
27. Klik `[Save]`
28. Verifikasi tabel memakai konfigurasi default
29. Tekan F5
30. Klik tab `Responsibilities (3)`
31. Verifikasi tabel tetap memakai konfigurasi default

### TC-AC-SU-362: Tutup popup tanpa Save membuang perubahan

32. Klik header `⋯`, klik `[Setup Column]`
33. Hapus centang `Transaction` dan drag `Submission Date` ke posisi awal
34. Klik icon `(X)`
35. Verifikasi popup tertutup tanpa dialog
36. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default)
37. Klik header `⋯`, klik `[Setup Column]`
38. Hapus centang `Requester`
39. Tekan Esc
40. Verifikasi popup tertutup tanpa dialog
41. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default)

### TC-AC-SU-363: Satu kolom tersisa tidak bisa di-unceklis

42. Klik header `⋯`, klik `[Setup Column]`
43. Hapus centang `Transaction`, `Requester`, dan `Submission Date`
44. Hover checkbox `ID`
45. Verifikasi checkbox `ID` tetap tampil dan checked
46. Verifikasi checkbox `ID` berstatus disabled
47. Verifikasi tooltip `At least one column must remain visible.`
48. Klik icon `(X)` pada popup

## Notes

- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); mengatur dan memulihkan lebar viewport (langkah 5 dan 20); menyimpan konfigurasi pada TC-361 memenuhi precondition ("konfigurasi sudah diubah"); icon `(X)` menutup popup tanpa menyimpan; langkah 13 dan 30 (klik tab `Responsibilities (3)` sesudah F5, karena PRD tidak menyatakan tab Detail yang aktif sesudah muat ulang).
- Alasan di atas ±35 langkah: keempat TC adalah Setup Column Tab Responsibilities dengan dataset sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-101` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-361 precondition c menyebut konfigurasi sudah diubah (kolom tersembunyi, urutan berubah, pin aktif) tanpa nilai; spec mengubah Transaction disembunyikan, Submission Date diseret ke awal, dan ID di-pin.
  - PRD tidak menyatakan tab Detail User mana yang aktif sesudah F5; spec mengklik tab `Responsibilities (3)` sesudah tiap F5 sebelum asersi tabel.
