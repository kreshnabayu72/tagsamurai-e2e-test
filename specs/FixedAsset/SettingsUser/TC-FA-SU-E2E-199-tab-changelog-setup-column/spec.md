---
id: TC-FA-SU-E2E-199-tab-changelog-setup-column
title: "Tab Changelog: Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-594
  - TC-FA-SU-595
  - TC-FA-SU-596
  - TC-FA-SU-597
coverage:
  web: automated
---

# Tab Changelog: Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Field `Home Group`, Modified By `Lina M`
  - T-5: Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Tabel "Kolom Setup Column Hideable" (parameter langkah berulang): Date, Action, Field, Old Value, New Value, Modified By.
- Tabel parameter "Urutan drag kolom Hideable" (urutan awal: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`; arah ditetapkan spec, drag berurutan kumulatif):

| No | Kolom yang di-drag | Arah (satu posisi) | Urutan kolom sesudah drag |
|---|---|---|---|
| 1 | `Date` | bawah | `Action`, `Date`, `Field`, `Old Value`, `New Value`, `Modified By` |
| 2 | `Action` | bawah | `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` |
| 3 | `Field` | bawah | `Date`, `Action`, `Old Value`, `Field`, `New Value`, `Modified By` |
| 4 | `Old Value` | atas | `Date`, `Old Value`, `Action`, `Field`, `New Value`, `Modified By` |
| 5 | `New Value` | bawah | `Date`, `Old Value`, `Action`, `Field`, `Modified By`, `New Value` |
| 6 | `Modified By` | atas | `Date`, `Old Value`, `Action`, `Modified By`, `Field`, `New Value` |

- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-594: Screening Overlay Column Visibility

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
3. Klik header kolom Actions (⋯)
4. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
5. Verifikasi daftar kolom berurutan Date, Action, Field, Old Value, New Value, Modified By dengan checkbox Hideable terpilih dan enabled serta drag handle
6. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-595: Screening Popup Setup Column dan Preview Table

7. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
8. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
9. Verifikasi body: daftar kolom Date, Action, Field, Old Value, New Value, Modified By dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
10. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
11. Klik ✕ untuk menutup popup Setup Column

### TC-FA-SU-596: Ceklis dan unceklis kelas Hideable

12. Buka Setup Column
13. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 14 sampai 15):
14. Hilangkan centang kolom tersebut pada daftar Setup Column
15. Verifikasi perubahan tampil di Live Preview (kolom tersebut tidak tampil)
16. Hover checkbox kolom `Modified By`
17. Verifikasi checkbox kolom Modified By disabled dengan tooltip `At least one column must remain visible.` karena menjadi satu-satunya kolom visible
18. Klik `[Save]`
19. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 20):
20. Verifikasi kolom tersebut tidak tampil di tabel
21. Klik F5
22. Untuk setiap kolom pada tabel "Kolom Setup Column Hideable" selain Modified By (langkah 23):
23. Verifikasi kolom tersebut tetap tidak tampil di tabel setelah refresh (F5)
24. Buka Setup Column, centang kembali seluruh kolom selain Modified By, lalu hilangkan centang kolom Modified By
25. Verifikasi perubahan kolom Modified By tampil di Live Preview
26. Klik `[Save]`
27. Verifikasi kolom Modified By tidak tampil di tabel
28. Klik F5
29. Verifikasi kolom Modified By tetap tidak tampil di tabel setelah refresh (F5)
30. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

### TC-FA-SU-597: Geser (drag reorder) kelas Hideable

31. Buka Setup Column
32. Untuk setiap baris tabel "Urutan drag kolom Hideable" (langkah 32 sampai 33): drag kolom baris itu satu posisi sesuai kolom "Arah" baris itu
33. Verifikasi urutan Live Preview sama dengan kolom "Urutan kolom sesudah drag" baris itu
34. Klik `[Save]`
35. Verifikasi urutan kolom tabel sama dengan kolom "Urutan kolom sesudah drag" baris terakhir
36. Klik F5
37. Verifikasi urutan kolom tabel tetap sama dengan baris terakhir tabel parameter setelah refresh (F5)
38. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- Langkah penghubung tambahan (S-03): langkah 16 (Hover checkbox `Modified By`) mendahului `Verifikasi` tooltip (TC-FA-SU-596 Expected g, bagian 8b butir 5).
- Langkah berulang (idiom bagian 8b butir 7): langkah 14 sampai 15 dijalankan 5 kali, satu iterasi per kolom di tabel "Kolom Setup Column Hideable"; langkah 20 dijalankan 5 kali, satu iterasi per kolom di tabel itu; langkah 23 dijalankan 5 kali, satu iterasi per kolom di tabel itu; langkah 32 sampai 33 dijalankan 6 kali, satu iterasi per baris tabel "Urutan drag kolom Hideable".
- Spec ini berjumlah 64 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji lima kolom pertama bersamaan lalu kolom terakhir terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC tidak menyebut arah drag; spec menetapkan arah tiap kolom pada tabel "Urutan drag kolom Hideable" (satu posisi, kolom tetangga bertukar tempat) dan mengasersi urutan kumulatif setelah tiap drag, setelah `[Save]`, dan setelah F5, karena enam drag berurutan disimpan dengan satu `[Save]` sehingga posisi akhir tiap kolom tidak berdiri sendiri.
