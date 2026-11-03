---
id: TC-AC-SU-E2E-157-changelog-user-aksi-group-role
title: "Popup Changelog User Mencatat Aksi Assign, Edit Permission, dan Remove Group Role per Group dari Settings > User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-538
  - TC-AC-SU-539
  - TC-AC-SU-540
coverage:
  web: automated
---

# Popup Changelog User Mencatat Aksi Assign, Edit Permission, dan Remove Group Role per Group dari Settings > User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (role "Manage partner" adalah Group Role bawaan katalog; Region A, Region B dari Group Tree Pre-setup, hanya dipakai sebagai target assignment dan tidak diubah):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-157A` | `miketan+{runId}-157a@qwertysystem.net` | tanpa tier, "Manage partner" aktif di Region A |
| U2 | `Mike Tan {runId}-157B` | `miketan+{runId}-157b@qwertysystem.net` | tanpa tier, "Manage partner" aktif di Region A dengan Create unchecked |
| U3 | `Mike Tan {runId}-157C` | `miketan+{runId}-157c@qwertysystem.net` | tanpa tier, "Manage partner" aktif di Region A dan Region B |

- Kemampuan teknis: Fixture BE (seeding user, role, dan group assignment); nama tampil aktor Total Control untuk Modified By format `[First Name] [Last Initial]` dari `Fixture.settingsUser.totalControlActor.modifiedBy` (disediakan tim FE). Jam server dan jam browser sinkron; Date dibandingkan dengan waktu aksi (dicatat sesudah aksi) dengan toleransi satu menit. Format Date mengikuti General Settings (tidak diubah). Tanpa intercept dan tanpa klien HTTP.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-538: Assign Group Role per group
1. Ketik Search `Mike Tan {runId}-157A`, tekan Enter
2. Klik Name baris U1 untuk membuka Detail
3. Klik Tab Role, lalu sub-tab Group Role
4. Klik `[Assign Group]` pada baris "Manage partner"
5. Klik `[+ Assign Group]`, centang Region B, klik `[Select]`
6. Klik `[Save]`, lalu catat waktu aksi
7. Tunggu aksi selesai, lalu klik Tab Changelog
8. Verifikasi Tab Changelog menampilkan entri teratas: Action `Assign`, Field `Manage partner — Region B — Access`, Old Value `—`, New Value `Assigned`, Modified By nama aktor format singkat
9. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name
10. Klik menu Settings > User di sidebar
11. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
12. Verifikasi baris teratas: Action `Assign`, User Name `Mike Tan {runId}-157A`, Field `Manage partner — Region B — Access`, Old Value `—`, New Value `Assigned`, Modified By nama aktor format singkat
13. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
### TC-AC-SU-539: Edit permission Group Role per group
14. Tutup Popup Changelog: User, ketik Search `Mike Tan {runId}-157B`, tekan Enter
15. Klik Name baris U2 untuk membuka Detail
16. Klik Tab Role, lalu sub-tab Group Role
17. Klik `[Assign Group]` pada baris "Manage partner", centang Create pada baris Region A
18. Klik `[Save]`, lalu catat waktu aksi
19. Tunggu aksi selesai, lalu klik Tab Changelog
20. Verifikasi Tab Changelog menampilkan entri teratas: Action `Edit`, Field `Manage partner — Region A — Create`, Old Value `Inactive`, New Value `Active`, Modified By nama aktor format singkat
21. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name
22. Klik menu Settings > User di sidebar
23. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
24. Verifikasi baris teratas: Action `Edit`, User Name `Mike Tan {runId}-157B`, Field `Manage partner — Region A — Create`, Old Value `Inactive`, New Value `Active`, Modified By nama aktor format singkat
25. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
### TC-AC-SU-540: Remove Group Role per group
26. Tutup Popup Changelog: User, ketik Search `Mike Tan {runId}-157C`, tekan Enter
27. Klik Name baris U3 untuk membuka Detail
28. Klik Tab Role, lalu sub-tab Group Role
29. Klik `[Assign Group]` pada baris "Manage partner", klik `[🗑]` pada baris Region B
30. Klik `[Save]`, lalu catat waktu aksi
31. Tunggu aksi selesai, lalu klik Tab Changelog
32. Verifikasi Tab Changelog menampilkan entri teratas: Action `Remove`, Field `Manage partner — Region B — Access`, Old Value `Assigned`, New Value `—`, Modified By nama aktor format singkat
33. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name
34. Klik menu Settings > User di sidebar
35. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
36. Verifikasi baris teratas: Action `Remove`, User Name `Mike Tan {runId}-157C`, Field `Manage partner — Region B — Access`, Old Value `Assigned`, New Value `—`, Modified By nama aktor format singkat
37. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search dan pembukaan Detail (langkah 1, 14, 26, R-16), menutup popup, kembali ke daftar lewat sidebar, dan pencatatan waktu aksi.
- Urutan: Expected TC menempatkan Tab Changelog Detail (butir c) sesudah Popup Changelog; spec memverifikasi Tab Changelog lebih dulu karena Detail sudah terbuka saat aksi (S-10). Baris target dicari sebagai baris teratas (Newest First) karena aksi baru saja dilakukan (S-14).
- Spec berisi tiga blok TC independen berpola sama dengan user seeding sendiri; 37 langkah (di atas smell 35 langkah) dipertahankan karena kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC-538 sampai TC-540 (Tab System Log aktor dan Activity Log dicatat) tidak punya langkah observasi di TC; tidak diasersi di spec ini. System Log diasersi pada spec 166 sampai 168.
  - TC tidak menyatakan apakah popup Assign Group Role menutup sendiri sesudah `[Save]`; spec menunggu aksi selesai lalu berpindah ke Tab Changelog.
  - TC memakai nama literal `Mike Tan` untuk ketiganya dengan state awal berbeda; spec memakai tiga user bersuffix (S-12).
  - Nama tampil akun Total Control tidak tertulis di Pre-setup TC (hanya contoh `Admin U`).
