---
id: TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search
title: "Tab User Log Detail: Screening, Device Tidak Terparse, Search, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-409
  - TC-GS-USER-411
  - TC-GS-USER-412
  - TC-GS-USER-631
  - TC-GS-USER-632
  - TC-GS-USER-633
  - TC-GS-USER-634
  - TC-GS-USER-635
  - TC-GS-USER-636
  - TC-GS-USER-637
coverage:
  web: automated
---

# Tab User Log Detail: Screening, Device Tidak Terparse, Search, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`, `USER_PASSWORD_NEW` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). TC memakai `John Doe` (Pre-setup No. 18) sebagai pemilik log, sedangkan isi User Log-nya bergantung pada riwayat login lingkungan dan tidak boleh diubah; spec memakai user seed milik spec (S-06, S-11). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before`. Tiap user diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `John Doe {runId}-102`, email `johndoe+{runId}-102@qwertysystem.net`, status Activated, password `Spectra.env.USER_PASSWORD`. Pemilik User Log yang diuji (pengganti `John Doe` di TC).
  - U-2: Name `Lukman Hakim {runId}-102`, email `lukmanhakim+{runId}-102@qwertysystem.net`, dibuat lewat API dan tidak pernah login atau diubah sesudah dibuat (User Log kosong; TC-GS-USER-411).
  - Riwayat event U-1 (7 event, dipicu berurutan di hook `before`; sedikitnya dua nilai distinct pada tiap kolom yang di-search, S-11):
    - Event 1 (terlama): Activity `Login`, Status `Failed`, Note `Invalid password`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password salah sembarang yang disediakan tim FE/BE).
    - Event 2: Activity `Login`, Status `Success`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 3: Activity `Change Password`, Status `Success`, Note `Password changed`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password diganti dari `Spectra.env.USER_PASSWORD` menjadi `Spectra.env.USER_PASSWORD_NEW`; login berikutnya memakai password baru).
    - Event 4: Activity `Logout`, Status `—`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 5: Activity `Login`, Status `Success`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 6: Activity `Logout`, Status `—`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 7 (terbaru): Activity `Login`, Status `Success`, Note `—`, IP Address `172.16.9.3`, Device / Browser `—` (User-Agent tidak dikenal, tidak terparse).
  - Hasil pada tabel: Activity memuat `Login` (4 baris), `Logout` (2), dan `Change Password` (1); Status memuat `Success` (4), `Failed` (1), dan `—` (2); Note memuat `Invalid password` (1), `Password changed` (1), dan `—` (5); IP Address memuat `192.168.5.7` (4), `10.0.0.11` (2), dan `172.16.9.3` (1); Device / Browser memuat `Firefox on macOS` (4), `Chrome on Windows` (2), dan `—` (1). Tabel memuat 7 baris pada halaman 1.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1 dan U-2, serta sisa user bersuffix `-102` dari run lama. Entri User Log tidak bisa dihapus.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanisme maupun endpoint): (a) seeding user berstatus Activated lewat API dengan password `Spectra.env.USER_PASSWORD`; (b) memicu event Login (Success dan Failed), Logout, dan Change Password (Success) untuk user uji dengan IP Address dan User-Agent tertentu, berurutan dengan jeda sedikitnya satu detik antar-event supaya cap waktu tiap event berbeda. Event dipicu berurutan sesuai daftar dan bercap waktu hari uji.
- Kemampuan teknis lain: mengetik di kotak Search; menyalin teks sel kolom Date; mengamati fokus kursor input; menyetel visibilitas kolom lewat Overlay Column Visibility.
- State global yang diubah dan dipulihkan: visibilitas kolom `Device / Browser` pada tabel User Log (di-hide lalu dicentang kembali pada langkah 58); hook `before` mengosongkan preferensi Setup Column tab User Log (tempat penyimpanan preferensi tidak disebut TC User; disediakan tim FE) dan hook `after` memulihkannya sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-409, 411, 412, 631 sampai 637: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-409: Screening Tab User Log di User Detail

1. Klik icon Search di User List, ketik `John Doe {runId}-102`, tekan Enter
2. Klik Name `John Doe {runId}-102`
3. Klik Tab `User Log`
4. Verifikasi tabel memuat 7 baris (7 event seed)
5. Verifikasi Toolbar `Search | Filter | Download`
6. Verifikasi kolom tabel berurutan `Date | Activity | Status | Note | IP Address | Device / Browser | Column Visibility (⋯)`
7. Verifikasi kolom `Date` berurutan Newest First secara default (baris pertama IP Address `172.16.9.3`, baris terakhir Status `Failed`)
8. Verifikasi tidak ada row action pada baris mana pun
9. Verifikasi Pagination default 10 baris per halaman

### TC-GS-USER-412: Device / Browser tidak terparse tampil `—`

10. Verifikasi sel Device / Browser baris IP Address `172.16.9.3` bernilai `—`
11. Verifikasi enam baris lain berformat `[Browser] on [OS]`: `Chrome on Windows` (2 baris) dan `Firefox on macOS` (4 baris)

