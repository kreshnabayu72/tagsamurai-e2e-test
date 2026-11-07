---
id: TC-FA-SU-E2E-148-sub-tab-borrowed-assets-setup-column-pin-dan-unpin
title: "Sub-tab Borrowed Assets: Setup Column Pin dan Unpin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-432
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Setup Column Pin dan Unpin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Tabel "Putaran pin" (maksimum 3 kolom di-pin sekaligus, sehingga kolom dipin dalam putaran; satu putaran per iterasi):

  | Putaran | Kolom ke-1 | Kolom ke-2 | Kolom ke-3 | Kolom lain |
  |---|---|---|---|---|
  | 1 | Photo | Name | Asset ID | Transaction ID |
  | 2 | Transaction ID | Brand | Model / Type | Photo |
- State yang diubah: preferensi kolom tabel tersimpan per perangkat setelah `[Save]`. Dipulihkan dengan menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi), bukan `[Reset to Default]`; langkah pemulihan ada di akhir blok yang menyimpan, dan hook `after` mengulangnya sebagai cadangan. Spec tidak mengubah data backend.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).

## Test Steps

### TC-FA-SU-432: Pin dan unpin Setup Column Sub-tab Borrowed Assets kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Untuk setiap baris tabel "Putaran pin" di Prerequisites (langkah 3 sampai 23): klik header kolom Column Visibility (⋯)
4. Klik `Setup Column...`
5. Klik icon Pin pada kolom ke-1 baris itu
6. Klik icon Pin pada kolom ke-2 baris itu
7. Klik icon Pin pada kolom ke-3 baris itu
8. Arahkan kursor ke icon Pin kolom yang tercantum pada kolom Kolom lain baris itu
9. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
10. Klik `[Save]`
11. Scroll tabel secara horizontal
12. Verifikasi ketiga kolom baris itu membeku di kiri saat tabel di-scroll horizontal
13. Tekan F5
14. Scroll tabel secara horizontal
15. Verifikasi ketiga kolom baris itu tetap membeku setelah F5
16. Klik header kolom Column Visibility (⋯)
17. Klik `Setup Column...`
18. Klik icon Pin pada kolom ke-1 baris itu untuk unpin
19. Klik icon Pin pada kolom ke-2 baris itu untuk unpin
20. Klik icon Pin pada kolom ke-3 baris itu untuk unpin
21. Klik `[Save]`
22. Scroll tabel secara horizontal
23. Verifikasi unpin melepaskan: ketiga kolom baris itu tidak lagi membeku
24. Klik header kolom Column Visibility (⋯)
25. Klik `Setup Column...`
26. Klik icon Pin pada kolom Due Return Date
27. Klik icon Pin pada kolom PIC
28. Klik `[Save]`
29. Scroll tabel secara horizontal
30. Verifikasi kolom Due Return Date dan PIC membeku di kiri saat tabel di-scroll horizontal
31. Tekan F5
32. Scroll tabel secara horizontal
33. Verifikasi kolom Due Return Date dan PIC tetap membeku setelah F5
34. Klik header kolom Column Visibility (⋯)
35. Klik `Setup Column...`
36. Klik icon Pin pada kolom Due Return Date untuk unpin
37. Klik icon Pin pada kolom PIC untuk unpin
38. Klik `[Save]`
39. Scroll tabel secara horizontal
40. Verifikasi unpin melepaskan: kolom Due Return Date dan PIC tidak lagi membeku
41. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Rentang langkah 3 sampai 23 diulang untuk dua putaran pada tabel "Putaran pin" (Prerequisites); putaran ketiga (Due Return Date dan PIC) ditulis eksplisit karena hanya dua kolom tersisa.
- Pemulihan konfigurasi kolom: preferensi kolom yang disimpan spec dihapus di browser pada akhir blok dan di hook `after` (Prerequisites); `[Reset to Default]` tidak dipakai sebagai pemulihan.
- Alasan melewati sekitar 35 langkah (41 langkah tertulis, 62 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-432: langkah 3 meminta delapan kolom di-pin sekaligus, sedangkan butir i menyatakan maksimum tiga kolom; spec mem-pin kolom dalam tiga putaran (Photo, Name, Asset ID; Transaction ID, Brand, Model / Type; Due Return Date, PIC) dan mengasersi tiap putaran dalam satu `Verifikasi` per putaran. Langkah 5 TC hanya meng-unpin satu kolom, sedangkan butir a sampai h menyebut unpin melepaskan untuk tiap kolom; spec meng-unpin seluruh kolom putaran. Scroll horizontal membutuhkan viewport sempit (Prerequisites). Post Condition tidak diasersi.
