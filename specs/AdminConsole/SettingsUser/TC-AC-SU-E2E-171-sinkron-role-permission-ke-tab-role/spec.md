---
id: TC-AC-SU-E2E-171-sinkron-role-permission-ke-tab-role
title: "Sinkron Dua Arah Antara Tab Role Settings > User dan Settings > Role & Permission untuk Switch Global Role, CRUD, dan Assign Group Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-588
  - TC-AC-SU-589
  - TC-AC-SU-590
coverage:
  web: automated
---

# Sinkron Dua Arah Antara Tab Role Settings > User dan Settings > Role & Permission untuk Switch Global Role, CRUD, dan Assign Group Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (Region A dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Mike Tan {runId}-171A` | `miketan+{runId}-171a@qwertysystem.net` | Activated, tanpa tier, "Manage group" OFF (TC-588) |
| U2 | `Mike Tan {runId}-171B` | `miketan+{runId}-171b@qwertysystem.net` | Activated, tanpa tier, "Manage group" ter-assign dengan Update unchecked (TC-589) |
| U3 | `Mike Tan {runId}-171C` | `miketan+{runId}-171c@qwertysystem.net` | Activated, tanpa tier, tanpa assignment "Manage partner" (TC-590) |

- Kemampuan teknis: Fixture BE (seeding user, role, dan assignment). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-588: Switch Global Role tercermin di Detail Role
1. Ketik Search `Mike Tan {runId}-171A`, tekan Enter, klik Name baris U1, klik Tab Role, lalu sub-tab Global Role
2. Switch "Manage group" OFF ke ON
3. Verifikasi toast `"Success, role has been updated."`
4. Klik menu Settings > Role & Permission di sidebar, lalu buka Detail role "Manage group" tanpa memuat ulang halaman
5. Ketik Search `Mike Tan {runId}-171A` pada Detail Role "Manage group", tekan Enter
6. Verifikasi U1 tampil di tabel user Detail Role "Manage group" dengan R checked
### TC-AC-SU-589: CRUD dari Role & Permission tercermin di Tab Role
7. Klik menu Settings > Role & Permission di sidebar, lalu buka Detail role "Manage group"
8. Ketik Search `Mike Tan {runId}-171B` pada Detail Role "Manage group", tekan Enter
9. Centang Update untuk U2 (`Mike Tan {runId}-171B`)
10. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U2 lewat Search nama, klik Tab Role, lalu sub-tab Global Role
11. Verifikasi checkbox Update "Manage group" ter-centang
12. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-171B` pada Popup Changelog: User, tekan Enter
13. Verifikasi Popup Changelog: User memuat tepat 1 entri Edit dengan Field `Manage group — Update`
14. Tutup popup, klik menu Settings > Role & Permission di sidebar, buka Detail role "Manage group", lalu klik icon Changelog
15. Ketik Search `Mike Tan {runId}-171B` pada modal Changelog: Role & Permission, tekan Enter
16. Verifikasi Changelog: Role & Permission > Manage group memuat tepat 1 entri Edit untuk U2 (Field `Update`)
### TC-AC-SU-590: Assign Group Role dari Role & Permission tercermin di sub-tab Group Role
17. Tutup modal Changelog, buka Detail role "Manage partner" di Settings > Role & Permission
18. Assign U3 (`Mike Tan {runId}-171C`) ke Region A pada Detail role "Manage partner"
19. Tunggu aksi selesai, klik menu Settings > User di sidebar, buka Detail U3 lewat Search nama, klik Tab Role, lalu sub-tab Group Role
20. Verifikasi baris "Manage partner" tampil aktif karena memiliki sedikitnya 1 group, tanpa switch
21. Verifikasi kolom Group baris "Manage partner" menampilkan badge `Region A`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search nama target dan pembukaan Detail (R-16), Search nama user di Detail Role dan di Popup Changelog: User dan modal Changelog: Role & Permission (user bernama unik sehingga baseline entri nol dan "tepat 1 entri" menjadi asersi jumlah, S-14, S-12), serta menutup popup dan modal.
- Tiga blok TC dengan aktor sama dan permukaan sinkronisasi yang sama; user seeding sendiri per blok.
- Temuan untuk QA:
  - TC-589 butir b menyebut entri Edit "satu entri, juga tampil di Changelog: Role & Permission > Manage group"; TC tidak menyebut kolom yang diasersi di surface Role & Permission; spec mengasersi Field `Update` dan user target.
  - TC-590 butir a menyebut "tampil aktif" tanpa menyebut penanda visual; spec mengasersi tidak adanya switch sesuai Expected.
  - TC memakai nama literal `Mike Tan`; spec memakai nama bersuffix (S-12).
