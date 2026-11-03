---
id: TC-FA-RP-E2E-184-tabel-role-transaksi-setup-column-4
title: "Tabel Role Transaksi: Setup Column (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-609
  - TC-FA-RP-610
  - TC-FA-RP-611
  - TC-FA-RP-1074
coverage:
  web: automated
---

# Tabel Role Transaksi: Setup Column (4/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center`, `Joined Date`, `Badge No`; nilai Ahmad Fauzi, Budi Santoso) dipakai TC-FA-RP-1074.
- Kolom uji Custom Field (Cost Center, Joined Date, Badge No):

| Kolom |
|---|
| Cost Center |
| Joined Date |
| Badge No |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-609: Tutup popup Setup Column lewat `(X)` atau Esc membuang perubahan

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
3. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
4. Hapus centang kolom `Division`
5. Klik `(X)`
6. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Division` tetap tampil)
7. Buka kembali popup Setup Column
8. Verifikasi checkbox kolom `Division` tercentang (perubahan preview dibatalkan)
9. Hapus centang kolom `Division`
10. Tekan Esc
11. Verifikasi tabel memakai konfigurasi tersimpan terakhir (kolom `Division` tetap tampil)
12. Buka kembali popup Setup Column
13. Verifikasi checkbox kolom `Division` tercentang (perubahan preview dibatalkan)
14. Tutup popup Setup Column dengan Esc

### TC-FA-RP-610: Guard satu kolom tersisa pada Setup Column tabel Role Transaksi

15. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
16. Hapus centang semua kolom kecuali satu (hapus centang `Position` dan `Division`, sisakan `Name`)
17. Arahkan kursor ke checkbox kolom terakhir (`Name`)
18. Verifikasi checkbox kolom terakhir Disabled dengan tooltip `At least one column must remain visible.`
19. Tutup popup Setup Column dengan klik `(X)`

### TC-FA-RP-611: Konfigurasi kolom tabel Role Transaksi tidak memengaruhi tabel lain

20. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
21. Hapus centang kolom `Division` lalu klik `[Save]`
22. Klik Tab `Total Control`
23. Verifikasi tabel Tab `Total Control` memakai konfigurasi kolomnya sendiri (kolom bawaan `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated` tetap tampil)
24. Klik Tab `Transaction Role`, node `IT Infrastructure`, sub-tab `Disposal`, lalu buka popup Setup Column
25. Centang kembali kolom `Division` lalu klik `[Save]`

### TC-FA-RP-1074: Ceklis dan unceklis kolom curated Custom Field

26. Gunakan section `Asset Admin` (terbuka secara default)
27. Untuk setiap kolom pada tabel `Kolom uji Custom Field (Cost Center, Joined Date, Badge No)` di Prerequisites, lakukan langkah 28 sampai 39
28. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
29. Centang kolom pada baris iterasi
30. Verifikasi Live Preview menampilkan kolom pada baris iterasi
31. Klik `[Save]`
32. Verifikasi tabel menampilkan kolom pada baris iterasi
33. Muat ulang halaman (F5)
34. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
35. Verifikasi kolom pada baris iterasi tetap tampil pada tabel
36. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
37. Verifikasi checkbox kolom pada baris iterasi tercentang
38. Hapus centang kolom pada baris iterasi lalu klik `[Save]`
39. Verifikasi kolom pada baris iterasi tidak tampil lagi pada tabel

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-609, 610, 611, 1074). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 7, 12, 14, 19, 24, 25, 26, 34.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 28 sampai 39 (3 iterasi).
- Spec ini di atas 35 langkah (39 langkah nominal, sekitar 63 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC tidak menyatakan posisi Tab, node, dan sub-tab setelah F5 pada Tab Transaction Role; spec menulis langkah penghubung yang membuka kembali Tab, node, dan sub-tab sebelum asersi lanjutan.
  - TC-FA-RP-609 menyebut tutup lewat `(X)` lalu Esc dengan expected "perubahan preview dibatalkan dan tabel memakai konfigurasi tersimpan terakhir" tanpa cara mengamati preview setelah popup tertutup; spec mengamatinya lewat tabel dan checkbox saat popup dibuka kembali.
  - TC-FA-RP-611 memberi pilihan "tab lain atau modal Changelog" tanpa menyebut konfigurasi kolom tabel lain; spec memakai Tab `Total Control` dengan kolom bawaannya (Pre-setup #36, data kolom Tab Total Control di TC-FA-RP-74).
  - TC-FA-RP-1074 langkah 1 menulis "buka section `Asset Admin`" padahal section itu terbuka secara default (TC-FA-RP-1050); spec tidak menekan header section agar tidak menutupnya.
