---
id: TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi
title: "Absence Log: Aksi Gagal, Ditolak Validasi, Request Ditolak, dan Ditolak Lisensi Tidak Menulis Entri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-505
  - TC-FA-CF-557
  - TC-FA-CF-572
  - TC-FA-CF-514
  - TC-FA-CF-575
  - TC-FA-CF-576
coverage:
  web: automated
---

# Absence Log: Aksi Gagal, Ditolak Validasi, Request Ditolak, dan Ditolak Lisensi Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun pengirim request TC-FA-CF-557: pemegang Create saja Company Alpha (Pre-setup #5) `masterCreate_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MC_PASSWORD`, lewat login API (sesi API aktor, lihat `suite.md`; tidak ada ganti akun UI untuk akun ini).
- Akun kedua (ganti akun eksplisit pada langkah 41): Total Control Company License Lapse (Pre-setup #24) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company License Lapse; login UI dengan `Spectra.env.FA_TC_LICENSELAPSE_PASSWORD` (email tidak tertulis di Pre-setup TC; disediakan tim FE). Pengguna Total Control Company License Lapse ini adalah pelaku TC-FA-CF-514, 575, dan 576.
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Field `Legacy Tag` dipakai sebagai target Delete yang gagal (TC-FA-CF-505) dan target Edit yang ditolak (TC-FA-CF-557). Asset Name `Turbine` tanpa aset terkait dipakai TC-FA-CF-572. Company License Lapse (Pre-setup #24): field Accounting `Cost Center` (Text, General, Active, Required Yes) dan lisensi FA-7 aktif pada keadaan awal seed; lisensi dapat dicabut saat sesi berjalan dan waktu seed dapat dimajukan melewati T+30 hari lewat seed.
- Data Dinamis: Field Name payload yang ditolak atau digagalkan, tidak pernah tersimpan: `Fail 5xx {runId}-132`, `Req Create Edit {runId}-132`, `Req 572 {runId}-132`, `Acc Create {runId}-132`; Placeholder `Lapse {runId}-132`.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada Create dan Delete (Pre-setup #26), dilepas segera setelah pemicu (S-09); pencabutan lisensi FA-7 dan pemajuan waktu seed Company License Lapse (disediakan tim FE/BE); klien HTTP untuk request langsung ke server dengan token akun pengirim (asersi request langsung hanya status respons, pesan, dan state data lewat fixture BE; 8b butir 1); sesi API Total Control Company Alpha untuk menghapus Asset Name `Turbine`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General dan Accounting, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- State global: Asset Name `Turbine` Company Alpha dihapus pada langkah 29; lisensi FA-7 Company License Lapse dicabut pada langkah 44 dan waktu seed dimajukan pada langkah 53. Hook `after` memulihkan Asset Name `Turbine` lewat seed reset Company Alpha, mengaktifkan kembali lisensi FA-7 Company License Lapse, dan mengembalikan sesi ke akun default suite. Seed reset Company memulihkan baseline.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-505: Aksi yang gagal atau ditolak tidak menulis entri log

1. Catat jumlah entri Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
2. Klik `[+ Custom Field]`, isi Field Name `Fail 5xx {runId}-132` dan Data Type `Text`
3. Intersep respons Create dengan 500 (pemicu kegagalan, Pre-setup #26), lalu klik `[Submit]`
4. Lepas intersep respons Create
5. Kosongkan Field Name lalu klik `[Submit]`
6. Klik icon close `[✕]`
7. Verifikasi dialog `Unsaved Changes` tampil
8. Klik `[Leave]` pada dialog `Unsaved Changes`
9. Klik row action `⋯` > `Delete` pada baris `Legacy Tag` sampai dialog Delete tampil, dengan respons Delete diintersep 500
10. Klik `[Delete]` pada dialog
11. Lepas intersep respons Delete
12. Tunggu aksi selesai
13. Buka Modal Changelog tab General dan hitung ulang jumlah entri
14. Verifikasi jumlah entri Changelog tab General sama dengan baseline
15. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
16. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
17. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
18. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-557: Request Edit langsung oleh pemegang Create saja ditolak 403

19. Catat jumlah entri Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
20. Kirim request Edit langsung untuk field `Legacy Tag` dengan token pemegang Create (Pre-setup #5), payload valid dengan Field Name `Req Create Edit {runId}-132`
21. Verifikasi server merespons 403 Forbidden
22. Verifikasi field `Legacy Tag` tidak berubah (dibaca lewat fixture BE)
23. Buka Modal Changelog tab General dan hitung ulang jumlah entri
24. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada entri baru)
25. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
26. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru)
27. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
28. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-572: Request Scope berisi Asset Name yang sudah tidak ada ditolak 422

29. Hapus Asset Name `Turbine` di Settings > Asset Name lewat sesi API hingga penghapusan tersimpan
30. Catat jumlah entri Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
31. Kirim request Create langsung (klien HTTP) dengan Asset Name `Turbine` yang sudah dihapus pada Scope dan Field Name `Req 572 {runId}-132`
32. Verifikasi server menolak dengan 422
33. Verifikasi pesan `Turbine no longer exists. Please select another.`
34. Verifikasi field `Req 572 {runId}-132` tidak tersimpan (dibaca lewat fixture BE)
35. Buka Modal Changelog tab General dan hitung ulang jumlah entri
36. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada entri baru dari request ini)
37. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
38. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri baru dari request ini)
39. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
40. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru dari request ini)

