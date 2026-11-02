---
id: TC-FA-GRP-E2E-274-tab-assets-setup-column-komposisi-tanpa-group-custom-field-cost-center-dan-custom-field-inactive
title: "Tab Assets Setup Column: Komposisi Tanpa Group, Kolom Curated Custom Field (Centang, Geser, Pin, Reset), dan Custom Field Inactive/Baru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1189
  - TC-FA-GRP-1238
  - TC-FA-GRP-1239
coverage:
  web: automated
---

# Tab Assets Setup Column: Komposisi Tanpa Group, Kolom Curated Custom Field (Centang, Geser, Pin, Reset), dan Custom Field Inactive/Baru

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: allValueAccess (Pre-setup No 17: Group Role Manage purchase pada Value Gate Node A, Global Role Manage accounting, lisensi FA-7 aktif) `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit, untuk TC-1238 dan TC-1239): Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Data Pre-setup tambahan: Value Gate Node A (Tabel Dinamis No 10, G1-G6) di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-274` (mekanisme seeding disediakan tim FE/BE); langkah dan asersi memakai nama bersuffix itu. Custom field Tabel Dinamis No 13: Cost Center dan Insurance Policy (Active), Legacy Note (Inactive), PO Number, Purchase Date, Cost Account.
- Data Dinamis yang dibuat spec: Probe Field `Probe Field {runId}-274` (grup General, Scope General, Active, lalu dinonaktifkan oleh spec). Pembuatan dan penonaktifan lewat kemampuan seeding Custom Field yang disediakan tim FE/BE (tanpa endpoint karangan). Field tetap Inactive sesudah spec (lifecycle Tabel Dinamis No 17); hook `after` tidak menghapusnya.
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser agar TC-1189 mengamati konfigurasi default (precondition d); hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE). Aksi [Reset to Default] pada TC-1238 adalah bagian objek uji.
- Kemampuan teknis: scroll horizontal tabel dan refresh F5 oleh browser.
- State global: tidak ada yang diubah selain field Probe Field.

## Test Steps

