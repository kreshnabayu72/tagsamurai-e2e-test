---
id: TC-FA-RP-E2E-181-tabel-role-transaksi-setup-column-1
title: "Tabel Role Transaksi: Setup Column (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-600
  - TC-FA-RP-601
  - TC-FA-RP-602
  - TC-FA-RP-603
coverage:
  web: automated
---

# Tabel Role Transaksi: Setup Column (1/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini.
- Kolom uji Hideable-tampil (Name, Position, Division):

| Kolom |
|---|
| Name |
| Position |
| Division |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-600: Screening overlay Column Visibility tabel Role Transaksi

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
3. Klik header `(⋯)` kolom Column Visibility
4. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
5. Verifikasi kolom bawaan tampil tercentang aktif: `Name`, `Position`, `Division`
6. Verifikasi kolom curated tidak tercentang: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`
7. Verifikasi drag handle tersedia pada daftar
8. Tutup overlay dengan Esc

### TC-FA-RP-601: Screening popup Setup Column tabel Role Transaksi (3 zona)

9. Klik header `(⋯)`
10. Klik `Setup Column...`
11. Verifikasi Zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`
12. Verifikasi Zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel
13. Verifikasi Zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`
14. Tutup popup Setup Column dengan klik `(X)`

### TC-FA-RP-602: Ceklis dan unceklis kolom kelas Hideable-tampil

15. Untuk setiap kolom pada tabel `Kolom uji Hideable-tampil (Name, Position, Division)` di Prerequisites, lakukan langkah 16 sampai 27
16. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
17. Hapus centang kolom pada baris iterasi
18. Verifikasi Live Preview tidak lagi menampilkan kolom pada baris iterasi
19. Klik `[Save]`
20. Verifikasi tabel tidak menampilkan kolom pada baris iterasi
21. Muat ulang halaman (F5)
22. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
23. Verifikasi kolom pada baris iterasi tetap tidak tampil pada tabel
24. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
25. Verifikasi checkbox kolom pada baris iterasi tidak tercentang
26. Centang kembali kolom pada baris iterasi lalu klik `[Save]`
27. Verifikasi kolom pada baris iterasi tampil kembali pada tabel

### TC-FA-RP-603: Geser urutan kolom kelas Hideable-tampil

28. Untuk setiap kolom pada tabel `Kolom uji Hideable-tampil (Name, Position, Division)` di Prerequisites, lakukan langkah 29 sampai 36
29. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
30. Seret kolom pada baris iterasi ke posisi paling akhir pada daftar
31. Verifikasi kolom pada baris iterasi berada di posisi paling akhir pada Live Preview
32. Klik `[Save]`
33. Verifikasi tabel memakai urutan kolom yang sama (kolom pada baris iterasi di posisi paling akhir)
34. Muat ulang halaman (F5)
35. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
36. Verifikasi urutan kolom tetap (kolom pada baris iterasi di posisi paling akhir)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-600, 601, 602, 603). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 8, 14, 22, 35.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 16 sampai 27 (3 iterasi); langkah 29 sampai 36 (3 iterasi).
- Spec ini di atas 35 langkah (36 langkah nominal, sekitar 76 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Seret kolom `Name`, `Position`, lalu `Division` ke posisi paling akhir berurutan mengembalikan urutan awal ketiga kolom; hook `after` tetap menghapus preferensi kolom.
- Temuan untuk QA:
  - TC-FA-RP-600 sampai 603 mulai dari posisi Tab Transaction Role, tetapi halaman dibuka di Tab Total Control oleh hook suite; spec menulis langkah penghubung membuka Tab itu.
  - TC tidak menyatakan posisi Tab, node, dan sub-tab setelah F5 pada Tab Transaction Role; spec menulis langkah penghubung yang membuka kembali Tab, node, dan sub-tab sebelum asersi lanjutan.
  - TC-FA-RP-602 dan 603 menulis langkah buka popup hanya sekali sebelum pengulangan; spec membuka popup di awal tiap iterasi karena popup tertutup oleh `[Save]` dan F5.
