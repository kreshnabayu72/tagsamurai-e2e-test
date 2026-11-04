---
id: TC-AC-SU-E2E-178-resilience-tab-role-autosave-popup-assign-group-dan-auto-revert-gagal
title: "Resilience Autosave Checkbox, Switch Global Role, Save Popup Assign Group Role, dan Auto-Revert Gagal 5xx Mengembalikan State dan Menampilkan Toast Error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-181
  - TC-AC-SU-182
  - TC-AC-SU-231
  - TC-AC-SU-262
coverage:
  web: automated
---

# Resilience Autosave Checkbox, Switch Global Role, Save Popup Assign Group Role, dan Auto-Revert Gagal 5xx Mengembalikan State dan Menampilkan Toast Error

## Prerequisites

- Mode: FE+BE.
- Akun aktor blok TC-181, TC-182, dan TC-231: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Akun aktor blok TC-262: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login Total Control di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; ganti akun ke Default User dilakukan eksplisit pada langkah 20 dan 21; hook `after` memulihkan sesi ke Default User.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per kebutuhan state (kegagalan server tidak mengubah state). Region A dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah:

| Kode | Name | Email | State awal |
|---|---|---|---|
| A | `Budi Santoso {runId}-178A` | `budisantoso+{runId}-178a@qwertysystem.net` | Activated, tanpa tier, bukan Group Manager; "Manage device master data" ON dengan C unchecked; "Manage language" OFF; "Manage partner" aktif di Region A |
| B | `Rina Putri {runId}-178B` | `rinaputri+{runId}-178b@qwertysystem.net` | Activated, bertier Total Control, "Manage TAG stock" dengan D checked |

- Kemampuan teknis (kelas b): `Spectra.intercept()` pada respons HTTP simpan permission, toggle role, dan Save assignment dengan 5xx; endpoint tidak disebut TC, PRD, atau LLD, sehingga pola request disediakan tim FE/BE tanpa endpoint karangan di spec. Spec memakai backend nyata dengan intercept parsial (bukan `Mode: mock`) karena status dibaca dari state nyata. Intercept dilepas segera setelah asersi toast (S-09).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-181: Autosave CRUD gagal 5xx
1. Atur intercept: respons request simpan permission dikembalikan 5xx
2. Ketik Search `Budi Santoso {runId}-178A`, tekan Enter, klik Name baris A, lalu pastikan Tab Role aktif
3. Centang C pada baris `Manage device master data`
4. Verifikasi checkbox C kembali ke `[☐]` (rollback)
5. Verifikasi toast error `"Error, failed to update permissions."`
### TC-AC-SU-182: Toggle switch Global Role gagal 5xx
6. Lepas intercept sebelumnya, lalu atur intercept: respons request toggle role dikembalikan 5xx dan tunggu toast error lama hilang otomatis
7. Klik switch baris `Manage language`
8. Verifikasi switch kembali OFF (rollback)
9. Verifikasi toast error `"Error, failed to update role."`
### TC-AC-SU-231: Save popup Assign Group Role gagal 5xx
10. Lepas intercept sebelumnya, atur intercept: respons request Save assignment dikembalikan 5xx, dan tunggu toast error lama hilang otomatis
11. Klik sub-tab Group Role, lalu klik `[Assign Group]` pada baris `Manage partner`
12. Centang C pada baris Region A
13. Klik `[Save]`
14. Verifikasi toast error `"Error, failed to save group role."`
15. Verifikasi popup tetap terbuka dan C baris Region A tetap tercentang
16. Verifikasi `[Save]` enabled kembali untuk retry
17. Lepas intercept, lalu klik `✕` untuk menutup popup
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`
### TC-AC-SU-262: Auto-Revert gagal 5xx
20. Lakukan Logout dari akun Total Control
21. Login sebagai Default User
22. Buka Settings > User lewat sidebar
23. Ketik Search `Rina Putri {runId}-178B`, tekan Enter, klik Name baris B, lalu pastikan Tab Role aktif
24. Atur intercept: respons request simpan permission dikembalikan 5xx
25. Uncheck D pada baris `Manage TAG stock`
26. Klik `[Remove]` pada dialog Remove Total Control
27. Verifikasi D kembali `[☑]` (rollback)
28. Verifikasi toast error `"Error, failed to update permissions."`
29. Verifikasi banner Total Control tetap tampil
30. Lepas intercept

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemasangan dan pelepasan intercept, Search baris target (R-16), pemilihan sub-tab, dan menunggu toast lama hilang (R-12). Ganti akun eksplisit pada langkah 20 dan 21 (login Default User), disusul langkah 22 (Buka Settings > User lewat sidebar), karena TC-262 mensyaratkan Default User sedangkan TC-181, TC-182, dan TC-231 mensyaratkan Total Control. Form dirty pada TC-231 ditutup deterministik lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Post Condition TC-181 ("Permission Create tetap false"), TC-182, TC-231, dan TC-262 (tingkat akses tetap Total Control; tidak ada entri log) tidak punya langkah observasi di TC dan tidak diasersi, kecuali yang sama dengan Expected TC (banner Total Control TC-262).
- Empat blok kelas b berpola sama dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, namun TC-262 memakai akun berbeda sehingga ditaruh terakhir.
- Temuan untuk QA:
  - TC-181, TC-182, TC-231, dan TC-262 menyebut "Server dikondisikan mengembalikan 5xx ... (intercept network)" tanpa endpoint; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC memakai nama literal `Budi Santoso` dan `Rina Putri`; spec memakai nama bersuffix (S-12).
