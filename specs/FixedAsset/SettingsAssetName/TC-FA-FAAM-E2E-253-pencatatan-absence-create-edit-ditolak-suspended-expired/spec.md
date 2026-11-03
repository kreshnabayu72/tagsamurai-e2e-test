---
id: TC-FA-FAAM-E2E-253-pencatatan-absence-create-edit-ditolak-suspended-expired
title: "Pencatatan Absence: Create dan Edit yang Ditolak Saat Client Suspended atau Expired Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-842
coverage:
  web: automated
---

# Pencatatan Absence: Create dan Edit yang Ditolak Saat Client Suspended atau Expired Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat Changelog, System Log, dan Activity Log FAMS): Total Control client utama `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) sebagai akun default hook `before`. Langkah 1 pada tiap iterasi tabel mengganti akun dan client secara eksplisit; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Tabel "Client yang diuji" (spec dijalankan untuk setiap baris, langkah 1 sampai 51; email Total Control tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE):

  | Client | Pre-setup | Akun Total Control | Env |
  |---|---|---|---|
  | Suspended (plan Growth) | No. 18 | disediakan tim FE | `Spectra.env.FA_SUSP_TC_PASSWORD` |
  | Expired (plan Growth) | No. 18c | disediakan tim FE | `Spectra.env.FA_EXP_TC_PASSWORD` |

- Env var: `FA_TC_PASSWORD`, `FA_SUSP_TC_PASSWORD`, `FA_EXP_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): pada client Suspended dan Expired terdapat salinan `Dell Latitude` (Code `DLAT`); seluruh aksi tulis di sana ditolak server sehingga data tidak berubah. Nama literal karena dipakai pada client khusus tanpa mutasi. Nama request `Blocked Create Item` (literal, tidak tercipta).
- Data uji: Asset Name `Blocked Create Item`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`; Code `DLAT` menjadi `DLX`.
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; membuka Detail User aktor tab System Log dan Activity Log FAMS beserta Search di dalamnya; membaca jumlah entri hasil Search di ketiganya sebelum aksi (baseline). Ketiganya adalah audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi, bukan total absolut. Client Suspended dan Expired dengan akun Total Control.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus Asset Name apa pun yang ternyata terbentuk oleh request yang ditolak (seharusnya tidak ada); pulihkan state client (status Suspended dan Expired) bila diubah.
- State global yang diubah: tidak ada (status client tidak diubah spec ini). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-842: login sebagai Total Control pada client Suspended (lalu Expired) dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

Untuk setiap baris tabel "Client yang diuji" (langkah 1 sampai 51):

