---
id: TC-AC-ACHA-E2E-029-cancel-allocation
title: "Cancel Allocation: Menu Row Action, Dialog Konfirmasi, Pembatalan oleh Creator, Idempoten, dan Double-submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-220
  - TC-AC-ACHA-221
  - TC-AC-ACHA-222
  - TC-AC-ACHA-223
  - TC-AC-ACHA-224
  - TC-AC-ACHA-225
  - TC-AC-ACHA-226
  - TC-AC-ACHA-227
  - TC-AC-ACHA-233
  - TC-AC-ACHA-234
coverage:
  web: automated
---

# Cancel Allocation: Menu Row Action, Dialog Konfirmasi, Pembatalan oleh Creator, Idempoten, dan Double-submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Member Distributor toggle ON (MB_ON, Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, nama pengguna Budi Santoso (PIC pada Allocation Log = Budi Santoso), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun di tengah spec: Group Member Partner CV Karya Mandiri toggle ON (MB_P2, Pre-setup #47) `memberOnPartner2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P2_PASSWORD`; Group Member Principal toggle ON (MB_PRIN, Pre-setup #24) `memberOnPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_PRIN_PASSWORD`.
- Akun approver aktif (ganti akun pada langkah 37 dan 40): Total Control Distributor PT Global Distribusi TC_DIST (Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD`; MB_ON (pembuat) tidak melihat transaksinya sendiri di Approvals Active Tab (TC-AC-ACHA-263), sehingga absence TC-224 butir f diamati oleh TC_DIST.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor (dipakai juga sebagai pelaku pertama pada blok TC-AC-ACHA-233), flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, fixture API Pre-setup #20, dan pemulihan preferensi Setup Column di hook `after`.
- Data milik spec (dibuat lewat fixture seeding "disediakan tim FE/BE" di hook `before` dan di awal blok yang memerlukannya, dibersihkan di hook `after`; Allocation ID dibaca saat seeding sebagai Dynamic Reference dan dipakai sebagai kata kunci Search): transaksi Waiting for Approval dibuat MB_ON yang mereplikasi Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi saldo $20,000.00), satu transaksi per blok pembatalan: T-A (blok TC-AC-ACHA-220 s.d. 224), T-233, T-234, T-227; satu replika Pre-setup #50 untuk MB_P2 (T-226: NFC, Quantity 40, Client PT Cipta Kreasi, Pay From kantong A saldo $1,000.00 Reserved $60.00; kantong B saldo $3,000.00, Pre-setup #18 dan #19); satu replika Pre-setup #51 untuk MB_PRIN (T-225: Handheld Reader Long Range, Quantity 10, Client PT Manufaktur Unggul, Payment Free). Notes `Batch uji` literal karena diasersi TC (pengecualian S-12, Lampiran A butir A-6).
- Kemampuan teknis: (1) fixture API Pre-setup #20; (2) sesi API aktor MB_ON untuk membatalkan transaksi (TC-AC-ACHA-233, pelaku pertama), sehingga sesi UI tetap satu dan baris pada UI basi; (3) kemampuan membaca Reserved dan saldo kantong serta jumlah entri Allocation Log transaksi (disediakan tim FE/BE, tanpa endpoint karangan, S-13); (4) jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit); (5) Page Object Approvals untuk membaca Approvals > Device Allocation > Active Tab (modul lain).
- State global: tidak ada state global yang diubah; transaksi milik spec dibersihkan di hook `after`; suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_DA_MB_ON_PASSWORD`, `AC_DA_MB_P2_PASSWORD`, `AC_DA_MB_PRIN_PASSWORD`, `AC_DA_TC_DIST_PASSWORD` (satu nama satu arti).

## Test Steps

### TC-AC-ACHA-220: Urutan, ikon, dan severity row action pada transaksi Waiting for Approval

1. Ketik Search Allocation ID transaksi T-A, tekan Enter
2. Catat jumlah entri Allocation Log transaksi T-A sebagai baseline
3. Buka menu row action `⋯` pada transaksi Waiting for Approval milik sendiri
4. Verifikasi menu berurutan: `Allocation Log` (ikon `FileInfoLine`, dark), `Edit` (ikon `Edit2Line`, dark), `Cancel Allocation` (ikon `CloseLine`, danger); aksi dark mendahului aksi danger
5. Tutup menu dengan Esc

### TC-AC-ACHA-221: Screening dialog konfirmasi Cancel Allocation

6. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
7. Verifikasi header dialog: judul `Cancel Device Allocation Confirmation` dan ikon close `[×]`
8. Verifikasi body dialog: bullet `• [Allocation ID]` berisi Allocation ID transaksi (tanpa field input) lalu kalimat "Are you sure you want to cancel it?"
9. Verifikasi footer dialog: `[Go Back]` (text, contrast) dan `[Cancel Allocation]` (danger)

### TC-AC-ACHA-222: Go Back menutup dialog tanpa membatalkan

10. Klik `[Go Back]`
11. Verifikasi dialog tertutup
12. Verifikasi Status transaksi tetap `Waiting for Approval`
13. Verifikasi Wallet kantong PT Global Distribusi: Reserved tetap $250.00
14. Verifikasi tidak ada toast
15. Verifikasi jumlah entri Allocation Log transaksi sama dengan baseline pada langkah 2 (tidak ada entri log baru)

### TC-AC-ACHA-223: Backdrop no-op dan Esc setara Go Back pada dialog Cancel

16. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
17. Klik area backdrop
18. Verifikasi dialog tidak tertutup
19. Tekan Esc
20. Verifikasi dialog tertutup
21. Verifikasi Status transaksi tetap `Waiting for Approval` dan Reserved tetap $250.00 (tanpa mutasi)

### TC-AC-ACHA-224: Cancel manual oleh creator: Release, status Canceled, log

22. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
23. Klik `[Cancel Allocation]` pada dialog
24. Verifikasi toast sukses: "Success, device allocation has been canceled."
25. Catat waktu sesudah Cancel
26. Verifikasi Status transaksi menjadi `Canceled` (badge danger)
27. Verifikasi Last Updated berubah ke waktu Cancel (toleransi satu menit terhadap waktu pada langkah 25)
28. Verifikasi Wallet kantong PT Global Distribusi: Reserved menjadi $0.00 (Release)
29. Verifikasi Wallet kantong PT Global Distribusi: saldo $20,000.00 tidak berubah
30. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
31. Verifikasi jumlah entri bertambah satu dari baseline pada langkah 2 dan entri baru `Allocation canceled by [PIC]` tanpa Description
32. Tutup modal Allocation Log
33. Buka menu row action `⋯` transaksi itu
34. Verifikasi menu row action memuat `Allocation Log` dan `Resubmit`
35. Verifikasi `Edit` dan `Cancel Allocation` tidak ada di menu row action
36. Tutup menu dengan Esc
37. Ganti akun: Logout, login sebagai TC_DIST (approver aktif, Pre-setup #27), buka Approvals > Device Allocation > Active Tab
38. Ketik Search Allocation ID transaksi T-A, tekan Enter
39. Verifikasi empty state `No results found` (subject hilang dari Approvals Active Tab milik TC_DIST)
40. Ganti akun: Logout, login sebagai MB_ON (Pre-setup #32), buka Allocation > Device Allocation

### TC-AC-ACHA-233: Cancel yang diulang oleh creator yang sama bersifat idempoten

41. Siapkan transaksi T-233 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
42. Catat jumlah entri Allocation Log transaksi T-233 sebagai baseline
43. Lewat sesi API MB_ON, batalkan transaksi T-233 hingga status `Canceled` tersimpan
44. Pada baris yang basi di sesi UI, buka menu row action `⋯`, klik `Cancel Allocation`
45. Klik `[Cancel Allocation]` pada dialog
46. Verifikasi toast sukses yang sama dengan aksi pertama: "Success, device allocation has been canceled."
47. Verifikasi Status transaksi T-233 tetap `Canceled`
48. Verifikasi Wallet kantong PT Global Distribusi: Reserved tetap $0.00 (tidak ada Release baru)
49. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
50. Verifikasi jumlah entri bertambah tepat satu dari baseline pada langkah 42 dan hanya satu entri `Allocation canceled by [PIC]`
51. Tutup modal Allocation Log

### TC-AC-ACHA-234: Double-submit Cancel hanya memproses satu request

52. Siapkan transaksi T-234 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
53. Tunggu toast lama hilang otomatis
54. Catat jumlah entri Allocation Log transaksi T-234 sebagai baseline
55. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
56. Klik `[Cancel Allocation]` dua kali cepat pada dialog
57. Verifikasi hanya satu toast sukses: "Success, device allocation has been canceled."
58. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
59. Verifikasi jumlah entri bertambah tepat satu dari baseline pada langkah 54 dan hanya satu entri `Allocation canceled by [PIC]`
60. Tutup modal Allocation Log
61. Verifikasi Wallet kantong PT Global Distribusi: Reserved $0.00 (Release dilakukan satu kali)

### TC-AC-ACHA-227: Cancel setelah Edit commit melepas Reserve hasil Edit

62. Siapkan transaksi T-227 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
63. Buka menu row action `⋯` transaksi itu, klik `Edit`
64. Ubah Quantity menjadi `150`
65. Klik `[Save]`
66. Tunggu form Edit tertutup
67. Verifikasi Wallet kantong PT Global Distribusi: Reserved $375.00 (hasil Edit)
68. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
69. Klik `[Cancel Allocation]` pada dialog
70. Verifikasi toast sukses karena status masih `Waiting for Approval`: "Success, device allocation has been canceled."
71. Verifikasi Wallet kantong PT Global Distribusi: Reserved $375.00 dilepas penuh menjadi $0.00

### TC-AC-ACHA-226: Cancel transaksi Partner dua kantong melepas Reserve kantong terpilih

72. Ganti akun: Logout, login sebagai MB_P2 (Pre-setup #47), buka Allocation > Device Allocation
73. Ketik Search Allocation ID transaksi T-226, tekan Enter
74. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
75. Klik `[Cancel Allocation]` pada dialog
76. Verifikasi toast sukses: "Success, device allocation has been canceled."
77. Verifikasi Wallet kantong A: Reserved menjadi $0.00
78. Verifikasi Wallet kantong B: saldo $3,000.00 tidak berubah

### TC-AC-ACHA-225: Cancel transaksi Principal tanpa wallet

79. Ganti akun: Logout, login sebagai MB_PRIN (Pre-setup #24), buka Allocation > Device Allocation
80. Ketik Search Allocation ID transaksi T-225, tekan Enter
81. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
82. Klik `[Cancel Allocation]` pada dialog
83. Verifikasi toast sukses: "Success, device allocation has been canceled."
84. Verifikasi Status transaksi menjadi `Canceled`

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan TC (S-05, S-10): blok tanpa perubahan data (TC-AC-ACHA-220 s.d. 223) lebih dulu, lalu blok pembatalan MB_ON (TC-AC-ACHA-224, 233, 234, 227; semuanya aksi yang menghabiskan transaksi, masing-masing dengan transaksi sendiri), lalu blok ganti akun TC-AC-ACHA-226 (MB_P2) dan TC-AC-ACHA-225 (MB_PRIN) agar tiap ganti akun satu kali. TC-AC-ACHA-221 dan TC-AC-ACHA-222 berbagi satu pembukaan dialog: langkah 10 melanjutkan dialog yang dibuka pada langkah 6 (prinsip 8).
- TC-AC-ACHA-233 dijalankan dengan satu sesi UI dan satu sesi API (pelaku pertama MB_ON): sesi API aktor bukan konteks kedua (tidak memakai `P-2` dan bukan kelas c); hasil yang diasersi hanya di sesi UI. Karena sesi API tidak menampilkan toast, toast sukses pembatalan pertama pada TC tidak diasersi (hanya toast pengulangan di langkah 46).
- Langkah penghubung (S-03, R-16): langkah 1 (Search Allocation ID untuk menemukan baris target; juga langkah 41, 52, 62, 73, 80); langkah 2, 42, 54 (baseline jumlah entri Allocation Log, S-12); langkah 5 dan 36 (menutup menu); langkah 25 (waktu pembanding Last Updated); langkah 32, 51, 60 (menutup modal Allocation Log); langkah 37 dan 40 (ganti akun ke TC_DIST dan kembali ke MB_ON, S-07); langkah 41, 52, 62 (membuat transaksi baru dan muat ulang); langkah 43 (pelaku pertama lewat sesi API hingga tersimpan); langkah 53 (menunggu toast lama hilang, R-12); langkah 66 (menunggu form tertutup); langkah 72 dan 79 (ganti akun).
- P-1 (state berat): asersi "tidak ada entri log baru" pada langkah 15 memakai baseline (S-12) di spec ini karena aksi `[Go Back]` hanya bermakna sesudah dialog dibuka pada transaksi yang sama; tidak ada spec absence yang memuat aksi nyata untuk TC-AC-ACHA-222.
- Spec ini melewati sekitar 35 langkah. Alasan: seluruhnya satu topik (aksi Cancel Allocation), tiap blok pembatalan memakai transaksi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan `Verifikasi` dipecah per klausa (S-01).
- Pengecualian S-12: Notes `Batch uji` dan nama entitas Pre-setup bernilai literal karena diasersi TC (Lampiran A butir A-6).
- Temuan untuk QA:
  - TC-AC-ACHA-224 Post Condition ("Tidak ada kuota yang ditambahkan; notifikasi dikirim ke approver aktif"), TC-AC-ACHA-225, 226, 227, 234 Post Condition (Wallet Transaction List, Dashboard widget `Pending Device Allocation`, notifikasi in-app ke approver aktif): tanpa langkah observasi di TC, tidak diasersi.
  - TC-AC-ACHA-225 menyatakan "tidak ada Release karena Principal tanpa wallet" tanpa cara observasi (Principal tanpa wallet); spec hanya mengasersi toast dan Status `Canceled`.
  - TC-AC-ACHA-233 butir b menyatakan "tidak ada entri log, notifikasi, atau Release baru"; notifikasi tidak punya langkah observasi sehingga tidak diasersi, sedangkan entri log dan Release diasersi sebagai jumlah (satu entri `Allocation canceled by [PIC]`, Reserved $0.00).
  - TC-AC-ACHA-233 langkah 1 menyebut "sesi pertama dan sesi kedua (akun yang sama)"; spec memakai satu sesi UI dan satu sesi API (aturan pelaku kedua). Jika QA menghendaki dua sesi UI sebagai objek asersi, TC itu masuk spec multi-konteks (kelas c).
  - TC-AC-ACHA-224 butir f ("Subject hilang dari Approvals Active Tab milik TC_DIST") diamati oleh TC_DIST (approver aktif, langkah 4 TC) lewat ganti akun, bukan oleh pembuat MB_ON yang memang tidak melihat transaksinya sendiri di tab itu (TC-AC-ACHA-263); TC tidak menyatakan cara mencari, sehingga spec memakai Search Allocation ID dan empty state `No results found`. Spec tidak punya langkah yang membuktikan subject sempat tampil di Active Tab TC_DIST sebelum Cancel, sehingga empty state adalah satu-satunya anchor.
  - Kontrak fixture (seeding transaksi milik spec, baca Reserved dan saldo kantong, baca jumlah entri Allocation Log) tidak tertulis di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (R-19, S-13).