### TC-FA-CF-514: Penolakan 403 karena lisensi FA-7 tidak menulis log

41. Ganti akun: logout, lalu login sebagai Total Control Company License Lapse (Pre-setup #24)
42. Catat jumlah entri Changelog tab Accounting, System Log pelaku (pengguna Total Control Company License Lapse), dan Activity Log sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
43. Klik tab `Accounting`, lalu klik row action `⋯` > `Edit` pada baris `Cost Center` dan ubah Placeholder menjadi `Lapse {runId}-132`
44. Cabut lisensi FA-7 Company License Lapse lewat seed saat sesi berjalan hingga tersimpan
45. Klik `[Save]`
46. Tunggu aksi selesai
47. Buka Modal Changelog tab Accounting dan hitung ulang jumlah entri
48. Verifikasi jumlah entri Changelog tab Accounting sama dengan baseline
49. Buka System Log pelaku (Settings > User > Detail pengguna Total Control Company License Lapse > Tab System Log) dan hitung ulang jumlah entri
50. Verifikasi jumlah entri System Log pelaku sama dengan baseline (tidak ada entri baru)
51. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
52. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-575: Request Create field grup Accounting saat FA-7 tidak aktif ditolak 403

53. Majukan waktu seed Company License Lapse melewati T+30 hari sejak pencabutan lisensi FA-7 pada langkah 44 sehingga Grace Period berakhir (Pre-setup #24)
54. Catat jumlah entri Modal Changelog tab General, System Log pelaku, dan Activity Log sebagai baseline
55. Kirim request Create field grup Accounting langsung (klien HTTP) dengan Field Name `Acc Create {runId}-132`
56. Verifikasi server merespons 403 Forbidden
57. Verifikasi field `Acc Create {runId}-132` tidak dibuat (dibaca lewat fixture BE)
58. Buka Modal Changelog tab General dan hitung ulang jumlah entri
59. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada entri log)
60. Buka System Log pelaku dan hitung ulang jumlah entri
61. Verifikasi jumlah entri System Log pelaku sama dengan baseline (tidak ada entri log)
62. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
63. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri log)

### TC-FA-CF-576: Request Edit field grup Accounting saat FA-7 tidak aktif ditolak 403

