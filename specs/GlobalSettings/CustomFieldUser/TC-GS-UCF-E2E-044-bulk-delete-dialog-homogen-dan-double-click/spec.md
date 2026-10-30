---
id: TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click
title: "Bulk Delete: Dialog Container Scrollable, Collapse ke Dialog Single, Cancel, Klik Ganda, dan Penghapusan Homogen"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-147
  - TC-GS-UCF-148
  - TC-GS-UCF-149
  - TC-GS-UCF-150
  - TC-GS-UCF-155
coverage:
  web: automated
---

# Bulk Delete: Dialog Container Scrollable, Collapse ke Dialog Single, Cancel, Klik Ganda, dan Penghapusan Homogen

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini bergantung pada total tepat 14 Custom Field pada blok awal (TC-GS-UCF-147; kebersihan field sisa dijamin butir hook suite "Field sisa Client A" di `suite.md`), menghapus Custom Field milik sendiri, dan membaca Changelog yang dibagi suite; tidak berjalan bersamaan dengan spec lain.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah tidak mengulang pembukaan layar kecuali sesudah berpindah halaman.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca, tidak diubah atau dihapus; dialog Delete atasnya dibatalkan lewat `[Cancel]`, sehingga Last Updated tidak berubah, pengecualian S-06): 14 Custom Field (6 Pre-setup `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date` dan 8 Population `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`) di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada). User `Rahmat Hidayat` (`rahmatHidayat_automated_qaTeam1@qwertysystem.net`, Pre-setup) dengan nilai `Grade 5` pada `Employee Grade` dipakai sebagai anchor pembanding di Detail User.
- Data Dinamis (bersuffix per run; fixture baru `Fixture.customFieldUser.bulkDelete044`; mekanisme seeding nilai Custom Field pada User disediakan tim FE/BE, lihat Temuan untuk QA). Karena TC-GS-UCF-147 mengandalkan total tepat 14 baris pada page size 25, seluruh Data Dinamis di-seed lewat API pada langkah penghubung 12 (disediakan tim FE/BE), bukan di hook `before`:
  - `Bulk Single {runId}-044`: Text; bebas nilai User (TC-GS-UCF-148); tetap ada.
  - `Bulk Keep A {runId}-044`, `Bulk Keep B {runId}-044`: Text (TC-GS-UCF-150); tetap ada.
  - `Bulk Dbl A {runId}-044`, `Bulk Dbl B {runId}-044`: Text (TC-GS-UCF-155); dihapus oleh spec ini.
  - `Bulk Del A {runId}-044` (nilai User Rahmat Hidayat = `A`), `Bulk Del B {runId}-044`, `Bulk Del C {runId}-044`: Text (TC-GS-UCF-149); dihapus oleh spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-044` yang masih ada dan nilai Custom Field milik spec pada Rahmat Hidayat; kembalikan page size tabel ke default (10).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: scroll pada container daftar bullet dialog; klik ganda cepat pada `[Delete]` (TC-GS-UCF-155); Search tabel dan Changelog Custom Field dengan filter Action. Entri Changelog bersifat permanen; asersi jumlah entri memakai Search `{runId}-044` (suffix berisi digit run saja) sehingga baseline entri milik run ini adalah nol.
- State global: page size tabel (cache browser) diubah ke 25 dan dipulihkan ke 10 pada langkah 13; flag Guided Tooltip diatur hook suite.

## Test Steps

### TC-GS-UCF-147: Dialog Bulk Delete menampilkan seluruh nama dalam container scrollable

1. Ubah page size menjadi 25
2. Klik checkbox header halaman, lalu uncheck baris `Cost Center` dan `Joining Date` (12 baris tersisa terpilih)
3. Klik `Bulk Action` > `Delete`
4. Verifikasi dialog `Delete Custom Fields` menampilkan body "All user data for these fields will be permanently lost.", pertanyaan "This action cannot be undone. Are you sure you want to delete them?", serta tombol `[Cancel]` dan `[Delete]`
5. Verifikasi dialog memuat 12 bullet `Annual Target`, `badge number`, `Birth Date`, `Blood Type`, `Bonus`, `Emergency Phone`, `Employee Grade`, `Job Description`, `Office Phone`, `Shirt Size`, `Tax ID`, `Work Notes` dalam container scrollable
6. Scroll daftar bullet
7. Verifikasi daftar memuat 12 bullet lengkap (tidak diringkas) dan dapat di-scroll
8. Klik `[Cancel]`
9. Verifikasi dialog tertutup
10. Verifikasi seleksi 12 baris tetap
11. Verifikasi Bulk Action Bar tetap tampil
12. Klik `(✕)` pada Bulk Action Bar, seed Data Dinamis spec ini lewat API (disediakan tim FE/BE), lalu muat ulang halaman (F5)
13. Ubah page size kembali menjadi 10

### TC-GS-UCF-148: Bulk Delete dengan 1 baris terpilih memakai dialog single

14. Ketik Search `Bulk Single {runId}-044`, tekan Enter
15. Centang baris `Bulk Single {runId}-044`
16. Klik `Bulk Action` > `Delete`
17. Verifikasi dialog `Delete Custom Field` (singular) menampilkan 1 bullet `Bulk Single {runId}-044`, body "All user data for this field will be permanently lost.", pertanyaan "This action cannot be undone. Are you sure you want to delete it?" (bukan "...delete them?"), serta tombol `[Cancel]` dan `[Delete]`
18. Klik `[Cancel]`
19. Klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-150: Cancel dialog Bulk Delete mempertahankan seleksi

20. Ketik Search `Bulk Keep`, tekan Enter
21. Centang baris `Bulk Keep A {runId}-044` dan `Bulk Keep B {runId}-044`
22. Klik `Bulk Action` > `Delete`
23. Klik `[Cancel]`
24. Verifikasi tidak ada toast
25. Verifikasi dialog tertutup
26. Verifikasi baris `Bulk Keep A {runId}-044` dan `Bulk Keep B {runId}-044` tetap ada
27. Verifikasi kedua baris tetap checked
28. Verifikasi Bulk Action Bar tetap tampil
29. Klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-155: Klik ganda [Delete] pada dialog Bulk Delete hanya memproses satu batch

30. Ketik Search `Bulk Dbl`, tekan Enter
31. Centang baris `Bulk Dbl A {runId}-044` dan `Bulk Dbl B {runId}-044`
32. Klik `Bulk Action` > `Delete`
33. Klik `[Delete]` dua kali cepat
34. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been deleted."
35. Klik `(←)` pada kotak Search, lalu klik icon Changelog, pilih filter Action `Delete`, Search `{runId}-044`, tekan Enter
36. Verifikasi Changelog memuat tepat 1 entri Delete per field (`Bulk Dbl A {runId}-044` dan `Bulk Dbl B {runId}-044`)
37. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-149: Bulk Delete homogen menghapus seluruh field terpilih

38. Dismiss toast dari langkah 34
39. Ketik Search `Bulk Del`, tekan Enter
40. Centang baris `Bulk Del A {runId}-044`, `Bulk Del B {runId}-044`, dan `Bulk Del C {runId}-044`
41. Klik `Bulk Action` > `Delete`
42. Verifikasi dialog `Delete Custom Fields` menampilkan 3 bullet `Bulk Del A {runId}-044`, `Bulk Del B {runId}-044`, `Bulk Del C {runId}-044`
43. Klik `[Delete]`
44. Verifikasi muncul toast sukses: "Success, custom field has been deleted."
45. Verifikasi baris `Bulk Del A {runId}-044`, `Bulk Del B {runId}-044`, dan `Bulk Del C {runId}-044` hilang dari tabel
46. Verifikasi Bulk Action Bar hilang
47. Verifikasi seleksi di-reset
48. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
49. Verifikasi Detail User Rahmat Hidayat menampilkan `Employee Grade` dengan nilai `Grade 5`
50. Verifikasi Detail User Rahmat Hidayat tidak lagi memuat field `Bulk Del A {runId}-044`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (50 langkah). Seluruhnya satu kelas (Bulk Delete pada satu dataset). Blok TC-GS-UCF-147 hanya membaca 14 field Pre-setup dan Population (dialog dibatalkan); blok sesudahnya memakai field milik sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Urutan TC dalam spec: 147 (mengandalkan total tepat 14 baris), seeding Data Dinamis (langkah 12), 148, 150 (tanpa penghapusan), lalu 155 dan 149 (aksi yang menghapus data, paling akhir; prinsip 5). TC-GS-UCF-155 ditempatkan sebelum TC-GS-UCF-149 supaya jumlah entri Delete pada langkah 36 hanya memuat dua entri milik TC-GS-UCF-155. Urutan menyimpang dari urutan TC sumber (147, 148, 149, 150, 155).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 13 (page size 25 untuk TC-GS-UCF-147 dan pemulihannya), langkah 12 (membersihkan seleksi, seeding, dan muat ulang), langkah 14, 20, 30, 39 (Search agar baris target tampil), langkah 18 (menutup dialog TC-GS-UCF-148 lewat `[Cancel]`; TC tidak menyebut cara menutup), langkah 19, 29, 35 (membersihkan seleksi, Search, atau membuka Changelog), langkah 37 (menutup modal), dan langkah 38 (dismiss toast lama supaya toast pada langkah 44 adalah toast hasil Delete TC-GS-UCF-149).
- Asersi tambahan di luar Expected TC (S-03): langkah 49 (anchor pembanding `Employee Grade` untuk asersi absence di Detail User) dan langkah 24 (TC-GS-UCF-150 butir a "tertutup tanpa toast" dipecah menjadi tidak ada toast dan dialog tertutup).
- Pembagian TC lintas spec: Bulk Delete campuran yang melibatkan item sudah dihapus admin lain (TC-GS-UCF-151, 152, 153) ada di spec 047.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-UCF-149 ("Bulk Del A, B, C terhapus"; hanya baris tabel dan Detail User `Bulk Del A` yang punya Expected, tidak untuk `Bulk Del B` dan `C`) dan tidak ada Expected atas entri Changelog untuk TC-GS-UCF-149.
  - TC-GS-UCF-147 dan 148 mengandalkan total tepat 14 baris pada page size 25; Data Dinamis spec yang sama menambah baris sehingga spec men-seed Data Dinamis sesudah TC-GS-UCF-147 (langkah 12). Mekanisme seeding oleh tim FE/BE.
  - TC-GS-UCF-148 tidak menyebut cara menutup dialog sesudah asersi; spec menutup dengan `[Cancel]` (dialog konfirmasi memang memiliki `[Cancel]`).
  - TC-GS-UCF-149 mencantumkan `Bulk Del C` (D-48) tanpa nilai User; spec men-seed Text tanpa nilai. TC-GS-UCF-147 mengasumsikan urutan bullet `badge number` setelah `Annual Target` (urutan alfabet tanpa membedakan huruf besar kecil); spec mengikuti urutan Data Uji TC.
  - Mekanisme seeding nilai Custom Field pada User (`A`) tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE.
