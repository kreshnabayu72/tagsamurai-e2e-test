---
id: TC-FA-RP-E2E-198-detail-role-setup-column-2
title: "Detail Role: Setup Column (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-647
  - TC-FA-RP-648
coverage:
  web: automated
---

# Detail Role: Setup Column (2/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Kolom uji Hideable-tampil Detail Role (Name, Group, Position, Division):

| Kolom |
|---|
| Name |
| Group |
| Position |
| Division |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-647: Geser urutan kolom kelas Hideable-tampil

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Untuk setiap kolom pada tabel `Kolom uji Hideable-tampil Detail Role (Name, Group, Position, Division)` di Prerequisites, lakukan langkah 5 sampai 11
5. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
6. Seret kolom pada baris iterasi ke posisi paling akhir pada daftar
7. Verifikasi kolom pada baris iterasi berada di posisi paling akhir pada Live Preview
8. Klik `[Save]`
9. Verifikasi tabel memakai urutan kolom yang sama (kolom pada baris iterasi di posisi paling akhir)
10. Muat ulang halaman (F5)
11. Verifikasi urutan kolom tetap (kolom pada baris iterasi di posisi paling akhir)

### TC-FA-RP-648: Pin dan unpin kolom kelas Hideable-tampil

12. Untuk setiap kolom pada tabel `Kolom uji Hideable-tampil Detail Role (Name, Group, Position, Division)` di Prerequisites, lakukan langkah 13 sampai 23
13. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
14. Klik ikon Pin pada kolom pada baris iterasi
15. Verifikasi ikon Pin kolom pada baris iterasi aktif pada Live Preview
16. Klik `[Save]`
17. Scroll tabel horizontal
18. Verifikasi kolom pada baris iterasi membeku (sticky) pada tabel
19. Muat ulang halaman (F5)
20. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
21. Verifikasi kolom pada baris iterasi tetap ter-pin (ikon Pin aktif)
22. Klik ikon Pin kolom pada baris iterasi lagi lalu klik `[Save]`
23. Verifikasi pembekuan kolom pada baris iterasi terlepas

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-647, 648). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 5 sampai 11 (4 iterasi); langkah 13 sampai 23 (4 iterasi).
- Spec ini di atas 35 langkah (23 langkah nominal, sekitar 77 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Seret keempat kolom ke posisi paling akhir berurutan mengembalikan urutan awal; hook `after` tetap menghapus preferensi kolom.
