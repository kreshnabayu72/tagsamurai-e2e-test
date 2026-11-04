---
id: TC-FA-RP-E2E-190-detail-role-search-2
title: "Detail Role: Search (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-619
  - TC-FA-RP-620
  - TC-FA-RP-621
  - TC-FA-RP-622
coverage:
  web: automated
---

# Detail Role: Search (2/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, 41 baris: 6 baris non-pola dan 35 baris pola Group Role. Baris non-pola: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata. Baris pola `Manage files` ada pada tujuh group Pre-setup #18 untuk lima user pola: Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, Maya Anggraeni) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): membaca teks sel tabel (untuk menyalin nilai kolom tanggal); hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-619: Search Detail Role per kelas badge dan enum

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
5. Centang kolom `Activation Status` lalu klik `[Save]`
6. Ketik Search `pending email`, tekan Enter
7. Verifikasi kolom Activation Status: hanya baris Fitri Handayani yang tampil
8. Kosongkan isi kotak search, tekan Enter
9. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
10. Centang kolom `Temporary User` lalu klik `[Save]`
11. Ketik Search `yes`, tekan Enter
12. Verifikasi kolom Temporary User: hanya baris Fitri Handayani yang tampil
13. Kosongkan isi kotak search, tekan Enter
14. Sembunyikan kembali kolom `Activation Status` dan `Temporary User` lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-620: Search Detail Role tidak mencocokkan kolom tanggal (guard non-searchable)

15. Tampilkan kolom `Temporary Until` lewat Setup Column lalu klik `[Save]`, lalu salin teks tanggal sel Temporary Until baris Fitri Handayani
16. Ketik Search teks tanggal Temporary Until yang disalin, tekan Enter
17. Verifikasi tabel menampilkan empty state `No results found` karena kolom tanggal tidak dapat dicari
18. Klik ikon Filter
19. Verifikasi Filter Panel memuat field `Temporary Until` (date range picker) sebagai jalur penyaringan kolom tanggal
20. Tutup Filter Panel dengan klik ikon Filter
21. Klik `(←)` pada kotak Search
22. Sembunyikan kembali kolom `Temporary Until` lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-621: Search Detail Role terikat visibilitas kolom: kolom Group disembunyikan tidak dapat dicari

23. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
24. Hapus centang kolom `Group` lalu klik `[Save]`
25. Ketik Search `dock`, tekan Enter
26. Verifikasi tabel menampilkan empty state `No results found` (tidak ada kolom lain yang cocok dengan `dock`, sehingga keyword tidak mencocokkan baris lewat kolom Group yang disembunyikan)
27. Ganti isi kotak search dengan `endah`, tekan Enter
28. Verifikasi kolom Name tetap dapat dicari: hanya baris Endah Susanti yang tampil

### TC-FA-RP-622: Search Detail Role terikat visibilitas kolom: kolom Group ditampilkan kembali dapat dicari

29. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
30. Centang kembali kolom `Group` lalu klik `[Save]`
31. Ganti isi kotak search dengan `dock`, tekan Enter
32. Verifikasi pencarian kembali mencocokkan baris Fitri Handayani di `Dock 1` dan lima baris pola Group Role `Manage files` (Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, Maya Anggraeni; Pre-setup #39) di `Dock 1`
33. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-619, 620, 621, 622). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 14, 15, 20, 21, 22, 27, 31, 33.
- Langkah sembunyikan kolom `Group` pada TC-FA-RP-622 (dependensi TC-FA-RP-621) dipenuhi oleh langkah TC-FA-RP-621 di spec ini; spec hanya menampilkan kembali kolom itu.
- Temuan untuk QA:
  - TC-FA-RP-620 menyalin teks tanggal sel Temporary Until tanpa menampilkan kolom itu lebih dulu (kolom curated tersembunyi secara default); spec menampilkan kolom lewat Setup Column agar sel dapat disalin dan kolom tetap tampil selama Search.
  - Nilai Temporary Until Fitri Handayani tidak tertulis di Pre-setup #39 (hanya "terisi"); spec menunjuk nilai hasil seeding Pre-setup tanpa menuliskan tanggalnya.
  - TC-FA-RP-621 expected b ("kolom lain yang tampil tetap dapat dicari") tidak punya langkah; spec menambah Search `endah` pada kolom Name sebagai observasi (Notes S-03).
