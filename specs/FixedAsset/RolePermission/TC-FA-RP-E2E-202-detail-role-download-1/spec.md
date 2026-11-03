---
id: TC-FA-RP-E2E-202-detail-role-download-1
title: "Detail Role: Download (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-661
  - TC-FA-RP-662
  - TC-FA-RP-663
  - TC-FA-RP-664
coverage:
  web: automated
---

# Detail Role: Download (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV dan XLSX (nama berkas, kolom header, jumlah dan isi baris); hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-661: Download Detail Role: tanpa Search atau Filter mengekspor seluruh data

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik ikon Download
5. Pilih `Download as CSV`
6. Verifikasi tidak ada toast sukses
7. Buka file
8. Verifikasi berkas `Role-Permission-Manage-Files.csv` terunduh
9. Verifikasi berkas memuat kolom Name, Group, Position, Division, Create, Read, Update, Delete
10. Verifikasi berkas memuat seluruh 6 baris Detail Role `Manage files` pada `All Groups` (Pre-setup #39)

### TC-FA-RP-662: Download Detail Role: Search dan Filter aktif hanya mengekspor baris yang cocok

11. Ketik Search `Officer`, tekan Enter
12. Klik ikon Filter
13. Pilih opsi `Finance Officer` dan `HR Officer` pada field `Position`, klik `[Apply]`
14. Tutup Filter Panel dengan klik ikon Filter
15. Klik ikon Download lalu `Download as XLSX`
16. Buka file
17. Verifikasi berkas `Role-Permission-Manage-Files.xlsx` terunduh
18. Verifikasi berkas hanya memuat baris Fitri Handayani dan Citra Lestari
19. Lepas Filter: klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`, kemudian tutup panel dengan klik ikon Filter
20. Klik `(←)` pada kotak Search

### TC-FA-RP-663: Download Detail Role: kolom yang disembunyikan tidak ikut diekspor

21. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
22. Hapus centang kolom `Division` lalu klik `[Save]`
23. Klik ikon Download lalu `Download as CSV`
24. Buka file
25. Verifikasi berkas tidak memuat kolom `Division` (sama dengan kolom yang sedang tampil)

### TC-FA-RP-664: Download Detail Role: kolom yang ditampilkan kembali ikut diekspor

26. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
27. Centang kembali kolom `Division` lalu klik `[Save]`
28. Klik ikon Download lalu `Download as CSV`
29. Buka file
30. Verifikasi berkas memuat kembali kolom `Division` yang tadi disembunyikan

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-661, 662, 663, 664). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 14, 19, 20.
- Langkah menyembunyikan kolom `Division` pada TC-FA-RP-664 (dependensi TC-FA-RP-663) dipenuhi oleh langkah TC-FA-RP-663 di spec ini; spec hanya menampilkan kembali kolom itu.
- Temuan untuk QA:
  - TC-FA-RP-661 expected c ("tidak ada toast sukses") diasersi segera setelah memilih format unduhan; kemunculan berkas menjadi anchor positif pada Verifikasi berikutnya.
