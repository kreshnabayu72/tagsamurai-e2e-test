---
id: TC-FA-RP-E2E-183-tabel-role-transaksi-setup-column-3
title: "Tabel Role Transaksi: Setup Column (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-606
  - TC-FA-RP-607
  - TC-FA-RP-608
coverage:
  web: automated
---

# Tabel Role Transaksi: Setup Column (3/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini.
- Kolom uji Curated-tersembunyi (Email, Activation Status, Temporary User, Temporary Until, TAG):

| Kolom |
|---|
| Email |
| Activation Status |
| Temporary User |
| Temporary Until |
| TAG |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-606: Geser urutan kolom kelas Curated-tersembunyi

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
3. Untuk setiap kolom pada tabel `Kolom uji Curated-tersembunyi (Email, Activation Status, Temporary User, Temporary Until, TAG)` di Prerequisites, lakukan langkah 4 sampai 11
4. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
5. Seret kolom pada baris iterasi ke posisi paling akhir pada daftar
6. Verifikasi kolom pada baris iterasi berada di posisi paling akhir pada Live Preview
7. Klik `[Save]`
8. Verifikasi tabel memakai urutan kolom yang sama (kolom pada baris iterasi di posisi paling akhir)
9. Muat ulang halaman (F5)
10. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
11. Verifikasi urutan kolom tetap (kolom pada baris iterasi di posisi paling akhir)

### TC-FA-RP-607: Pin dan unpin kolom kelas Curated-tersembunyi

12. Untuk setiap kolom pada tabel `Kolom uji Curated-tersembunyi (Email, Activation Status, Temporary User, Temporary Until, TAG)` di Prerequisites, lakukan langkah 13 sampai 24
13. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
14. Klik ikon Pin pada kolom pada baris iterasi
15. Verifikasi ikon Pin kolom pada baris iterasi aktif pada Live Preview
16. Klik `[Save]`
17. Scroll tabel horizontal
18. Verifikasi kolom pada baris iterasi membeku (sticky) pada tabel
19. Muat ulang halaman (F5)
20. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
21. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
22. Verifikasi kolom pada baris iterasi tetap ter-pin (ikon Pin aktif)
23. Klik ikon Pin kolom pada baris iterasi lagi lalu klik `[Save]`
24. Verifikasi pembekuan kolom pada baris iterasi terlepas

### TC-FA-RP-608: Reset to Default pada Setup Column tabel Role Transaksi

25. Hapus centang kolom `Division`, seret kolom `Position` ke posisi paling akhir pada daftar, dan klik ikon Pin pada kolom `Name`, lalu klik `[Save]`
26. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
27. Klik `[Reset to Default]` lalu `[Save]`
28. Verifikasi kolom `Division` tampil kembali pada tabel
29. Verifikasi kolom `Position` kembali ke urutan semula
30. Verifikasi kolom `Name` tidak ter-pin
31. Muat ulang halaman (F5)
32. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
33. Verifikasi susunan kolom tetap default setelah F5 (`Division` tampil, `Position` pada urutan semula, `Name` tidak ter-pin)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-606, 607, 608). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 10, 20, 32.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 4 sampai 11 (5 iterasi); langkah 13 sampai 24 (5 iterasi).
- Spec ini di atas 35 langkah (33 langkah nominal, sekitar 113 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Spec 606 mengubah urutan kolom lewat seret; urutan itu dikembalikan oleh `[Reset to Default]` pada TC-FA-RP-608 dan preferensi dihapus di hook `after`.
- Temuan untuk QA:
  - TC tidak menyatakan posisi Tab, node, dan sub-tab setelah F5 pada Tab Transaction Role; spec menulis langkah penghubung yang membuka kembali Tab, node, dan sub-tab sebelum asersi lanjutan.
