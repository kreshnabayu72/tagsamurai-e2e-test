---
id: TC-FA-RP-E2E-182-tabel-role-transaksi-setup-column-2
title: "Tabel Role Transaksi: Setup Column (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-604
  - TC-FA-RP-605
coverage:
  web: automated
---

# Tabel Role Transaksi: Setup Column (2/5)

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

### TC-FA-RP-604: Pin dan unpin kolom kelas Hideable-tampil

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
3. Untuk setiap kolom pada tabel `Kolom uji Hideable-tampil (Name, Position, Division)` di Prerequisites, lakukan langkah 4 sampai 15
4. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
5. Klik ikon Pin pada kolom pada baris iterasi
6. Verifikasi ikon Pin kolom pada baris iterasi aktif pada Live Preview
7. Klik `[Save]`
8. Scroll tabel horizontal
9. Verifikasi kolom pada baris iterasi membeku (sticky) pada tabel
10. Muat ulang halaman (F5)
11. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
12. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
13. Verifikasi kolom pada baris iterasi tetap ter-pin (ikon Pin aktif)
14. Klik ikon Pin kolom pada baris iterasi lagi lalu klik `[Save]`
15. Verifikasi pembekuan kolom pada baris iterasi terlepas

### TC-FA-RP-605: Ceklis dan unceklis kolom kelas Curated-tersembunyi

16. Untuk setiap kolom pada tabel `Kolom uji Curated-tersembunyi (Email, Activation Status, Temporary User, Temporary Until, TAG)` di Prerequisites, lakukan langkah 17 sampai 28
17. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
18. Centang kolom pada baris iterasi
19. Verifikasi Live Preview menampilkan kolom pada baris iterasi
20. Klik `[Save]`
21. Verifikasi tabel menampilkan kolom pada baris iterasi
22. Muat ulang halaman (F5)
23. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
24. Verifikasi kolom pada baris iterasi tetap tampil pada tabel
25. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
26. Verifikasi checkbox kolom pada baris iterasi tercentang
27. Hapus centang kolom pada baris iterasi lalu klik `[Save]`
28. Verifikasi kolom pada baris iterasi tidak tampil lagi pada tabel

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-604, 605). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 11, 23.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 4 sampai 15 (3 iterasi); langkah 17 sampai 28 (5 iterasi).
- Spec ini di atas 35 langkah (28 langkah nominal, sekitar 100 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC tidak menyatakan posisi Tab, node, dan sub-tab setelah F5 pada Tab Transaction Role; spec menulis langkah penghubung yang membuka kembali Tab, node, dan sub-tab sebelum asersi lanjutan.
