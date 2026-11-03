---
id: TC-FA-RP-E2E-192-detail-role-filter-1
title: "Detail Role: Filter (1/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-625
  - TC-FA-RP-626
  - TC-FA-RP-627
  - TC-FA-RP-628
coverage:
  web: automated
---

# Detail Role: Filter (1/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center` `CC-100`/`CC-200`, `Joined Date`, `Badge No`; Ahmad Fauzi `CC-100`, 10/01/26, `BN-77`; Budi Santoso `CC-200`, 15/02/26, `BN-88`).
- Pilihan Filter TC-FA-RP-626:

| Field | Opsi | Hasil |
|---|---|---|
| Position | `Warehouse Staff` | hanya baris Budi Santoso |
| Division | `Logistics` | baris Ahmad Fauzi dan Budi Santoso tampil |
| Activation Status | `Pending Email Confirmation` | hanya baris Fitri Handayani |
| Temporary User | `Yes` | hanya baris Fitri Handayani |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): memilih rentang tanggal pada date range picker; hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-625: Screening Filter Panel Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik ikon Filter
5. Verifikasi Panel Filter memuat field `Position` (`All positions`), `Division` (`All divisions`), `Activation Status` (`All statuses`), `Temporary User` (`All options`), `Temporary Until` (date range picker, `Select date`), dan Custom Field aktif
6. Verifikasi Panel Filter tidak memuat field `Group` dan tidak memuat field `Status`
7. Verifikasi footer panel memuat `[Clear Field]` dan `[Apply]`
8. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-626: Filter Detail Role per kelas multi-select searchable

9. Klik ikon Filter
10. Untuk setiap baris tabel `Pilihan Filter TC-FA-RP-626` di Prerequisites, lakukan langkah 11 sampai 13
11. Pilih opsi pada baris iterasi di field baris iterasi, lalu klik `[Apply]`
12. Verifikasi hasil Filter sesuai kolom Hasil pada baris iterasi
13. Klik `[Clear Field]` lalu `[Apply]`
14. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-627: Filter Detail Role per kelas date range

15. Klik ikon Filter
16. Pilih rentang tanggal field `Temporary Until` yang mencakup tanggal Temporary Until Fitri Handayani, lalu klik `[Apply]`
17. Verifikasi field Temporary Until: hanya baris Fitri Handayani yang tampil
18. Klik `[Clear Field]` lalu `[Apply]`
19. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-628: Isi opsi dropdown Filter Detail Role diambil dari data tabel saat ini

20. Klik ikon Filter
21. Buka dropdown field `Position`
22. Verifikasi opsi Position: `Asset Custodian`, `Finance Officer`, `HR Officer`, `IT Support`, `Procurement Officer`, `Warehouse Staff`
23. Tutup dropdown dengan Esc
24. Buka dropdown field `Division`
25. Verifikasi opsi Division: `Finance`, `HR`, `IT Operations`, `Logistics`, `Procurement`
26. Tutup dropdown dengan Esc
27. Buka dropdown field `Activation Status`
28. Verifikasi opsi Activation Status: `Activated`, `Pending Email Confirmation`
29. Tutup dropdown dengan Esc
30. Buka dropdown field `Temporary User`
31. Verifikasi opsi Temporary User: `Yes`, `No`
32. Tutup dropdown dengan Esc
33. Tutup Filter Panel dengan klik ikon Filter

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-625, 626, 627, 628). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 8, 14, 19, 23, 26, 29, 32, 33.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 11 sampai 13 (4 iterasi).
- Spec ini di atas 35 langkah (33 langkah nominal, sekitar 42 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - Nilai Temporary Until Fitri Handayani tidak tertulis di Pre-setup #39 (hanya "terisi"); spec menunjuk nilai hasil seeding Pre-setup tanpa menuliskan tanggalnya.
  - TC-FA-RP-625 dan TC-FA-RP-639 menyebut Custom Field aktif pada Filter Panel tetapi tidak merujuk Pre-setup #22 pada Precondition; spec memakai #22.
  - TC-FA-RP-626 menyebut Filter Panel tetap terbuka setelah `[Apply]` (langkah `[Clear Field]` dan `[Apply]` berlanjut tanpa membuka ulang panel); spec mengikuti urutan itu dan menutup panel dengan klik ikon Filter.
