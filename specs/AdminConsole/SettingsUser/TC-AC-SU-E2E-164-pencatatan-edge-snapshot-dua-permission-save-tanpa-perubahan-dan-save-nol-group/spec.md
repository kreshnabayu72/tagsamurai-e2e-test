---
id: TC-AC-SU-E2E-164-pencatatan-edge-snapshot-dua-permission-save-tanpa-perubahan-dan-save-nol-group
title: "Pencatatan Edge Changelog User, Snapshot Entri Lama, Dua Permission Sekaligus, Save Popup Assign Group Role tanpa Perubahan, dan Save 0 Group"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-564
  - TC-AC-SU-572
  - TC-AC-SU-573
  - TC-AC-SU-574
coverage:
  web: automated
---

# Pencatatan Edge Changelog User, Snapshot Entri Lama, Dua Permission Sekaligus, Save Popup Assign Group Role tanpa Perubahan, dan Save 0 Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (Region A dan Region B dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah). Nama tampil U1 diganti spec (langkah 4) dan dipulihkan di hook `after` bersama penghapusan user:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-164A` | `miketan+{runId}-164a@qwertysystem.net` | Activated, tanpa tier, "Manage group" aktif dengan Update unchecked |
| U2 | `Mike Tan {runId}-164B` | `miketan+{runId}-164b@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A dengan Create dan Update unchecked |
| U3 | `Mike Tan {runId}-164C` | `miketan+{runId}-164c@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A |
| U4 | `Mike Tan {runId}-164D` | `miketan+{runId}-164d@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A dan Region B |

- Kemampuan teknis: Fixture BE (seeding user, role, dan assignment). Aktor Total Control membuka Tab System Log miliknya sendiri; nama tampil akun Total Control dibaca dari `Fixture.settingsUser.totalControlActor.displayName` (disediakan tim FE; tidak tertulis di Pre-setup TC). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-572: Snapshot immutability
1. Ketik Search `Mike Tan {runId}-164A`, tekan Enter, klik Name baris U1, klik Tab Role, lalu sub-tab Global Role
2. Centang Update pada "Manage group" (Inactive ke Active)
3. Tunggu aksi selesai, lalu uncheck Update pada "Manage group" (Active ke Inactive)
4. Tunggu aksi selesai, lalu buka Global Settings > User dan ubah nama tampilan U1 menjadi `Michael Tan {runId}-164A`, lalu tunggu aksi selesai
5. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-164A` pada Popup Changelog: User, tekan Enter
6. Verifikasi entri pertama (lebih lama): Field `Manage group — Update`, Old Value `Inactive`, New Value `Active`
7. Verifikasi entri kedua (lebih baru): Field `Manage group — Update`, Old Value `Active`, New Value `Inactive`
8. Verifikasi User Name kedua entri tetap `Mike Tan {runId}-164A` (snapshot saat entri ditulis), bukan `Michael Tan {runId}-164A`
### TC-AC-SU-573: Dua permission sekaligus
9. Tutup popup, ketik Search `Mike Tan {runId}-164B`, tekan Enter, klik Name baris U2, klik Tab Role, lalu sub-tab Group Role
10. Klik `[Assign Group]` pada baris "Manage partner", centang Create dan Update pada baris Region A, lalu klik `[Save]`
11. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
12. Verifikasi tepat 2 baris Edit `Manage partner — Region A`
13. Verifikasi kedua baris Edit memiliki Field `Create` dan Field `Update`
14. Verifikasi tidak ada baris duplikat untuk Field `Create` maupun Field `Update`
15. Verifikasi tidak ada baris untuk Field `Read` maupun Field `Delete`
### TC-AC-SU-574: Save tanpa perubahan
16. Tutup modal, klik menu Settings > User di sidebar, ketik Search `Mike Tan {runId}-164C`, tekan Enter, klik Name baris U3, klik Tab Role, lalu sub-tab Group Role
17. Catat jumlah baris U3 pada Modal Changelog: User > Group Role, Popup Changelog: User (Search `Mike Tan {runId}-164C`), Tab System Log aktor (Search `Mike Tan {runId}-164C`), dan Activity Log (Search `Mike Tan {runId}-164C`)
18. Kembali ke Detail U3, Tab Role, sub-tab Group Role, lalu klik `[Assign Group]` pada baris "Manage partner" dan klik `[Save]` tanpa perubahan
19. Verifikasi toast `"No changes to save."`
20. Klik `✕` untuk menutup popup Assign Group Role, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
21. Verifikasi jumlah baris Modal Changelog: User > Group Role sama dengan nilai yang dicatat pada langkah 17
22. Tutup modal, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-164C`, tekan Enter
23. Verifikasi jumlah baris Popup Changelog: User sama dengan nilai yang dicatat pada langkah 17
24. Tutup popup, buka Detail akun aktor Total Control lewat Search nama tampil aktor, lalu klik Tab System Log dan ketik Search `Mike Tan {runId}-164C`, tekan Enter
25. Verifikasi jumlah baris Tab System Log aktor sama dengan nilai yang dicatat pada langkah 17
26. Klik menu Admin Console > Activity Log di sidebar, lalu ketik Search `Mike Tan {runId}-164C`, tekan Enter
27. Verifikasi jumlah baris Activity Log sama dengan nilai yang dicatat pada langkah 17
### TC-AC-SU-564: Save 0 group lalu Assign ulang
28. Klik menu Settings > User di sidebar, ketik Search `Mike Tan {runId}-164D`, tekan Enter, klik Name baris U4, klik Tab Role, lalu sub-tab Group Role
29. Klik `[Assign Group]` pada baris "Manage partner", klik `[Clear Field]`, lalu klik `[Save]`
30. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
31. Verifikasi 2 baris `Remove` untuk `Manage partner — Region A` dan `Manage partner — Region B`
32. Verifikasi kedua baris `Remove` memiliki Field `Access`, Old Value `Assigned`, New Value `—`
33. Tutup modal, klik `[Assign Group]` pada baris "Manage partner", klik `[+ Assign Group]`, centang Region A dan Region B, klik `[Select]`, lalu klik `[Save]`
34. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Modal Changelog: User > Group Role terbuka
35. Verifikasi 2 baris `Assign` baru untuk `Manage partner — Region A` dan `Manage partner — Region B`
36. Verifikasi kedua baris `Assign` baru memiliki Field `Access`, Old Value `—`, New Value `Assigned`
37. Verifikasi total 4 entri
38. Verifikasi tidak ada baris Edit permission pada modal

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search nama user dan pembukaan Detail (langkah 16, 28 dan langkah serupa, R-16), Search nama user di popup, tab, dan Activity Log (user bernama unik sehingga baseline entri nol), menutup modal dan popup, pencatatan jumlah baris awal (langkah 17), dan langkah `✕` pada popup Assign Group Role yang tidak dirty (S-08 tidak berlaku karena tidak ada perubahan).
- Urutan: TC-572, TC-573, TC-574, lalu TC-564; Save 0 group (menghapus seluruh assignment) ditaruh paling akhir sebagai aksi yang mengubah data paling besar (S-10).
- Empat blok TC independen dengan aktor yang sama dan permukaan yang sama (Changelog User); 38 langkah (di atas smell 35 langkah) dipertahankan karena kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-574 butir b menyatakan "jumlah baris di keempat surface sama dengan sebelum Save" tanpa menyebut baseline; spec mencatat jumlah baris sebelum Save (langkah 17) dan membandingkannya. Asersi "tidak dicatat" (Post Condition) atas empat surface ditulis sebagai asersi jumlah dengan baseline, bukan absence kelas g.
  - TC-574 tidak menyatakan apakah popup Assign Group Role menutup sendiri sesudah toast `"No changes to save."`; spec menutup lewat `✕`.
  - TC-572 langkah 4 tidak menyatakan apakah Search di Popup Changelog: User mencari nama snapshot atau nama saat ini; spec mencari nama lama (snapshot).
  - TC-572 menyebut nama baru literal "Michael Tan"; spec memakai `Michael Tan {runId}-164A`. Nama tampil akun Total Control tidak tertulis di Pre-setup TC. Nama literal `Mike Tan` diganti nama bersuffix (S-12).
