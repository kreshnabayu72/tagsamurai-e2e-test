---
id: TC-FA-FAAM-E2E-254-pencatatan-absence-delete-bulk-delete-import-ditolak-suspended-expired
title: "Pencatatan Absence: Delete, Bulk Delete, dan Import yang Ditolak Saat Client Suspended atau Expired Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-843
coverage:
  web: automated
---

# Pencatatan Absence: Delete, Bulk Delete, dan Import yang Ditolak Saat Client Suspended atau Expired Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat Changelog, System Log, dan Activity Log FAMS): Total Control client utama `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) sebagai akun default hook `before`. Langkah 1 pada tiap iterasi tabel mengganti akun dan client secara eksplisit; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Tabel "Client yang diuji" (spec dijalankan untuk setiap baris, langkah 1 sampai 73; email Total Control tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE; keduanya pada plan Growth sehingga modul Import tersedia):

  | Client | Pre-setup | Akun Total Control | Env |
  |---|---|---|---|
  | Suspended (plan Growth) | No. 18 | disediakan tim FE | `Spectra.env.FA_SUSP_TC_PASSWORD` |
  | Expired (plan Growth) | No. 18c | disediakan tim FE | `Spectra.env.FA_EXP_TC_PASSWORD` |

- Env var: `FA_TC_PASSWORD`, `FA_SUSP_TC_PASSWORD`, `FA_EXP_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): pada client Suspended dan Expired terdapat salinan `Warehouse Pallet`, `Bulk Clean A`, dan `Bulk Clean B` (Total Asset 0); seluruh aksi tulis di sana ditolak server sehingga data tidak berubah. Nama literal karena dipakai pada client khusus tanpa mutasi. Nama baris impor `Blocked Import Item` (literal, tidak tercipta).
- Data uji: Asset Name `Warehouse Pallet`, `Bulk Clean A`, dan `Bulk Clean B`, serta baris impor `Blocked Import Item` (berkas impor satu baris disediakan tim FE).
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; membuka Detail User aktor tab System Log dan Activity Log FAMS beserta Search di dalamnya; membaca jumlah entri hasil Search di ketiganya sebelum aksi (baseline). Ketiganya adalah audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi, bukan total absolut. Client Suspended dan Expired dengan akun Total Control; modul Import tab Asset Name pada plan Growth.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus Asset Name apa pun yang ternyata terbentuk oleh request yang ditolak (seharusnya tidak ada); pulihkan state client (status Suspended dan Expired) bila diubah.
- State global yang diubah: tidak ada (status client tidak diubah spec ini). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-843: login sebagai Total Control pada client Suspended (lalu Expired) dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

Untuk setiap baris tabel "Client yang diuji" (langkah 1 sampai 73):

1. Logout lalu login sebagai Total Control pada client baris tabel
2. Buka Fixed Asset > Settings > Asset Master > Asset Name
3. Klik icon Changelog
4. Ketik Search `Warehouse Pallet`, tekan Enter
5. Catat jumlah baris Changelog `Warehouse Pallet` sebagai baseline
6. Ketik Search `Bulk Clean A`, tekan Enter
7. Catat jumlah baris Changelog `Bulk Clean A` sebagai baseline
8. Ketik Search `Bulk Clean B`, tekan Enter
9. Catat jumlah baris Changelog `Bulk Clean B` sebagai baseline
10. Ketik Search `Blocked Import Item`, tekan Enter
11. Catat jumlah baris Changelog `Blocked Import Item` sebagai baseline
12. Tutup Modal Changelog
13. Buka Detail User aktor lalu tab System Log
14. Ketik Search `Warehouse Pallet`, tekan Enter
15. Catat jumlah entri System Log `Warehouse Pallet` sebagai baseline
16. Ketik Search `Bulk Clean A`, tekan Enter
17. Catat jumlah entri System Log `Bulk Clean A` sebagai baseline
18. Ketik Search `Bulk Clean B`, tekan Enter
19. Catat jumlah entri System Log `Bulk Clean B` sebagai baseline
20. Ketik Search `Blocked Import Item`, tekan Enter
21. Catat jumlah entri System Log `Blocked Import Item` sebagai baseline
22. Buka Activity Log FAMS
23. Ketik Search `Warehouse Pallet`, tekan Enter
24. Catat jumlah entri Activity Log FAMS `Warehouse Pallet` sebagai baseline
25. Ketik Search `Bulk Clean A`, tekan Enter
26. Catat jumlah entri Activity Log FAMS `Bulk Clean A` sebagai baseline
27. Ketik Search `Bulk Clean B`, tekan Enter
28. Catat jumlah entri Activity Log FAMS `Bulk Clean B` sebagai baseline
29. Ketik Search `Blocked Import Item`, tekan Enter
30. Catat jumlah entri Activity Log FAMS `Blocked Import Item` sebagai baseline
31. Buka Fixed Asset > Settings > Asset Master > Asset Name
32. Ketik Search `Warehouse Pallet`, tekan Enter
33. Klik `⋯` baris `Warehouse Pallet` lalu `Delete`
34. Klik `[Delete]`
35. Verifikasi server menolak dengan 403 Forbidden (Delete; TC-FA-FAAM-843 butir i)
36. Ganti isi kotak search dengan `Bulk Clean`, tekan Enter
37. Centang `Bulk Clean A` dan `Bulk Clean B`
38. Klik `Bulk Action` lalu `Delete`
39. Klik `[Delete]`
40. Verifikasi server menolak dengan 403 Forbidden (Bulk Delete; TC-FA-FAAM-843 butir i)
41. Klik Unselect All
42. Buka modul Import tab Asset Name
43. Impor satu baris Asset Name baru `Blocked Import Item` lewat modul Import
44. Verifikasi server menolak dengan 403 Forbidden (Import; TC-FA-FAAM-843 butir i)
45. Buka Fixed Asset > Settings > Asset Master > Asset Name dan muat ulang List
46. Klik icon Changelog
47. Ketik Search `Warehouse Pallet`, tekan Enter
48. Verifikasi jumlah baris Changelog `Warehouse Pallet` sama dengan baseline pada langkah 5 (TC-FA-FAAM-843 butir ii pada client baris tabel)
49. Ketik Search `Bulk Clean A`, tekan Enter
50. Verifikasi jumlah baris Changelog `Bulk Clean A` sama dengan baseline pada langkah 7 (TC-FA-FAAM-843 butir ii pada client baris tabel)
51. Ketik Search `Bulk Clean B`, tekan Enter
52. Verifikasi jumlah baris Changelog `Bulk Clean B` sama dengan baseline pada langkah 9 (TC-FA-FAAM-843 butir ii pada client baris tabel)
53. Ketik Search `Blocked Import Item`, tekan Enter
54. Verifikasi jumlah baris Changelog `Blocked Import Item` sama dengan baseline pada langkah 11 (TC-FA-FAAM-843 butir ii pada client baris tabel)
55. Tutup Modal Changelog
56. Buka Detail User aktor lalu tab System Log
57. Ketik Search `Warehouse Pallet`, tekan Enter
58. Verifikasi jumlah entri System Log `Warehouse Pallet` sama dengan baseline pada langkah 15 (TC-FA-FAAM-843 butir iii pada client baris tabel)
59. Ketik Search `Bulk Clean A`, tekan Enter
60. Verifikasi jumlah entri System Log `Bulk Clean A` sama dengan baseline pada langkah 17 (TC-FA-FAAM-843 butir iii pada client baris tabel)
61. Ketik Search `Bulk Clean B`, tekan Enter
62. Verifikasi jumlah entri System Log `Bulk Clean B` sama dengan baseline pada langkah 19 (TC-FA-FAAM-843 butir iii pada client baris tabel)
63. Ketik Search `Blocked Import Item`, tekan Enter
64. Verifikasi jumlah entri System Log `Blocked Import Item` sama dengan baseline pada langkah 21 (TC-FA-FAAM-843 butir iii pada client baris tabel)
65. Buka Activity Log FAMS
66. Ketik Search `Warehouse Pallet`, tekan Enter
67. Verifikasi jumlah entri Activity Log FAMS `Warehouse Pallet` sama dengan baseline pada langkah 24 (TC-FA-FAAM-843 butir iv pada client baris tabel)
68. Ketik Search `Bulk Clean A`, tekan Enter
69. Verifikasi jumlah entri Activity Log FAMS `Bulk Clean A` sama dengan baseline pada langkah 26 (TC-FA-FAAM-843 butir iv pada client baris tabel)
70. Ketik Search `Bulk Clean B`, tekan Enter
71. Verifikasi jumlah entri Activity Log FAMS `Bulk Clean B` sama dengan baseline pada langkah 28 (TC-FA-FAAM-843 butir iv pada client baris tabel)
72. Ketik Search `Blocked Import Item`, tekan Enter
73. Verifikasi jumlah entri Activity Log FAMS `Blocked Import Item` sama dengan baseline pada langkah 30 (TC-FA-FAAM-843 butir iv pada client baris tabel)

## Notes

- P-5(a): spec ini kelas g; pemicu kelas h (Delete, Bulk Delete, dan Import saat client Suspended atau Expired: TC-FA-FAAM-843) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Nama dan baseline milik spec ini sendiri.
- Di atas smell 35 langkah. Spec berisi 73 langkah tertulis yang diulang untuk baris Suspended lalu baris Expired (ekspansi 146 langkah). Alasan: satu TC (TC-FA-FAAM-843) tidak dipecah antar spec; TC membaca tiga surface log (Changelog, System Log, Activity Log FAMS) untuk empat nama setelah tiga aksi (Delete, Bulk Delete, Import), yang masing-masing memerlukan navigasi dan satu Search per nama; kedua client tenant memakai langkah identik sehingga diulang per baris tabel, bukan dipecah per client.
- Langkah 35, 40, 44 (status 403) menjadi anchor positif bahwa pemicu benar-benar mencapai server sebelum asersi absence berikutnya; pembanding tiap surface adalah jumlah awal yang dicatat pada langkah baseline.
- Langkah penghubung tanpa `Verifikasi`: seluruh langkah selain langkah berawalan `Verifikasi`, yaitu membuka dan mencari di Modal Changelog, Detail User aktor tab System Log, dan Activity Log FAMS (S-12, S-14), mencatat baseline, navigasi, mengirim pemicu, dan menutup form dirty secara deterministik (S-08).
- Urutan: urutan final per client (bukan per TC) agar login client tidak berulang. Perubahan urutan ini dicatat sebagai keputusan penulis.
- Pembagian TC lintas spec: butir status penolakan dan state data TC-FA-FAAM-843 ada pada TC-FA-FAAM-621, 622, 623 (spec 250). TC-FA-FAAM-842 ada di spec 253. TC-FA-FAAM-611 sampai 614 tetap di spec 247.
- Temuan untuk QA:
  - TC-FA-FAAM-843 meminta hitungan entri System Log dan Activity Log FAMS "yang memuat nama itu" lewat Search; TC tidak menyebut apakah tab System Log pada Detail User memiliki Search. Spec memakai Search pada ketiga surface; bila System Log tidak punya Search, hitungan perlu didefinisikan ulang.
  - Pre-setup No. 18 dan 18c tidak memuat email akun Total Control untuk client Suspended dan Expired; disediakan tim FE.
  - TC-FA-FAAM-843 tidak menyebut format berkas impor; disediakan tim FE.
  - Nama `Blocked Import Item` pada client Suspended dan Expired memakai nama literal TC (sama dengan spec 250); baseline entri nama itu dan nama lain bisa lebih dari nol.
