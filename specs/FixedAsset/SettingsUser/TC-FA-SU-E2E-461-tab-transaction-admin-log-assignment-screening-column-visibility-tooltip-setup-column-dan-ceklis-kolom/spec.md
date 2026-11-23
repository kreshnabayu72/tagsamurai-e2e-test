---
id: TC-FA-SU-E2E-461-tab-transaction-admin-log-assignment-screening-column-visibility-tooltip-setup-column-dan-ceklis-kolom
title: "Tab Transaction Admin Log Sub-tab Assignment: Screening Column Visibility, Tooltip Icon, Setup Column, dan Ceklis Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1160
  - TC-FA-SU-1171
  - TC-FA-SU-1161
  - TC-FA-SU-1162
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Screening Column Visibility, Tooltip Icon, Setup Column, dan Ceklis Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Transaction ID, Name, Assignee, Group.

## Test Steps

### TC-FA-SU-1160: Screening Overlay Column Visibility

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Klik header kolom `⋯` (Actions)
3. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
4. Verifikasi daftar kolom berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Assignee`, `Group` dengan checkbox Hideable terpilih dan enabled serta drag handle
5. Verifikasi item `Setup Column...` di bagian bawah overlay
6. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-1171: Tooltip icon Table Tools dan header Actions

7. Hover icon Search
8. Verifikasi tooltip `Search` tampil
9. Hover icon Filter
10. Verifikasi tooltip `Filter` tampil
11. Hover icon Download
12. Verifikasi tooltip `Download` tampil
13. Hover header kolom Actions (`⋯`)
14. Verifikasi tooltip `Column Visibility` tampil

### TC-FA-SU-1161: Screening Popup Setup Column dan Preview Table

15. Klik header kolom `⋯`, lalu klik item `Setup Column...`
16. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close `✕` tampil
17. Verifikasi body: daftar kolom `Date`, `Activity`, `Transaction ID`, `Name`, `Assignee`, `Group` dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
18. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
19. Klik `✕` untuk menutup popup Setup Column

### TC-FA-SU-1162: Ceklis dan unceklis Setup Column kelas Hideable (default tampil)

20. Klik header kolom `⋯`, lalu klik item `Setup Column...`
21. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Group (langkah 22 sampai 23):
22. Hilangkan centang kolom tersebut pada daftar Setup Column
23. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
24. Hover checkbox kolom `Group`
25. Verifikasi checkbox kolom `Group` disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
26. Klik `[Save]`
27. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Group (langkah 28):
28. Verifikasi kolom tersebut tidak tampil di tabel
29. Klik F5
30. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Group (langkah 31):
31. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
32. Buka Setup Column, centang kembali seluruh kolom selain `Group`, lalu hilangkan centang kolom `Group`
33. Verifikasi perubahan kolom `Group` tampil di Live Preview
34. Klik `[Save]`
35. Verifikasi kolom `Group` tidak tampil di tabel
36. Klik F5
37. Verifikasi kolom `Group` tetap tidak tampil di tabel setelah refresh (F5)
38. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan overlay dan popup, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: geser kolom dan Reset to Default ada di spec 462; Pin dan unpin ada di spec 463; pagination dan state per sub-tab ada di spec 464.
- Langkah berulang (idiom bagian 8b butir 7): langkah 22 sampai 23 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites; langkah 28 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites; langkah 31 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible (TC-FA-SU-1162 butir g); spec menguji kolom selain `Group` bersamaan lalu kolom `Group` terpisah setelah kolom lain dicentang kembali. (2) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
- Spec ini berjumlah 38 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
