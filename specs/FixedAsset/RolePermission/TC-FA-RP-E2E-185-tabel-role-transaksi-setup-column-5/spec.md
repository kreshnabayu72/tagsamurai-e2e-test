---
id: TC-FA-RP-E2E-185-tabel-role-transaksi-setup-column-5
title: "Tabel Role Transaksi: Setup Column (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1075
  - TC-FA-RP-1076
coverage:
  web: automated
---

# Tabel Role Transaksi: Setup Column (5/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center`, `Joined Date`, `Badge No`).
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

### TC-FA-RP-1075: Geser urutan kolom curated Custom Field

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
3. Gunakan section `Asset Admin` (terbuka secara default)
4. Untuk setiap kolom pada tabel `Kolom uji Custom Field (Cost Center, Joined Date, Badge No)` di Prerequisites, lakukan langkah 5 sampai 12
5. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
6. Seret kolom pada baris iterasi ke posisi paling akhir pada daftar
7. Verifikasi kolom pada baris iterasi berada di posisi paling akhir pada Live Preview
8. Klik `[Save]`
9. Verifikasi tabel memakai urutan kolom yang sama (kolom pada baris iterasi di posisi paling akhir)
10. Muat ulang halaman (F5)
11. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
12. Verifikasi urutan kolom tetap (kolom pada baris iterasi di posisi paling akhir)

### TC-FA-RP-1076: Pin dan unpin kolom curated Custom Field

13. Untuk setiap kolom pada tabel `Kolom uji Custom Field (Cost Center, Joined Date, Badge No)` di Prerequisites, lakukan langkah 14 sampai 25
14. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
15. Klik ikon Pin pada kolom pada baris iterasi
16. Verifikasi ikon Pin kolom pada baris iterasi aktif pada Live Preview
17. Klik `[Save]`
18. Scroll tabel horizontal
19. Verifikasi kolom pada baris iterasi membeku (sticky) pada tabel
20. Muat ulang halaman (F5)
21. Buka kembali Tab `Transaction Role`, node `IT Infrastructure`, dan sub-tab `Disposal`
22. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
23. Verifikasi kolom pada baris iterasi tetap ter-pin (ikon Pin aktif)
24. Klik ikon Pin kolom pada baris iterasi lagi lalu klik `[Save]`
25. Verifikasi pembekuan kolom pada baris iterasi terlepas

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-1075, 1076). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 3, 11, 21.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 5 sampai 12 (3 iterasi); langkah 14 sampai 25 (3 iterasi).
- Spec ini di atas 35 langkah (25 langkah nominal, sekitar 65 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC tidak menyatakan posisi Tab, node, dan sub-tab setelah F5 pada Tab Transaction Role; spec menulis langkah penghubung yang membuka kembali Tab, node, dan sub-tab sebelum asersi lanjutan.
  - TC-FA-RP-1075 dan 1076 menulis "buka section `Asset Admin`" padahal section itu terbuka secara default (TC-FA-RP-1050); spec tidak menekan header section.
