---
id: TC-FA-RP-E2E-199-detail-role-setup-column-3
title: "Detail Role: Setup Column (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-649
  - TC-FA-RP-650
coverage:
  web: automated
---

# Detail Role: Setup Column (3/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center` `CC-100`/`CC-200`, `Joined Date`, `Badge No`; Ahmad Fauzi `CC-100`, 10/01/26, `BN-77`; Budi Santoso `CC-200`, 15/02/26, `BN-88`).
- Kolom uji Curated-tersembunyi Detail Role (Email, Activation Status, Temporary User, Temporary Until, TAG, Cost Center, Joined Date, Badge No):

| Kolom |
|---|
| Email |
| Activation Status |
| Temporary User |
| Temporary Until |
| TAG |
| Cost Center |
| Joined Date |
| Badge No |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-649: Ceklis dan unceklis kolom kelas Curated-tersembunyi

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Untuk setiap kolom pada tabel `Kolom uji Curated-tersembunyi Detail Role (Email, Activation Status, Temporary User, Temporary Until, TAG, Cost Center, Joined Date, Badge No)` di Prerequisites, lakukan langkah 5 sampai 15
5. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
6. Centang kolom pada baris iterasi
7. Verifikasi Live Preview menampilkan kolom pada baris iterasi
8. Klik `[Save]`
9. Verifikasi tabel menampilkan kolom pada baris iterasi
10. Muat ulang halaman (F5)
11. Verifikasi kolom pada baris iterasi tetap tampil pada tabel
12. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
13. Verifikasi checkbox kolom pada baris iterasi tercentang
14. Hapus centang kolom pada baris iterasi lalu klik `[Save]`
15. Verifikasi kolom pada baris iterasi tidak tampil lagi pada tabel

### TC-FA-RP-650: Geser urutan kolom kelas Curated-tersembunyi

16. Untuk setiap kolom pada tabel `Kolom uji Curated-tersembunyi Detail Role (Email, Activation Status, Temporary User, Temporary Until, TAG, Cost Center, Joined Date, Badge No)` di Prerequisites, lakukan langkah 17 sampai 23
17. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
18. Seret kolom pada baris iterasi ke posisi paling akhir pada daftar
19. Verifikasi kolom pada baris iterasi berada di posisi paling akhir pada Live Preview
20. Klik `[Save]`
21. Verifikasi tabel memakai urutan kolom yang sama (kolom pada baris iterasi di posisi paling akhir)
22. Muat ulang halaman (F5)
23. Verifikasi urutan kolom tetap (kolom pada baris iterasi di posisi paling akhir)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-649, 650). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 5 sampai 15 (8 iterasi); langkah 17 sampai 23 (8 iterasi).
- Spec ini di atas 35 langkah (23 langkah nominal, sekitar 149 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
