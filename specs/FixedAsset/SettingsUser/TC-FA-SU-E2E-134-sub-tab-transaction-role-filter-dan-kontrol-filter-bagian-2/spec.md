---
id: TC-FA-SU-E2E-134-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-2
title: "Sub-tab Transaction Role: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-395
coverage:
  web: automated
---

# Sub-tab Transaction Role: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-395: Pelepasan kontrol Sub-tab Transaction Role: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

1. Ketik Search `Yuda Pratama`, tekan Enter
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
3. Ketik Search `Transfer`, tekan Enter
4. Klik icon Filter
5. Buka dropdown Transaction
6. Centang `Borrowing & Assignment`
7. Klik `[Apply]`
8. Klik header kolom Transaction satu kali
9. Klik `[Clear Field]`
10. Klik `[Apply]`
11. Verifikasi Clear Field saat Search `Transfer` dan Sort aktif: Search tetap berlaku, tabel menyisakan `Transfer - Asset Admin` dan `Transfer - Monitoring & Report`
12. Verifikasi Clear Field saat Search dan Sort aktif: Sort kolom Transaction tetap berlaku
13. Buka dropdown Transaction
14. Centang `Borrowing & Assignment`
15. Klik `[Apply]`
16. Klik `✕` pada Search, tekan Enter
17. Verifikasi setelah Search dikosongkan saat Filter Transaction dan Sort aktif: Filter tetap berlaku, tabel menyisakan `Borrowing & Assignment - Approver`
18. Verifikasi setelah Search dikosongkan saat Filter dan Sort aktif: Sort kolom Transaction tetap berlaku
19. Ketik Search `Transfer`, tekan Enter
20. Klik header kolom Group satu kali
21. Verifikasi mengganti kolom sort memindahkan Sort ke kolom Group
22. Verifikasi Search `Transfer` tidak direset oleh ganti sort
23. Verifikasi Filter Transaction `Borrowing & Assignment` tidak direset oleh ganti sort
24. Verifikasi kombinasi Search dan Filter yang menghasilkan 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
25. Klik `✕` pada Search, tekan Enter
26. Verifikasi melepas Search langsung memulihkan baris yang cocok: `Borrowing & Assignment - Approver` tampil
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Tutup panel Filter dengan klik icon Filter
30. Klik header kolom Group dua kali lagi sampai kembali netral

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-396 dan TC-FA-SU-397 ada di spec 149.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung Search (S-03, R-16): langkah 1 (Ketik Search `Yuda Pratama`, tekan Enter) untuk menemukan baris Yuda Pratama di User List 25 pengguna (3 halaman) sebelum membuka Detail.
- Temuan untuk QA (S-15):
  - TC-FA-SU-395 langkah 6: "keyword yang tidak ada hasilnya" tidak diberi nilai; spec memakai kombinasi Search `Transfer` dan Filter Transaction `Borrowing & Assignment` (0 baris, sesuai TC-FA-SU-394). Sort pada kombinasi 0 baris diasersi lewat indikator sort kolom.
