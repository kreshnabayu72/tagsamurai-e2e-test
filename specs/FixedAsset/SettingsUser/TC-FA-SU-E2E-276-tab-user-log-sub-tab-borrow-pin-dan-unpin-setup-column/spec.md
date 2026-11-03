---
id: TC-FA-SU-E2E-276-tab-user-log-sub-tab-borrow-pin-dan-unpin-setup-column
title: "Tab User Log sub-tab Borrow: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-828
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan viewport (disediakan tim FE): ukuran viewport browser diatur cukup sempit di hook `before` spec ini supaya tabel memiliki scroll horizontal; langkah `Scroll tabel secara horizontal` bergantung pada kemampuan ini.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-828: Pin dan unpin Setup Column kelas Hideable (default tampil)

2. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Klik icon Pin pada kolom `Date`, `Activity`, `Transaction ID`
4. Hover icon Pin pada kolom `Name`
5. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` setelah tiga kolom di-pin
6. Klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi kolom `Date` membeku di kiri saat tabel di-scroll horizontal
9. Verifikasi kolom `Activity` membeku di kiri saat tabel di-scroll horizontal
10. Verifikasi kolom `Transaction ID` membeku di kiri saat tabel di-scroll horizontal
11. Klik F5
12. Scroll tabel secara horizontal
13. Verifikasi kolom `Date` tetap membeku di kiri setelah refresh (F5)
14. Verifikasi kolom `Activity` tetap membeku di kiri setelah refresh (F5)
15. Verifikasi kolom `Transaction ID` tetap membeku di kiri setelah refresh (F5)
16. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
17. Unpin kolom `Date`, `Activity`, `Transaction ID`
18. Klik `[Save]`
19. Scroll tabel secara horizontal
20. Verifikasi kolom `Date` terlepas (tidak membeku) saat tabel di-scroll horizontal
21. Verifikasi kolom `Activity` terlepas (tidak membeku) saat tabel di-scroll horizontal
22. Verifikasi kolom `Transaction ID` terlepas (tidak membeku) saat tabel di-scroll horizontal
23. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
24. Klik icon Pin pada kolom `Name`, `PIC`
25. Klik `[Save]`
26. Scroll tabel secara horizontal
27. Verifikasi kolom `Name` membeku di kiri saat tabel di-scroll horizontal
28. Verifikasi kolom `PIC` membeku di kiri saat tabel di-scroll horizontal
29. Klik F5
30. Scroll tabel secara horizontal
31. Verifikasi kolom `Name` tetap membeku di kiri setelah refresh (F5)
32. Verifikasi kolom `PIC` tetap membeku di kiri setelah refresh (F5)
33. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
34. Unpin kolom `Name`, `PIC`
35. Klik `[Save]`
36. Scroll tabel secara horizontal
37. Verifikasi kolom `Name` terlepas (tidak membeku) saat tabel di-scroll horizontal
38. Verifikasi kolom `PIC` terlepas (tidak membeku) saat tabel di-scroll horizontal
39. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pin dikerjakan dalam dua kelompok (`Date`, `Activity`, `Transaction ID` lalu `Name`, `PIC`) karena batas tiga kolom Pin (butir f TC-FA-SU-828); TC memerintahkan Pin pada kelima kolom sekaligus yang bertentangan dengan butir f.
- Pembagian TC lintas spec: TC-FA-SU-826 dan 827 ada di spec 272; TC-FA-SU-829 ada di spec 273.
- Temuan untuk QA (S-15): (1) TC-FA-SU-828 Langkah Uji nomor 3 memerintahkan Pin pada kelima kolom, sedangkan butir f menyatakan hanya tiga kolom dapat di-pin; spec memakai dua kelompok. (2) TC tidak menyebut cara men-scroll horizontal; skrip uji menentukan. (3) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
- Spec ini berjumlah 39 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
