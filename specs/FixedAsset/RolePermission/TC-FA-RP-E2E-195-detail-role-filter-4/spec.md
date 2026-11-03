---
id: TC-FA-RP-E2E-195-detail-role-filter-4
title: "Detail Role: Filter (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-637
  - TC-FA-RP-638
  - TC-FA-RP-639
  - TC-FA-RP-640
  - TC-FA-RP-1078
coverage:
  web: automated
---

# Detail Role: Filter (4/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center` `CC-100`/`CC-200`, `Joined Date`, `Badge No`; Ahmad Fauzi `CC-100`, 10/01/26, `BN-77`; Budi Santoso `CC-200`, 15/02/26, `BN-88`).
- Pilihan Filter TC-FA-RP-1078:

| Field | Pilihan | Hasil |
|---|---|---|
| Cost Center | opsi `CC-200` | hanya baris Budi Santoso |
| Joined Date | rentang tanggal yang mencakup Joined Date Budi Santoso (15/02/26) saja | hanya baris Budi Santoso |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): memilih rentang tanggal pada date range picker; hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-637: Kombinasi Filter lalu Search Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik ikon Filter
5. Pilih opsi `Logistics` pada field `Division`, klik `[Apply]`
6. Ketik Search `Ware`, tekan Enter
7. Verifikasi tabel menampilkan irisan Filter Division `Logistics` dan Search `Ware`: hanya baris Budi Santoso
8. Verifikasi kriteria Filter Division `Logistics` tetap aktif (badge titik pada ikon Filter)
9. Lepas Filter: klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`, kemudian tutup panel dengan klik ikon Filter
10. Klik `(←)` pada kotak Search

### TC-FA-RP-638: Menutup Filter Panel Detail Role tanpa `[Apply]` membuang draft

11. Klik ikon Filter
12. Pilih opsi `Warehouse Staff` pada field `Position` tanpa Apply
13. Klik ikon Filter lagi
14. Verifikasi tabel tidak berubah (enam baris tetap tampil)
15. Buka panel Filter kembali
16. Verifikasi panel menampilkan nilai ter-Apply terakhir: field `Position` kembali `All positions` (draft dibuang)
17. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-639: Indikator filter aktif dan nilai kosong pada Filter Detail Role

18. Klik ikon Filter
19. Buka dropdown field `Cost Center`
20. Verifikasi dropdown field Cost Center memuat `CC-100` dan `CC-200` tanpa opsi untuk nilai kosong
21. Pilih opsi `CC-100` pada field `Cost Center`, klik `[Apply]`
22. Verifikasi badge titik (tanpa angka) muncul pada ikon Filter saat panel terbuka
23. Verifikasi hanya baris Ahmad Fauzi yang tampil
24. Verifikasi baris bernilai kosong pada Cost Center tersaring keluar
25. Klik ikon Filter untuk menutup panel
26. Verifikasi badge titik (tanpa angka) tetap muncul pada ikon Filter saat panel tertutup
27. Klik ikon Filter lalu klik `[Clear Field]` dan `[Apply]`
28. Verifikasi badge titik hilang setelah filter di-clear
29. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-640: Filter Detail Role independen dari visibilitas kolom

30. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
31. Hapus centang kolom `Position` lalu klik `[Save]`
32. Klik ikon Filter
33. Verifikasi field filter `Position` tetap tersedia walau kolom disembunyikan
34. Tutup Filter Panel dengan klik ikon Filter
35. Tampilkan kembali kolom `Position` lewat Setup Column lalu klik `[Save]`
36. Klik ikon Filter
37. Pilih opsi `Warehouse Staff` pada field `Position`, klik `[Apply]`
38. Sembunyikan kembali kolom `Position` lewat Setup Column lalu klik `[Save]`
39. Verifikasi filter yang sudah ter-Apply tetap aktif setelah kolom disembunyikan (tabel hanya menampilkan Budi Santoso)
40. Lepas Filter: klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`, kemudian tutup panel dengan klik ikon Filter
41. Tampilkan kembali kolom `Position` lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-1078: Filter Detail Role per kelas Custom Field Cost Center dan Joined Date

42. Klik ikon Filter
43. Untuk setiap baris tabel `Pilihan Filter TC-FA-RP-1078` di Prerequisites, lakukan langkah 44 sampai 46
44. Pilih pilihan baris iterasi pada field baris iterasi, lalu klik `[Apply]`
45. Verifikasi hasil Filter sesuai kolom Hasil pada baris iterasi
46. Klik `[Clear Field]` lalu `[Apply]`
47. Tutup Filter Panel dengan klik ikon Filter

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-637, 638, 639, 640, 1078). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 9, 10, 17, 29, 34, 35, 40, 41, 47.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 44 sampai 46 (2 iterasi).
- Spec ini di atas 35 langkah (47 langkah nominal, sekitar 50 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-640 tidak menyebut nilai filter Position; spec memakai `Warehouse Staff`.
  - TC-FA-RP-639 menulis expected b tanpa urutan yang jelas terhadap Apply; spec mengasersi isi dropdown sebelum Apply dan hasil sesudah Apply.
  - TC-FA-RP-639 dan 1078 memakai Custom Field aktif tetapi Precondition TC-FA-RP-639 tidak merujuk Pre-setup #22; spec memakai #22.
  - Pre-setup #22 tidak merinci rentang tanggal; rentang Joined Date pada TC-FA-RP-1078 ditulis sebagai rentang yang mencakup 15/02/26 saja dan tidak mencakup 10/01/26.
