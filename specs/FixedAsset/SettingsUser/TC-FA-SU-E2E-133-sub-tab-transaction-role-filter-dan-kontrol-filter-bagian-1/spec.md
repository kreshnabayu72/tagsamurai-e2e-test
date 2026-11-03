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

1. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
2. Klik icon Filter
3. Buka dropdown Transaction
4. Verifikasi opsi dropdown Transaction sama dengan DISTINCT data tabel (`Borrowing & Assignment`, `Damaged`, `Disposal`, `Missing`, `Transfer`)
5. Centang `Borrowing & Assignment`
6. Klik `[Apply]`
7. Verifikasi memilih `Borrowing & Assignment` menyisakan `Borrowing & Assignment - Approver` (1 baris)
8. Verifikasi chip `Borrowing & Assignment` tampil di dalam field Transaction
9. Klik `[Clear Field]` pada field tersebut
10. Klik `[Apply]`
11. Buka dropdown Role
12. Verifikasi opsi dropdown Role sama dengan DISTINCT data tabel (`Approver`, `Asset Admin`, `Monitoring & Report`, `Staff`)
13. Centang `Approver`
14. Klik `[Apply]`
15. Verifikasi memilih `Approver` menyisakan `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver` (3 baris)
16. Verifikasi chip `Approver` tampil di dalam field Role
17. Klik `[Clear Field]` pada field tersebut
18. Klik `[Apply]`

### TC-FA-SU-393: Filter Sub-tab Transaction Role kelas fk: Group

19. Buka dropdown Group
20. Verifikasi opsi dropdown Group sama dengan DISTINCT data tabel (`All Groups`, `Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`)
21. Centang `All Groups`
22. Klik `[Apply]`
23. Verifikasi memilih `All Groups` menyisakan `Disposal - Approver` (1 baris)
24. Verifikasi chip `All Groups` tampil di dalam field Group
25. Klik `[Clear Field]` pada field tersebut
26. Klik `[Apply]`
27. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-394: Kombinasi Search dan Filter Sub-tab Transaction Role dua arah

28. Ketik Search `Transfer`, tekan Enter
29. Klik icon Filter
30. Buka dropdown Transaction
31. Centang `Borrowing & Assignment`
32. Klik `[Apply]`
33. Verifikasi Search `Transfer` lalu Filter Transaction `Borrowing & Assignment`: hasil irisan tidak ada baris (0 baris), dengan empty state `No results found` tampil sebagai anchor
34. Verifikasi kotak Search tetap berisi `Transfer` setelah Filter diterapkan
35. Verifikasi indikator pagination menunjukkan halaman 1 saat kriteria berubah
36. Klik `[Clear Field]`
37. Klik `[Apply]`
38. Klik `(←)` pada kotak Search
39. Buka dropdown Transaction
40. Centang `Borrowing & Assignment`
41. Klik `[Apply]`
42. Ketik Search `Transfer`, tekan Enter
43. Verifikasi Filter Transaction `Borrowing & Assignment` lalu Search `Transfer`: hasil identik, tidak ada baris, dengan empty state `No results found` tampil sebagai anchor
44. Verifikasi chip `Borrowing & Assignment` tetap tampil di field Transaction setelah Search dijalankan
45. Klik `[Clear Field]`
46. Klik `[Apply]`
47. Klik `(←)` pada kotak Search
48. Tutup panel Filter dengan klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Asersi tambahan (S-03): TC-FA-SU-394 butir a dan b menyebut 0 baris; empty state `No results found` ditulis dalam `Verifikasi` yang sama sebagai anchor absence baris (bagian 8b butir 2).
- Alasan melewati sekitar 35 langkah (48 langkah tertulis, 48 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-392 langkah 5: `[Clear Field]` disebut "pada field tersebut", sedangkan footer Filter Panel (TC-FA-SU-391) hanya punya satu `[Clear Field]`; spec mengklik `[Clear Field]` footer.
  - TC-FA-SU-394 butir d: "halaman 1 saat kriteria berubah" tidak dapat dibedakan pada fixture satu halaman (TC-FA-SU-404 butir e); spec mengasersi indikator pagination halaman 1.
