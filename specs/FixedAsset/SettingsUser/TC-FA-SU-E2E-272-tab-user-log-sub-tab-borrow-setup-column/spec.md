---
id: TC-FA-SU-E2E-272-tab-user-log-sub-tab-borrow-setup-column
title: "Tab User Log sub-tab Borrow: Setup Column (Ceklis dan Drag Reorder)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-826
  - TC-FA-SU-827
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Setup Column (Ceklis dan Drag Reorder)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Activity, Transaction ID, Name, PIC.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-826: Ceklis dan unceklis Setup Column kelas Hideable (default tampil)

2. Klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain PIC (langkah 4 sampai 5):
4. Hilangkan centang kolom tersebut pada daftar Setup Column
5. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
6. Hover checkbox kolom `PIC`
7. Verifikasi checkbox kolom `PIC` disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
8. Klik `[Save]`
9. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain PIC (langkah 10):
10. Verifikasi kolom tersebut tidak tampil di tabel
11. Klik F5
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain PIC (langkah 13):
13. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
14. Buka Setup Column, centang kembali seluruh kolom selain `PIC`, lalu hilangkan centang kolom `PIC`
15. Verifikasi perubahan kolom `PIC` tampil di Live Preview
16. Klik `[Save]`
17. Verifikasi kolom `PIC` tidak tampil di tabel
18. Klik F5
19. Verifikasi kolom `PIC` tetap tidak tampil di tabel setelah refresh (F5)
20. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-827: Geser (drag reorder) Setup Column kelas Hideable (default tampil)

21. Klik header kolom `⋯`, lalu klik item `Setup Column...`
22. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 23 sampai 24):
23. Drag kolom tersebut satu posisi
24. Verifikasi urutan Live Preview berubah
25. Klik `[Save]`
26. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 27):
27. Verifikasi posisi kolom tersebut pada tabel berubah
28. Klik F5
29. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" (langkah 30):
30. Verifikasi posisi kolom tersebut pada tabel tetap berubah setelah refresh (F5)
31. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-SU-828 (Pin dan unpin) ada di spec 276; TC-FA-SU-829 ada di spec 273.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji kolom selain `PIC` bersamaan lalu kolom `PIC` terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC tidak menyebut apakah tab tetap aktif setelah F5; spec mengikuti TC (Klik F5 lalu Verifikasi pada tabel) dan pembukaan ulang tab bila perlu ditentukan skrip uji.
- Temuan untuk QA (S-15): TC tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan arah drag ditentukan skrip uji.
- Langkah berulang (idiom bagian 8b butir 7): langkah 4 sampai 5 dijalankan 4 kali, satu iterasi per baris di tabel Prerequisites; langkah 10 dijalankan 4 kali, satu iterasi per baris di tabel Prerequisites; langkah 13 dijalankan 4 kali, satu iterasi per baris di tabel Prerequisites; langkah 23 sampai 24 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites; langkah 27 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites; langkah 30 dijalankan 5 kali, satu iterasi per baris di tabel Prerequisites.
- Spec ini berjumlah 59 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
