---
id: TC-FA-RP-E2E-197-detail-role-setup-column-1
title: "Detail Role: Setup Column (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-644
  - TC-FA-RP-645
  - TC-FA-RP-646
coverage:
  web: automated
---

# Detail Role: Setup Column (1/5)

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

### TC-FA-RP-644: Screening overlay Column Visibility Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik header `(⋯)` kolom Column Visibility
5. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
6. Verifikasi kolom bawaan tampil tercentang aktif: `Name`, `Group`, `Position`, `Division`
7. Verifikasi kolom curated tidak tercentang: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`
8. Verifikasi drag handle tersedia pada daftar
9. Tutup overlay dengan Esc

### TC-FA-RP-645: Screening popup Setup Column Detail Role (3 zona)

10. Klik header `(⋯)`
11. Klik `Setup Column...`
12. Verifikasi Zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`
13. Verifikasi Zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel
14. Verifikasi Zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`
15. Tutup popup Setup Column dengan klik `(X)`

### TC-FA-RP-646: Ceklis dan unceklis kolom kelas Hideable-tampil

16. Untuk setiap kolom pada tabel `Kolom uji Hideable-tampil Detail Role (Name, Group, Position, Division)` di Prerequisites, lakukan langkah 17 sampai 27
17. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
18. Hapus centang kolom pada baris iterasi
19. Verifikasi Live Preview tidak lagi menampilkan kolom pada baris iterasi
20. Klik `[Save]`
21. Verifikasi tabel tidak menampilkan kolom pada baris iterasi
22. Muat ulang halaman (F5)
23. Verifikasi kolom pada baris iterasi tetap tidak tampil pada tabel
24. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
25. Verifikasi checkbox kolom pada baris iterasi tidak tercentang
26. Centang kembali kolom pada baris iterasi lalu klik `[Save]`
27. Verifikasi kolom pada baris iterasi tampil kembali pada tabel

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-644, 645, 646). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 9, 15.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 17 sampai 27 (4 iterasi).
- Spec ini di atas 35 langkah (27 langkah nominal, sekitar 60 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-646 menulis langkah buka popup sekali sebelum pengulangan; spec membuka popup di awal tiap iterasi karena `[Save]` menutup popup.
