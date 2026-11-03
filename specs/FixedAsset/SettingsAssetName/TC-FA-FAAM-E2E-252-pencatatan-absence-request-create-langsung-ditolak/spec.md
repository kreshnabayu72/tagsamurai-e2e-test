---
id: TC-FA-FAAM-E2E-252-pencatatan-absence-request-create-langsung-ditolak
title: "Pencatatan Absence: Request Create Langsung yang Ditolak Server (Category Excess, TAG Type Terkunci Paket, Default Addon pada Non-TAG, Addon Tanpa Lisensi) Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-845
coverage:
  web: automated
---

# Pencatatan Absence: Request Create Langsung yang Ditolak Server (Category Excess, TAG Type Terkunci Paket, Default Addon pada Non-TAG, Addon Tanpa Lisensi) Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat Changelog, System Log, dan Activity Log FAMS): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; langkah 52 mengganti akun ke client Starter secara eksplisit; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor pengirim request langsung (login API password, token tidak dihitung sebagai sesi web; disediakan tim BE/FE): Total Control client utama (`Spectra.env.FA_TC_PASSWORD`) untuk pemicu a, c, d dan Total Control client Starter untuk pemicu b. Klien HTTP untuk request langsung disediakan tim BE/FE; endpoint tidak disebut TC dan tidak dikarang spec. Payload request Create langsung valid selain bagian yang diuji.
- Akun client Starter (pemicu b): Total Control client Starter (Pre-setup #16), email tidak tertulis di Pre-setup TC dan disediakan tim FE, `Spectra.env.FA_STARTER_PASSWORD`. Langkah 52 mengganti akun secara eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `FA_TC_PASSWORD`, `FA_STARTER_PASSWORD`.
- Data Pre-setup (hanya dibaca): client utama No. 22 (Category excess `Legacy Category`, Pre-setup #22d; Category `IT Equipment`), No. 10b (lisensi addon `Maps` tidak teralokasi aktif), client Starter (No. 16).
- Data Dinamis: tidak ada seed. Nama request Create bersuffix `{runId}-252` (tidak boleh tercipta setelah request ditolak): `Absence Excess 845 {runId}-252`, `Absence Locked 845 {runId}-252`, `Absence NonTag 845 {runId}-252`, dan `Absence Maps 845 {runId}-252`.
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; membuka Detail User aktor tab System Log dan Activity Log FAMS beserta Search di dalamnya; membaca jumlah entri hasil Search di ketiganya sebelum aksi (baseline). Ketiganya adalah audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi, bukan total absolut. Klien HTTP request langsung; client Starter dengan akun Total Control.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus Asset Name apa pun yang ternyata terbentuk oleh request yang ditolak (seharusnya tidak ada).
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition: pengamat UI Total Control berada di Fixed Asset > Settings > Asset Master > Asset Name; sesi API berperan sebagaimana ditulis per langkah.

## Test Steps

### TC-FA-FAAM-845: Request Create langsung yang ditolak tidak menulis entri di tiga surface log (client utama)

1. Klik icon Changelog
2. Ketik Search `Absence Excess 845 {runId}-252`, tekan Enter
3. Catat jumlah baris Changelog `Absence Excess 845 {runId}-252` sebagai baseline
4. Ketik Search `Absence NonTag 845 {runId}-252`, tekan Enter
5. Catat jumlah baris Changelog `Absence NonTag 845 {runId}-252` sebagai baseline
6. Ketik Search `Absence Maps 845 {runId}-252`, tekan Enter
7. Catat jumlah baris Changelog `Absence Maps 845 {runId}-252` sebagai baseline
8. Tutup Modal Changelog
9. Buka Detail User aktor lalu tab System Log
10. Ketik Search `Absence Excess 845 {runId}-252`, tekan Enter
11. Catat jumlah entri System Log `Absence Excess 845 {runId}-252` sebagai baseline
12. Ketik Search `Absence NonTag 845 {runId}-252`, tekan Enter
13. Catat jumlah entri System Log `Absence NonTag 845 {runId}-252` sebagai baseline
14. Ketik Search `Absence Maps 845 {runId}-252`, tekan Enter
15. Catat jumlah entri System Log `Absence Maps 845 {runId}-252` sebagai baseline
16. Buka Activity Log FAMS
17. Ketik Search `Absence Excess 845 {runId}-252`, tekan Enter
18. Catat jumlah entri Activity Log FAMS `Absence Excess 845 {runId}-252` sebagai baseline
19. Ketik Search `Absence NonTag 845 {runId}-252`, tekan Enter
20. Catat jumlah entri Activity Log FAMS `Absence NonTag 845 {runId}-252` sebagai baseline
21. Ketik Search `Absence Maps 845 {runId}-252`, tekan Enter
22. Catat jumlah entri Activity Log FAMS `Absence Maps 845 {runId}-252` sebagai baseline
23. Kirim request Create langsung ke server untuk pemicu a: `Absence Excess 845 {runId}-252` dengan Category excess `Legacy Category`
24. Verifikasi server menolak dengan `422` (error validasi pada Category)
25. Kirim request Create langsung untuk pemicu c: `Absence NonTag 845 {runId}-252` dengan TAG Type `Non-TAG` dan Default Addon `Audit`
26. Verifikasi server menolak (karena Default Addon mensyaratkan TAG)
27. Kirim request Create langsung untuk pemicu d: `Absence Maps 845 {runId}-252` dengan Default Addon `Maps` saat lisensi Maps tidak aktif
28. Verifikasi server menolak (lisensi addon tidak aktif)
29. Buka Fixed Asset > Settings > Asset Master > Asset Name dan muat ulang List
30. Klik icon Changelog
31. Ketik Search `Absence Excess 845 {runId}-252`, tekan Enter
32. Verifikasi jumlah baris Changelog `Absence Excess 845 {runId}-252` sama dengan baseline pada langkah 3 (TC-FA-FAAM-845 pemicu a butir ii)
33. Ketik Search `Absence NonTag 845 {runId}-252`, tekan Enter
34. Verifikasi jumlah baris Changelog `Absence NonTag 845 {runId}-252` sama dengan baseline pada langkah 5 (TC-FA-FAAM-845 pemicu c butir ii)
35. Ketik Search `Absence Maps 845 {runId}-252`, tekan Enter
36. Verifikasi jumlah baris Changelog `Absence Maps 845 {runId}-252` sama dengan baseline pada langkah 7 (TC-FA-FAAM-845 pemicu d butir ii)
37. Tutup Modal Changelog
38. Buka Detail User aktor lalu tab System Log
39. Ketik Search `Absence Excess 845 {runId}-252`, tekan Enter
40. Verifikasi jumlah entri System Log `Absence Excess 845 {runId}-252` sama dengan baseline pada langkah 11 (TC-FA-FAAM-845 pemicu a butir iii)
41. Ketik Search `Absence NonTag 845 {runId}-252`, tekan Enter
42. Verifikasi jumlah entri System Log `Absence NonTag 845 {runId}-252` sama dengan baseline pada langkah 13 (TC-FA-FAAM-845 pemicu c butir iii)
43. Ketik Search `Absence Maps 845 {runId}-252`, tekan Enter
44. Verifikasi jumlah entri System Log `Absence Maps 845 {runId}-252` sama dengan baseline pada langkah 15 (TC-FA-FAAM-845 pemicu d butir iii)
45. Buka Activity Log FAMS
46. Ketik Search `Absence Excess 845 {runId}-252`, tekan Enter
47. Verifikasi jumlah entri Activity Log FAMS `Absence Excess 845 {runId}-252` sama dengan baseline pada langkah 18 (TC-FA-FAAM-845 pemicu a butir iv)
48. Ketik Search `Absence NonTag 845 {runId}-252`, tekan Enter
49. Verifikasi jumlah entri Activity Log FAMS `Absence NonTag 845 {runId}-252` sama dengan baseline pada langkah 20 (TC-FA-FAAM-845 pemicu c butir iv)
50. Ketik Search `Absence Maps 845 {runId}-252`, tekan Enter
51. Verifikasi jumlah entri Activity Log FAMS `Absence Maps 845 {runId}-252` sama dengan baseline pada langkah 22 (TC-FA-FAAM-845 pemicu d butir iv)

### TC-FA-FAAM-845: pemicu b dari client Starter

52. Ganti akun: keluar (Logout), lalu login sebagai Total Control client Starter (Pre-setup #16; email disediakan tim FE, `Spectra.env.FA_STARTER_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
53. Klik icon Changelog
54. Ketik Search `Absence Locked 845 {runId}-252`, tekan Enter
55. Catat jumlah baris Changelog `Absence Locked 845 {runId}-252` sebagai baseline
56. Tutup Modal Changelog
57. Buka Detail User aktor lalu tab System Log
58. Ketik Search `Absence Locked 845 {runId}-252`, tekan Enter
59. Catat jumlah entri System Log `Absence Locked 845 {runId}-252` sebagai baseline
60. Buka Activity Log FAMS
61. Ketik Search `Absence Locked 845 {runId}-252`, tekan Enter
62. Catat jumlah entri Activity Log FAMS `Absence Locked 845 {runId}-252` sebagai baseline
63. Kirim request Create langsung dari client Starter untuk pemicu b: `Absence Locked 845 {runId}-252` dengan TAG Type `RFID`
64. Verifikasi server menolak dengan `409 PLAN_LIMIT_EXCEEDED` dengan `reason: "feature_locked"`
65. Buka Fixed Asset > Settings > Asset Master > Asset Name dan muat ulang List
66. Klik icon Changelog
67. Ketik Search `Absence Locked 845 {runId}-252`, tekan Enter
68. Verifikasi jumlah baris Changelog `Absence Locked 845 {runId}-252` sama dengan baseline pada langkah 55 (TC-FA-FAAM-845 pemicu b butir ii)
69. Tutup Modal Changelog
70. Buka Detail User aktor lalu tab System Log
71. Ketik Search `Absence Locked 845 {runId}-252`, tekan Enter
72. Verifikasi jumlah entri System Log `Absence Locked 845 {runId}-252` sama dengan baseline pada langkah 59 (TC-FA-FAAM-845 pemicu b butir iii)
73. Buka Activity Log FAMS
74. Ketik Search `Absence Locked 845 {runId}-252`, tekan Enter
75. Verifikasi jumlah entri Activity Log FAMS `Absence Locked 845 {runId}-252` sama dengan baseline pada langkah 62 (TC-FA-FAAM-845 pemicu b butir iv)

## Notes

- P-5(a): spec ini kelas g; pemicu kelas a (request Create langsung ditolak: TC-FA-FAAM-845) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Nama bersuffix dan baseline milik spec ini sendiri.
- Di atas smell 35 langkah. Spec berisi 75 langkah tertulis. Alasan: satu TC (TC-FA-FAAM-845) tidak dipecah antar spec dan memuat empat pemicu (a, b, c, d) yang masing-masing menuntut baseline dan pengamatan pada tiga surface log (Changelog, System Log, Activity Log FAMS); tiap surface memerlukan navigasi dan satu Search per nama; pemicu b memakai client Starter sehingga memerlukan penggantian akun.
- Langkah 24, 26, 28, 64 (status atau respons penolakan) menjadi anchor positif bahwa pemicu benar-benar mencapai server sebelum asersi absence berikutnya; pembanding tiap surface adalah jumlah awal yang dicatat pada langkah baseline.
- Langkah penghubung tanpa `Verifikasi`: seluruh langkah selain langkah berawalan `Verifikasi`, yaitu membuka dan mencari di Modal Changelog, Detail User aktor tab System Log, dan Activity Log FAMS (S-12, S-14), mencatat baseline, navigasi, mengirim pemicu, dan menutup form dirty secara deterministik (S-08).
- Urutan: baseline seluruh nama pada tiga surface sebelum request pertama blok itu, lalu seluruh pemicu, lalu pengamatan tiga surface. Blok client utama (pemicu a, c, d) mendahului client Starter (pemicu b) agar penggantian akun hanya sekali.
- Pembagian TC lintas spec: butir status penolakan dan state data TC-FA-FAAM-845 ada pada TC-FA-FAAM-105, 112, 120, 121 (spec 052). TC-FA-FAAM-611 sampai 614 tetap di spec 247 bersama sisi presence di spec 231.
- Temuan untuk QA:
  - TC-FA-FAAM-845 meminta hitungan entri System Log dan Activity Log FAMS "yang memuat nama itu" lewat Search; TC tidak menyebut apakah tab System Log pada Detail User memiliki Search. Spec memakai Search pada ketiga surface; bila System Log tidak punya Search, hitungan perlu didefinisikan ulang.
  - Pre-setup No. 16 tidak memuat email akun Total Control untuk client Starter; disediakan tim FE.
  - TC-FA-FAAM-845 butir c dan d (i) menulis "Server menolak" tanpa kode status; spec mengasersi penolakan tanpa kode tertentu. TC tidak menyebut client pengirim pemicu a, c, d; spec memakai client utama (sesuai TC-FA-FAAM-105, 120, 121).
