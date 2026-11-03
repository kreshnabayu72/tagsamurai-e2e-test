---
id: TC-FA-SU-E2E-135-sub-tab-transaction-role-filter-dan-kontrol-filter-dan-setup-column
title: "Sub-tab Transaction Role: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-398
  - TC-FA-SU-399
  - TC-FA-SU-400
  - TC-FA-SU-409
coverage:
  web: automated
---

# Sub-tab Transaction Role: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- State yang diubah: preferensi kolom tabel tersimpan per perangkat setelah `[Save]`. Dipulihkan dengan menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi), bukan `[Reset to Default]`; langkah pemulihan ada di akhir blok yang menyimpan, dan hook `after` mengulangnya sebagai cadangan. Spec tidak mengubah data backend.

## Test Steps

### TC-FA-SU-409: Pencarian dan filter Sub-tab Transaction Role mencocokkan baris yang memuat grup terpilih

1. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
2. Klik icon Filter
3. Buka dropdown Group
4. Centang `Branch Surabaya`
5. Klik `[Apply]`
6. Verifikasi Filter Group `Branch Surabaya` menyisakan seluruh baris yang memuat Branch Surabaya walau memuat grup lain: `Damaged - Monitoring & Report`, `Missing - Approver`, dan `Transfer - Monitoring & Report`
7. Klik `[Clear Field]`
8. Klik `[Apply]`
9. Ketik Search `Surabaya`, tekan Enter
10. Verifikasi Search `Surabaya` menyisakan baris yang sama dengan Filter Group `Branch Surabaya`: `Damaged - Monitoring & Report`, `Missing - Approver`, dan `Transfer - Monitoring & Report`
11. Klik `(←)` pada kotak Search
12. Buka dropdown Role
13. Centang `Approver`
14. Klik `[Apply]`
15. Verifikasi Filter Role `Approver` menyisakan baris Role Approver: `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver`
16. Klik `[Clear Field]`
17. Klik `[Apply]`
18. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-398: Screening Overlay Column Visibility Sub-tab Transaction Role

19. Klik header kolom Actions (⋯)
20. Arahkan kursor ke header kolom Actions (⋯)
21. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
22. Verifikasi daftar kolom berurutan Transaction, Role, Group
23. Verifikasi tiap kolom memiliki checkbox ☑ Hideable terpilih dan enabled
24. Verifikasi tiap kolom memiliki drag handle
25. Verifikasi item `Setup Column...` di bagian bawah overlay
26. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-399: Screening Popup Setup Column dan Preview Table Sub-tab Transaction Role

27. Klik header kolom Actions (⋯)
28. Klik `Setup Column...`
29. Verifikasi Title popup `Setup Column`
30. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
31. Verifikasi icon close ✕ pada header popup
32. Verifikasi body memuat daftar kolom Transaction, Role, Group
33. Verifikasi tiap kolom memiliki checkbox
34. Verifikasi tiap kolom memiliki drag handle
35. Verifikasi tiap kolom memiliki icon Pin
36. Verifikasi Live Preview tabel tampil
37. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
38. Verifikasi footer tanpa `[Cancel]`
39. Tutup popup Setup Column dengan ✕

### TC-FA-SU-400: Ceklis dan unceklis Setup Column Sub-tab Transaction Role kelas Hideable (default tampil)

40. Klik header kolom Actions (⋯)
41. Klik `Setup Column...`
42. Hapus centang kolom Transaction
43. Verifikasi perubahan kolom Transaction tampil di Live Preview
44. Hapus centang kolom Role
45. Verifikasi perubahan kolom Role tampil di Live Preview
46. Arahkan kursor ke checkbox kolom Group (satu-satunya kolom visible)
47. Verifikasi checkbox kolom Group disabled dengan tooltip `At least one column must remain visible.`
48. Klik `[Save]`
49. Verifikasi kolom Group tetap tampil di tabel
50. Verifikasi kolom Transaction tidak tampil di tabel
51. Verifikasi kolom Role tidak tampil di tabel
52. Tekan F5
53. Verifikasi kolom Group tetap tampil setelah refresh (F5)
54. Verifikasi kolom Transaction tetap tidak tampil setelah refresh (F5)
55. Verifikasi kolom Role tetap tidak tampil setelah refresh (F5)
56. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengarahkan kursor ke header kolom Actions sebelum asersi tooltip; menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Pemulihan konfigurasi kolom: preferensi kolom yang disimpan spec dihapus di browser pada akhir blok dan di hook `after` (Prerequisites); `[Reset to Default]` tidak dipakai sebagai pemulihan.
- Alasan melewati sekitar 35 langkah (56 langkah tertulis, 56 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-409 butir a dan b tidak menyebut daftar baris; spec memakai tiga baris yang memuat Branch Surabaya menurut TC-FA-SU-385.
  - TC-FA-SU-400: butir a sampai c meminta ketiga kolom diubah centangnya, sedangkan butir d menyatakan kolom terakhir tidak dapat di-uncheck; spec meng-uncheck Transaction dan Role, lalu mengasersi kolom Group lewat butir d (perubahan Group di Live Preview tidak dapat terjadi). Post Condition (preferensi tersimpan per perangkat) tidak punya langkah observasi dan tidak diasersi.
