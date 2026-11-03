---
id: TC-FA-RP-E2E-203-detail-role-download-2
title: "Detail Role: Download (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-666
  - TC-FA-RP-668
  - TC-FA-RP-670
  - TC-FA-RP-1005
coverage:
  web: automated
---

# Detail Role: Download (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV dan XLSX (nama berkas, kolom header, jumlah dan isi baris).
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-666: Download Detail Role: extension berkas mengikuti pilihan format

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik ikon Download lalu `Download as CSV`
5. Verifikasi berkas `Role-Permission-Manage-Files.csv` terunduh untuk pilihan CSV
6. Klik ikon Download lalu `Download as XLSX`
7. Verifikasi berkas `Role-Permission-Manage-Files.xlsx` terunduh untuk pilihan XLSX

### TC-FA-RP-668: Download Detail Role dengan nol baris: tombol tetap aktif dan berkas berisi header saja

8. Ketik Search `zzzz`, tekan Enter
9. Verifikasi tombol Download tetap aktif
10. Klik ikon Download lalu `Download as CSV`
11. Buka file
12. Verifikasi berkas hanya memuat baris header kolom
13. Klik `(←)` pada kotak Search

### TC-FA-RP-670: Filename Download Detail Role memakai nama role aktual dalam Title-Case dipisah hyphen

14. Klik segmen `System` pada Breadcrumb
15. Klik Role Name `Manage asset & TAG` pada section Group Role, klik ikon Download lalu `Download as CSV`
16. Verifikasi berkas `Role-Permission-Manage-Asset-And-TAG.csv` terunduh
17. Klik segmen `System` pada Breadcrumb
18. Klik Role Name `Manage Open API` pada section Global Role, klik ikon Download lalu `Download as CSV`
19. Verifikasi berkas `Role-Permission-Manage-Open-API.csv` terunduh

### TC-FA-RP-1005: Download Detail Role Global Role: berkas tanpa kolom Group

20. Klik segmen `System` pada Breadcrumb
21. Klik Role Name `Manage accounting` pada section Global Role
22. Klik ikon Download lalu `Download as CSV`
23. Buka file
24. Verifikasi berkas `Role-Permission-Manage-Accounting.csv` terunduh
25. Verifikasi header berkas: Name, Position, Division, Create, Read, Update, Delete
26. Verifikasi header berkas tidak memuat kolom Group
27. Verifikasi baris berkas: Ahmad Fauzi, Budi Santoso, Citra Lestari, dan Dimas Pranata

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-666, 668, 670, 1005). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 13, 14, 17, 20.
- Temuan untuk QA:
  - TC-FA-RP-670 tidak menyebut node Sidebar Group Tree untuk Detail Role Group Role `Manage asset & TAG`; spec mengunduh tanpa memilih node, sesuai langkah TC.
  - TC-FA-RP-668 tidak menyebut urutan antara asersi tombol Download dan unduhan; spec mengasersi tombol aktif sebelum klik unduh.