1. Logout lalu login sebagai Total Control pada client baris tabel
2. Buka Fixed Asset > Settings > Asset Master > Asset Name
3. Klik icon Changelog
4. Ketik Search `Blocked Create Item`, tekan Enter
5. Catat jumlah baris Changelog `Blocked Create Item` sebagai baseline
6. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
7. Catat jumlah baris Changelog `Dell Latitude` sebagai baseline
8. Tutup Modal Changelog
9. Buka Detail User aktor lalu tab System Log
10. Ketik Search `Blocked Create Item`, tekan Enter
11. Catat jumlah entri System Log `Blocked Create Item` sebagai baseline
12. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
13. Catat jumlah entri System Log `Dell Latitude` sebagai baseline
14. Buka Activity Log FAMS
15. Ketik Search `Blocked Create Item`, tekan Enter
16. Catat jumlah entri Activity Log FAMS `Blocked Create Item` sebagai baseline
17. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
18. Catat jumlah entri Activity Log FAMS `Dell Latitude` sebagai baseline
19. Buka Fixed Asset > Settings > Asset Master > Asset Name
20. Klik `[+ Asset Name]`
21. Isi Asset Name `Blocked Create Item`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`
22. Klik `[Submit]`
23. Verifikasi server menolak dengan 403 Forbidden (Create; TC-FA-FAAM-842 butir i)
24. Klik `✕` pada Modal Create
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]` pada dialog `Unsaved Changes`
27. Ketik Search `Dell Latitude`, tekan Enter
28. Klik `⋯` baris `Dell Latitude` lalu `Edit`
29. Ubah Code dari `DLAT` menjadi `DLX`
30. Klik `[Save]`
31. Verifikasi server menolak dengan 403 Forbidden (Edit; TC-FA-FAAM-842 butir i)
32. Klik `✕` pada Modal Edit
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]` pada dialog `Unsaved Changes`
35. Muat ulang List
36. Klik icon Changelog
37. Ketik Search `Blocked Create Item`, tekan Enter
38. Verifikasi jumlah baris Changelog `Blocked Create Item` sama dengan baseline pada langkah 5 (TC-FA-FAAM-842 butir ii pada client baris tabel)
39. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
40. Verifikasi jumlah baris Changelog `Dell Latitude` sama dengan baseline pada langkah 7 (TC-FA-FAAM-842 butir ii pada client baris tabel)
41. Tutup Modal Changelog
42. Buka Detail User aktor lalu tab System Log
43. Ketik Search `Blocked Create Item`, tekan Enter
44. Verifikasi jumlah entri System Log `Blocked Create Item` sama dengan baseline pada langkah 11 (TC-FA-FAAM-842 butir iii pada client baris tabel)
45. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
46. Verifikasi jumlah entri System Log `Dell Latitude` sama dengan baseline pada langkah 13 (TC-FA-FAAM-842 butir iii pada client baris tabel)
47. Buka Activity Log FAMS
48. Ketik Search `Blocked Create Item`, tekan Enter
49. Verifikasi jumlah entri Activity Log FAMS `Blocked Create Item` sama dengan baseline pada langkah 16 (TC-FA-FAAM-842 butir iv pada client baris tabel)
50. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
51. Verifikasi jumlah entri Activity Log FAMS `Dell Latitude` sama dengan baseline pada langkah 18 (TC-FA-FAAM-842 butir iv pada client baris tabel)

## Notes

- P-5(a): spec ini kelas g; pemicu kelas h (Create dan Edit saat client Suspended atau Expired: TC-FA-FAAM-842) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Nama dan baseline milik spec ini sendiri.
- Di atas smell 35 langkah. Spec berisi 51 langkah tertulis yang diulang untuk baris Suspended lalu baris Expired (ekspansi 102 langkah). Alasan: satu TC (TC-FA-FAAM-842) tidak dipecah antar spec; TC membaca tiga surface log (Changelog, System Log, Activity Log FAMS) untuk dua nama setelah aksi Create dan Edit, yang masing-masing memerlukan navigasi dan satu Search per nama; kedua client tenant memakai langkah identik sehingga diulang per baris tabel, bukan dipecah per client.
- Langkah 23 dan 31 (status 403) menjadi anchor positif bahwa pemicu benar-benar mencapai server sebelum asersi absence berikutnya; pembanding tiap surface adalah jumlah awal yang dicatat pada langkah baseline.
- Langkah penghubung tanpa `Verifikasi`: seluruh langkah selain langkah berawalan `Verifikasi`, yaitu membuka dan mencari di Modal Changelog, Detail User aktor tab System Log, dan Activity Log FAMS (S-12, S-14), mencatat baseline, navigasi, mengirim pemicu, dan menutup form dirty secara deterministik (S-08).
- Urutan: urutan final per client (bukan per TC) agar login client tidak berulang; TC-FA-FAAM-842 menyebut "Ulangi langkah 1 sampai 3 pada Client Expired". Perubahan urutan ini dicatat sebagai keputusan penulis.
- Pembagian TC lintas spec: butir status penolakan dan state data TC-FA-FAAM-842 ada pada TC-FA-FAAM-619 dan 620 (spec 233). TC-FA-FAAM-843 ada di spec 254. TC-FA-FAAM-611 sampai 614 tetap di spec 247.
- Temuan untuk QA:
  - TC-FA-FAAM-842 meminta hitungan entri System Log dan Activity Log FAMS "yang memuat nama itu" lewat Search; TC tidak menyebut apakah tab System Log pada Detail User memiliki Search. Spec memakai Search pada ketiga surface; bila System Log tidak punya Search, hitungan perlu didefinisikan ulang.
  - Pre-setup No. 18 dan 18c tidak memuat email akun Total Control untuk client Suspended dan Expired; disediakan tim FE.
  - Nama `Blocked Create Item` pada client Suspended dan Expired memakai nama literal TC (sama dengan spec 233); baseline entri nama itu dan `Dell Latitude` bisa lebih dari nol.
