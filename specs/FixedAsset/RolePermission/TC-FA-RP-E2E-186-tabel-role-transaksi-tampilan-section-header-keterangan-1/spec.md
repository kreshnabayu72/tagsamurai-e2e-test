---
id: TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1
title: "Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-612
  - TC-FA-RP-613
  - TC-FA-RP-614
  - TC-FA-RP-1013
  - TC-FA-RP-1027
coverage:
  web: automated
---

# Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (1/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini.
- Pre-setup #43 (Fajar Nugroho Group Manager di `IT Infrastructure`; Total Control Siti Rahmawati dan Rina Wulandari) dipakai TC-FA-RP-1013.
- Pre-setup #21 (pemegang Update `Manage asset & TAG`; Detail Role `Manage asset & TAG`, node `IT Infrastructure` dengan toggle `Require Approval for Registration` OFF) dipakai TC-FA-RP-1027. Toggle diaktifkan lalu dimatikan kembali oleh spec; nilai akhirnya OFF dan dipulihkan juga di hook `after`.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon info dan avatar; membaca nilai toggle `Require Approval for Registration` untuk pemulihan di hook `after`.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-612: Search tabel Role Transaksi pada keempat section

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
3. Buka section `Monitoring & Report`, `Staff`, dan `Approver` (ketiganya tertutup secara default)
4. Ketik Search `a` pada section `Asset Admin`, tekan Enter
5. Verifikasi tabel section `Asset Admin` menampilkan hasil Search `a` (Ahmad Fauzi, Dimas Pranata, Nadia Putri)
6. Verifikasi section `Monitoring & Report` tidak ikut tersaring dan menampilkan Oscar Pratama
7. Verifikasi section `Staff` tidak ikut tersaring dan menampilkan Putri Wulandari
8. Verifikasi section `Approver` tidak ikut tersaring dan menampilkan Pandu Wijaya
9. Ketik Search `pandu` pada section `Approver`, tekan Enter
10. Verifikasi section `Approver` menampilkan Pandu Wijaya
11. Klik `(←)` pada kotak Search section `Approver`
12. Klik `(←)` pada kotak Search section `Asset Admin`

### TC-FA-RP-613: Tabel Role Transaksi tanpa pagination, tanpa Download, dan tanpa bulk

13. Verifikasi toolbar tiap section hanya `Search | Filter | [+ Assign]`
14. Verifikasi tidak ada ikon Download atau Changelog pada section, tidak ada pagination, dan tidak ada kolom Checkbox

### TC-FA-RP-614: State tabel Role Transaksi disimpan per sub-tab selama di halaman

15. Ketik Search `nadia` pada section `Asset Admin`, tekan Enter
16. Klik sub-tab `Damaged`
17. Klik kembali sub-tab `Disposal`
18. Verifikasi Search `nadia` pada section `Asset Admin` sub-tab `Disposal` tetap terpasang (state tiap sub-tab dipulihkan)
19. Klik `(←)` pada kotak Search section `Asset Admin`

### TC-FA-RP-1013: Tabel Approver tidak memuat Group Manager dan Total Control serta tanpa kolom Type

20. Verifikasi tabel section `Approver` memuat baris Pandu Wijaya (Approver manual) sebagai satu-satunya baris
21. Verifikasi Fajar Nugroho (Group Manager) serta Siti Rahmawati dan Rina Wulandari (Total Control) tidak tampil sebagai baris
22. Verifikasi header kolom `Name`, `Position`, `Division` tanpa kolom `Type`

### TC-FA-RP-1027: Keterangan approver registrasi berupa tooltip pada ikon info

23. Klik Tab `System`
24. Klik Role Name `Manage asset & TAG` pada section Group Role
25. Klik node `IT Infrastructure` di Sidebar Group Tree (toggle `Require Approval for Registration` OFF)
26. Verifikasi tidak ada baris teks keterangan approver di bawah sub-label toggle
27. Arahkan kursor ke ikon info `ⓘ` di samping label toggle
28. Verifikasi tooltip ikon info tampil dengan teks `Approvers are users with Update access on Manage asset & TAG that covers this group, Group Managers over this group, and Total Control users. Grant Update access in the table below.`
29. Aktifkan toggle `Require Approval for Registration`
30. Arahkan kursor ke ikon info `ⓘ`
31. Verifikasi ikon info tetap ada pada toggle ON
32. Verifikasi tooltip tampil dengan teks yang sama pada toggle ON
33. Matikan toggle `Require Approval for Registration` kembali
34. Arahkan kursor ke ikon info `ⓘ`
35. Verifikasi ikon info tetap ada pada toggle OFF
36. Verifikasi tooltip tampil dengan teks yang sama pada toggle OFF
37. Verifikasi panel tidak memuat tabel atau daftar approver, tanpa Checkbox, Actions, Search, maupun Filter

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-612, 613, 614, 1013, 1027). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 3, 11, 12, 19.
- Spec ini di atas 35 langkah (37 langkah nominal, sekitar 37 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-612 berjudul Search, Filter, dan Setup Column pada keempat section, tetapi langkah dan expected hanya memuat Search; spec hanya menulis Search.
  - TC-FA-RP-612: keyword `a` cocok dengan seluruh baris seed pada keempat section (Ahmad Fauzi, Dimas Pranata, Nadia Putri, Oscar Pratama, Putri Wulandari, Pandu Wijaya), sehingga hasil Search `a` tidak membedakan section yang tersaring dari yang tidak; spec mengasersi baris yang tampil sesuai TC.
  - TC-FA-RP-612 dan 613 mengamati section Monitoring & Report, Staff, dan Approver yang tertutup secara default (TC-FA-RP-1050); spec menambah langkah penghubung membuka ketiga section agar toolbar dan tabelnya teramati.
  - TC-FA-RP-1027 mengaktifkan toggle registrasi pada node `IT Infrastructure` tanpa menyebut toast, dialog konfirmasi, atau entri log; spec tidak mengasersinya dan hanya memulihkan nilai awal OFF.
