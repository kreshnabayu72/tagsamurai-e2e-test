---
id: TC-AC-SU-E2E-181-resilience-download-gagal-system-log-user-log-dan-modal-changelog
title: "Resilience Download Gagal 5xx pada Tab System Log, Tab User Log, Popup Changelog User, dan Modal Changelog Group Role Menampilkan Toast Error tanpa Berkas"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-424
  - TC-AC-SU-440
  - TC-AC-SU-478
  - TC-AC-SU-647
coverage:
  web: automated
---

# Resilience Download Gagal 5xx pada Tab System Log, Tab User Log, Popup Changelog User, dan Modal Changelog Group Role Menampilkan Toast Error tanpa Berkas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec: A `Jane Smith {runId}-181A`, email `janesmith+{runId}-181a@qwertysystem.net`, Activated, dengan sedikitnya satu entri pada tab dan modal yang diunduh.
- Kemampuan teknis (kelas b): `Spectra.intercept()` pada respons HTTP request Download dengan 5xx; endpoint tidak disebut TC, PRD, atau LLD, sehingga pola request disediakan tim FE/BE tanpa endpoint karangan di spec; pemantauan event unduhan browser untuk memastikan tidak ada berkas terunduh. Nama berkas pada toast mengikuti nama user bersuffix dengan spasi diganti tanda hubung (lihat Temuan untuk QA). Intercept dilepas segera setelah asersi toast (S-09).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-424: Download Tab System Log gagal
1. Ketik Search `Jane Smith {runId}-181A`, tekan Enter, klik Name baris A, lalu klik tab `System Log`
2. Atur intercept: respons request Download Tab System Log dikembalikan 5xx
3. Klik icon Download, lalu klik `Download as CSV`
4. Verifikasi toast error `"Error, failed to download System-Log-Jane-Smith-{runId}-181A."`
5. Verifikasi tidak ada berkas terunduh
### TC-AC-SU-440: Download Tab User Log gagal
6. Lepas intercept sebelumnya, tunggu toast error lama hilang otomatis, lalu klik tab `User Log`
7. Atur intercept: respons request Download Tab User Log dikembalikan 5xx
8. Klik icon Download, lalu klik `Download as CSV`
9. Verifikasi toast error `"Error, failed to download User-Log-Jane-Smith-{runId}-181A."`
10. Verifikasi tidak ada berkas terunduh
### TC-AC-SU-647: Download Modal Changelog Group Role gagal
11. Lepas intercept sebelumnya, tunggu toast error lama hilang otomatis, klik Tab Role, lalu klik sub-tab Group Role
12. Atur intercept: respons request Download Modal Changelog: User > Group Role dikembalikan 5xx
13. Klik icon `[📋]` Changelog, klik icon Download, lalu klik `Download as XLSX`
14. Verifikasi toast error `"Error, failed to download Changelog-Jane-Smith-{runId}-181A-Group-Role."`
15. Verifikasi tidak ada berkas terunduh
### TC-AC-SU-478: Download Popup Changelog User gagal
16. Lepas intercept sebelumnya, tutup modal, tunggu toast error lama hilang otomatis, lalu klik menu Settings > User di sidebar
17. Atur intercept: respons request Download Popup Changelog: User dikembalikan 5xx
18. Klik icon Changelog di toolbar User List, klik icon Download, lalu klik `Download as CSV`
19. Verifikasi toast error `"Error, failed to download Changelog-User."`
20. Verifikasi tidak ada berkas terunduh
21. Lepas intercept

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemasangan dan pelepasan intercept, Search baris target dan pembukaan Detail (R-16), menutup modal, pemilihan tab, dan menunggu toast lama hilang (R-12).
- Urutan: TC-647 dijalankan sebelum TC-478 agar seluruh blok pada Detail A berurutan dan Popup Changelog: User terakhir (S-10).
- Asersi "tidak ada berkas terunduh" didahului toast error pada surface yang sama sebagai anchor positif (bagian 8b butir 2 dan butir 11).
- TC-AC-SU-248, TC-AC-SU-320, TC-AC-SU-366, dan TC-AC-SU-402 (download gagal User List, Detail Group Assignment, Responsibilities, dan Changelog) ada di spec 180.
- Temuan untuk QA:
  - Nama berkas pada toast TC-424, TC-440, dan TC-647 memuat nama user literal (`Jane-Smith`); spec memakai nama bersuffix, sehingga nama berkas diasumsikan mengikuti nama bersuffix dengan spasi diganti tanda hubung. Pola penamaan berkas perlu dikonfirmasi.
  - TC-424, TC-440, TC-478, dan TC-647 menyebut "Endpoint download disimulasikan 5xx (intercept network)" tanpa endpoint; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC memakai nama literal `Jane Smith`; spec memakai nama bersuffix (S-12).
