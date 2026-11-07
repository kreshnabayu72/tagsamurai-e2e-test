---
id: TC-FA-SU-E2E-208-modal-changelog-user-global-role-setup-column-bagian-1
title: "Modal Changelog User > Global Role: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-626
  - TC-FA-SU-627
  - TC-FA-SU-628
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, Role Name, Field, Old Value, New Value, Modified By.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-626: Screening Overlay Column Visibility

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Klik header kolom Actions (⋯)
3. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
4. Verifikasi daftar kolom berurutan Date, Action, Role Name, Field, Old Value, New Value, Modified By dengan checkbox Hideable terpilih dan enabled serta drag handle
5. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-627: Screening Popup Setup Column dan Preview Table

6. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
7. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
8. Verifikasi body: daftar kolom Date, Action, Role Name, Field, Old Value, New Value, Modified By dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
9. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
10. Klik ✕ untuk menutup popup Setup Column

### TC-FA-SU-628: Ceklis dan unceklis kelas Hideable

11. Buka Setup Column
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 13 sampai 14):
13. Hilangkan centang kolom tersebut pada daftar Setup Column
14. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
15. Hover checkbox kolom `Modified By`
16. Verifikasi checkbox kolom Modified By disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
17. Klik `[Save]`
18. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 19):
19. Verifikasi kolom tersebut tidak tampil di tabel
20. Klik F5
21. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 22):
22. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
23. Buka Setup Column, centang kembali seluruh kolom selain Modified By, lalu hilangkan centang kolom Modified By
24. Verifikasi perubahan kolom Modified By tampil di Live Preview
25. Klik `[Save]`
26. Verifikasi kolom Modified By tidak tampil di tabel
27. Klik F5
28. Verifikasi kolom Modified By tetap tidak tampil di tabel setelah refresh (F5)
29. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Langkah penghubung tambahan (S-03): langkah 15 (Hover checkbox `Modified By`) mendahului `Verifikasi` tooltip (TC-FA-SU-628 Expected g, bagian 8b butir 5).
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 13 sampai 14 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 19 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 22 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- Spec ini berjumlah 49 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji enam kolom pertama bersamaan lalu kolom terakhir terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
