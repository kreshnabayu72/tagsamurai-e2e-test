---
id: TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter
title: "Sub-tab Transaction Role: Search, Sort, dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-387
  - TC-FA-SU-388
  - TC-FA-SU-389
  - TC-FA-SU-390
  - TC-FA-SU-391
coverage:
  web: automated
---

# Sub-tab Transaction Role: Search, Sort, dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-387: Search Sub-tab Transaction Role terikat visibilitas kolom Transaction: hide lalu unhide

1. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
2. Ketik Search `Transfer`, tekan Enter
3. Verifikasi sebelum hide: keyword `Transfer` menyisakan `Transfer - Asset Admin` dan `Transfer - Monitoring & Report`
4. Klik header kolom Actions (⋯)
5. Hapus centang Transaction pada overlay Column Visibility
6. Tutup overlay Column Visibility dengan Esc
7. Ganti isi kotak search dengan `Transfer`, tekan Enter
8. Verifikasi setelah kolom Transaction di-hide: keyword yang sama menyisakan tidak ada baris (kolom tersembunyi tidak dicari; kolom lain yang tampil tetap dicari), dengan empty state `No results found` tampil sebagai anchor
9. Klik header kolom Actions (⋯)
10. Centang kembali Transaction pada overlay Column Visibility
11. Tutup overlay Column Visibility dengan Esc
12. Ganti isi kotak search dengan `Transfer`, tekan Enter
13. Verifikasi setelah kolom Transaction di-unhide: hasil kembali `Transfer - Asset Admin` dan `Transfer - Monitoring & Report`
14. Klik `(←)` pada kotak Search

### TC-FA-SU-388: Sort Sub-tab Transaction Role kelas teks: Transaction

15. Klik header kolom Transaction satu kali
16. Verifikasi Transaction klik 1 ascending (↑): `Borrowing & Assignment - Approver`, `Damaged - Monitoring & Report`, `Disposal - Approver`, `Disposal - Staff`, `Missing - Approver`
17. Klik header kolom Transaction kedua kali
18. Verifikasi Transaction klik 2 descending (↓): `Transfer - Asset Admin`, `Transfer - Monitoring & Report`, `Missing - Approver`, `Disposal - Approver`, `Disposal - Staff`
19. Klik header kolom Transaction ketiga kali
20. Verifikasi Transaction klik 3 netral kembali ke default: `Borrowing & Assignment - Approver`, `Damaged - Monitoring & Report`, `Disposal - Approver`, `Disposal - Staff`, `Missing - Approver`

### TC-FA-SU-389: Sort Sub-tab Transaction Role kelas group: Group

21. Klik header kolom Group satu kali
22. Verifikasi Group klik 1 ascending (↑): `Disposal - Approver`, `Damaged - Monitoring & Report`, `Transfer - Monitoring & Report`, `Borrowing & Assignment - Approver`, `Disposal - Staff`
23. Klik header kolom Group kedua kali
24. Verifikasi Group klik 2 descending (↓): `Missing - Approver`, `Transfer - Asset Admin`, `Disposal - Staff`, `Borrowing & Assignment - Approver`, `Damaged - Monitoring & Report`
25. Klik header kolom Group ketiga kali
26. Verifikasi Group klik 3 netral kembali ke default: `Borrowing & Assignment - Approver`, `Damaged - Monitoring & Report`, `Disposal - Approver`, `Disposal - Staff`, `Missing - Approver`

### TC-FA-SU-390: Guard kolom non-sortable Sub-tab Transaction Role: Role

27. Hover header kolom Role
28. Klik header kolom Role
29. Verifikasi header Role tidak memiliki icon sort
30. Verifikasi klik header Role tidak mengubah urutan

### TC-FA-SU-391: Screening Filter Panel Sub-tab Transaction Role: field, label, placeholder, dan tombol

31. Klik icon Filter
32. Verifikasi panel Filter terbuka di bawah Table Tools
33. Verifikasi icon Filter menjadi gelap
34. Hover icon Filter
35. Verifikasi tooltip `Filter`
36. Verifikasi field pertama Transaction berupa multi-select searchable dengan placeholder `All transactions`
37. Verifikasi field kedua Role berupa multi-select searchable dengan placeholder `All roles`
38. Verifikasi field ketiga Group berupa multi-select searchable dengan placeholder `All groups`
39. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
40. Verifikasi icon Filter tanpa badge titik selama belum ada filter ter-Apply
41. Tutup panel Filter dengan klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Asersi tambahan (S-03): TC-FA-SU-387 butir b tidak menyebut empty state; `Verifikasi` empty state `No results found` ditambahkan pada langkah yang sama sebagai anchor absence baris (bagian 8b butir 2).
- Alasan melewati sekitar 35 langkah (41 langkah tertulis, 41 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-388: klik 1 ascending menghasilkan urutan yang sama dengan default (TC-FA-SU-383), sehingga klik 3 netral tidak terbedakan dari klik 1 hanya lewat urutan baris; spec mengasersi urutan sesuai TC.
