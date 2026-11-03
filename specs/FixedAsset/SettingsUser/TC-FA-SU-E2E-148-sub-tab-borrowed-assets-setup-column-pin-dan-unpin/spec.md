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

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Untuk setiap baris tabel "Putaran pin" di Prerequisites (langkah 2 sampai 22): klik header kolom Column Visibility (⋯)
3. Klik `Setup Column...`
4. Klik icon Pin pada kolom ke-1 baris itu
5. Klik icon Pin pada kolom ke-2 baris itu
6. Klik icon Pin pada kolom ke-3 baris itu
7. Arahkan kursor ke icon Pin kolom yang tercantum pada kolom Kolom lain baris itu
8. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
9. Klik `[Save]`
10. Scroll tabel secara horizontal
11. Verifikasi ketiga kolom baris itu membeku di kiri saat tabel di-scroll horizontal
12. Tekan F5
13. Scroll tabel secara horizontal
14. Verifikasi ketiga kolom baris itu tetap membeku setelah F5
15. Klik header kolom Column Visibility (⋯)
16. Klik `Setup Column...`
17. Klik icon Pin pada kolom ke-1 baris itu untuk unpin
18. Klik icon Pin pada kolom ke-2 baris itu untuk unpin
19. Klik icon Pin pada kolom ke-3 baris itu untuk unpin
20. Klik `[Save]`
21. Scroll tabel secara horizontal
22. Verifikasi unpin melepaskan: ketiga kolom baris itu tidak lagi membeku
23. Klik header kolom Column Visibility (⋯)
24. Klik `Setup Column...`
25. Klik icon Pin pada kolom Due Return Date
26. Klik icon Pin pada kolom PIC
27. Klik `[Save]`
28. Scroll tabel secara horizontal
29. Verifikasi kolom Due Return Date dan PIC membeku di kiri saat tabel di-scroll horizontal
30. Tekan F5
31. Scroll tabel secara horizontal
32. Verifikasi kolom Due Return Date dan PIC tetap membeku setelah F5
33. Klik header kolom Column Visibility (⋯)
34. Klik `Setup Column...`
35. Klik icon Pin pada kolom Due Return Date untuk unpin
36. Klik icon Pin pada kolom PIC untuk unpin
37. Klik `[Save]`
38. Scroll tabel secara horizontal
39. Verifikasi unpin melepaskan: kolom Due Return Date dan PIC tidak lagi membeku
40. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Rentang langkah 2 sampai 22 diulang untuk dua putaran pada tabel "Putaran pin" (Prerequisites); putaran ketiga (Due Return Date dan PIC) ditulis eksplisit karena hanya dua kolom tersisa.
- Pemulihan konfigurasi kolom: preferensi kolom yang disimpan spec dihapus di browser pada akhir blok dan di hook `after` (Prerequisites); `[Reset to Default]` tidak dipakai sebagai pemulihan.
- Alasan melewati sekitar 35 langkah (40 langkah tertulis, 61 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-432: langkah 3 meminta delapan kolom di-pin sekaligus, sedangkan butir i menyatakan maksimum tiga kolom; spec mem-pin kolom dalam tiga putaran (Photo, Name, Asset ID; Transaction ID, Brand, Model / Type; Due Return Date, PIC) dan mengasersi tiap putaran dalam satu `Verifikasi` per putaran. Langkah 5 TC hanya meng-unpin satu kolom, sedangkan butir a sampai h menyebut unpin melepaskan untuk tiap kolom; spec meng-unpin seluruh kolom putaran. Scroll horizontal membutuhkan viewport sempit (Prerequisites). Post Condition tidak diasersi.
