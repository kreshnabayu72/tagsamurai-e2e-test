---
id: TC-AC-SU-E2E-209-modal-changelog-group-role-mencatat-cascade-total-control-dan-read-only
title: "Modal Changelog User > Group Role Mencatat Assign dan Remove via Total Control atau Read Only per Group (Cascade)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-560
  - TC-AC-SU-561
  - TC-AC-SU-562
  - TC-AC-SU-563
coverage:
  web: automated
---

# Modal Changelog User > Group Role Mencatat Assign dan Remove via Total Control atau Read Only per Group (Cascade)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12). Nama unik sehingga entri audit trail user hanya berasal dari spec ini; asersi memakai Action, Role Name, dan Group Name, bukan jumlah entri absolut. Data Pre-setup bersama tidak diubah. Satu user per TC: user blok Remove di-seed langsung bertier sehingga blok Remove tidak bergantung pada blok Assign. Region A dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-209A` | `miketan+{runId}-209a@qwertysystem.net` | Activated, tanpa tier, "Manage partner" belum ter-assign di Region A (TC-560) |
| U2 | `Mike Tan {runId}-209B` | `miketan+{runId}-209b@qwertysystem.net` | Activated, bertier Total Control, "Manage partner" ter-assign di Region A (TC-562) |
| U3 | `Mike Tan {runId}-209C` | `miketan+{runId}-209c@qwertysystem.net` | Activated, tanpa tier, "Manage partner" belum ter-assign di Region A (TC-561) |
| U4 | `Mike Tan {runId}-209D` | `miketan+{runId}-209d@qwertysystem.net` | Activated, bertier Read Only, "Manage partner" ter-assign di Region A (TC-563) |

