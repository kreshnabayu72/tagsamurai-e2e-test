---
id: TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses
title: "Delete Custom Field Tunggal: Dialog, Accessibility, Cancel, Sukses dengan Efek ke User dan Log, Klik Ganda, dan Field Inactive"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-134
  - TC-GS-UCF-409
  - TC-GS-UCF-135
  - TC-GS-UCF-136
  - TC-GS-UCF-137
  - TC-GS-UCF-139
coverage:
  web: automated
---

# Delete Custom Field Tunggal: Dialog, Accessibility, Cancel, Sukses dengan Efek ke User dan Log, Klik Ganda, dan Field Inactive

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menghapus Custom Field milik sendiri dan memakai Changelog, Activity Log, dan System Log yang dibagi suite; tidak berjalan bersamaan dengan spec lain.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah pertama tiap blok tidak mengulang pembukaan layar kecuali sesudah berpindah ke halaman User atau Log.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tidak diubah atau dihapus spec ini, tanpa suffix): 14 Custom Field (6 Pre-setup `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date` dan 8 Population `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`) di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada). Baris `Cost Center` hanya dibuka dialog Delete-nya lalu dibatalkan (TC-GS-UCF-409), sehingga record dan Last Updated-nya tidak berubah (pengecualian S-06). User `Rahmat Hidayat` (`rahmatHidayat_automated_qaTeam1@qwertysystem.net`, Pre-setup) memiliki nilai `Grade 5` pada `Employee Grade` (dipakai sebagai anchor pembanding) dan dipakai sebagai pemilik nilai Custom Field milik spec.
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; fixture baru `Fixture.customFieldUser.deleteSingle039`; mekanisme seeding nilai Custom Field pada User disediakan tim FE/BE, lihat Temuan untuk QA):
  - `Delete Me {runId}-039`: Text; nilai User Rahmat Hidayat = `Gone Soon` (TC-GS-UCF-134, TC-GS-UCF-135); dihapus oleh spec ini.
  - `Delete Keep {runId}-039`: Text; nilai User Rahmat Hidayat = `Stay` (TC-GS-UCF-136); tetap ada.
  - `Delete Twice {runId}-039`: Text; bebas nilai User (TC-GS-UCF-137); dihapus oleh spec ini.
  - `Delete Inactive {runId}-039`: Text; Inactive (TC-GS-UCF-139); dihapus oleh spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-039` yang masih ada dan nilai Custom Field milik spec pada Rahmat Hidayat.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: Tab berulang pada dialog dan pembacaan elemen yang sedang fokus (TC-GS-UCF-409); klik ganda cepat pada `[Delete]` (TC-GS-UCF-137); Search pada tabel Custom Field, Changelog Custom Field, Changelog User, System Log, dan Activity Log; menunggu toast sukses lama hilang otomatis (jeda pendek, ≤ 4 detik, TC-GS-UCF-489) pada langkah 53.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-UCF-409: Accessibility dialog Delete, fokus keyboard berputar di dalam dialog

1. Ketik Search `Cost Center`, tekan Enter
2. Klik `⋯` pada baris `Cost Center`, pilih `Delete`
3. Verifikasi dialog `Delete Custom Field` terbuka
4. Tekan Tab berulang melewati elemen terakhir dialog
5. Verifikasi fokus keyboard berputar di dalam dialog dan tidak berpindah ke elemen di belakang dialog
6. Klik `[Cancel]`
7. Verifikasi dialog tertutup
8. Verifikasi baris `Cost Center` tetap ada di tabel
9. Klik `(←)` pada kotak Search

### TC-GS-UCF-136: Cancel dialog Delete tidak menghapus apa pun

10. Ketik Search `Delete Keep {runId}-039`, tekan Enter
11. Klik `⋯` pada baris `Delete Keep {runId}-039`, pilih `Delete`
12. Klik `[Cancel]`
13. Verifikasi tidak ada toast
14. Verifikasi dialog tertutup
15. Verifikasi baris `Delete Keep {runId}-039` tetap ada di tabel
16. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
17. Verifikasi Detail User Rahmat Hidayat tetap menampilkan nilai `Stay` pada `Delete Keep {runId}-039`
18. Buka Global Settings > User > Custom Field

### TC-GS-UCF-134 dan TC-GS-UCF-135: Dialog konfirmasi Delete single dan penghapusan permanen

19. Ketik Search `Delete Me {runId}-039`, tekan Enter
20. Klik `⋯` pada baris `Delete Me {runId}-039`, pilih `Delete`
21. Verifikasi dialog `Delete Custom Field` menampilkan bullet `Delete Me {runId}-039`, body "All user data for this field will be permanently lost.", pertanyaan "This action cannot be undone. Are you sure you want to delete it?", serta tombol `[Cancel]` dan `[Delete]`
22. Verifikasi tidak ada dialog blok in-use
23. Klik `[Delete]`
24. Verifikasi muncul toast sukses: "Success, custom field has been deleted."
25. Verifikasi baris `Delete Me {runId}-039` hilang dari tabel
26. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
27. Verifikasi Detail User Rahmat Hidayat menampilkan `Employee Grade` dengan nilai `Grade 5`
28. Verifikasi Detail User Rahmat Hidayat tidak lagi menampilkan field `Delete Me {runId}-039`
29. Verifikasi Detail User Rahmat Hidayat tidak lagi menampilkan nilai `Gone Soon`
30. Buka Global Settings > User > User List (sub-tab Login User), klik `[+ User]`, perhatikan section Custom Field dinamis
31. Verifikasi section Custom Field dinamis form Create User memuat field `Cost Center`
32. Verifikasi form Create User tidak memuat field `Delete Me {runId}-039`
33. Tutup popup lewat `[✕]`
34. Buka Global Settings > User > Custom Field, klik icon Changelog, Search `Delete Me {runId}-039`, tekan Enter
35. Verifikasi Changelog Custom Field memuat entri Delete: Field `Delete Me {runId}-039`, Old Value `Delete Me {runId}-039`, New Value `-`
36. Tutup modal Changelog dengan `[✕]`
37. Buka Global Settings > User > User List (sub-tab Login User), klik icon Changelog, Search `Delete Me {runId}-039`, tekan Enter
38. Verifikasi Changelog: User menampilkan empty state "No results found" (tidak memuat entri dengan Field `Delete Me {runId}-039` untuk Rahmat Hidayat)
39. Tutup modal Changelog dengan `[✕]`
40. Buka Global Settings > User > Detail Sari Dewi > tab System Log, Search `Delete Me {runId}-039`, tekan Enter
41. Verifikasi System Log memuat entri Delete Object `Custom Field` dengan Name `Delete Me {runId}-039`
42. Verifikasi hasil Search System Log tidak memuat entri Object `User` dengan Field `Delete Me {runId}-039`
43. Buka Global Settings > Activity Log > tab `User Action`, Search `Delete Me {runId}-039`, tekan Enter
44. Verifikasi Activity Log tab `User Action` memuat entri Delete Object `Custom Field` dengan Name `Delete Me {runId}-039` dan Modified By `Sari D`
45. Verifikasi hasil Search Activity Log tab `User Action` tidak memuat entri Object `User` dengan Field `Delete Me {runId}-039`
46. Buka Global Settings > User > Custom Field

### TC-GS-UCF-139: Field Inactive dapat dihapus tanpa guard

47. Ketik Search `Delete Inactive {runId}-039`, tekan Enter
48. Klik `⋯` pada baris `Delete Inactive {runId}-039`, pilih `Delete`
49. Verifikasi dialog `Delete Custom Field` tampil
50. Klik `[Delete]`
51. Verifikasi muncul toast sukses: "Success, custom field has been deleted."
52. Verifikasi baris `Delete Inactive {runId}-039` hilang dari tabel

### TC-GS-UCF-137: Klik ganda [Delete] hanya memproses satu penghapusan

53. Tunggu toast dari langkah 51 hilang otomatis
54. Ketik Search `Delete Twice {runId}-039`, tekan Enter
55. Klik `⋯` pada baris `Delete Twice {runId}-039`, pilih `Delete`
56. Klik `[Delete]` dua kali cepat
57. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been deleted."
58. Klik icon Changelog, Search `Delete Twice {runId}-039`, tekan Enter
59. Verifikasi Changelog memuat tepat 1 entri Delete untuk `Delete Twice {runId}-039`
60. Tutup modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (60 langkah). Seluruhnya satu kelas (Delete single), satu dataset milik spec, tanpa kelas harness lain. Blok TC-GS-UCF-136, 134 dan 135, 139, dan 137 memakai Custom Field milik sendiri dan blok TC-GS-UCF-409 hanya membaca `Cost Center`, sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Sebagian besar langkah muncul dari TC-GS-UCF-135 yang memeriksa lima surface (Detail User, form Create User, dua Changelog, System Log, Activity Log) dengan satu `Verifikasi` per klausa.
- Urutan TC dalam spec: 409, 136, 134 dan 135 (dialog yang dibuka pada langkah 20 dipakai bersama TC-GS-UCF-134 dan langkah 1 sampai 2 TC-GS-UCF-135), 139, 137. Kasus yang menghapus data (135, 139, 137) berada sesudah semua kasus yang membutuhkan baris tetap ada (prinsip 5). Urutan menyimpang dari urutan TC sumber (134, 409, 135, 136, 137, 139).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 10, 19, 47, 54 (Search agar baris target tampil pada halaman aktif), langkah 9 (menutup input Search lewat `(←)`), langkah 18, 33, 36, 39, 46, 60 (kembali ke tab Custom Field atau menutup popup dan modal), dan langkah 53 (menunggu toast sukses lama hilang otomatis supaya hitungan toast pada langkah 57 hanya memuat toast hasil klik ganda).
- Asersi tambahan di luar Expected TC (S-03): langkah 27 (anchor pembanding `Employee Grade` untuk asersi absence di Detail User), langkah 31 (anchor pembanding `Cost Center` untuk asersi absence di form Create User), dan langkah 22 mengikuti Expected TC-GS-UCF-134 butir b. Langkah 38 memakai empty state "No results found" sebagai anchor absence Changelog: User; langkah 41 dan 44 menjadi anchor absence untuk langkah 42 dan 45 (baris pembanding Object `Custom Field` pada surface yang sama).
- Pembagian TC lintas spec: asersi "tidak ada entri log" bagian TC-GS-UCF-135 butir f, g, dan h (tidak ada entri Object `User` untuk Field `Delete Me`) tidak punya aksi nyata di spec absence (spec 070 tidak memuat aksi Delete untuk TC itu), sehingga ditulis sebagai `Verifikasi` berbaseline dengan anchor positif di spec ini (S-05, S-12). Nama bersuffix unik `{runId}-039` menjadi baseline nol.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-UCF-135 ("efek ke User, Non-Login User, My Profile, FA > Settings > User, AC > Settings > User, AC > Settings > Group popup Total User Detail, Import"; hanya Detail User, form Create User, Changelog, System Log, dan Activity Log yang punya Expected).
  - TC-GS-UCF-134, 135, 136, 137, dan 139 memakai nama field tanpa suffix (`Delete Me`, `Delete Keep`, `Delete Twice`, `Delete Inactive`); spec memakai versi bersuffix `{runId}-039` dan menyesuaikan Search serta bullet dialog.
  - Mekanisme seeding nilai Custom Field pada User (`Gone Soon`, `Stay`) dan akses ke Detail User tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE.
  - TC-GS-UCF-135 langkah 3 menyebut Detail Rahmat Hidayat tanpa cara mencari user; spec menulis "Buka ... Detail Rahmat Hidayat" sesuai TC.
  - TC-GS-UCF-409 menyebut Tab berulang tanpa jumlah penekanan; spec menulis "berulang melewati elemen terakhir dialog".
