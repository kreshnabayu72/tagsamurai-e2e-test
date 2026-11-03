---
id: TC-FA-RP-E2E-209-table-user-picker-search-filter-dan-sort-4
title: "Table User Picker: Search, Filter, dan Sort (4/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-688
  - TC-FA-RP-689
  - TC-FA-RP-1080
  - TC-FA-RP-1081
coverage:
  web: automated
---

# Table User Picker: Search, Filter, dan Sort (4/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #41 (kandidat popup Assign Total Control, belum Total Control, 12 pengguna: Citra Lestari (HR Officer, HR), Dimas Pranata (IT Support, IT Operations; `TAG-2002`; `CC-100`; 10/01/26; `BN-77`), Endah Susanti (Procurement Officer, Procurement; `CC-200`; 15/02/26; `BN-88`), Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama (Inactive), Gilang Prakoso (Pending Activation), Hana Permata (Temporary User Yes dengan Temporary Until terisi); email `[namalengkaptanpaspasi]@qwertysystem.net`), #36, #37, dan #17 (pengguna yang sudah Total Control, Read Only, dan variasi Home Group). Popup hanya dibaca; tidak ada Assign yang dikirim dan Pre-setup tidak diubah.
- Pre-setup #22 (Custom Field aktif `Cost Center`, `Joined Date`, `Badge No`) dipakai TC kolom Custom Field.
- Urutan ascending TC-FA-RP-689:

| Kolom | Urutan ascending |
|---|---|
| Name | Citra Lestari, Dewi Anggraini, Dimas Pranata, Endah Susanti, Gilang Prakoso, Gunawan Halim, Hana Permata, Hesti Rahma, Indra Kusuma, Joko Santoso, Maya Anggraeni, Yoga Pratama (halaman pertama memuat sepuluh nama pertama) |
| Email | urutan A-Z alamat email `[namalengkaptanpaspasi]@qwertysystem.net` |

- Urutan ascending TC-FA-RP-1080:

| Kolom | Urutan ascending |
|---|---|
| Position | HR Officer (Citra Lestari) mendahului IT Support (Dimas Pranata) dan IT Support mendahului Procurement Officer (Endah Susanti) |
| Division | HR (Citra Lestari) mendahului IT Operations (Dimas Pranata) dan IT Operations mendahului Procurement (Endah Susanti) |
| Status | seluruh baris `Active` mendahului Yoga Pratama (`Inactive`) |

- Urutan ascending TC-FA-RP-1081:

| Kolom | Label klik 1 dan 2 | Urutan ascending |
|---|---|---|
| Activation Status | ascending, descending | `Activated` (sebelas baris) lalu `Pending Activation` (Gilang Prakoso) |
| Temporary User | ascending, descending | `No` (sebelas baris) sebelum `Yes` (Hana Permata) |
| Temporary Until | ascending (Oldest First), descending (Newest First) | Hana Permata lebih dulu lalu sebelas baris tanpa nilai di akhir |
| TAG | ascending, descending | Dimas Pranata (`TAG-2002`) lebih dulu lalu sebelas baris tanpa nilai di akhir |
| Cost Center | ascending, descending | Dimas Pranata (`CC-100`), Endah Susanti (`CC-200`), lalu sepuluh baris tanpa nilai di akhir |
| Joined Date | ascending (Oldest First), descending (Newest First) | Dimas Pranata, Endah Susanti, lalu sepuluh baris tanpa nilai di akhir |
| Badge No | ascending, descending | Dimas Pranata (`BN-77`), Endah Susanti (`BN-88`), lalu sepuluh baris tanpa nilai di akhir |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon Search; membaca teks sel tabel; hapus preferensi kolom di browser (hook `after`).
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-688: Sort default Table User Picker

1. Klik Tab `Total Control`
2. Klik `[+ Assign]` pada Tab `Total Control` (popup Assign Total Control dengan Table User Picker)
3. Verifikasi daftar terurut Name A-Z (halaman pertama: Citra Lestari, Dewi Anggraini, Dimas Pranata, Endah Susanti, Gilang Prakoso, Gunawan Halim, Hana Permata, Hesti Rahma, Indra Kusuma, Joko Santoso)

### TC-FA-RP-689: Sort Table User Picker siklus tiga state kelas teks

4. Untuk setiap baris tabel `Urutan ascending TC-FA-RP-689` di Prerequisites, lakukan langkah 5 sampai 10
5. Klik header kolom pada baris iterasi sekali
6. Verifikasi baris terurut ascending sesuai kolom Urutan ascending pada baris iterasi
7. Klik header kolom pada baris iterasi kedua kali
8. Verifikasi baris terurut descending (kebalikan urutan ascending)
9. Klik header kolom pada baris iterasi ketiga kali
10. Verifikasi urutan kembali ke default sort tabel (Name A-Z)

### TC-FA-RP-1080: Sort Table User Picker siklus tiga state kolom Position, Division, Status

11. Untuk setiap baris tabel `Urutan ascending TC-FA-RP-1080` di Prerequisites, lakukan langkah 12 sampai 17
12. Klik header kolom pada baris iterasi sekali
13. Verifikasi baris terurut ascending sesuai kolom Urutan ascending pada baris iterasi
14. Klik header kolom pada baris iterasi kedua kali
15. Verifikasi baris terurut descending (kebalikan urutan ascending)
16. Klik header kolom pada baris iterasi ketiga kali
17. Verifikasi urutan kembali ke default sort tabel (Name A-Z)

### TC-FA-RP-1081: Sort Table User Picker siklus tiga state kolom curated

18. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
19. Centang kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, dan `Badge No` lewat Setup Column popup lalu klik `[Save]`
20. Untuk setiap baris tabel `Urutan ascending TC-FA-RP-1081` di Prerequisites, lakukan langkah 21 sampai 26
21. Klik header kolom pada baris iterasi sekali
22. Verifikasi baris terurut ascending sesuai kolom Urutan ascending pada baris iterasi (label klik 1 sesuai kolom Label)
23. Klik header kolom pada baris iterasi kedua kali
24. Verifikasi baris terurut descending (label klik 2 sesuai kolom Label)
25. Klik header kolom pada baris iterasi ketiga kali
26. Verifikasi urutan kembali ke default sort tabel (Name A-Z)
27. Sembunyikan kembali kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, dan `Badge No` lewat Setup Column popup lalu klik `[Save]` (pemulihan kolom bawaan)
28. Tutup popup Assign Total Control dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-688, 689, 1080, 1081). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 27, 28.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 5 sampai 10 (2 iterasi); langkah 12 sampai 17 (3 iterasi); langkah 21 sampai 26 (7 iterasi).
- Spec ini di atas 35 langkah (28 langkah nominal, sekitar 82 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-1080 dan 1081 menyebut urutan descending hanya sebagai "klik 2 descending"; spec mengasersinya sebagai kebalikan urutan ascending dan tidak mengasersi urutan antar baris bernilai sama atau tanpa nilai.
  - TC-FA-RP-1080 dan 1081 tidak merujuk Pre-setup #36 dan #37 pada Precondition (hanya #41 dan #22); spec memakai #41 dan #22 untuk data yang diasersi.
  - TC picker memulai dari Tab `Total Control` lalu `[+ Assign]` pada tiap TC; spec membuka popup sekali dan membersihkan state (Search, Filter, Sort, kolom) antar TC.
