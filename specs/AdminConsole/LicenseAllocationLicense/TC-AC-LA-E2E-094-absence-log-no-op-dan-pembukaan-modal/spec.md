---

id: TC-AC-LA-E2E-094-absence-log-no-op-dan-pembukaan-modal

title: "Absence Log: Pembukaan Modal, Request Langsung Ditolak, Edit Tanpa Perubahan, Cancel Ulang, dan Aksi Tulis Gagal"

priority: Critical

caseType: Edge

status: draft

sourceTc:

  - TC-AC-LA-413

  - TC-AC-LA-198

  - TC-AC-LA-226

  - TC-AC-LA-419

  - TC-AC-LA-482

  - TC-AC-LA-479

  - TC-AC-LA-471

coverage:

  web: automated

---



# Absence Log: Pembukaan Modal, Request Langsung Ditolak, Edit Tanpa Perubahan, Cancel Ulang, dan Aksi Tulis Gagal



## Prerequisites



- Mode: FE+BE.

- Akun aktor pertama: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

- Akun ganti akun (langkah eksplisit): Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`.

- Akun yang hanya dipakai lewat sesi API sebagai pemicu (login API tidak dihitung sebagai sesi web, `suite.md`): Create+Read dan Additional Approver `createApproverLic_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`, Pre-setup #56), password `Spectra.env.AC_LA_CREATE_APPROVER_PASSWORD`; Group Manager + Manage allocation `gmAllocLic_automated_{namaCompany}@qwertysystem.net` (`Hadi Setiawan`, Pre-setup #9), password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`.

- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.

- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.

- Data Pre-setup (hanya dibaca): alokasi dengan riwayat log lengkap (#55) untuk TC-AC-LA-413, PT Sejahtera (#19), hierarki group Region Jawa (#32) tempat `Hadi Setiawan` di-assign (PT Sejahtera di luar Region Jawa), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38). Blok TC-AC-LA-471 memerlukan toggle OFF (#39), diatur fixture backend yang disediakan tim FE/BE di langkah penghubung 86 dan dipulihkan ke ON di hook `after`.

- Data Dinamis (seeding lewat API di hook `before`, milik spec ini; baseline log nol karena seed baru, S-12). Bentuk #41: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve), satu tiap untuk TC-AC-LA-198, TC-AC-LA-226 (dibatalkan oleh `Dewi A` lewat sesi API sebelum Cancel kedua), TC-AC-LA-419, dan TC-AC-LA-479. Bentuk #65: alokasi `Waiting for Approval` Concurrent User +2 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Eko S` (Cost $60.00 di-Reserve) untuk TC-AC-LA-482. Allocation ID dibaca dari hasil seeding.

- Pelaku kedua dan pemicu lewat sesi API: `Dewi Anggraini` untuk Cancel pertama pada TC-AC-LA-226; `Eko Saputra` untuk request Reject langsung pada TC-AC-LA-482; `Hadi Setiawan` untuk request Approve langsung pada TC-AC-LA-479. Request langsung memakai klien HTTP atau fixture BE yang disediakan tim FE/BE (tanpa mengarang endpoint, S-13).

- Jendela absence notifikasi in-app: pilihan spec (bukan nilai TC atau PRD), "Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi absence notifikasi (konvensi bagian 6); anchor positif notifikasi memakai notifikasi `Dewi Anggraini` yang sudah tercatat pada baseline.

- Kemampuan teknis (disediakan tim FE/BE): intercept respons 500 pada Cancel dan submit Allocate; membaca jumlah entri Changelog, Activity Log, System Log, Allocation Log, jumlah notifikasi, dan saldo Wallet sebagai baseline.

- State global yang diubah: toggle Require Approval for Allocation (blok TC-AC-LA-471), dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).



## Test Steps



### TC-AC-LA-413: Pembukaan modal dan penyalinan Allocation ID tidak dicatat ke log