- Kemampuan teknis: Fixture BE (seeding user, tier, role, dan assignment). Daftar Group Role dan group yang terdampak cascade tier mengikuti katalog Settings > Role & Permission dan Group Tree Pre-setup (`Fixture.settingsUser.groupRoles`, kunci fixture baru yang disediakan tim FE). Akun aktor Default User membuka Tab System Log miliknya sendiri lewat Search email Default User Pre-setup #1 (`defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`), bukan nama tampil. Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-560: Assign (via Total Control)
1. Klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu assign U1 ke Total Control
2. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U1 lewat Search nama, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
3. Ubah page size Modal Changelog menjadi 100
4. Verifikasi baris modal: Action `Assign (via Total Control)`, Role Name — Group Name `Manage partner — Region A`, Field `Access`, Old Value `—`, New Value `Assigned`
5. Verifikasi tiap pasangan Group Role dan group terdampak memiliki tepat 1 baris Action `Assign (via Total Control)`
6. Tutup modal, klik menu Settings > User di sidebar, buka Detail Default User lewat Search email Default User, lalu klik Tab System Log
7. Ketik Search `Mike Tan {runId}-209A`, tekan Enter
8. Ubah page size Tab System Log menjadi 100
9. Verifikasi Tab System Log aktor memuat baris cascade Object `Group Role`, Action `Assign (via Total Control)`, Name `Mike Tan {runId}-209A`, Field `Manage partner — Region A — Access`
### TC-AC-SU-562: Remove (via Total Control)
10. Klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu remove U2 dari Total Control
11. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U2 lewat Search nama, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
12. Ubah page size Modal Changelog menjadi 100
13. Verifikasi baris modal: Action `Remove (via Total Control)`, Role Name — Group Name `Manage partner — Region A`, Field `Access`, Old Value `Assigned`, New Value `—`
14. Verifikasi tiap pasangan Group Role dan group terdampak memiliki tepat 1 baris Action `Remove (via Total Control)`
15. Tutup modal, klik menu Settings > User di sidebar, buka Detail Default User lewat Search email Default User, lalu klik Tab System Log
16. Ketik Search `Mike Tan {runId}-209B`, tekan Enter
17. Ubah page size Tab System Log menjadi 100
18. Verifikasi Tab System Log aktor memuat baris cascade Object `Group Role`, Action `Remove (via Total Control)`, Name `Mike Tan {runId}-209B`, Field `Manage partner — Region A — Access`
### TC-AC-SU-561: Assign (via Read Only)
19. Klik menu Settings > Role & Permission di sidebar, klik Tab Read Only, lalu assign U3 ke Read Only
20. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U3 lewat Search nama, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
21. Ubah page size Modal Changelog menjadi 100
22. Verifikasi baris modal: Action `Assign (via Read Only)`, Role Name — Group Name `Manage partner — Region A`, Field `Access`, Old Value `—`, New Value `Assigned`
23. Verifikasi tiap pasangan Group Role dan group terdampak memiliki tepat 1 baris Action `Assign (via Read Only)`
24. Tutup modal, klik menu Settings > User di sidebar, buka Detail Default User lewat Search email Default User, lalu klik Tab System Log
25. Ketik Search `Mike Tan {runId}-209C`, tekan Enter
26. Ubah page size Tab System Log menjadi 100
27. Verifikasi Tab System Log aktor memuat baris cascade Object `Group Role`, Action `Assign (via Read Only)`, Name `Mike Tan {runId}-209C`, Field `Manage partner — Region A — Access`
### TC-AC-SU-563: Remove (via Read Only)
28. Klik menu Settings > Role & Permission di sidebar, klik Tab Read Only, lalu remove U4 dari Read Only
29. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U4 lewat Search nama, klik Tab Role, sub-tab Group Role, lalu klik icon Changelog di toolbar
30. Ubah page size Modal Changelog menjadi 100
31. Verifikasi baris modal: Action `Remove (via Read Only)`, Role Name — Group Name `Manage partner — Region A`, Field `Access`, Old Value `Assigned`, New Value `—`
32. Verifikasi tiap pasangan Group Role dan group terdampak memiliki tepat 1 baris Action `Remove (via Read Only)`
33. Tutup modal, klik menu Settings > User di sidebar, buka Detail Default User lewat Search email Default User, lalu klik Tab System Log
34. Ketik Search `Mike Tan {runId}-209D`, tekan Enter
35. Ubah page size Tab System Log menjadi 100
36. Verifikasi Tab System Log aktor memuat baris cascade Object `Group Role`, Action `Remove (via Read Only)`, Name `Mike Tan {runId}-209D`, Field `Manage partner — Region A — Access`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search nama user dan pembukaan Detail (langkah 2 dan langkah serupa, R-16), Search email Default User (langkah 6 dan langkah serupa, R-16), mengubah page size Modal Changelog menjadi 100 agar semua baris cascade tampil sebelum asersi "tepat 1 baris" (langkah 3, 12, 21, 30; S-14), Search nama target pada Tab System Log aktor agar baris cascade user target tampil (langkah 7, 16, 25, 34; R-16), mengubah page size Tab System Log menjadi 100 agar semua baris cascade tampil (langkah 8, 17, 26, 35; S-14; tabel adalah audit trail permanen dengan default 10 baris dan cascade Group Role menulis satu entri per Group Role per group), serta menutup modal. Baris target dicari lewat Action, Role Name, dan Group Name (bukan lewat posisi baris).
- Urutan blok: TC-560 (U1), TC-562 (U2), TC-561 (U3), TC-563 (U4); dua pasangan Total Control lalu Read Only. Urutan ini mengubah urutan nomor TC (S-10). Tiap blok memakai user sendiri sehingga blok Remove tidak bergantung pada blok Assign.
- Pembagian TC lintas spec: TC-557, TC-558, dan TC-559 ada di spec 163. Empat blok di spec ini berpola sama pada empat user terpisah dan satu aktor; 36 langkah (di atas smell 35 langkah) dengan alasan: satu surface, satu aktor, dan empat blok independen dengan user seeding sendiri (A sampai D) yang masing-masing tetap utuh jika dipecah tanpa data bersama.
- Temuan untuk QA:
  - TC-560 sampai TC-563 butir b menyebut Action, Object `Group Role`, Name, dan Field `Manage partner — Region A — Access`; spec membatasi tampilan Tab System Log lewat Search nama target bersuffix (S-12) dan page size 100, bukan lewat Search Field.
  - TC-560 sampai TC-563 tidak menyebut daftar group terdampak cascade; spec mengasersi baris `Manage partner — Region A` dan keunikan tiap pasangan Group Role dan group. Daftar pasangan disediakan tim FE.
  - Precondition TC-560 dan TC-561 menyatakan Manage partner belum ter-assign di Region A, dan TC-562 serta TC-563 menyatakan user sudah bertier; spec men-seed sesuai precondition itu.
  - Nama tampil akun Default User tidak tertulis di Pre-setup TC (hanya email); spec mencari Default User lewat email.
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
  - TC-553 sampai TC-556 dan TC-560 sampai TC-563 menyebut pembatas tampilan (page size 100 atau Search/Filter); spec mengubah page size menjadi 100 (dasar PRD settings-user.md baris 1767, 1946, 1966). Page size 100 tidak dipulihkan ke 10 di spec ini karena Tab System Log dibuka ulang per blok; QA perlu memastikan state page size tidak bertahan lintas sesi.
