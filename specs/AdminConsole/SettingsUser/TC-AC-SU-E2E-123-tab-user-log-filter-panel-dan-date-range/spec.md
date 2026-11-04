---
id: TC-AC-SU-E2E-123-tab-user-log-filter-panel-dan-date-range
title: "Tab User Log: Filter Panel Hanya Field Date dan Date Range Inklusif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-436
  - TC-AC-SU-437
coverage:
  web: automated
---

# Tab User Log: Filter Panel Hanya Field Date dan Date Range Inklusif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-123` (email `janesmith+{runId}-123@qwertysystem.net`) dengan 3 sesi Admin Console pada Date relatif terhadap hari uji: T-10, T-7, dan T-4 (T-N berarti N hari sebelum hari uji; Note, IP Address, Device / Browser bebas dan tidak diasersi, dipakai sebagai precondition TC).
- Kemampuan teknis: kemampuan seed sesi User Log dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-436: Filter Panel User Log hanya berisi field Date

1. Ketik Search `Jane Smith {runId}-123`, tekan Enter
2. Klik Name `Jane Smith {runId}-123`
3. Klik tab `User Log`
4. Klik icon Filter
5. Verifikasi Filter Panel memuat field `Date` berupa date range picker dengan placeholder `Select date`
6. Verifikasi Filter Panel tidak memuat field Activity maupun Status
7. Klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-437: Date range Date inklusif

8. Klik icon Filter
9. Klik field `Date`
10. Pilih tanggal awal T-10 dan tanggal akhir T-7
11. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
12. Klik `[Apply]`
13. Verifikasi baris Date T-10 dan T-7 tampil (batas inklusif)
14. Verifikasi baris Date T-4 tidak tampil
15. Klik icon Filter
16. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- `[Clear Field]` lalu `[Apply]` pada akhir blok adalah langkah penghubung yang mengosongkan Filter (S-09); klik icon Filter sebelum tiap pengaturan Filter membuka panel.
- Temuan untuk QA:
  - TC-436 mengasersi tidak adanya field Activity dan Status tanpa menyebut anchor; field `Date` yang tampil pada panel yang sama menjadi anchor positifnya.
  - Nilai Date Format General Settings tidak tertulis di TC; asersi format tanggal dibaca dari General Settings entitas Principal.
  - Cara men-seed sesi User Log (Date, Note, IP Address, user agent, asal Admin Console atau Global Settings, user pemilik sesi) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
