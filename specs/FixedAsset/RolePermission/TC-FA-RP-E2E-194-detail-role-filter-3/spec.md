---
id: TC-FA-RP-E2E-194-detail-role-filter-3
title: "Detail Role: Filter (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-633
  - TC-FA-RP-634
  - TC-FA-RP-635
  - TC-FA-RP-636
coverage:
  web: automated
---

# Detail Role: Filter (3/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, 41 baris: 6 baris non-pola dan 35 baris pola Group Role. Baris non-pola: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata. Baris pola `Manage files` ada pada tujuh group Pre-setup #18 untuk lima user pola: Admin Utama (System Administrator, IT Operations), Siti Rahmawati (Finance Officer, Accounting & Tax), Rina Wulandari (`Operations Manager, Region 1`, `Asset Management "North"`), Dewi Anggraini (Internal Auditor, Internal Audit), Maya Anggraeni (Compliance Analyst, Legal)) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-633: Chip opsi terpilih pada Filter Detail Role: hapus lewat uncheck di dalam dropdown

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik ikon Filter
5. Pilih opsi `Warehouse Staff` dan `Finance Officer` pada field `Position`
6. Buka dropdown field itu dan hapus centang opsi `Finance Officer`
7. Verifikasi chip `Finance Officer` hilang dari field
8. Verifikasi chip `Warehouse Staff` tetap ada
9. Tutup dropdown dengan Esc
10. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-RP-634: Penghapusan chip Filter Detail Role mengubah hasil hanya setelah `[Apply]`

11. Pilih opsi `Warehouse Staff` dan `Finance Officer` pada field `Position` lalu klik `[Apply]`
12. Hapus chip `Finance Officer`
13. Verifikasi setelah chip dihapus dan sebelum Apply, tabel masih menampilkan Budi Santoso, Fitri Handayani, dan tujuh baris pola Siti Rahmawati (kriteria lama; Pre-setup #39)
14. Klik `[Apply]`
15. Verifikasi setelah Apply, tabel menampilkan hanya Budi Santoso (opsi `Warehouse Staff`)
16. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-RP-635: Overflow banyak chip pada field Filter Detail Role

17. Pilih keenam opsi field `Position`: `Asset Custodian`, `Finance Officer`, `HR Officer`, `IT Support`, `Procurement Officer`, `Warehouse Staff`
18. Tutup dropdown dengan Esc
19. Verifikasi closed-state field memuat chip `+N more` untuk chip yang tidak muat sesuai komponen MultiSelect
20. Verifikasi field tidak terpotong
21. Klik `[Clear Field]` lalu `[Apply]`
22. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-636: Kombinasi Search lalu Filter Detail Role

23. Ketik Search `Ware`, tekan Enter
24. Klik ikon Filter
25. Pilih opsi `Logistics` pada field `Division`, klik `[Apply]`
26. Verifikasi tabel menampilkan irisan Search `Ware` dan Filter Division `Logistics`: hanya baris Budi Santoso
27. Verifikasi Filter tidak mereset keyword Search (kotak Search tetap berisi `Ware`)
28. Klik `[Clear Field]` lalu `[Apply]`
29. Tutup Filter Panel dengan klik ikon Filter
30. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-633, 634, 635, 636). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 9, 10, 16, 18, 21, 22, 28, 29, 30.
- Temuan untuk QA:
  - TC-FA-RP-635 expected bersyarat ("Bila ruang field habis, chip yang tidak muat diringkas menjadi `+N more`"); spec mengasersi bahwa enam chip meringkas menjadi `+N more`, dan nilai N tidak diasersi karena TC tidak menyebutnya.
  - TC-FA-RP-635 menyebut "closed-state field" tanpa menyebut cara menutup dropdown; spec menutupnya dengan Esc.
