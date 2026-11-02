---
id: TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point
title: "Alert Group Consolidation Pasca-T-0: Tampil untuk Total Control/Default User Saat Group > Cap, Hidden Saat <= Cap atau untuk Aktor Lain, Cap Turun Langsung, dan Tidak Ada Entry Point Sebelum T-0"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-320
  - TC-FA-GRP-1107
  - TC-FA-GRP-1108
  - TC-FA-GRP-1109
  - TC-FA-GRP-1114
  - TC-FA-GRP-1115
coverage:
  web: automated
---

# Alert Group Consolidation Pasca-T-0: Tampil untuk Total Control/Default User Saat Group > Cap, Hidden Saat <= Cap atau untuk Aktor Lain, Cap Turun Langsung, dan Tidak Ada Entry Point Sebelum T-0

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Alert (plan Growth; client punya 5 group dengan status Excess sesuai blok; email dan `Spectra.env.FA_ALERT_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Role yang diuji (client Alert; akun selain Total Control disediakan tim FE karena Pre-setup No 2 sampai 5 berada di client lain; ganti akun ditulis eksplisit pada langkah 19, 25, 30, 35):

| TC | Role | Env var password |
|---|---|---|
| TC-1107, TC-1108, TC-1115, TC-320 | Total Control (hook `before`; TC-1115 memakai client khusus Group Consolidation, Pre-setup No 25, bukan client Tabel A) | `Spectra.env.FA_ALERT_TC_PASSWORD` |
| TC-1114 | Default User | `Spectra.env.FA_ALERT_DU_PASSWORD` |
| TC-1109 | Group Manager (scope Region West) | `Spectra.env.FA_ALERT_GM_PASSWORD` |
| TC-1109 | Read Only | `Spectra.env.FA_ALERT_RO_PASSWORD` |
| TC-1109 | Manage Group CRUD penuh | `Spectra.env.FA_ALERT_MGCRUD_PASSWORD` |

- Keadaan tiap blok (di-seed ulang oleh fixture BE pada langkah penghubung): S2 (TC-1108): cap berlaku 5, 5 group; S3 (TC-1115): client khusus Group Consolidation (Pre-setup No 25) dengan tepat 6 group, cap berlaku 25, downgrade terjadwal ke cap 3 (T-30 berjalan, T-0 belum tercapai); TC-320: cap diturunkan langsung ke 3 dari S3 (T-0 = saat disimpan, Admin Console); S1 (TC-1107, TC-1114, TC-1109): cap berlaku 3, 5 group, 2 berstatus Excess.
- State tenant (kelas h): cap plan dan status Excess diatur per blok oleh fixture BE (disediakan tim FE/BE); plan, cap, dan status Excess dipulihkan di hook `after`. Suite berjalan serial.
- Cleanup di `after`: hapus data seed dan pulihkan keadaan lewat fixture BE.

## Test Steps

### TC-FA-GRP-1108: Hidden saat jumlah group <= cap (S2)

1. Verifikasi Group Context Header tampil
2. Verifikasi Alert Group Consolidation tidak tampil

### TC-FA-GRP-1115: Tidak ada entry point sebelum T-0 (S3)

3. Setel keadaan S3 lewat fixture BE, lalu muat ulang halaman
4. Verifikasi Group Context Header tampil
5. Verifikasi Alert Group Consolidation tidak tampil walau jumlah group (6) melebihi cap baru (3)
6. Verifikasi tombol [Choose Groups] tidak tersedia di Settings > Groups
7. Verifikasi tidak ada node berstatus Excess (nama tidak di-dim)
8. Buka Wizard Reconciliation > Step Group Consolidation
9. Verifikasi [Save Selection] tampil di step (seleksi hanya dapat disimpan di Wizard Reconciliation > Step Group Consolidation)
10. Klik [Cancel]

### TC-FA-GRP-320: Cap diturunkan langsung

11. Admin Console menurunkan cap langsung ke 3 sehingga jumlah group melebihi cap (fixture BE)
12. Buka Fixed Asset > Settings > Groups
13. Verifikasi Alert Group Consolidation dengan [Choose Groups] tampil seketika

### TC-FA-GRP-1107: Tampil untuk Total Control saat jumlah group > cap (S1)

14. Setel keadaan S1 lewat fixture BE, lalu muat ulang halaman
15. Verifikasi Alert Warning With Action tampil tepat di atas Group Context Header dengan title "Your plan allows 3 groups", body "You have 5 groups. Choose which groups stay active.", dan aksi [Choose Groups]
16. Coba tutup Alert
17. Verifikasi Alert tidak punya ikon close
18. Verifikasi Alert tetap tampil

### TC-FA-GRP-1114: Tampil untuk Default User

19. Logout, lalu login sebagai Default User client Alert
20. Buka Fixed Asset > Settings > Groups
21. Verifikasi Alert Group Consolidation tampil dengan title "Your plan allows 3 groups", body "You have 5 groups. Choose which groups stay active.", dan aksi [Choose Groups]
22. Klik [Choose Groups]
23. Verifikasi popup Group Consolidation terbuka dengan header "Choose which groups stay active"
24. Klik [Cancel]

### TC-FA-GRP-1109: Hidden untuk aktor selain Total Control dan Default User

25. Logout, lalu login sebagai Group Manager scope Region West
26. Buka Fixed Asset > Settings > Groups
27. Verifikasi Group Context Header tampil
28. Verifikasi Alert Group Consolidation tidak tampil untuk Group Manager
29. Verifikasi entry point [Choose Groups] tidak tersedia untuk Group Manager
30. Logout, lalu login sebagai Read Only
31. Buka Fixed Asset > Settings > Groups
32. Verifikasi Group Context Header tampil
33. Verifikasi Alert Group Consolidation tidak tampil untuk Read Only
34. Verifikasi entry point [Choose Groups] tidak tersedia untuk Read Only
35. Logout, lalu login sebagai Manage Group CRUD penuh
36. Buka Fixed Asset > Settings > Groups
37. Verifikasi Group Context Header tampil
38. Verifikasi Alert Group Consolidation tidak tampil untuk Manage Group CRUD penuh
39. Verifikasi entry point [Choose Groups] tidak tersedia untuk Manage Group CRUD penuh

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3, 8, 10 sampai 12, 14, 19 dan 20, 24 sampai 26, 30 dan 31, 35 dan 36: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan mengikuti keadaan tenant: S2, S3, penurunan cap langsung, lalu S1 dengan Total Control, Default User, dan tiga aktor selain Total Control/Default User. Ganti akun ditulis eksplisit (langkah 19 sampai 35); akun pertama login di hook `before` (S-07). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30), walau langkah tiap role identik.
- Group Context Header dipakai sebagai anchor positif untuk asersi Alert tidak tampil (Table Tools/halaman yang sudah termuat, 8b butir 2).
- Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (h, visibilitas Alert Group Consolidation terhadap keadaan plan dan role) dan berdiri sendiri; sekitar 14 langkah adalah penghubung ganti akun, buka halaman, dan seeding keadaan, bukan asersi baru.
- Temuan untuk QA:
  - Akun role selain Total Control (Default User, Group Manager, Read Only, Manage Group CRUD penuh) tidak sesuai dengan akun Pre-setup No 2 sampai 5; akun khusus disediakan tim FE.
  - TC-1115 Expected c ("Seleksi hanya dapat disimpan di Wizard") adalah kesimpulan; spec mengamati lewat [Save Selection] di step Wizard.
  - TC-1109 Langkah 2 dan 3 ("Ulangi sebagai Read Only" dan "Manage Group CRUD penuh") ditulis sebagai blok per role.
