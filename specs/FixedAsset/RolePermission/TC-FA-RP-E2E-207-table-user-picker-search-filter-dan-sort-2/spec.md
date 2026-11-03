---
id: TC-FA-RP-E2E-207-table-user-picker-search-filter-dan-sort-2
title: "Table User Picker: Search, Filter, dan Sort (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-680
  - TC-FA-RP-681
  - TC-FA-RP-682
  - TC-FA-RP-683
coverage:
  web: automated
---

# Table User Picker: Search, Filter, dan Sort (2/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #41 (kandidat popup Assign Total Control, belum Total Control, 12 pengguna: Citra Lestari (HR Officer, HR), Dimas Pranata (IT Support, IT Operations; `TAG-2002`; `CC-100`; 10/01/26; `BN-77`), Endah Susanti (Procurement Officer, Procurement; `CC-200`; 15/02/26; `BN-88`), Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama (Inactive), Gilang Prakoso (Pending Activation), Hana Permata (Temporary User Yes dengan Temporary Until terisi); email `[namalengkaptanpaspasi]@qwertysystem.net`), #36, #37, dan #17 (pengguna yang sudah Total Control, Read Only, dan variasi Home Group). Popup hanya dibaca; tidak ada Assign yang dikirim dan Pre-setup tidak diubah.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon Search; membaca teks sel tabel; hapus preferensi kolom di browser (hook `after`).
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-680: Search Table User Picker per kelas badge dan enum

1. Klik Tab `Total Control`
2. Klik `[+ Assign]` pada Tab `Total Control` (popup Assign Total Control dengan Table User Picker)
3. Ketik Search `inactive`, tekan Enter
4. Verifikasi kolom Status: hanya Yoga Pratama yang tampil
5. Kosongkan isi kotak search, tekan Enter
6. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
7. Centang kolom `Activation Status` lewat Setup Column popup lalu klik `[Save]`
8. Ketik Search `pending activation`, tekan Enter
9. Verifikasi kolom Activation Status: hanya Gilang Prakoso yang tampil
10. Kosongkan isi kotak search, tekan Enter
11. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
12. Centang kolom `Temporary User` lewat Setup Column popup lalu klik `[Save]`
13. Ketik Search `yes`, tekan Enter
14. Verifikasi kolom Temporary User: hanya Hana Permata yang tampil
15. Kosongkan isi kotak search, tekan Enter
16. Sembunyikan kembali kolom `Activation Status` dan `Temporary User` lewat Setup Column popup lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-681: Search Table User Picker tidak mencocokkan kolom tanggal (guard non-searchable)

17. Tampilkan kolom `Temporary Until` lewat Setup Column popup lalu klik `[Save]`, lalu salin teks tanggal sel Temporary Until baris Hana Permata
18. Ketik Search teks tanggal Temporary Until yang disalin, tekan Enter
19. Verifikasi tabel menampilkan empty state `No results found` karena kolom tanggal tidak dapat dicari
20. Klik ikon Filter
21. Verifikasi Panel Filter memuat field `Temporary Until` (date range picker) sebagai jalur penyaringan kolom tanggal
22. Tutup Filter Panel dengan klik ikon Filter
23. Klik `(←)` pada kotak Search
24. Sembunyikan kembali kolom `Temporary Until` lewat Setup Column popup lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-682: Search Table User Picker terikat visibilitas kolom: kolom Position disembunyikan tidak dapat dicari

25. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
26. Hapus centang kolom `Position` lalu klik `[Save]`
27. Ketik Search `procure`, tekan Enter
28. Verifikasi keyword `procure` mencocokkan baris hanya lewat kolom yang tampil (Endah Susanti melalui kolom Division `Procurement`), bukan lewat kolom Position yang disembunyikan
29. Verifikasi kolom Division yang tampil tetap dapat dicari (baris Endah Susanti tampil melalui `Procurement`)

### TC-FA-RP-683: Search Table User Picker terikat visibilitas kolom: kolom Position ditampilkan kembali dapat dicari

30. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
31. Centang kembali kolom `Position` lalu klik `[Save]`
32. Ganti isi kotak search dengan `procure`, tekan Enter
33. Verifikasi pencarian kembali mencocokkan Endah Susanti
34. Klik `(←)` pada kotak Search
35. Tutup popup Assign Total Control dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-680, 681, 682, 683). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 16, 17, 20, 22, 23, 24, 32, 34, 35.
- Langkah menyembunyikan kolom `Position` pada TC-FA-RP-683 (dependensi TC-FA-RP-682) dipenuhi oleh langkah TC-FA-RP-682 di spec ini; spec hanya menampilkan kembali kolom itu.
- Temuan untuk QA:
  - TC-FA-RP-681 menyalin teks tanggal sel Temporary Until tanpa menampilkan kolom itu lebih dulu (kolom curated tersembunyi secara default); spec menampilkan kolom lewat Setup Column popup agar sel dapat disalin dan kolom tetap tampil selama Search.
  - Nilai Temporary Until Hana Permata tidak tertulis di Pre-setup #41 (hanya "terisi"); spec menunjuk nilai hasil seeding Pre-setup tanpa menuliskan tanggalnya.
  - TC-FA-RP-682: keyword `procure` juga cocok dengan kolom Division `Procurement` milik Endah Susanti yang tetap tampil, sehingga hasilnya sama dengan TC-FA-RP-683 dan tidak membuktikan bahwa kolom Position yang disembunyikan tidak dicari; spec mengasersi hasil yang teramati sesuai expected bersyarat TC.
