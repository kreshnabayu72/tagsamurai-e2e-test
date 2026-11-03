---
id: TC-FA-RP-E2E-210-table-user-picker-search-filter-dan-sort-5
title: "Table User Picker: Search, Filter, dan Sort (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1082
  - TC-FA-RP-1083
  - TC-FA-RP-1092
  - TC-FA-RP-1108
coverage:
  web: automated
---

# Table User Picker: Search, Filter, dan Sort (5/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #41 (kandidat popup Assign Total Control, belum Total Control, 12 pengguna: Citra Lestari (HR Officer, HR), Dimas Pranata (IT Support, IT Operations; `TAG-2002`; `CC-100`; 10/01/26; `BN-77`), Endah Susanti (Procurement Officer, Procurement; `CC-200`; 15/02/26; `BN-88`), Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama (Inactive), Gilang Prakoso (Pending Activation), Hana Permata (Temporary User Yes dengan Temporary Until terisi); email `[namalengkaptanpaspasi]@qwertysystem.net`), #36, #37, dan #17 (pengguna yang sudah Total Control, Read Only, dan variasi Home Group). Popup hanya dibaca; tidak ada Assign yang dikirim dan Pre-setup tidak diubah.
- Pre-setup #22 (Custom Field aktif `Cost Center`, `Joined Date`, `Badge No`) dipakai TC kolom Custom Field.
- Kolom uji Search TC-FA-RP-1082:

| Kolom | Keyword | Hasil |
|---|---|---|
| TAG | `tag-2002` | hanya Dimas Pranata |
| Cost Center | `cc-200` | hanya Endah Susanti |
| Badge No | `bn-88` | hanya Endah Susanti |

- Pilihan Filter TC-FA-RP-1083:

| Field | Pilihan | Hasil |
|---|---|---|
| Cost Center | opsi `CC-200` | hanya Endah Susanti |
| Joined Date | rentang tanggal yang mencakup Joined Date Endah Susanti (15/02/26) saja | hanya Endah Susanti |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon Search; membaca teks sel tabel; hapus preferensi kolom di browser (hook `after`). Memilih rentang tanggal pada date range picker.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-1082: Search Table User Picker kolom curated TAG dan Custom Field

1. Klik Tab `Total Control`
2. Klik `[+ Assign]` pada Tab `Total Control` (popup Assign Total Control dengan Table User Picker)
3. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
4. Centang kolom `TAG`, `Cost Center`, dan `Badge No` lewat Setup Column popup lalu klik `[Save]`
5. Untuk setiap baris tabel `Kolom uji Search TC-FA-RP-1082` di Prerequisites, lakukan langkah 6 sampai 8
6. Ketik Search keyword pada baris iterasi, tekan Enter
7. Verifikasi hasil Search sesuai kolom Hasil pada baris iterasi (hanya baris yang disebut tampil)
8. Kosongkan isi kotak search, tekan Enter
9. Sembunyikan kembali kolom `TAG`, `Cost Center`, dan `Badge No` lewat Setup Column popup lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-1083: Filter Table User Picker per kelas Custom Field Dropdown (Cost Center) dan Date (Joined Date)

10. Klik ikon Filter
11. Untuk setiap baris tabel `Pilihan Filter TC-FA-RP-1083` di Prerequisites, lakukan langkah 12 sampai 14
12. Pilih pilihan baris iterasi pada field baris iterasi, lalu klik `[Apply]`
13. Verifikasi hasil Filter sesuai kolom Hasil pada baris iterasi
14. Klik `[Clear Field]` lalu `[Apply]`
15. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-1092: Search Status Table User Picker memakai pencocokan exact: `active` tidak mencocokkan Inactive

16. Ketik Search `active`, tekan Enter
17. Verifikasi halaman pertama hanya memuat baris berstatus `Active` dan Yoga Pratama (`Inactive`) tidak tampil
18. Pindah ke halaman 2
19. Verifikasi halaman 2 memuat satu baris berstatus `Active` (kandidat kesebelas) dan Yoga Pratama (`Inactive`) tidak tampil
20. Kosongkan isi kotak search, tekan Enter
21. Ketik Search `inactive`, tekan Enter
22. Verifikasi hanya Yoga Pratama yang tampil
23. Klik `(←)` pada kotak Search

### TC-FA-RP-1108: Search Table User Picker tidak mencocokkan kolom Custom Field bertipe Date `Joined Date`

24. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
25. Centang kolom `Joined Date` lewat Setup Column popup lalu klik `[Save]`
26. Salin teks tanggal sel Joined Date baris Dimas Pranata (sesuai Date Format General Settings)
27. Ketik Search teks tanggal Joined Date yang disalin, tekan Enter
28. Verifikasi tabel menampilkan empty state `No results found` karena kolom Custom Field bertipe Date tidak dapat dicari
29. Klik ikon Filter
30. Verifikasi Panel Filter memuat field `Joined Date` sebagai jalur penyaringan kolom tanggal
31. Tutup Filter Panel dengan klik ikon Filter
32. Klik `(←)` pada kotak Search
33. Sembunyikan kembali kolom `Joined Date` lewat Setup Column popup lalu klik `[Save]` (pemulihan kolom bawaan)
34. Tutup popup Assign Total Control dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-1082, 1083, 1092, 1108). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 9, 15, 23, 26, 31, 32, 33, 34.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 6 sampai 8 (3 iterasi); langkah 12 sampai 14 (2 iterasi).
- Spec ini di atas 35 langkah (34 langkah nominal, sekitar 43 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - Precondition TC picker menyebut Pre-setup #23 (`Company Volume`, 120 pengguna) padahal data uji yang diasersi adalah #41 (12 kandidat); spec memakai #41 pada Company Alpha dengan Total Control #2 dan tidak memakai #23.
  - TC-FA-RP-1092 expected a menyebut "seluruh baris berstatus `Active`", tetapi sebelas kandidat Active melebihi ukuran halaman 10; spec mengasersi halaman pertama dan halaman 2.
  - TC-FA-RP-1108 expected b ("penyaringan kolom tanggal hanya melalui Filter Panel") tidak punya langkah observasi; spec mengasersinya lewat ketersediaan field `Joined Date` pada Panel Filter (Notes S-03).
  - TC-FA-RP-1082, 1083, 1092, dan 1108 tidak merujuk Pre-setup #23; precondition TC-FA-RP-1108 merujuk #36 dan #37 tanpa dipakai asersi.
  - TC picker memulai dari Tab `Total Control` lalu `[+ Assign]` pada tiap TC; spec membuka popup sekali dan membersihkan state (Search, Filter, Sort, kolom) antar TC.
