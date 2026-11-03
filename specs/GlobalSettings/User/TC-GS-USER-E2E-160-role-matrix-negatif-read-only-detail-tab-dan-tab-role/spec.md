---
id: TC-GS-USER-E2E-160-role-matrix-negatif-read-only-detail-tab-dan-tab-role
title: "Role Matrix Negatif: Detail User untuk Read Only (Tooltip Checkbox Tab Role Baris Switch OFF, Keenam Tab Detail Tanpa Kontrol Tulis, dan Tab Responsibilities Murni Tampilan)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-1107
  - TC-GS-USER-1128
  - TC-GS-USER-1129
coverage:
  web: automated
---

# Role Matrix Negatif: Detail User untuk Read Only (Tooltip Checkbox Tab Role Baris Switch OFF, Keenam Tab Detail Tanpa Kontrol Tulis, dan Tab Responsibilities Murni Tampilan)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (satu role; seluruh TC sumber berprecondition Read Only):

| Role | Akun | Nama user | Env var password |
|---|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Yudi Pratomo (Tabel Pre-setup No. 3) | `Spectra.env.GS_RO_PASSWORD` |

- Login akun Read Only dilakukan di hook `before` (aktor pertama dan satu-satunya spec); halaman dibuka hook `beforeEach` suite; tidak ada langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_RO_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after` (padanan Ahmad Fauzi, Tabel Pre-setup No. 13): `Ahmad Fauzi {runId}-160`, email `ahmadfauzi+{runId}-160@qwertysystem.net`, Activated, holder `Manage user and role` (non-tier); baris `Manage files` belum pernah di-assign (switch Active OFF). Target memiliki data pada Tab Changelog, System Log, User Log, dan keempat sub-tab Responsibilities (sedikitnya satu baris per sub-tab), dipakai sebagai precondition TC dan tidak diasersi selain keberadaan baris sub-tab Responsibilities (TC-GS-USER-1129).
- Tabel "Sub-tab diuji" (dipakai langkah 32 sampai 34): `Borrowed Assets`, `Assigned Assets`, `Pending Approvals`, `Pending Tasks`.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): seeding user dengan assignment role dan data Changelog, System Log, User Log, serta baris Responsibilities FAMS (borrowed, assigned, approval, task) lewat API; hover elemen disabled untuk membaca tooltip.
- State global yang diubah: tidak ada. Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): hapus user seed dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-USER-1107: Tooltip checkbox baris switch OFF untuk Read Only

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-160`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-160` di User List
3. Klik Tab `Role`
4. Hover checkbox Delete baris `Manage files`
5. Verifikasi checkbox Delete baris `Manage files` tampil namun disabled dengan tooltip `"Read Only access cannot modify data."`

### TC-GS-USER-1128: Keenam tab Detail dapat dibuka tanpa kontrol tulis aktif

6. Verifikasi Tab `Role` dapat dibuka dan kontennya tampil
7. Hover switch Active baris `Manage files`
8. Verifikasi switch Active baris `Manage files` tampil namun disabled dengan tooltip `"Read Only access cannot modify data."`
9. Hover checkbox Update baris `Manage user and role`
10. Verifikasi checkbox Update baris `Manage user and role` tampil namun disabled dengan tooltip `"Read Only access cannot modify data."`
11. Klik Tab `Responsibilities`
12. Verifikasi Tab `Responsibilities` dapat dibuka dan kontennya tampil
13. Verifikasi Tab `Responsibilities` tanpa kontrol tulis
14. Klik Tab `Non-Login User`
15. Verifikasi Tab `Non-Login User` dapat dibuka dan kontennya tampil
16. Verifikasi Tab `Non-Login User` tanpa kontrol tulis
17. Klik Tab `Changelog`
18. Verifikasi Tab `Changelog` dapat dibuka dan kontennya tampil
19. Verifikasi Download CSV/XLSX tersedia di Tab `Changelog`
20. Verifikasi Tab `Changelog` tanpa kontrol tulis
21. Klik Tab `System Log`
22. Verifikasi Tab `System Log` dapat dibuka dan kontennya tampil
23. Verifikasi Download CSV/XLSX tersedia di Tab `System Log`
24. Verifikasi Tab `System Log` tanpa kontrol tulis
25. Klik Tab `User Log`
26. Verifikasi Tab `User Log` dapat dibuka dan kontennya tampil
27. Verifikasi Download CSV/XLSX tersedia di Tab `User Log`
28. Verifikasi Tab `User Log` tanpa kontrol tulis

### TC-GS-USER-1129: Tab Responsibilities murni tampilan

29. Klik Tab `Responsibilities`
30. Verifikasi Tab `Responsibilities` tampil dan aktif
31. Verifikasi keempat sub-tab `Borrowed Assets`, `Assigned Assets`, `Pending Approvals`, dan `Pending Tasks` tampil dan aktif
Untuk setiap sub-tab pada tabel "Sub-tab diuji" (langkah 32 sampai 34):
32. Klik sub-tab
33. Verifikasi sedikitnya satu baris tampil di sub-tab
34. Verifikasi baris sub-tab tanpa kontrol tulis maupun deep-link

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (34 langkah nominal, 43 dengan ekspansi langkah 32 sampai 34 untuk empat sub-tab) karena tiga TC berada di satu kelas harness (role matrix negatif, baca saja), satu aktor (Read Only), dan satu Detail user seed yang sama; tiap blok TC berdiri sendiri dan tidak mengubah data.
- Langkah yang diulang per sub-tab (langkah 32 sampai 34) sah karena parameter tiap iterasi ada di tabel "Sub-tab diuji" di Prerequisites; `Verifikasi` tetap satu per klausa.
- Urutan TC sumber: TC-GS-USER-1107 dan TC-GS-USER-1128 memakai Detail dan Tab Role yang sama (langkah 1 sampai 2 TC-GS-USER-1128 dipenuhi langkah 2 sampai 3); TC-GS-USER-1129 terakhir karena membuka kembali Tab `Responsibilities`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search target sebelum Klik Name, R-16), 11, 14, 17, 21, 25, 29 (pindah tab), dan 32 (pindah sub-tab).
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC, hanya sebagai anchor): langkah 12, 15, 18, 22, 26 (tab tampil dengan kontennya) mendahului asersi "tanpa kontrol tulis"; langkah 33 (sedikitnya satu baris tampil) mendahului langkah 34.
- Pemilihan elemen yang di-hover pada TC-GS-USER-1128 (switch Active baris `Manage files`, checkbox Update baris `Manage user and role`) adalah pilihan spec karena TC tidak menyebut baris.
- Pembagian TC lintas spec: Role Matrix Read Only untuk kontrol User List dan Detail lain ada di spec 009; tooltip prioritas suspended melawan Read Only (TC-GS-USER-1130) ada di spec 176.
- Temuan untuk QA:
  - TC-GS-USER-1128 Expected c ("tab lain tanpa kontrol tulis") tidak mendefinisikan kontrol tulis per tab; spec mengasersi tidak ada kontrol tulis tanpa merinci elemen.
  - TC-GS-USER-1128 langkah 3 "Amati kontrol di tiap tab" tidak menyebut baris Tab Role yang diamati; spec memilih baris sendiri.
  - TC-GS-USER-1129 Expected b ("kontrol tulis maupun deep-link pada baris") tidak menyebut sub-tab mana; spec mengasersi pada keempat sub-tab dengan data yang disediakan tim FE/BE.
  - TC-GS-USER-1107, 1128, 1129 memakai user Pre-setup (Ahmad Fauzi); spec memakai seed milik spec (S-06).
