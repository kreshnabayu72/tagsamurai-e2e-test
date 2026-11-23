---
id: TC-FA-SU-E2E-275-tab-transaction-admin-log-pin-dan-unpin-setup-column
title: "Tab Transaction Admin Log: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-787
coverage:
  web: automated
---

# Tab Transaction Admin Log: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Tabel "Kolom Putaran 1" (parameter langkah berulang; di-pin bersamaan, maksimum tiga kolom): `Date`, `Activity`, `Transaction ID`.
- Tabel "Kolom Putaran 2": `Name`, `Borrower`, `Group`.
- Kemampuan teknis (disediakan tim FE): viewport browser dikecilkan sehingga tabel enam kolom dapat di-scroll horizontal, dan scroll horizontal tabel; `Esc`, hover, dan muat ulang halaman (`F5`).

## Test Steps

### TC-FA-SU-787: Pin dan unpin Setup Column kelas Hideable (default tampil)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Putaran 1. Klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 4):
4. Klik icon Pin pada kolom pada baris tersebut
5. Hover icon Pin pada kolom `Name`
6. Verifikasi icon Pin kolom `Name` disabled
7. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
8. Klik `[Save]`
9. Scroll tabel secara horizontal ke kanan
10. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 11):
11. Verifikasi kolom pada baris tersebut membeku di kiri saat tabel di-scroll horizontal
12. Klik `F5`
13. Scroll tabel secara horizontal ke kanan
14. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 15):
15. Verifikasi kolom pada baris tersebut tetap membeku di kiri setelah refresh (`F5`)
16. Klik header kolom `⋯`, lalu klik item `Setup Column...`
17. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 18):
18. Unpin kolom pada baris tersebut
19. Klik `[Save]`
20. Scroll tabel secara horizontal ke kanan
21. Untuk setiap baris pada tabel "Kolom Putaran 1" (langkah 22):
22. Verifikasi kolom pada baris tersebut tidak lagi membeku dan ikut bergeser saat tabel di-scroll horizontal
23. Putaran 2. Klik header kolom `⋯`, lalu klik item `Setup Column...`
24. Untuk setiap baris pada tabel "Kolom Putaran 2" (langkah 25):
25. Klik icon Pin pada kolom pada baris tersebut
26. Klik `[Save]`
27. Scroll tabel secara horizontal ke kanan
28. Untuk setiap baris pada tabel "Kolom Putaran 2" (langkah 29):
29. Verifikasi kolom pada baris tersebut membeku di kiri saat tabel di-scroll horizontal
30. Klik `F5`
31. Scroll tabel secara horizontal ke kanan
32. Untuk setiap baris pada tabel "Kolom Putaran 2" (langkah 33):
33. Verifikasi kolom pada baris tersebut tetap membeku di kiri setelah refresh (`F5`)
34. Klik header kolom `⋯`, lalu klik item `Setup Column...`
35. Untuk setiap baris pada tabel "Kolom Putaran 2" (langkah 36):
36. Unpin kolom pada baris tersebut
37. Klik `[Save]`
38. Scroll tabel secara horizontal ke kanan
39. Untuk setiap baris pada tabel "Kolom Putaran 2" (langkah 40):
40. Verifikasi kolom pada baris tersebut tidak lagi membeku dan ikut bergeser saat tabel di-scroll horizontal

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan Setup Column, dan scroll horizontal tabel. Unpin semua kolom beserta `[Save]` pada akhir tiap putaran memulihkan perubahan kolom di dalam spec (bagian 8b butir 14); hook `after` hanya cadangan.
- Langkah berulang (idiom bagian 8b butir 7): langkah 4, 11, 15, 18, dan 22 masing-masing dijalankan 3 kali (satu iterasi per baris tabel "Kolom Putaran 1"); langkah 25, 29, 33, 36, dan 40 masing-masing dijalankan 3 kali (tabel "Kolom Putaran 2"). Enam kolom diuji dalam dua putaran sesuai Langkah Uji nomor 3 TC-FA-SU-787 dan batas tiga kolom yang di-pin bersamaan (butir g).
- Pembagian TC lintas spec: TC-FA-SU-785 ada di spec 439; TC-FA-SU-786 dan TC-FA-SU-788 ada di spec 260; TC-FA-SU-782 sampai TC-FA-SU-784 ada di spec 259.
- Temuan untuk QA (S-15): (1) TC-FA-SU-787 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (#1) dari hook suite. (2) TC-FA-SU-787 Langkah Uji nomor 5 ("Unpin satu kolom") hanya melepas satu kolom, sedangkan Expected a sampai f menyebut unpin untuk tiap kolom; spec meng-unpin ketiga kolom tiap putaran. (3) Scroll horizontal membutuhkan tabel yang lebih lebar daripada viewport; TC tidak menyebut ukuran viewport sehingga dinyatakan sebagai kemampuan di Prerequisites. (4) Post Condition TC-FA-SU-787 tidak punya langkah observasi dan tidak diasersi.
- Spec ini berjumlah 60 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01) dan dari langkah berulang per kolom (batas tiga kolom di-pin), bukan dari langkah tambahan.
