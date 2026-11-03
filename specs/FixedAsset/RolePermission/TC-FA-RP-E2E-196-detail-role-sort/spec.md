---
id: TC-FA-RP-E2E-196-detail-role-sort
title: "Detail Role: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-641
  - TC-FA-RP-642
  - TC-FA-RP-643
  - TC-FA-RP-1079
coverage:
  web: automated
---

# Detail Role: Sort

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center` `CC-100`/`CC-200`, `Joined Date`, `Badge No`; Ahmad Fauzi `CC-100`, 10/01/26, `BN-77`; Budi Santoso `CC-200`, 15/02/26, `BN-88`).
- Urutan ascending TC-FA-RP-642:

| Kolom | Urutan ascending |
|---|---|
| Name | Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata, Endah Susanti, Fitri Handayani |
| Group | `Data Center` (Ahmad Fauzi, Dimas Pranata), `Dock 1` (Fitri Handayani), `Head Office` (Citra Lestari), `Helpdesk` (Budi Santoso), `Rack A1` (Endah Susanti), berdasarkan nama group |
| Position | Asset Custodian (Ahmad), Finance Officer (Fitri), HR Officer (Citra), IT Support (Dimas), Procurement Officer (Endah), Warehouse Staff (Budi) |
| Division | Finance (Fitri), HR (Citra), IT Operations (Dimas), Logistics (Ahmad, Budi), Procurement (Endah) |

- Urutan ascending TC-FA-RP-1079:

| Kolom | Label klik 1 dan 2 | Urutan ascending |
|---|---|---|
| Email | ascending, descending | Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata, Endah Susanti, Fitri Handayani |
| Activation Status | ascending, descending | `Activated` (lima baris) lalu `Pending Email Confirmation` (Fitri Handayani) |
| Temporary User | ascending, descending | `No` (lima baris) sebelum `Yes` (Fitri Handayani) |
| Temporary Until | ascending (Oldest First), descending (Newest First) | Fitri Handayani lebih dulu lalu lima baris tanpa nilai di akhir |
| TAG | ascending, descending | Ahmad Fauzi (`TAG-1001`) lebih dulu lalu lima baris tanpa nilai di akhir |
| Cost Center | ascending, descending | Ahmad Fauzi (`CC-100`), Budi Santoso (`CC-200`), lalu empat baris tanpa nilai di akhir |
| Joined Date | ascending (Oldest First), descending (Newest First) | Ahmad Fauzi, Budi Santoso, lalu empat baris tanpa nilai di akhir |
| Badge No | ascending, descending | Ahmad Fauzi (`BN-77`), Budi Santoso (`BN-88`), lalu empat baris tanpa nilai di akhir |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-641: Sort default Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Verifikasi tabel terurut Name A-Z: Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata, Endah Susanti, Fitri Handayani

### TC-FA-RP-642: Sort Detail Role siklus tiga state kelas teks

5. Untuk setiap baris tabel `Urutan ascending TC-FA-RP-642` di Prerequisites, lakukan langkah 6 sampai 11
6. Klik header kolom pada baris iterasi sekali
7. Verifikasi baris terurut ascending sesuai kolom Urutan ascending pada baris iterasi
8. Klik header kolom pada baris iterasi kedua kali
9. Verifikasi baris terurut descending (kebalikan urutan ascending)
10. Klik header kolom pada baris iterasi ketiga kali
11. Verifikasi urutan kembali ke default sort tabel (Name A-Z)

### TC-FA-RP-643: Guard kolom non-sortable Detail Role

12. Arahkan kursor ke header kolom Checkbox, matriks CRUD, dan Actions
13. Verifikasi ketiga kolom tidak memiliki ikon sort
14. Klik header kolom Checkbox
15. Klik header kolom Checkbox sekali lagi untuk membatalkan seleksi baris
16. Klik header kolom matriks CRUD
17. Klik header kolom Actions
18. Verifikasi klik pada header ketiga kolom tidak mengubah urutan (urutan Name A-Z: Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata, Endah Susanti, Fitri Handayani)

### TC-FA-RP-1079: Sort Detail Role siklus tiga state kolom curated

19. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
20. Centang kolom `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, dan `Badge No` lalu klik `[Save]`
21. Untuk setiap baris tabel `Urutan ascending TC-FA-RP-1079` di Prerequisites, lakukan langkah 22 sampai 27
22. Klik header kolom pada baris iterasi sekali
23. Verifikasi baris terurut ascending sesuai kolom Urutan ascending pada baris iterasi (label klik 1 sesuai kolom Label)
24. Klik header kolom pada baris iterasi kedua kali
25. Verifikasi baris terurut descending (label klik 2 sesuai kolom Label)
26. Klik header kolom pada baris iterasi ketiga kali
27. Verifikasi urutan kembali ke default sort tabel (Name A-Z)
28. Sembunyikan kembali kedelapan kolom curated lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-641, 642, 643, 1079). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 15, 28.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 6 sampai 11 (4 iterasi); langkah 22 sampai 27 (8 iterasi).
- Spec ini di atas 35 langkah (28 langkah nominal, sekitar 88 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-642 dan 1079 menyebut urutan descending hanya sebagai "klik 2 descending"; spec mengasersinya sebagai kebalikan urutan ascending dan tidak mengasersi urutan antar baris bernilai sama atau tanpa nilai.
  - TC-FA-RP-643 menyuruh mengklik header Checkbox tanpa menyebut efeknya pada seleksi baris; spec menambah langkah penghubung klik ulang untuk membatalkan kemungkinan seleksi semua baris.