64. Catat jumlah entri Modal Changelog tab General, System Log pelaku, dan Activity Log sebagai baseline
65. Kirim request Edit untuk `Cost Center` langsung (klien HTTP)
66. Verifikasi server merespons 403 Forbidden
67. Verifikasi `Cost Center` tidak berubah (dibaca lewat fixture BE)
68. Buka Modal Changelog tab General dan hitung ulang jumlah entri
69. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada log)
70. Buka System Log pelaku dan hitung ulang jumlah entri
71. Verifikasi jumlah entri System Log pelaku sama dengan baseline (tidak ada log)
72. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
73. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada log)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 73 langkah bernomor; langkah blok baca-log berpola (buka surface, hitung entri, `Verifikasi` jumlah; 36 langkah, nomor 13 sampai 18, 23 sampai 28, 35 sampai 40, 47 sampai 52, 58 sampai 63, dan 68 sampai 73) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 37 langkah. Spec dipertahankan karena semua blok satu kelas (absence log, kelas g), tiap TC punya aksi, user, dan baseline sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-5 (a): spec absence kelas g; pemicu kelas a (request langsung ke server pada TC-FA-CF-557, 572, 575, 576), kelas b (respons 500 pada Create dan Delete lewat intersep) dan kelas h (lisensi FA-7 dicabut saat sesi dan Grace Period berakhir) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya user dan baseline sendiri (S-12). Intersep dilepas segera setelah pemicu.
- Anchor positif (8b butir 2): jumlah entri awal yang dicatat pada baseline tiap TC pada ketiga surface, serta status respons 403 atau 422 dan pesan penolakan pada TC request langsung; asersi "tidak ada entri baru" ditulis sebagai kesamaan jumlah entri dengan baseline.
- TC-FA-CF-514, 575, dan 576 berjalan terakhir karena ganti akun ke Company License Lapse (langkah 41); TC-FA-CF-575 dan 576 membutuhkan Grace Period yang sudah berakhir sehingga dijalankan sesudah pencabutan lisensi pada TC-FA-CF-514 dan pemajuan waktu seed (langkah 53). Pada keadaan itu tab `Accounting` terkunci, sehingga baseline dan pembacaan Changelog TC-FA-CF-575 dan 576 memakai Modal Changelog tab General.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 41 (ganti akun), langkah 29 (pemicu state), langkah 44 dan 53 (seed), baseline, "Tunggu aksi selesai", pelepasan intersep, pengiriman request langsung, dan langkah buka surface serta hitung ulang jumlah entri.
- S-05: asersi absence log TC-FA-CF-557, 572, 575, dan 576 hanya ada di spec ini; spec 149, 181, dan 147 mencatat rujukan ke sini di `## Notes`.
- Temuan untuk QA:
  - TC-FA-CF-505 Expected hanya berupa absence log dan tidak memuat hasil UI (toast error atau pesan validasi) untuk ketiga aksi; spec tidak mengasersi hasil UI dan memakai jumlah entri awal sebagai anchor.
  - TC-FA-CF-505 tidak menyebut apakah modal Create tetap terbuka setelah respons 500 (langkah 2 bergantung pada modal masih terbuka) dan apakah dialog Delete tertutup setelah respons 500; spec mengikuti urutan langkah TC.
  - TC-FA-CF-514 tidak menyebut perubahan yang di-Save pada field Accounting; spec memakai Placeholder `Cost Center` dan tidak mengasersi toast 403 (NC-05) karena Expected TC hanya absence log. TC juga tidak menyebut apakah modal Edit tertutup setelah penolakan.
  - TC-FA-CF-514 menyebut "System Log pelaku" tetapi Pre-setup #24 tidak memuat nama pengguna Total Control Company License Lapse; spec membaca System Log pengguna itu dan nama pengguna disediakan tim FE.
  - TC-FA-CF-557 menyebut "Sebagai Total Control" membuka tiga surface log tanpa path menu; spec memakai sesi UI Total Control Company Alpha di hook `before`. Payload Edit valid tidak diperinci; spec memakai Field Name `Req Create Edit {runId}-132`.
  - TC-FA-CF-572 tidak menyebut cara Asset Name `Turbine` dihapus dan tidak menyebut kode penolakan pada baris langkah; spec memakai sesi API Total Control Company Alpha dan Expected 422.
  - TC-FA-CF-575 dan 576 meminta "buka Modal Changelog, System Log aktor, dan Activity Log" tanpa path menu; Changelog tab Accounting tidak dapat dibuka selama tab terkunci, sehingga baseline dibaca pada Changelog tab General.
  - Email akun Total Control Company License Lapse tidak tertulis di Pre-setup TC; env var `FA_TC_LICENSELAPSE_PASSWORD` disediakan tim FE.
