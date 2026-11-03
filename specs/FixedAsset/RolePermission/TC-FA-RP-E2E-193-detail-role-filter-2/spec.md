---
id: TC-FA-RP-E2E-193-detail-role-filter-2
title: "Detail Role: Filter (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-629
  - TC-FA-RP-630
  - TC-FA-RP-631
  - TC-FA-RP-632
coverage:
  web: automated
---

# Detail Role: Filter (2/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-629: Search internal dropdown Filter Detail Role mempersempit opsi

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik ikon Filter
5. Buka dropdown field `Position`
6. Ketik sebagian teks `war` pada kotak pencarian dropdown
7. Verifikasi daftar opsi Position menyempit ke opsi yang memuat `war` (`Warehouse Staff`) tanpa membedakan huruf besar kecil
8. Ganti isi kotak pencarian dropdown dengan teks yang tidak ada (`zzz`)
9. Verifikasi teks `zzz` menampilkan keadaan tanpa opsi cocok
10. Tutup dropdown dengan Esc

### TC-FA-RP-630: Filter Detail Role: logika OR di dalam satu field multi-select

11. Buka dropdown field `Position` lalu pilih dua opsi: `Warehouse Staff` dan `Finance Officer`
12. Klik `[Apply]`
13. Verifikasi baris Budi Santoso dan Fitri Handayani tampil (gabungan OR, bukan irisan)
14. Verifikasi baris lain tidak tampil
15. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-RP-631: Filter Detail Role: logika AND antar field berbeda

16. Pilih `Warehouse Staff` pada field `Position`
17. Pilih `Logistics` pada field `Division`
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan irisan baris yang memenuhi kedua kriteria (Position `Warehouse Staff` dan Division `Logistics`: baris Budi Santoso)
20. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-RP-632: Chip opsi terpilih pada Filter Detail Role: hapus lewat `(X)` pada chip

21. Pilih opsi `Warehouse Staff` dan `Finance Officer` pada field `Position`
22. Klik `(X)` pada chip `Finance Officer` tanpa membuka dropdown
23. Verifikasi chip `Finance Officer` hilang dari field
24. Verifikasi chip `Warehouse Staff` tetap ada
25. Buka dropdown field `Position`
26. Verifikasi checkbox opsi `Finance Officer` di dalam dropdown tidak tercentang
27. Tutup dropdown dengan Esc
28. Klik `[Clear Field]` lalu `[Apply]`
29. Tutup Filter Panel dengan klik ikon Filter

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-629, 630, 631, 632). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 10, 15, 20, 27, 28, 29.
- Temuan untuk QA:
  - TC-FA-RP-631 expected "irisan baris yang memenuhi kedua kriteria" tanpa menyebut barisnya; spec menurunkannya dari Pre-setup #39 (Budi Santoso: Warehouse Staff dan Logistics).
  - TC-FA-RP-629 tidak menyatakan apakah teks `zzz` dimasukkan menggantikan `war`; spec mengganti isi kotak pencarian dropdown.
