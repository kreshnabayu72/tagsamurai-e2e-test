---
id: TC-FA-SU-E2E-227-modal-changelog-user-transaction-role-setup-column
title: "Modal Changelog User > Transaction Role: Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-690
  - TC-FA-SU-691
  - TC-FA-SU-692
  - TC-FA-SU-693
coverage:
  web: automated
---

# Modal Changelog User > Transaction Role: Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Transaction Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - TR-1: `Damaged — Branch Surabaya — Monitoring & Report`; Modified By `Ahmad D`
  - TR-2: `Missing — Branch Surabaya — Approver`; Modified By `Ahmad D`
  - TR-3: `Disposal — Logistics Warehouse — Asset Admin`; Modified By `Lina M`
  - TR-4: `Disposal — Logistics Warehouse — Staff`; Modified By `Lina M`
  - TR-5: `Transfer — Finance & Accounting — Asset Admin`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, Field, Old Value, New Value, Modified By.
- Tabel "Urutan Drag Setup Column" (parameter langkah berulang; dijalankan berurutan dari baris pertama, tiap baris drag satu posisi tanpa `[Save]` di antaranya sehingga efeknya kumulatif; posisi 1 = paling atas pada daftar Setup Column dan paling kiri pada tabel; posisi akhir dihitung dari urutan semula pada tabel "Kolom Setup Column Hideable"): (1) Action ke atas, posisi akhir 1; (2) Date ke bawah, posisi akhir 2; (3) Field ke bawah, posisi akhir 4; (4) Old Value ke bawah, posisi akhir 6; (5) New Value ke atas, posisi akhir 3; (6) Modified By ke atas, posisi akhir 5.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-690: Screening Overlay Column Visibility

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
2. Klik header kolom Actions (⋯)
3. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
4. Verifikasi daftar kolom berurutan Date, Action, Field, Old Value, New Value, Modified By dengan checkbox Hideable terpilih dan enabled serta drag handle
5. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-691: Screening Popup Setup Column dan Preview Table

6. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
7. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
8. Verifikasi body: daftar kolom Date, Action, Field, Old Value, New Value, Modified By dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
9. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
10. Klik ✕ untuk menutup popup Setup Column

### TC-FA-SU-692: Ceklis dan unceklis kelas Hideable

11. Buka Setup Column
12. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 13 sampai 14):
13. Hilangkan centang kolom tersebut pada daftar Setup Column
14. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
15. Hover checkbox kolom Modified By yang disabled
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

### TC-FA-SU-693: Geser (drag reorder) kelas Hideable

30. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
31. Buka Setup Column
32. Untuk setiap baris pada tabel "Urutan Drag Setup Column" secara berurutan (langkah 33 sampai 34):
33. Drag kolom pada baris tersebut satu posisi ke arah (atas atau bawah) yang tertulis pada tabel
34. Verifikasi urutan Live Preview berubah
35. Klik `[Save]`
36. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 37):
37. Verifikasi posisi kolom tersebut pada tabel berubah (menempati posisi akhir pada tabel)
38. Klik F5
39. Untuk setiap baris pada tabel "Urutan Drag Setup Column" (langkah 40):
40. Verifikasi posisi kolom tersebut pada tabel tetap berubah (menempati posisi akhir pada tabel) setelah refresh (F5)
41. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 15 (Hover checkbox kolom Modified By yang disabled) hanya memunculkan tooltip sebelum `Verifikasi` tooltip pada langkah 16 (bagian 8b butir 5); tidak ada asersi.
- TC-FA-SU-694 (pin dan unpin modal Transaction Role) ada di spec 231.
- Langkah berulang per kolom (idiom bagian 8b butir 7): langkah 13 sampai 14 dijalankan 5 kali, satu iterasi per kolom di tabel Prerequisites; langkah 19 dijalankan 5 kali, satu iterasi per kolom di tabel Prerequisites; langkah 22 dijalankan 5 kali, satu iterasi per kolom di tabel Prerequisites; langkah 33 sampai 34 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 37 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites; langkah 40 dijalankan 6 kali, satu iterasi per kolom di tabel Prerequisites.
- Spec ini berjumlah 77 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji lima kolom pertama bersamaan lalu kolom terakhir terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC tidak menyebut arah drag; spec menulis "satu posisi" mengikuti TC dan menetapkan sendiri urutan, arah, dan posisi akhir tiap kolom pada tabel "Urutan Drag Setup Column" di Prerequisites, karena drag berurutan tanpa `[Save]` bersifat kumulatif sehingga arah yang tidak ditentukan membuat posisi akhir tidak deterministik; arah dan posisi akhir itu pilihan spec, bukan ketentuan TC. (3) TC tidak menyebut apakah modal Changelog tetap terbuka setelah F5; spec mengikuti TC (Klik F5 lalu Verifikasi pada tabel modal) dan pembukaan ulang modal bila perlu ditentukan skrip uji. Setelah penghapusan preferensi kolom halaman dimuat ulang, sehingga TC berikutnya membuka modal lagi.