1. Catat jumlah entri Allocation Log, Changelog, dan Activity Log alokasi dengan riwayat lengkap (#55) sebagai baseline

2. Klik row action `Allocation Log` pada alokasi itu

3. Verifikasi modal Allocation Log tampil dengan entri riwayat (anchor)

4. Klik ikon Copy Allocation ID

5. Tutup modal Allocation Log

6. Buka Changelog, lalu bandingkan jumlah entri dengan baseline

7. Tutup modal Changelog

8. Buka Activity Log, lalu bandingkan jumlah entri dengan baseline

9. Verifikasi jumlah entri ketiga surface tidak berubah

10. Buka Allocation > License Allocation (tab Current)



### TC-AC-LA-482: Self-Reject lewat request langsung tidak mencatat entri Allocation rejected



11. Ketik Search Allocation ID seed 482 di tab Current, tekan Enter

12. Catat jumlah entri Allocation Log seed 482 sebagai baseline

13. Kirim request Reject langsung untuk alokasi seed 482 lewat sesi API `Eko Saputra` dengan Rejection Reason `Tidak sesuai`

14. Tunggu aksi selesai

15. Klik row action `Allocation Log` pada baris seed 482

16. Verifikasi entri `Allocation created by Eko S` seed 482 tampil (anchor)

17. Verifikasi tidak ada entri `Allocation rejected` pada Allocation Log seed 482

18. Verifikasi jumlah entri Allocation Log seed 482 sama dengan baseline

19. Tutup modal Allocation Log



### TC-AC-LA-479: Approve oleh Group Manager di luar scope tidak mencatat entri Allocation approved



20. Ganti isi kotak search dengan Allocation ID seed 479, tekan Enter

21. Catat jumlah entri Allocation Log seed 479 sebagai baseline

22. Kirim request Approve langsung untuk alokasi seed 479 lewat sesi API `Hadi Setiawan`

23. Tunggu aksi selesai

24. Klik row action `Allocation Log` pada baris seed 479

25. Verifikasi entri `Allocation created by Dewi A` seed 479 tampil (anchor)

26. Verifikasi tidak ada entri `Allocation approved` pada Allocation Log seed 479

27. Verifikasi jumlah entri Allocation Log seed 479 sama dengan baseline

28. Tutup modal Allocation Log



### TC-AC-LA-198: Edit tanpa perubahan lewat request langsung diproses sebagai no-op



29. Ganti akun: logout `Hendra W`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`

30. Catat jumlah entri Changelog, Activity Log, System Log, dan Allocation Log seed 198 serta nilai Last Updated seed 198 sebagai baseline

31. Kirim request Edit langsung dengan nilai identik dengan record seed 198

32. Verifikasi respons berhasil sebagai no-op dengan pesan netral "No changes to save." (T-05)

33. Buka Allocation > License Allocation (tab Current), ketik Search Allocation ID seed 198, tekan Enter

34. Verifikasi Last Updated seed 198 tidak berubah

35. Buka Allocation Log seed 198

36. Verifikasi entri `Allocation created by Dewi A` seed 198 tampil (anchor)

37. Verifikasi jumlah entri Allocation Log seed 198 sama dengan baseline

38. Tutup modal Allocation Log

39. Buka Changelog, lalu bandingkan jumlah entri seed 198 dengan baseline
40. Verifikasi jumlah entri Changelog seed 198 sama dengan baseline
41. Tutup modal Changelog
42. Buka Activity Log, lalu bandingkan jumlah entri seed 198 dengan baseline
43. Verifikasi jumlah entri Activity Log seed 198 sama dengan baseline
44. Buka System Log, lalu bandingkan jumlah entri seed 198 dengan baseline
45. Verifikasi jumlah entri System Log seed 198 sama dengan baseline




### TC-AC-LA-226: Cancel ulang oleh requester yang sama adalah no-op dengan toast sukses




46. Buka Allocation > License Allocation, klik tab `Current`

47. Ketik Search Allocation ID seed 226 di tab Current, tekan Enter (List memuat baris)

48. Pelaku kedua (sesi API `Dewi Anggraini`) membatalkan alokasi seed 226 hingga tersimpan

49. Tunggu aksi selesai

50. Catat jumlah entri log seed 226, jumlah notifikasi, dan saldo Wallet sebagai baseline (sesudah Cancel pertama)

51. Klik row action `Cancel Allocation` pada baris seed 226

52. Klik `[Cancel Request]`

53. Verifikasi toast "Success, license allocation has been canceled."

54. Verifikasi status seed 226 tetap `Canceled`

55. Buka Allocation Log seed 226

56. Verifikasi entri `Allocation canceled by Dewi A` seed 226 tampil (anchor)

57. Verifikasi tidak ada entri log baru pada Allocation Log seed 226 dibanding baseline

58. Tutup modal Allocation Log

59. Buka notifikasi `Dewi Anggraini`

60. Tunggu 5 detik tanpa memuat ulang halaman

61. Verifikasi notifikasi `Dewi Anggraini` yang tercatat pada baseline tampil di daftar (anchor)

62. Verifikasi tidak ada notifikasi baru dibanding baseline

63. Buka Wallet

64. Verifikasi entri Reserve alokasi seed 226 tampil (anchor)

65. Verifikasi tidak ada Release baru dibanding baseline

66. Buka Allocation > License Allocation, klik tab `Current`



### TC-AC-LA-419: Cancel gagal 5xx tidak mencatat entri log baru



67. Ketik Search Allocation ID seed 419, tekan Enter

68. Catat jumlah entri Changelog, Activity Log, System Log, dan Allocation Log seed 419 sebagai baseline

69. Pasang intercept Cancel: respons 500

70. Klik row action `Cancel Allocation` pada baris seed 419

71. Klik `[Cancel Request]`

72. Tunggu aksi selesai

73. Lepas intercept Cancel

74. Verifikasi status seed 419 tetap `Waiting for Approval`

75. Buka Allocation Log seed 419

76. Verifikasi entri `Allocation created by Dewi A` seed 419 tampil (anchor)

77. Verifikasi jumlah entri Allocation Log seed 419 sama dengan baseline

78. Tutup modal Allocation Log

79. Buka Changelog, lalu bandingkan jumlah entri seed 419 dengan baseline
80. Verifikasi jumlah entri Changelog seed 419 sama dengan baseline
81. Tutup modal Changelog
82. Buka Activity Log, lalu bandingkan jumlah entri seed 419 dengan baseline
83. Verifikasi jumlah entri Activity Log seed 419 sama dengan baseline
84. Buka System Log, lalu bandingkan jumlah entri seed 419 dengan baseline
85. Verifikasi jumlah entri System Log seed 419 sama dengan baseline




### TC-AC-LA-471: Allocate gagal 5xx tidak mencatat entri log




86. Atur toggle Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend hingga tersimpan

87. Catat jumlah entri Changelog, Activity Log, dan System Log sebagai baseline

88. Buka Allocation > License Allocation (tab Current)

89. Klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `2`

90. Pasang intercept submit Allocate: respons 500

91. Klik `[Submit]`

92. Tunggu aksi selesai

93. Lepas intercept submit Allocate

94. Verifikasi form tetap terbuka dengan input dipertahankan (anchor: respons 500 sudah diproses)

95. Klik `[×]`

96. Verifikasi dialog `Unsaved Changes`

97. Klik `[Leave]`

98. Buka Changelog, lalu bandingkan jumlah entri dengan baseline
99. Verifikasi jumlah entri Changelog sama dengan baseline
100. Tutup modal Changelog
101. Buka Activity Log, lalu bandingkan jumlah entri dengan baseline
102. Verifikasi jumlah entri Activity Log sama dengan baseline
103. Buka System Log, lalu bandingkan jumlah entri dengan baseline
104. Verifikasi jumlah entri System Log sama dengan baseline




## Notes



- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.

- K-1: TC kelas a yang Expected-nya respons API (TC-AC-LA-198) tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; modul ini tidak punya TC backend.

- P-5 butir a: spec absence (kelas g) memuat pemicu kelas lain bila hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji: request langsung (TC-AC-LA-482, 479, 198, kelas a), Cancel ulang setelah pelaku kedua (TC-AC-LA-226, kelas c), dan respons 500 yang dipaksa (TC-AC-LA-419 dan 471, kelas b); tiap TC punya seed dan baseline sendiri. TC-AC-LA-419 seluruhnya ada di spec ini (status di langkah 74).

- Pembagian TC lintas spec: butir absence log TC-AC-LA-482 c dan TC-AC-LA-479 c dan klausa log TC-AC-LA-471 c ada di spec ini (langkah 11 sampai 28 dan 86 sampai 104); butir lain TC-AC-LA-482 dan 253, 254, 460 ada di spec 092, TC-AC-LA-479 dan 453, 454 di spec 095, TC-AC-LA-471 a dan b di spec 086.

- Langkah penghubung (S-03): langkah 8 (membuka Activity Log sesudah modal Changelog ditutup pada langkah 7, S-09), langkah 46 dan 66 (membuka List dan klik tab `Current` tanpa `✕`; Search baru diketik pada langkah 47 dan 67; spec tidak mengandalkan sisa isi kotak Search, S-14), langkah 1, 12, 21, 30, 50, 68, 87 (baseline S-12), 6, 35, 39, 55, 59, 63, 75, 79, 98 (membuka surface), 60 (jendela 5 detik sebelum absence notifikasi, bagian 6), 7 (menutup modal Changelog sebelum pindah surface, S-09), 5, 19, 28, 38, 58, 78 (menutup modal Allocation Log sebelum langkah berikutnya, S-09; langkah 5 menutup modal sesudah Copy Allocation ID), 10, 33, 66, 88 (membuka ulang Allocation > License Allocation tab Current sesudah pindah surface Changelog, Activity Log, Wallet; langkah 33 sekaligus Search seed 198), 29 (ganti akun), 11, 20, 47, 67 (Search untuk menemukan baris target, R-16), 14, 23, 49, 72, 92 (menunggu aksi selesai karena berganti sesi atau aksi tanpa asersi, 8b butir 8), 69, 73, 90, 93 (memasang dan melepas intercept, S-09), 86 (mengatur toggle), 95 sampai 97 (menutup form dirty `[×]`, S-08). Langkah 41, 81, dan 100 menutup modal Changelog sebelum membuka Activity Log pada tiap blok (S-09); langkah 42, 44, 82, 84, 101, dan 103 membuka Activity Log atau System Log. Langkah 94 bukan penghubung: anchor bahwa respons 500 sudah diproses sebelum form ditutup.

- Alasan di atas sekitar 35 langkah (104 langkah; pembukaan ulang List, penutupan modal Log, dan pemisahan surface Allocation Log dari Changelog, Activity Log, System Log, notifikasi, serta Wallet menambah 11 langkah penghubung, ditambah 8 langkah untuk penutupan modal Changelog, jendela 5 detik notifikasi, serta anchor notifikasi dan Wallet, dan 13 langkah untuk pemisahan Changelog, Activity Log, dan System Log per surface pada tiga blok): seluruh blok satu kelas harness (asersi absence log, kelas g) dan satu pola alur (baseline, pemicu, anchor, absence); tiap blok berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah yang berulang adalah baseline, pemicu, dan pembukaan surface log (blok baca-log berpola).

- Langkah 50 mencatat baseline sesudah Cancel pertama (langkah 48), sehingga entri `Allocation canceled by Dewi A` dari Cancel pertama sudah termasuk baseline dan langkah 57 dan 62 hanya mengasersi tidak ada penambahan dari Cancel kedua.

- Asersi absence (langkah 9, 17, 26, 34, 37, 40, 43, 45, 57, 62, 65, 77, 80, 83, 85, 99, 102, 104) berbaseline dan beranchor entri positif pada surface yang sama (langkah 3, 16, 25, 36, 56, 61, 64, 76) atau, untuk pemicu yang tidak menyentuh entitas anchor (Verifikasi per surface pada langkah 40, 43, 45, 80, 83, 85, 99, 102, dan 104), memakai jumlah total sebelum dan sesudah (8b butir 2); langkah 34 berbaseline Last Updated langkah 30 pada baris yang dimuat lewat Search seed 198. Asersi request langsung hanya state data dan log (8b butir 1); respons server ditolak diasersi di spec 092 dan 095.

- Temuan untuk QA:

  - Penutup form dirty ditulis `[×]` sesuai S-08 (keputusan 2026-11-02); TC-AC-LA-177 dan PRD §4.4 menulis `[✕]`, spec mengikuti konvensi.

  - Anchor notifikasi (langkah 61) mengandaikan `Dewi Anggraini` sudah punya notifikasi pada baseline; TC-AC-LA-226 tidak menyebut notifikasi seed, sehingga seeding perlu menjamin satu notifikasi.

  - TC-AC-LA-413 Langkah 1 menyebut "Catat jumlah entri" ketiga surface tanpa menyebut surface mana yang dibuka untuk membandingkan; spec membuka Changelog dan Activity Log serta memakai Allocation Log yang terbuka.

  - TC-AC-LA-198 Langkah 1 tidak menyebut akun, endpoint, dan format request; request disediakan tim FE/BE.

  - TC-AC-LA-198 Expected b ("Last Updated tidak berubah") tidak menyebut surface Last Updated; spec memakai kolom Last Updated tabel List.

  - TC-AC-LA-226 Langkah 1 ("Di sesi lain Cancel alokasi") tidak menyebut sesi dan akun pelaku; spec memakai sesi API `Dewi Anggraini` yang sama dengan requester.

  - TC-AC-LA-226 Expected b ("notifikasi baru") tidak menyebut akun yang notifikasinya diperiksa; spec memakai notifikasi `Dewi Anggraini`.

  - TC-AC-LA-482 c dan TC-AC-LA-479 c tidak menyebut akun pengamat Allocation Log; spec memakai Total Control Principal `Hendra Wijaya` (Pre-setup #1) yang membaca seluruh alokasi, dan pemicu request langsung memakai sesi API akun masing-masing.

  - TC-AC-LA-419 tidak menyebut endpoint yang di-intercept dan tidak menyebut toast hasil 500 sebagai bagian Expected; endpoint disediakan tim FE (S-13) dan toast hasil 500 tidak diasersi pada langkah 71 dan 72.

  - TC-AC-LA-419 Langkah 2 menyebut Allocation Log tetapi tidak menyebut cara membuka tiap surface; spec membuka Allocation Log lewat row action dan Changelog, Activity Log, System Log lewat penelusuran yang sama dengan TC-AC-LA-413.

  - TC-AC-LA-471 c ("tidak ada log") tidak menyebut surface; spec memakai Changelog, Activity Log, dan System Log (Allocation Log tidak ada karena tidak ada record). Cara observasi log disediakan tim FE/BE.

  - TC-AC-LA-482 dan 479 menyebut "respons error generik" atau penolakan tanpa status HTTP; spec tidak mengasersi respons di sini (diasersi di spec 092 dan 095).