### TC-1189: Komposisi Setup Column Tab Assets tanpa Group: urutan, default Visible, dan kolom curated Hidden
1. Buka Detail Value Gate Node A (Tab Assets)
2. Amati header kolom tabel
3. Verifikasi header tabel (kolom Visible default) berurutan: Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated, diikuti Actions (⋯)
4. Klik icon (⋯), amati daftar Column Visibility
5. Verifikasi daftar Column Visibility berurutan: Name (checked, enabled), Asset ID (checked), TAG (checked), Brand (checked), Model/Type (checked), Measurement (unchecked, enabled), Category (unchecked), Label (unchecked), Status (checked), Transactional Policy (unchecked), Last Scanned (unchecked), Asset Value (Commercial) (unchecked), Asset Value (Fiscal) (unchecked), Warranty Expiry (unchecked), Cost Center (unchecked), Insurance Policy (unchecked), PO Number (unchecked), Purchase Date (unchecked), Cost Account (unchecked), Last Updated (checked)
6. Tutup daftar Column Visibility; buka Popup Setup Column
7. Verifikasi Popup Setup Column berurutan sama dengan daftar Column Visibility (Name hingga Last Updated beserta status centang yang sama)
8. Verifikasi custom field berurutan menurut grup General, Purchasing, Accounting, lalu Field Name A-Z dalam grup
9. Verifikasi Last Updated adalah kolom data terakhir sebelum Actions (⋯)
10. Verifikasi Custom Field Inactive (Legacy Note) tidak ada di daftar
11. Verifikasi tidak ada kolom Group
12. Tutup Popup Setup Column
### TC-1238: Setup Column kolom curated Custom Field (Cost Center): centang, geser (drag), pin, dan Reset to Default
13. Ganti akun: Logout, login sebagai Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`), buka Fixed Asset > Settings > Groups
14. Buka Detail Value Gate Node A (Tab Assets)
15. Buka Popup Setup Column, centang Cost Center, klik [Save]
16. Verifikasi kolom Cost Center tampil
17. Refresh halaman dengan F5
18. Verifikasi kolom Cost Center tetap tampil setelah F5
19. Buka Popup Setup Column, geser (drag) Cost Center ke posisi setelah Status, klik [Save]
20. Verifikasi urutan kolom tabel mengikuti posisi baru (Cost Center setelah Status)
21. Refresh halaman dengan F5
22. Verifikasi urutan kolom tetap mengikuti posisi baru setelah F5
23. Buka Popup Setup Column, pin kolom Cost Center, klik [Save]
24. Scroll horizontal tabel
25. Verifikasi kolom Cost Center membeku (sticky) saat scroll horizontal
26. Refresh halaman dengan F5
27. Buka Popup Setup Column, unpin kolom Cost Center, klik [Save]
28. Scroll horizontal tabel
29. Verifikasi kolom Cost Center ikut scroll setelah unpin
30. Buka Popup Setup Column, klik [Reset to Default], klik [Save]
31. Verifikasi kolom Cost Center kembali tersembunyi (curated)
### TC-1239: Custom Field Inactive tidak menjadi kolom; field baru tampil Hidden; field yang dinonaktifkan hilang dari Setup Column
32. Buka Popup Setup Column dan amati daftar kolom custom field
33. Verifikasi `Cost Center` dan `Insurance Policy` (Active) ada di daftar
34. Verifikasi `Legacy Note` (Inactive) tidak ada di daftar
35. Tutup Popup Setup Column
36. Buat field `Probe Field {runId}-274` (grup General, Scope General, Active) lewat kemampuan seeding Custom Field
37. Buka ulang Detail Value Gate Node A (Tab Assets), buka Popup Setup Column
38. Verifikasi `Probe Field {runId}-274` muncul di Popup Setup Column berstatus curated (unchecked, enabled)
39. Verifikasi header tabel Name tampil dan `Probe Field {runId}-274` tidak tampil di tabel sampai dicentang
40. Tutup Popup Setup Column; nonaktifkan `Probe Field {runId}-274` lewat kemampuan seeding Custom Field
41. Buka ulang Popup Setup Column
42. Verifikasi `Cost Center` ada di daftar
43. Verifikasi `Probe Field {runId}-274` hilang dari himpunan kolom
44. Tutup Popup Setup Column

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-1189 pertama karena membaca konfigurasi default (precondition d), diikuti TC-1238 (menyimpan konfigurasi, diakhiri [Reset to Default]) lalu TC-1239.
- Langkah penghubung (S-03): "Tutup Popup Setup Column"/"Tutup daftar Column Visibility"; satu langkah Ganti akun sebelum TC-1238 (aktor Total Control; TC-1239 melanjutkan dengan akun yang sama); refresh F5 setelah "Pin" pada TC-1238 mengikuti Langkah TC.
- Alasan di atas ~35 langkah: ketiga TC satu topik (Setup Column Tab Assets, dataset Value Gate Node A), tiap blok berdiri sendiri dan tidak bergantung pada hasil blok lain; tidak ada kelas harness lain. TC-1238 sendiri berisi alur centang, geser, pin, dan reset yang sengaja berurutan.
- Temuan untuk QA:
  - TC-1189 Expected b menyebut daftar Column Visibility dan Popup Setup Column dengan urutan yang sama tetapi Langkah 4 hanya membuka ikon (⋯); spec mengasersi keduanya.
  - TC-1238 langkah 5 ("Pin kolom, [Save], scroll horizontal; refresh F5; unpin") tidak menjelaskan apakah pin bertahan setelah F5; Expected c hanya menyebut sticky saat scroll dan ikut scroll setelah unpin. Spec tidak mengasersi persistensi pin.
  - TC-1239 langkah 6 ("buka ulang Popup Setup Column") tidak menjelaskan apakah Detail perlu dimuat ulang agar field yang dinonaktifkan hilang; spec membuka ulang popup saja.
  - TC-1239 Tabel Dinamis No 17 menyebut Probe Field sebagai nama literal; spec memakai nama bersuffix (S-12).