### TC-GS-USER-631: Siklus Search: reveal, Enter, clear ×, collapse ←

12. Klik icon Search
13. Verifikasi Search bar melebar
14. Verifikasi kursor auto-focus di input Search
15. Ketik `Logout` pada kotak Search
16. Verifikasi icon `×` muncul di dalam input
17. Verifikasi tabel belum tersaring (tetap 7 baris)
18. Tekan Enter
19. Verifikasi tabel tersaring: 2 baris, Activity `Logout`
20. Klik icon `×`
21. Verifikasi input Search kosong
22. Verifikasi tabel tetap menampilkan hasil search terakhir (2 baris Activity `Logout`)
23. Tekan Enter pada input kosong
24. Verifikasi tabel kembali menampilkan semua data (7 baris)
25. Isi Search dengan `Logout`, tekan Enter
26. Klik icon `←`
27. Verifikasi Search bar collapse menjadi icon Search biasa
28. Verifikasi tabel langsung kembali menampilkan semua data (7 baris) tanpa menekan Enter
29. Klik icon Search
30. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-632: Query Search di-trim dan tidak case-sensitive

31. Isi Search dengan `  LOGIN  ` (dua spasi di awal dan akhir), tekan Enter
32. Verifikasi tabel menampilkan 4 baris Activity `Login` (spasi di awal dan akhir diabaikan, huruf besar/kecil tidak dibedakan)
33. Verifikasi isi search box tetap `  LOGIN  ` seperti yang diketik

### TC-GS-USER-633: Search menemukan substring pada kolom kelas teks

34. Ganti isi kotak search dengan `ogou`, tekan Enter
35. Verifikasi Activity: 2 baris dengan Activity `Logout` (memuat `ogou`) tampil
36. Ganti isi kotak search dengan `ucces`, tekan Enter
37. Verifikasi Status: 4 baris dengan Status `Success` (memuat `ucces`) tampil
38. Ganti isi kotak search dengan `Invalid`, tekan Enter
39. Verifikasi Note: 1 baris dengan Note `Invalid password` (memuat `Invalid`) tampil
40. Ganti isi kotak search dengan `Firefox`, tekan Enter
41. Verifikasi Device / Browser: 4 baris dengan Device / Browser `Firefox on macOS` (memuat `Firefox`) tampil

### TC-GS-USER-634: Search menemukan substring pada kolom kelas IP

42. Ganti isi kotak search dengan `10.0`, tekan Enter
43. Verifikasi IP Address: 2 baris dengan IP Address `10.0.0.11` (memuat `10.0`) tampil

### TC-GS-USER-635: Kolom non-searchable tidak tercakup Search

44. Klik icon `×`
45. Tekan Enter pada input kosong
46. Verifikasi tabel menampilkan 7 baris (data pembanding sebelum Search tanggal)
47. Salin teks tanggal pada sel Date baris pertama (format yang tampil di kolom itu)
48. Isi Search dengan teks tanggal yang disalin, tekan Enter
49. Verifikasi tabel menampilkan pesan `No results found` (kolom Date tidak tercakup Search)

### TC-GS-USER-636: Search tidak mencocokkan kolom hidden, cocok kembali setelah unhide

50. Klik icon `×`
51. Tekan Enter pada input kosong
52. Klik header Column Visibility (⋯)
53. Hilangkan centang kolom `Device / Browser`
54. Verifikasi kolom `Device / Browser` tidak tampil di tabel, tabel tetap memuat 7 baris
55. Isi Search dengan `Firefox`, tekan Enter
56. Verifikasi tabel menampilkan pesan `No results found` (kolom `Device / Browser` hidden tidak dicari)
57. Klik header Column Visibility (⋯)
58. Centang kembali kolom `Device / Browser`
59. Tekan Enter pada input Search yang masih berisi `Firefox`
60. Verifikasi 4 baris dengan Device / Browser `Firefox on macOS` kembali cocok (tampil)

### TC-GS-USER-637: Empty filtered state

61. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
62. Verifikasi ilustrasi empty filtered state tampil
63. Verifikasi teks `No results found`
64. Verifikasi teks `Try adjusting your search or filter.`
65. Klik icon `←`

### TC-GS-USER-411: Empty state Tab User Log

