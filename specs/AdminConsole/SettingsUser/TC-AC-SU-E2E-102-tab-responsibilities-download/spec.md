---
id: TC-AC-SU-E2E-102-tab-responsibilities-download
title: "Tab Responsibilities Download: CSV Seluruh Baris dan XLSX dengan Search dan Filter Aktif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-364
  - TC-AC-SU-365
coverage:
  web: automated
---

# Tab Responsibilities Download: CSV Seluruh Baris dan XLSX dengan Search dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-102`): target `Jane Smith {runId}-102` dengan 12 Pending Approval (lebih dari 10 baris, lebih dari 1 halaman): `ID-HALC` (Device Allocation, Requester `Budi Santoso {runId}-102`, 08 Jun 2026) dan sebelas Pending Approval lain bertransaksi bervariasi (License Allocation dan Wallet Top-Up, Requester `Rina Putri {runId}-102` dan `PT Maju Bersama {runId}-102`), ID hasil seeding. Requester dan Submission Date tiap Pending Approval: precondition TC, tidak diasersi.
- Kemampuan teknis: membaca berkas unduhan (nama berkas, kolom, dan jumlah baris) disediakan tim FE.
- Nama berkas unduhan diturunkan dari nama user target: `Pending-Approvals-Jane-Smith-{runId}-102.csv` dan `Pending-Approvals-Jane-Smith-{runId}-102.xlsx` (nama target bersuffix; lihat Temuan untuk QA).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Ketik Search `Jane Smith {runId}-102`, tekan Enter
2. Klik Name `Jane Smith {runId}-102` untuk membuka Detail User

### TC-AC-SU-364: Download sebagai CSV tanpa search atau filter

3. Klik tab `Responsibilities (12)`
4. Hover icon Download
5. Verifikasi tooltip `Download` tampil
6. Klik icon Download
7. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`
8. Klik `Download as CSV`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `Pending-Approvals-Jane-Smith-{runId}-102.csv` terunduh
11. Verifikasi berkas berisi seluruh 12 baris Tab Responsibilities (semua halaman)
12. Verifikasi kolom berkas sesuai kolom yang visible

### TC-AC-SU-365: Download sebagai XLSX dengan search atau filter aktif

13. Klik icon Filter
14. Pilih `Device Allocation` di field `Transaction`
15. Klik `[Apply]`
16. Klik icon Download
17. Klik `Download as XLSX`
18. Verifikasi tidak ada toast sukses
19. Verifikasi berkas `Pending-Approvals-Jane-Smith-{runId}-102.xlsx` terunduh
20. Verifikasi berkas berisi 1 baris data (jumlah Pending Approval Transaction `Device Allocation` hasil seeding)
21. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); `[Clear Field]` lalu `[Apply]` melepas filter di akhir.
- Berkas unduhan diasersi pada nama berkas, kolom, dan jumlah baris (bagian 3 prinsip 13f); nilai sel TC-365 (format tanggal dan nilai kosong `—` ditulis `-`) diasersi di spec 195.
- Asersi tidak ada toast sukses diletakkan tepat setelah klik pilihan format Download dan sebelum Verifikasi berkas (bagian 8b butir 11).
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-102` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-364 dan TC-365 menyebut nama berkas `Pending-Approvals-Jane-Smith.csv` / `.xlsx`; dengan nama target bersuffix, penamaan berkas (pemisah dan penulisan suffix) tidak dinyatakan TC; spec menulis `Pending-Approvals-Jane-Smith-{runId}-102`.
  - TC-365 langkah 2 menyebut "filter/search" tanpa nilai; spec memakai Filter `Transaction` = `Device Allocation`.
- Pembagian TC lintas spec: TC-365 juga ada di `sourceTc` spec 195. Spec ini mengasersi nama berkas dan jumlah baris (kolom yang visible hanya pada TC-364); spec 195 mengasersi nilai sel berkas (kelas f).
