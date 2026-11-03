---
id: TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel
title: "Custom Field Pengguna: Accordion, Rename, Hapus, Tipe Date dan Phone, serta Filter Panel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-949
  - TC-FA-SU-1036
  - TC-FA-SU-1037
  - TC-FA-SU-1038
  - TC-FA-SU-1039
  - TC-FA-SU-1040
coverage:
  web: automated
---

# Custom Field Pengguna: Accordion, Rename, Hapus, Tipe Date dan Phone, serta Filter Panel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), Custom Field (#31), varian `FaUserCF` (#41), dan atribut User List (#43). Target baca: Budi Santoso Pre-setup (Shift `Morning`, Joined Date `01/03/22`, Mobile `+62 81234567890`), hanya dibaca dan tidak diubah. Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Varian `FaUserCF` (varian `FaUserMain` yang menambah Custom Field `Joined Date` (Date), `Mobile` (Phone), `Skills` (Multi-Dropdown: `Audit`, `Tax`), dan `Notes` (Text)) diterapkan lewat seed API pada langkah 1 dan dipulihkan ke Pre-setup #31 pada langkah 18 serta di hook `after` (disediakan tim FE/BE), karena TC-FA-SU-1037 mensyaratkan `Shift` sebagai satu-satunya Custom Field aktif.
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Pengguna Tanpa Nilai CF {runId}-308`, email `pengguna.tanpa.nilai.cf+{runId}-308@qwertysystem.net`: Active; tanpa nilai Custom Field `Shift` (TC-FA-SU-949 butir b).
- Custom Field `Shift` (Pre-setup #31, Dropdown dengan opsi `Morning` dan `Night`) adalah satu-satunya Custom Field aktif Client `FaUserMain` dan data bersama yang tidak dapat dimiliki spec; Principal Automation (Pre-setup #12) menonaktifkan, mengaktifkan, mengganti nama, mengubah Data Type, dan menghapusnya di Global Settings lewat sesi API (disediakan tim FE). Pemulihan ke keadaan Tabel Data Uji Pre-setup (label `Shift`, Data Type Dropdown, aktif, nilai per pengguna) lewat seed API pada langkah 40 dan 48 serta di hook `after` (S-06, pengecualian kuota/data tak dapat dimiliki; suite serial). Efek pada Pre-setup: Last Updated dan Modified By Custom Field `Shift` berubah.
- Principal Automation (Pre-setup #12) memicu perubahan di Global Settings (App Access, identitas, status aktif, email, Custom Field) lewat sesi API; kemampuan ini disediakan tim FE (S-13). Langkah pemicunya ditulis "... hingga ... tersimpan" (R-20) dan bukan konteks UI kedua, sehingga tidak memakai `P-2`.
- Kemampuan menghapus preferensi kolom Setup Column di browser (bagian 4 konvensi), disediakan tim FE: pemulihan di langkah 17 dan di hook `after`.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

1. Terapkan varian data `FaUserCF` (Pre-setup #41) pada Client `FaUserMain` lewat seed API

### TC-FA-SU-1038: Custom Field bertipe Date tidak dapat dicari lewat Search User List

2. Klik Setup Column, tampilkan kolom Joined Date dan Mobile, lalu klik `[Save]`
3. Ketik Search `Budi`, tekan Enter
4. Verifikasi baris Budi Santoso menampilkan Joined Date `01/03/22` pada kolom Joined Date (pembanding bahwa nilai ada)
5. Klik icon Search di Table Tools
6. Ketik Search `01/03/22`, tekan Enter
7. Verifikasi empty state `No results found` tampil (Joined Date bertipe Date tidak masuk kolom Search)
8. Klik `(←)` pada kotak Search

### TC-FA-SU-1039: Custom Field bertipe Phone tampil dengan format [+CountryCode] [Number]

9. Ketik Search `Budi`, tekan Enter
10. Verifikasi nilai Mobile baris Budi Santoso `+62 81234567890` dengan format `[+CountryCode] [Number]`
11. Klik `(←)` pada kotak Search

### TC-FA-SU-1040: Filter Panel hanya memuat Custom Field bertipe Dropdown, Multi-Dropdown, dan Date

12. Klik icon Filter
13. Verifikasi Filter Panel memuat field Shift dan Skills (multi-select searchable)
14. Verifikasi Filter Panel memuat field Joined Date (date range picker)
15. Verifikasi Filter Panel tidak memuat field Mobile (Phone) dan Notes (Text)
16. Tutup Filter Panel tanpa Apply
17. Hapus preferensi kolom Setup Column di browser
18. Pulihkan Client `FaUserMain` ke Pre-setup #31 (Custom Field `Shift` sebagai satu-satunya Custom Field aktif) lewat seed API

### TC-FA-SU-949: Custom Field aktif tampil read-only di Accordion; field yang di-Deactivate hilang dan tampil kembali saat di-Activate

19. Ketik Search `Budi`, tekan Enter, lalu klik nama Budi Santoso untuk membuka Detail
20. Verifikasi Accordion `Custom Field` collapsed secara default
21. Klik header `Custom Field`
22. Verifikasi Accordion mengembang menampilkan daftar label-nilai read-only dengan `Shift` bernilai `Morning`
23. Buka Detail Pengguna Tanpa Nilai CF {runId}-308
24. Klik header `Custom Field`
25. Verifikasi Custom Field aktif tanpa nilai tampil `—`
26. Principal Automation menonaktifkan Custom Field `Shift` di Global Settings hingga perubahan tersimpan
27. Tunggu aksi selesai, lalu muat ulang Detail Budi Santoso
28. Verifikasi header Detail tampil (pembanding bahwa halaman termuat)
29. Verifikasi Custom Field `Shift` beserta nilainya tidak tampil
30. Principal Automation mengaktifkan kembali Custom Field `Shift` di Global Settings hingga perubahan tersimpan
31. Tunggu aksi selesai, lalu muat ulang Detail Budi Santoso dan klik header `Custom Field`
32. Verifikasi Custom Field `Shift` tampil kembali dengan nilai `Morning` utuh

### TC-FA-SU-1036: Custom Field: rename label dan perubahan Data Type tercermin di Accordion tanpa edit lokal

33. Buka Detail Budi Santoso dan klik header `Custom Field`
34. Principal Automation mengganti label Custom Field `Shift` menjadi `Work Shift` di Global Settings hingga perubahan tersimpan
35. Tunggu aksi selesai, lalu muat ulang Detail Budi Santoso dan klik header `Custom Field`
36. Verifikasi label `Work Shift` tampil di Accordion `Custom Field` tanpa tindakan di FAMS
37. Principal Automation mengubah Data Type Custom Field `Work Shift` di Global Settings menjadi Text hingga perubahan tersimpan
38. Tunggu aksi selesai, lalu muat ulang Detail Budi Santoso dan klik header `Custom Field`
39. Verifikasi nilai `Work Shift` Budi Santoso `—` (nilai dikosongkan oleh perubahan Data Type)
40. Pulihkan Custom Field `Shift` ke label `Shift`, Data Type Dropdown, aktif, dan nilai per pengguna Pre-setup lewat seed API

### TC-FA-SU-1037: Custom Field: field yang dihapus hilang permanen dan section Hidden saat tidak ada Custom Field aktif

41. Buka Detail Budi Santoso dan klik header `Custom Field`
42. Principal Automation menghapus Custom Field `Shift` di Global Settings hingga penghapusan tersimpan
43. Tunggu aksi selesai, lalu muat ulang Detail Budi Santoso
44. Verifikasi header Detail tampil (pembanding bahwa halaman termuat)
45. Verifikasi Custom Field `Shift` tidak tampil (hilang permanen)
46. Pastikan tidak ada Custom Field aktif tersisa di Global Settings, lalu muat ulang Detail Budi Santoso
47. Verifikasi section `Custom Field` Hidden seluruhnya
48. Pulihkan Custom Field `Shift` ke keadaan Pre-setup #31 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-1038 sampai TC-FA-SU-1040 (varian `FaUserCF`, hanya membaca) dikerjakan lebih dulu, lalu TC-FA-SU-949 dan TC-FA-SU-1036, dan TC-FA-SU-1037 yang menghapus Custom Field terakhir (S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 3, 8, 9, 11, 12, 16, 17, 18, 1, 19, 23, 27, 31, 33, 35, 38, 41, 43, 46, 40, 48; langkah baseline jumlah entri (S-12): . Langkah 3, 9, dan 19 adalah Search untuk menemukan baris target (R-16); langkah 40, 48, 17, dan 18 adalah pemulihan state (S-09).
- Tampilan kolom Joined Date dan Mobile dilakukan sekali pada langkah 2 dan dipakai TC-FA-SU-1038 dan TC-FA-SU-1039 (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: seluruh TC satu topik (Custom Field Global Settings tercermin di User List dan Detail) dan satu kelas harness; TC pada langkah 2 sampai 16 hanya membaca dan TC pada langkah 19 sampai 46 mengubah Custom Field lewat Principal Automation. Kegagalan satu TC tidak membuat TC lain kehilangan makna (48 langkah).
- Pengguna milik spec `Pengguna Tanpa Nilai CF` bersuffix `{runId}-308` (S-06); Budi Santoso Pre-setup dibaca tanpa diubah.
- Temuan untuk QA (S-15):
  - TC-FA-SU-949 butir b ("Custom Field aktif tanpa nilai tampil `—`") tidak menyebut pengguna tanpa nilai; spec memakai pengguna milik spec tanpa nilai `Shift`. Langkah "Deactivate lalu Activate" TC tidak memisahkan asersi di antaranya; spec mengasersi hilang sesudah Deactivate dan tampil kembali sesudah Activate.
  - TC-FA-SU-1036 tidak menyebut Data Type tujuan; spec memilih Text. TC tidak menyebut apakah nilai `Work Shift` pengguna lain diperiksa; spec memeriksa Budi Santoso.
  - TC-FA-SU-1037 mensyaratkan "tidak ada Custom Field aktif tersisa" tanpa cara memastikan; Pre-setup #31 hanya menyebut `Shift` sebagai Custom Field aktif, sehingga langkah ditulis sebagai pemastian tanpa kondisi cabang.
  - TC-FA-SU-1038 menulis "01/03/22" sebagai nilai Joined Date sekaligus keyword Search; format tanggal mengikuti General Settings dan tidak dinyatakan TC. Pre-setup #41 disebut sebagai varian `FaUserMain` tetapi nama Client terpisah (`FaUserCF`); spec memperlakukannya sebagai varian data pada Client yang sama sesuai kolom Peruntukan Pre-setup #41.
