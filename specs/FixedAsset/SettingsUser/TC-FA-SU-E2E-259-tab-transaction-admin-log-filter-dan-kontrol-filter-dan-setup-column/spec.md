---
id: TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column
title: "Tab Transaction Admin Log: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-782
  - TC-FA-SU-783
  - TC-FA-SU-784
  - TC-FA-SU-785
coverage:
  web: automated
---

# Tab Transaction Admin Log: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Transaction ID, Group, Role, Action Taken, Date, Transaction Status.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment

### TC-FA-SU-782: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

2. Klik icon Filter, lalu buka dropdown `Group`
3. Centang `Branch Surabaya` dan `Finance & Accounting`
4. Klik `[Apply]`
5. Verifikasi dua chip `Branch Surabaya` dan `Finance & Accounting` tampil di dalam field `Group`
6. Verifikasi hasil adalah gabungan (OR) kedua opsi: `BRW-20260716-0314`, `BRW-20260713-0312`
7. Klik `✕` pada chip `Finance & Accounting` tanpa membuka dropdown
8. Verifikasi chip `Finance & Accounting` hilang
9. Verifikasi chip `Branch Surabaya` tetap tampil
10. Buka dropdown `Group`
11. Verifikasi checkbox opsi `Finance & Accounting` ter-uncheck
12. Centang kembali `Finance & Accounting`
13. Hilangkan centang `Branch Surabaya`
14. Verifikasi chip `Branch Surabaya` hilang
15. Verifikasi chip `Finance & Accounting` tetap tampil
16. Ketik `ACC` di kotak cari dropdown
17. Verifikasi opsi dropdown menyempit menjadi `Finance & Accounting` (substring, tidak case-sensitive)
18. Ganti keyword di kotak cari dropdown dengan `zzzz`
19. Verifikasi dropdown menampilkan `No results found`
20. Tutup dropdown, klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
21. Klik icon Filter untuk menutup panel

### TC-FA-SU-783: Screening Overlay Column Visibility

22. Klik header kolom `⋯` (Actions)
23. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
24. Verifikasi daftar kolom berurutan `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, `Transaction Status` dengan checkbox Hideable terpilih dan enabled serta drag handle
25. Verifikasi item `Setup Column...` di bagian bawah overlay
26. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-784: Screening Popup Setup Column dan Preview Table

27. Klik header kolom `⋯`, lalu klik item `Setup Column...`
28. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close `✕` tampil
29. Verifikasi body: daftar kolom `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, `Transaction Status` dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
30. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
31. Klik `✕` untuk menutup popup Setup Column

### TC-FA-SU-785: Ceklis dan unceklis Setup Column kelas Hideable (default tampil)

32. Klik header kolom `⋯`, lalu klik item `Setup Column...`
33. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Transaction Status (langkah 34 sampai 35):
34. Hilangkan centang kolom tersebut pada daftar Setup Column
35. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
36. Hover checkbox kolom `Transaction Status`
37. Verifikasi checkbox kolom `Transaction Status` disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
38. Klik `[Save]`
39. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Transaction Status (langkah 40):
40. Verifikasi kolom tersebut tidak tampil di tabel
41. Klik F5
42. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Transaction Status (langkah 43):
43. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
44. Buka Setup Column, centang kembali seluruh kolom selain `Transaction Status`, lalu hilangkan centang kolom `Transaction Status`
45. Verifikasi perubahan kolom `Transaction Status` tampil di Live Preview
46. Klik `[Save]`
47. Verifikasi kolom `Transaction Status` tidak tampil di tabel
48. Klik F5
49. Verifikasi kolom `Transaction Status` tetap tidak tampil di tabel setelah refresh (F5)
50. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan panel Filter, overlay, dan popup, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Hasil gabungan (OR) pada TC-FA-SU-782 butir a ditulis `BRW-20260716-0314` dan `BRW-20260713-0312`, diturunkan dari urutan Group TC-FA-SU-772 dan opsi dropdown TC-FA-SU-776 (`Branch Surabaya` pada `BRW-20260716-0314`, `Finance & Accounting` pada `BRW-20260713-0312`).
- Opsi kedua pada TC-FA-SU-782 butir c dipulihkan dengan mencentang kembali `Finance & Accounting` sebelum `Branch Surabaya` di-uncheck, supaya klausa "chip lain tetap" teramati; TC hanya menyebut "uncheck opsi yang tersisa". Keyword dropdown `ACC` dan `zzzz` dipilih spec karena TC tidak menyebutnya.
- Temuan untuk QA (S-15) tambahan: TC-FA-SU-782 Langkah Uji nomor 6 hanya menyebut "keyword tanpa hasil" sedangkan Expected butir d juga meminta penyempitan opsi; spec menguji keduanya dengan dua keyword.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji kolom selain `Transaction Status` bersamaan lalu kolom `Transaction Status` terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC tidak menyebut apakah tab tetap aktif setelah F5; spec mengikuti TC (Klik F5 lalu Verifikasi pada tabel) dan pembukaan ulang tab bila perlu ditentukan skrip uji.
- Langkah berulang (idiom bagian 8b butir 7): langkah 34 sampai 35 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites; langkah 40 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites; langkah 43 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites.
- Spec ini berjumlah 66 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
