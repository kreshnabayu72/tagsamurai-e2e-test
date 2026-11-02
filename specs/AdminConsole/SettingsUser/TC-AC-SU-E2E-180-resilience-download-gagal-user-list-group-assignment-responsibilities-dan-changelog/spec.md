---
id: TC-AC-SU-E2E-180-resilience-download-gagal-user-list-group-assignment-responsibilities-dan-changelog
title: "Resilience Download Gagal 5xx pada User List, Detail Group Assignment, Tab Responsibilities, dan Tab Changelog Menampilkan Toast Error tanpa Berkas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-248
  - TC-AC-SU-320
  - TC-AC-SU-366
  - TC-AC-SU-402
coverage:
  web: automated
---

# Resilience Download Gagal 5xx pada User List, Detail Group Assignment, Tab Responsibilities, dan Tab Changelog Menampilkan Toast Error tanpa Berkas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec (nama berprefix `{runId}-180`):

| Kode | Name | Email | State awal |
|---|---|---|---|
| A | `Jane Smith {runId}-180A` | `janesmith+{runId}-180a@qwertysystem.net` | Activated |
| B | `Budi Santoso {runId}-180B` | `budisantoso+{runId}-180b@qwertysystem.net` | Activated, tanpa tier, bukan Group Manager, "Manage distributor" aktif di Region A (Region A dari Group Tree Pre-setup, tidak diubah) |

- Kemampuan teknis (kelas b): `Spectra.intercept()` pada respons HTTP request Download dengan 5xx; endpoint tidak disebut TC, PRD, atau LLD, sehingga pola request disediakan tim FE/BE tanpa endpoint karangan di spec; pemantauan event unduhan browser untuk memastikan tidak ada berkas terunduh. Nama berkas pada toast mengikuti nama user bersuffix dengan spasi diganti tanda hubung (lihat Temuan untuk QA). Intercept dilepas segera setelah asersi toast (S-09).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-320: Download User List gagal
1. Atur intercept: respons request Download User List dikembalikan 5xx
2. Klik icon Download di toolbar, lalu klik `Download as CSV`
3. Verifikasi toast error `"Error, failed to download User."`
4. Verifikasi tidak ada berkas terunduh
### TC-AC-SU-248: Download Detail Group Assignment gagal
5. Lepas intercept sebelumnya, ketik Search `Budi Santoso {runId}-180B`, tekan Enter, klik Name baris B, klik Tab Role, lalu sub-tab Group Role
6. Atur intercept: respons request Download Detail Group Assignment dikembalikan 5xx
7. Klik `[Detail]` pada baris `Manage distributor`
8. Klik icon Download, lalu klik `Download as CSV`
9. Verifikasi toast error `"Error, failed to download Group-Assignment-Budi-Santoso-{runId}-180B-Manage-distributor."`
10. Verifikasi popup Detail Group Assignment tetap terbuka
### TC-AC-SU-366: Download Tab Responsibilities gagal
11. Lepas intercept sebelumnya, tutup popup, klik menu Settings > User di sidebar, ketik Search `Jane Smith {runId}-180A`, tekan Enter, klik Name baris A, lalu klik tab `Responsibilities (N)`
12. Atur intercept: respons request Download Tab Responsibilities dikembalikan 5xx
13. Klik icon Download, lalu klik `Download as CSV`
14. Verifikasi toast error `"Error, failed to download Pending-Approvals-Jane-Smith-{runId}-180A."`
15. Verifikasi tidak ada berkas terunduh
### TC-AC-SU-402: Download Tab Changelog gagal
16. Tunggu toast error lama hilang otomatis, lalu klik tab `Changelog`
17. Atur intercept: respons request Download Tab Changelog dikembalikan 5xx
18. Klik icon Download, lalu klik `Download as CSV`
19. Verifikasi toast error `"Error, failed to download Changelog-Jane-Smith-{runId}-180A."`
20. Verifikasi tidak ada berkas terunduh
21. Lepas intercept

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemasangan dan pelepasan intercept, Search baris target dan pembukaan Detail (R-16), menutup popup, dan menunggu toast lama hilang (R-12). Popup Detail Group Assignment tidak dirty sehingga ditutup lewat langkah penghubung tanpa dialog.
- Asersi "tidak ada berkas terunduh" didahului toast error pada surface yang sama sebagai anchor positif (bagian 8b butir 2 dan butir 11).
- TC-AC-SU-424, TC-AC-SU-440, TC-AC-SU-478, dan TC-AC-SU-647 (download gagal System Log, User Log, Popup Changelog: User, dan Modal Changelog Group Role) ada di spec 181.
- Temuan untuk QA:
  - Nama berkas pada toast TC-248, TC-366, dan TC-402 memuat nama user literal (`Budi-Santoso`, `Jane-Smith`); spec memakai nama bersuffix, sehingga nama berkas diasumsikan mengikuti nama bersuffix dengan spasi diganti tanda hubung. Pola penamaan berkas dengan angka dan huruf pada suffix perlu dikonfirmasi.
  - TC-320 langkah 1 ("Simulasikan response 5xx pada request Download") tidak menyebut endpoint; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-248 butir b ("Popup tetap terbuka") tidak menyebut popup mana; spec mengasersi popup Detail Group Assignment.
  - TC memakai nama literal `Jane Smith` dan `Budi Santoso`; spec memakai nama bersuffix (S-12).
