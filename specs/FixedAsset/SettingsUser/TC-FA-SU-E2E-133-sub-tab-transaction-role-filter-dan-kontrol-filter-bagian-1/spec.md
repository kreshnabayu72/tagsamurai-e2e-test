---
id: TC-FA-SU-E2E-133-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-1
title: "Sub-tab Transaction Role: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-392
  - TC-FA-SU-393
  - TC-FA-SU-394
coverage:
  web: automated
---

# Sub-tab Transaction Role: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-392: Filter Sub-tab Transaction Role kelas enum: Transaction, Role

1. Ketik Search `Yuda Pratama`, tekan Enter
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
3. Klik icon Filter
4. Buka dropdown Transaction
5. Verifikasi opsi dropdown Transaction sama dengan DISTINCT data tabel (`Borrowing & Assignment`, `Damaged`, `Disposal`, `Missing`, `Transfer`)
6. Centang `Borrowing & Assignment`
7. Klik `[Apply]`
8. Verifikasi memilih `Borrowing & Assignment` menyisakan `Borrowing & Assignment - Approver` (1 baris)
9. Verifikasi chip `Borrowing & Assignment` tampil di dalam field Transaction
10. Klik `[Clear Field]` pada field tersebut
11. Klik `[Apply]`
12. Buka dropdown Role
13. Verifikasi opsi dropdown Role sama dengan DISTINCT data tabel (`Approver`, `Asset Admin`, `Monitoring & Report`, `Staff`)
14. Centang `Approver`
15. Klik `[Apply]`
16. Verifikasi memilih `Approver` menyisakan `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver` (3 baris)
17. Verifikasi chip `Approver` tampil di dalam field Role
18. Klik `[Clear Field]` pada field tersebut
19. Klik `[Apply]`

### TC-FA-SU-393: Filter Sub-tab Transaction Role kelas fk: Group

20. Buka dropdown Group
21. Verifikasi opsi dropdown Group sama dengan DISTINCT data tabel (`All Groups`, `Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`)
22. Centang `All Groups`
23. Klik `[Apply]`
24. Verifikasi memilih `All Groups` menyisakan `Disposal - Approver` (1 baris)
25. Verifikasi chip `All Groups` tampil di dalam field Group
26. Klik `[Clear Field]` pada field tersebut
27. Klik `[Apply]`
28. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-394: Kombinasi Search dan Filter Sub-tab Transaction Role dua arah

29. Ketik Search `Transfer`, tekan Enter
30. Klik icon Filter
31. Buka dropdown Transaction
32. Centang `Borrowing & Assignment`
33. Klik `[Apply]`
34. Verifikasi Search `Transfer` lalu Filter Transaction `Borrowing & Assignment`: hasil irisan tidak ada baris (0 baris), dengan empty state `No results found` tampil sebagai anchor
35. Verifikasi kotak Search tetap berisi `Transfer` setelah Filter diterapkan
36. Verifikasi indikator pagination menunjukkan halaman 1 saat kriteria berubah
37. Klik `[Clear Field]`
38. Klik `[Apply]`
39. Klik `(←)` pada kotak Search
40. Buka dropdown Transaction
41. Centang `Borrowing & Assignment`
42. Klik `[Apply]`
43. Ketik Search `Transfer`, tekan Enter
44. Verifikasi Filter Transaction `Borrowing & Assignment` lalu Search `Transfer`: hasil identik, tidak ada baris, dengan empty state `No results found` tampil sebagai anchor
45. Verifikasi chip `Borrowing & Assignment` tetap tampil di field Transaction setelah Search dijalankan
46. Klik `[Clear Field]`
47. Klik `[Apply]`
48. Klik `(←)` pada kotak Search
49. Tutup panel Filter dengan klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung Search (S-03, R-16): langkah 1 (Ketik Search `Yuda Pratama`, tekan Enter) untuk menemukan baris Yuda Pratama di User List 25 pengguna (3 halaman) sebelum membuka Detail.
- Asersi tambahan (S-03): TC-FA-SU-394 butir a dan b menyebut 0 baris; empty state `No results found` ditulis dalam `Verifikasi` yang sama sebagai anchor absence baris (bagian 8b butir 2).
- Alasan melewati sekitar 35 langkah (49 langkah tertulis, 49 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-392 langkah 5: `[Clear Field]` disebut "pada field tersebut", sedangkan footer Filter Panel (TC-FA-SU-391) hanya punya satu `[Clear Field]`; spec mengklik `[Clear Field]` footer.
  - TC-FA-SU-394 butir d: "halaman 1 saat kriteria berubah" tidak dapat dibedakan pada fixture satu halaman (TC-FA-SU-404 butir e); spec mengasersi indikator pagination halaman 1.