66. Klik menu User di sidebar Global Settings
67. Klik icon Search di User List, ketik `Lukman Hakim {runId}-102`, tekan Enter
68. Klik Name `Lukman Hakim {runId}-102`
69. Klik Tab `User Log`
70. Verifikasi ilustrasi empty state tampil
71. Verifikasi teks `No activity yet`
72. Verifikasi teks `Login and session activity will appear here.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18) dan `Lukman Hakim` tanpa suffix. Isi User Log `John Doe` Pre-setup bergantung pada riwayat login lingkungan, sehingga spec memakai user milik spec dengan riwayat event yang diketahui (S-06, S-11) dan nama bersuffix per run (S-12).
- Urutan TC dalam spec: TC-GS-USER-409, 412, 631, 632, 633, 634, 635, 636, 637, lalu 411. TC-GS-USER-411 membuka user lain (Lukman Hakim) sehingga ditaruh terakhir dan memakai satu pembukaan ulang (langkah 66), menghindari dua kali navigasi bolak-balik. Urutan `sourceTc`: 409, 411, 412, 631 sampai 637. TC-GS-USER-412 diasersi tepat sesudah TC-GS-USER-409 karena memakai layar yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik), langkah 44 sampai 45 dan 50 sampai 51 (mengosongkan Search sebelum Search tanggal dan sebelum hide kolom), langkah 52 sampai 58 (hide dan unhide `Device / Browser` bagian TC-GS-USER-636), langkah 65 (menutup Search), dan langkah 66 (memuat ulang User List lewat menu User tanpa Search, agar Search user lain dimulai dari tabel segar). Langkah 29 sampai 30 (membuka Search kembali dan memastikan kosong) adalah observasi untuk Expected f "keyword kosong" pada TC-GS-USER-631 (S-14).
- Asersi tambahan (dicatat sesuai S-03): langkah 4 (tabel memuat 7 baris) dan pencantuman jumlah baris pada Expected Search adalah konkretisasi untuk data seed yang diketahui; langkah sesudah `×` pada TC-GS-USER-635 dan 636 (tabel 7 baris) adalah data pembanding sebelum asersi absence (8b butir 2). TC-GS-USER-631 tidak menyebut cara mengamati "tabel belum tersaring" atau "tersaring"; spec memakai jumlah baris (7 lalu 2).
- Kata kunci TC-GS-USER-633 dan 634 memakai potongan nilai yang hanya muncul pada kolom yang diuji: `ogou` (Activity `Logout`), `ucces` (Status `Success`), `Invalid` (Note `Invalid password`), `Firefox` (Device / Browser `Firefox on macOS`), dan `10.0` (IP Address `10.0.0.11`). Langkah "lalu clear" pada TC-GS-USER-633 dan 634 dipenuhi dengan mengganti isi kotak search (bagian 8b butir 9) dan mengosongkan Search di langkah 44 sampai 45.
- Spec melewati sekitar 35 langkah (72 langkah) karena sepuluh TC memakai permukaan tab yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01). Semua blok satu kelas (screening dan Search Tab User Log, baca saja), satu akun, satu dataset (U-1), dan tiap blok berdiri sendiri karena Search dikosongkan atau diganti di tiap blok; satu-satunya pembukaan layar kedua (langkah 66) khusus TC-GS-USER-411.
- Pembagian TC lintas spec: Filter Panel TC-GS-USER-638 sampai 646 diverifikasi di spec 103; kombinasi Search dan Filter TC-GS-USER-647 sampai 651 di spec 104; Sort, Pagination, dan kombinasi TC-GS-USER-652 sampai 654, 669, 670 di spec 105; Setup Column TC-GS-USER-655 sampai 663 di spec 106; Download TC-GS-USER-410 dan 664 sampai 668 di spec 107. Pencatatan event Login, Logout, dan Change Password ke User Log (TC-GS-USER-933 sampai 941) diverifikasi di spec 148.
- Temuan untuk QA: (1) TC-GS-USER-409, 412, dan 631 sampai 637 memakai `John Doe` Pre-setup sebagai pemilik log, padahal TC tidak menjamin isi User Log-nya (termasuk event dengan user-agent tidak dikenal untuk TC-GS-USER-412); spec memakai user seed milik spec. (2) Mekanisme memicu event Login, Logout, dan Change Password dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-412 dan 653 menyebut format `[Browser] on [OS]` tanpa nilai persis; spec memakai `Chrome on Windows` dan `Firefox on macOS`, dan penulisan persis nama OS ditentukan parser User-Agent (dikonfirmasi tim FE). (4) TC-GS-USER-633 dan 634 menyebut "potongan nilai" dan contoh `Login`/`10.0` tanpa nilai tiap kolom; spec memakai potongan di atas. (5) TC-GS-USER-635 Data Uji "Nilai tanggal/status sesuai data" menyebut status padahal Expected hanya kolom Date; spec memakai teks tanggal kolom Date. (6) TC-GS-USER-636 tidak menyebut nilai yang hanya ada di kolom Device / Browser; spec memakai `Firefox`. (7) TC-GS-USER-631 Expected f "keyword kosong" tidak punya langkah observasi di TC; spec mengamatinya lewat membuka Search kembali (langkah 29 sampai 30). (8) TC-GS-USER-411 menyebut "tanpa perubahan selain Create" tanpa menyatakan apakah Create menulis entri User Log; spec mengikuti Expected TC (empty state). (9) TC-GS-USER-409 b menyebut kolom aksi `Column Visibility (⋯)`, sedangkan TC-GS-USER-655 menyebutnya `Actions (⋯)`; spec memakai `Column Visibility (⋯)`. (10) Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan mengosongkan preferensi Setup Column tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
