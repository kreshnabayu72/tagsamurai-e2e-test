---
id: TC-AC-SU-E2E-156-changelog-user-aksi-global-role
title: "Popup Changelog User Mencatat Aksi Assign, Remove, dan Edit Permission Global Role dari Settings > User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-535
  - TC-AC-SU-536
  - TC-AC-SU-537
coverage:
  web: automated
---

# Popup Changelog User Mencatat Aksi Assign, Remove, dan Edit Permission Global Role dari Settings > User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (role "Manage group" adalah Global Role bawaan katalog):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-156A` | `miketan+{runId}-156a@qwertysystem.net` | tanpa tier, "Manage group" belum pernah aktif |
| U2 | `Mike Tan {runId}-156B` | `miketan+{runId}-156b@qwertysystem.net` | tanpa tier, "Manage group" aktif |
| U3 | `Mike Tan {runId}-156C` | `miketan+{runId}-156c@qwertysystem.net` | tanpa tier, "Manage group" aktif dengan Update unchecked |

- Kemampuan teknis: Fixture BE (seeding user dan role); nama tampil aktor Total Control untuk Modified By format `[First Name] [Last Initial]` dari `Fixture.settingsUser.totalControlActor.modifiedBy` (disediakan tim FE). Jam server dan jam browser sinkron; Date dibandingkan dengan waktu aksi (dicatat sesudah aksi) dengan toleransi satu menit. Format Date mengikuti General Settings (tidak diubah). Tanpa intercept dan tanpa klien HTTP.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-535: Assign Global Role
1. Ketik Search `Mike Tan {runId}-156A`, tekan Enter
2. Klik Name baris U1 untuk membuka Detail
3. Klik Tab Role, lalu sub-tab Global Role
4. Switch "Manage group" OFF ke ON, lalu catat waktu aksi
5. Tunggu aksi selesai, lalu klik Tab Changelog
6. Verifikasi Tab Changelog menampilkan tepat 1 entri dengan Action `Assign`, Field `Manage group — Access`, Old Value `—`, New Value `Assigned`, Modified By nama aktor format singkat
7. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name
8. Klik menu Settings > User di sidebar
9. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
10. Ketik Search `Mike Tan {runId}-156A` pada Popup Changelog: User, tekan Enter
11. Verifikasi tepat 1 baris: Action `Assign`, User Name `Mike Tan {runId}-156A`, Field `Manage group — Access`, Old Value `—`, New Value `Assigned`, Modified By nama aktor format singkat
12. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
### TC-AC-SU-536: Remove Global Role
13. Tutup Popup Changelog: User, ketik Search `Mike Tan {runId}-156B`, tekan Enter
14. Klik Name baris U2 untuk membuka Detail
15. Klik Tab Role, lalu sub-tab Global Role
16. Switch "Manage group" ON ke OFF, lalu catat waktu aksi
17. Tunggu aksi selesai, lalu klik Tab Changelog
18. Verifikasi Tab Changelog menampilkan tepat 1 entri dengan Action `Remove`, Field `Manage group — Access`, Old Value `Assigned`, New Value `—`, Modified By nama aktor format singkat
19. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name
20. Klik menu Settings > User di sidebar
21. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
22. Ketik Search `Mike Tan {runId}-156B` pada Popup Changelog: User, tekan Enter
23. Verifikasi tepat 1 baris: Action `Remove`, User Name `Mike Tan {runId}-156B`, Field `Manage group — Access`, Old Value `Assigned`, New Value `—`, Modified By nama aktor format singkat
24. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
### TC-AC-SU-537: Edit permission Global Role
25. Tutup Popup Changelog: User, ketik Search `Mike Tan {runId}-156C`, tekan Enter
26. Klik Name baris U3 untuk membuka Detail
27. Klik Tab Role, lalu sub-tab Global Role
28. Centang checkbox Update pada "Manage group", lalu catat waktu aksi
29. Tunggu aksi selesai, lalu klik Tab Changelog
30. Verifikasi Tab Changelog menampilkan tepat 1 entri dengan Action `Edit`, Field `Manage group — Update`, Old Value `Inactive`, New Value `Active`, Modified By nama aktor format singkat
31. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name
32. Klik menu Settings > User di sidebar
33. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
34. Ketik Search `Mike Tan {runId}-156C` pada Popup Changelog: User, tekan Enter
35. Verifikasi tepat 1 baris: Action `Edit`, User Name `Mike Tan {runId}-156C`, Field `Manage group — Update`, Old Value `Inactive`, New Value `Active`, Modified By nama aktor format singkat
36. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search dan pembukaan Detail (langkah 1, 13, 25, R-16), Search nama unik pada Popup Changelog: User (langkah 10, 22, 34), menutup popup, kembali ke daftar lewat sidebar, dan pencatatan waktu aksi. Langkah 8 mereset Search, sehingga Popup Changelog dibuka dari daftar tanpa filter.
- Urutan: Expected TC menempatkan Tab Changelog Detail (butir c) sesudah Popup Changelog; spec memverifikasi Tab Changelog lebih dulu karena Detail sudah terbuka saat aksi (S-10). Tab Changelog Detail dan Popup Changelog: User sama-sama diasersi "tepat 1" entri atau baris; Popup dicari dengan Search nama bersuffix unik dan baseline entri nol, sehingga keduanya asersi jumlah, bukan pembacaan baris teratas (S-14).
- Spec berisi tiga blok TC independen berpola sama dengan user seeding sendiri; 36 langkah (di atas smell 35 langkah) dipertahankan karena kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC-535 sampai TC-537 (Tab System Log aktor dan Activity Log dicatat) tidak punya langkah observasi di TC; tidak diasersi di spec ini. System Log diasersi pada spec 166 sampai 168.
  - TC-535 sampai TC-537 menyebut nama literal `Mike Tan` dan satu user untuk ketiganya dengan state awal berbeda; spec memakai tiga user bersuffix (S-12).
  - Nama tampil akun Total Control tidak tertulis di Pre-setup TC (hanya contoh `Admin U`).
