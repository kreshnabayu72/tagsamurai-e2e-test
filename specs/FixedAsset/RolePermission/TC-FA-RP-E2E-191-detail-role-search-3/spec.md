---
id: TC-FA-RP-E2E-191-detail-role-search-3
title: "Detail Role: Search (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-623
  - TC-FA-RP-624
  - TC-FA-RP-1077
  - TC-FA-RP-1107
coverage:
  web: automated
---

# Detail Role: Search (3/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center` `CC-100`/`CC-200`, `Joined Date`, `Badge No`; Ahmad Fauzi `CC-100`, 10/01/26, `BN-77`; Budi Santoso `CC-200`, 15/02/26, `BN-88`).
- Kolom uji Search TC-FA-RP-1077:

| Kolom | Keyword | Hasil |
|---|---|---|
| TAG | `tag-1001` | hanya baris Ahmad Fauzi |
| Cost Center | `cc-200` | hanya baris Budi Santoso |
| Badge No | `bn-88` | hanya baris Budi Santoso |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): membaca teks sel tabel (untuk menyalin nilai kolom tanggal); hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-623: Search Detail Role membuang spasi awal dan akhir query saat Enter

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Ketik Search `  endah  ` (spasi di awal dan akhir), tekan Enter
5. Verifikasi tabel tersaring seperti query `endah`: hanya baris Endah Susanti
6. Verifikasi isi input tidak berubah (spasi awal dan akhir tetap terlihat di input)
7. Klik `(←)` pada kotak Search

### TC-FA-RP-624: Search Detail Role tidak mencocokkan kolom CRUD, Checkbox, dan Actions

8. Ketik Search `Create`, tekan Enter
9. Verifikasi pencarian `Create` menampilkan empty state `No results found` karena kolom matriks CRUD dan aksi tidak dapat dicari
10. Ganti isi kotak search dengan `Remove`, tekan Enter
11. Verifikasi pencarian `Remove` menampilkan empty state `No results found` karena kolom matriks CRUD dan aksi tidak dapat dicari
12. Klik `(←)` pada kotak Search

### TC-FA-RP-1077: Search Detail Role kolom curated TAG dan Custom Field Dropdown (Cost Center) dan Text (Badge No)

13. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
14. Centang kolom `TAG`, `Cost Center`, dan `Badge No` lalu klik `[Save]`
15. Untuk setiap baris tabel `Kolom uji Search TC-FA-RP-1077` di Prerequisites, lakukan langkah 16 sampai 18
16. Ketik Search keyword pada baris iterasi, tekan Enter
17. Verifikasi hasil Search sesuai kolom Hasil pada baris iterasi (hanya baris yang disebut tampil)
18. Kosongkan isi kotak search, tekan Enter
19. Sembunyikan kembali kolom `TAG`, `Cost Center`, dan `Badge No` lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-1107: Search Detail Role tidak mencocokkan kolom Custom Field bertipe Date `Joined Date`

20. Tampilkan kolom `Joined Date` lewat Setup Column lalu klik `[Save]`, lalu salin teks tanggal sel Joined Date baris Ahmad Fauzi (sesuai Date Format General Settings)
21. Ketik Search teks tanggal Joined Date yang disalin, tekan Enter
22. Verifikasi tabel menampilkan empty state `No results found` karena kolom Custom Field bertipe Date tidak dapat dicari
23. Klik ikon Filter
24. Verifikasi Filter Panel memuat field `Joined Date` sebagai jalur penyaringan kolom tanggal
25. Tutup Filter Panel dengan klik ikon Filter
26. Klik `(←)` pada kotak Search
27. Sembunyikan kembali kolom `Joined Date` lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-623, 624, 1077, 1107). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 7, 12, 19, 20, 23, 25, 26, 27.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 16 sampai 18 (3 iterasi).
- Temuan untuk QA:
  - TC-FA-RP-1107 menyalin teks tanggal sel Joined Date tanpa menampilkan kolom itu sebelum langkah salin; spec menampilkan kolom lebih dulu (langkah 3 TC memang menampilkannya) dan menyalin teks sel sebelum Search.
  - TC-FA-RP-624 menyebut kolom CRUD; Detail Role `Manage files` memuat kolom `Read` dan `Delete` aktif (Create dan Update tidak berlaku, TC-FA-RP-669); spec memakai kata kunci `Create` dan `Remove` sesuai TC.
