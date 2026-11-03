---
id: TC-AC-SU-E2E-200-resilience-error-load-modal-changelog
title: "Resilience Error Load Modal Changelog User, Global Role, dan Group Role Menampilkan Pesan Error dengan Try Again"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-447
  - TC-AC-SU-483
  - TC-AC-SU-507
coverage:
  web: automated
---

# Resilience Error Load Modal Changelog User, Global Role, dan Group Role Menampilkan Pesan Error dengan Try Again

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec: A `Jane Smith {runId}-200`, email `janesmith+{runId}-200@qwertysystem.net`, Activated, dengan sedikitnya satu entri pada Popup Changelog: User, Modal Changelog: User > Global Role, dan Modal Changelog: User > Group Role (data seeding dibaca ulang setelah intercept dilepas).
- Kemampuan teknis (kelas b): `Spectra.intercept()` pada respons HTTP data tabel modal Changelog (500 sampai intercept dilepas); endpoint tidak disebut TC, PRD, atau LLD, sehingga pola request disediakan tim FE/BE tanpa endpoint karangan di spec. Spec memakai backend nyata dengan intercept parsial (bukan `Mode: mock`) karena data pemulihan dibaca dari backend nyata. Intercept dilepas segera setelah asersi kegagalan (S-09).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-447: Error load Popup Changelog User
1. Atur intercept: respons request data tabel Popup Changelog: User dikembalikan 500
2. Klik icon Changelog di toolbar User List
3. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
4. Lepas intercept, lalu klik `[Try Again]`
5. Verifikasi tabel Popup Changelog: User menampilkan data
### TC-AC-SU-483: Error load Modal Changelog Global Role
6. Tutup popup, ketik Search `Jane Smith {runId}-200`, tekan Enter, klik Name baris A, klik Tab Role, lalu sub-tab Global Role
7. Atur intercept: respons request data tabel Modal Changelog: User > Global Role dikembalikan 500
8. Klik icon `[📋]` Changelog
9. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
10. Lepas intercept, lalu klik `[Try Again]`
11. Verifikasi tabel Modal Changelog: User > Global Role menampilkan data
### TC-AC-SU-507: Error load Modal Changelog Group Role
12. Tutup modal, lalu klik sub-tab Group Role pada Tab Role
13. Atur intercept: respons request data tabel Modal Changelog: User > Group Role dikembalikan 500
14. Klik icon `[📋]` Changelog
15. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
16. Lepas intercept, lalu klik `[Try Again]`
17. Verifikasi tabel Modal Changelog: User > Group Role menampilkan data

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemasangan dan pelepasan intercept, Search baris target dan pembukaan Detail (R-16), menutup popup dan modal, dan pemilihan sub-tab.
- TC-AC-SU-20, TC-AC-SU-335, TC-AC-SU-372, TC-AC-SU-407, dan TC-AC-SU-430 (error load User List dan tab Detail) ada di spec 179.
- Temuan untuk QA:
  - TC-447, TC-483, dan TC-507 menyebut "Response: 500" tanpa endpoint; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC memakai nama literal `Jane Smith`; spec memakai nama bersuffix (S-12).
