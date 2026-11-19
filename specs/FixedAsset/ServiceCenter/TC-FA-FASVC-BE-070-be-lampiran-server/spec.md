---
id: TC-FA-FASVC-BE-070-be-lampiran-server
title: "Server: Lampiran: Ukuran, Tipe, Jumlah, dan Komit Bersama Create atau Edit"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["V-FASVC-12", "V-FASVC-37", "V-FASVC-38", "FLD-FASVC-18", "EC-FASVC-21a", "EC-FASVC-21b", "EC-FASVC-21c", "RS-FASVC-05a", "RS-FASVC-05b", "RS-FASVC-05c", "RS-FASVC-06", "F-FASVC-07.k1", "F-FASVC-07.k3", "F-FASVC-07.k2", "§6#p2"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-12": [19, 35]
  "V-FASVC-37": [17, 30, 33]
  "V-FASVC-38": [21, 37]
  "FLD-FASVC-18": [7, 19, 26, 30, 31, 47]
  "EC-FASVC-21a": [19, 35]
  "EC-FASVC-21b": [17, 33]
  "EC-FASVC-21c": [39]
  "RS-FASVC-05a": [24]
  "RS-FASVC-05b": [4, 9, 49]
  "RS-FASVC-05c": [21, 37]
  "RS-FASVC-06": [41, 43, 49, 52, 56]
  "F-FASVC-07.k1": [17, 19]
  "F-FASVC-07.k3": [21, 37]
  "F-FASVC-07.k2": [60]
  "§6#p2": [4, 7, 14]
anchor: []
---

# Server: Lampiran: Ukuran, Tipe, Jumlah, dan Komit Bersama Create atau Edit

## Prerequisites
- Aktor: Total Control pada client suite.
- Data:
  - DU-070-1: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `admin@sejukabadi.co.id`, Status `Active`, dengan satu lampiran `izin-usaha-sejuk.pdf` (PDF, 500 KB), ada di client suite.
  - Setiap Create yang dikirim memuat field wajib lain bernilai Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `info@gensetberkas.co.id`, kecuali yang disebut di langkah; Name dikirim sesuai langkah.
  - Setiap Edit yang dikirim memuat versi data terkini dan nilai tersimpan untuk semua field selain yang disebut di langkah.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.

## Test Steps
### Berkas baru dilampirkan dan dicatat hanya saat Create dikomit
1. Baca Changelog Service Center dengan Service Center Name `Sentral Genset Perkasa {runId}` dan catat jumlah entrinya sebagai L0
2. Unggah berkas `sertifikat-kalibrasi-genset.pdf` (PDF, 500 KB) tanpa mengirim Create
3. Baca ulang Changelog Service Center dengan Service Center Name `Sentral Genset Perkasa {runId}`
4. Verifikasi jumlah entri tetap L0, sehingga unggahan berkas belum menulis `Attachment added`
5. Kirim Create dengan Name `Sentral Genset Perkasa {runId}` dan lampiran `sertifikat-kalibrasi-genset.pdf` (PDF, 500 KB)
6. Baca `Sentral Genset Perkasa {runId}` dari daftar dengan pencarian `Sentral Genset Perkasa {runId}`
7. Verifikasi Service Center memiliki tepat satu lampiran yang berasal dari berkas `sertifikat-kalibrasi-genset.pdf`
8. Baca Changelog Service Center dengan Service Center Name `Sentral Genset Perkasa {runId}`
9. Verifikasi Changelog memuat entri Action `Attachment added` dengan New Value nama berkas pada lampiran tersimpan

### Berkas staging yang tidak dirujuk dibersihkan setelah lebih dari 24 jam
10. Unggah berkas `brosur-layanan-genset.pdf` (PDF, 500 KB) tanpa Create atau Save yang merujuknya
11. Waktu berlalu sampai 24 jam 1 menit sejak berkas `brosur-layanan-genset.pdf` diunggah, dan job pembersihan berkas staging berjalan
12. Kirim Create dengan Name `Karya Genset Mandiri {runId}` dan lampiran `brosur-layanan-genset.pdf` yang diunggah 24 jam 1 menit sebelumnya
13. Baca daftar Service Center client suite dengan pencarian `Karya Genset Mandiri {runId}`
14. Verifikasi tidak ada Service Center di hasil pencarian yang memiliki lampiran yang berasal dari berkas `brosur-layanan-genset.pdf`, karena berkas staging berumur lebih dari 24 jam tanpa rekaman yang merujuk sudah dibersihkan

### Ukuran, tipe, dan jumlah lampiran yang melanggar ditolak pada Create
15. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N0
16. Kirim Create dengan Name `Mega Mekanik Pratama {runId}` dan lampiran `kontrak-servis.docx` (DOCX, 200 KB)
17. Verifikasi permintaan ditolak dengan pesan `Select a PDF, JPG, or PNG file.`
18. Kirim Create dengan Name `Tirta Servis Utama {runId}` dan lampiran `brosur-layanan-11mb.pdf` (PDF, 11 MB)
19. Verifikasi permintaan ditolak dengan pesan `File size must not exceed 1 MB.`
20. Kirim Create dengan Name `Harapan Baru Teknik {runId}` dan dua lampiran `izin-usaha-sejuk.pdf` (PDF, 500 KB) dan `sertifikat-kalibrasi.pdf` (PDF, 400 KB)
21. Verifikasi permintaan ditolak dengan pesan `Up to 1 file.`
22. Unggah berkas `izin-usaha-sejuk.pdf` (PDF, 500 KB) dua kali
23. Kirim Create dengan Name `Cakrawala Servis Mandiri {runId}` dan kedua hasil unggahan itu sebagai lampiran
24. Verifikasi permintaan ditolak dengan pesan `Up to 1 file.`, karena setiap unggahan dihitung sebagai berkas tersendiri
25. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
26. Verifikasi jumlah baris tetap N0, sehingga keempat permintaan tidak membuat Service Center

### Lampiran JPG dan PNG diterima pada Create
27. Kirim Create dengan Name `Bengkel Maju Motor {runId}` dan lampiran `foto-bengkel-utama.jpg` (JPG, 300 KB)
28. Kirim Create dengan Name `Lab Kalibrasi Pratama {runId}` dan lampiran `denah-lokasi-servis.png` (PNG, 200 KB)
29. Baca daftar Service Center client suite dengan pencarian `{runId}`
30. Verifikasi `Bengkel Maju Motor {runId}` memiliki tepat satu lampiran yang berasal dari berkas `foto-bengkel-utama.jpg`
31. Verifikasi `Lab Kalibrasi Pratama {runId}` memiliki tepat satu lampiran yang berasal dari berkas `denah-lokasi-servis.png`

### Edit dengan lampiran yang melanggar ditolak dan lampiran lama tetap
32. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan lampiran diganti `kontrak-servis.docx` (DOCX, 200 KB)
33. Verifikasi permintaan ditolak dengan pesan `Select a PDF, JPG, or PNG file.`
34. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan lampiran diganti `brosur-layanan-11mb.pdf` (PDF, 11 MB)
35. Verifikasi permintaan ditolak dengan pesan `File size must not exceed 1 MB.`
36. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan lampiran `izin-usaha-sejuk.pdf` dipertahankan dan `sertifikat-kalibrasi.pdf` (PDF, 400 KB) ditambahkan
37. Verifikasi permintaan ditolak dengan pesan `Up to 1 file.`
38. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
39. Verifikasi Service Center tetap memiliki tepat satu lampiran yang berasal dari berkas `izin-usaha-sejuk.pdf`
40. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan lampiran `izin-usaha-sejuk.pdf` dihapus dan Country diganti `Atlantis`
41. Verifikasi Save ditolak dengan pesan `Select a valid country` walau lampiran ikut dihapus pada permintaan yang sama
42. Baca ulang `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
43. Verifikasi Service Center tetap memiliki lampiran yang berasal dari berkas `izin-usaha-sejuk.pdf`, karena penghapusan lampiran dikomit bersama Save yang ditolak

### Lampiran diganti dan dihapus saat Edit dikomit
44. Baca Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entri Action `Attachment added` sebagai L1 dan jumlah entri Action `Attachment removed` sebagai L2
45. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan lampiran `izin-usaha-sejuk.pdf` diganti `logo-sejuk-abadi.png` (PNG, 150 KB)
46. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
47. Verifikasi Service Center memiliki tepat satu lampiran yang berasal dari berkas `logo-sejuk-abadi.png`
48. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
49. Verifikasi jumlah entri Action `Attachment added` bertambah satu dari L1 dan jumlah entri Action `Attachment removed` bertambah satu dari L2, ditulis saat Edit dikomit
50. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan lampiran `logo-sejuk-abadi.png` dihapus
51. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
52. Verifikasi Service Center tersimpan tanpa lampiran
53. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entri Action `Attachment removed` sebagai L3
54. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` yang sama dengan lampiran tetap dikosongkan
55. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
56. Verifikasi jumlah entri Action `Attachment removed` tetap L3, karena Edit yang mengulang keadaan yang sudah tercapai tidak menulis entri kedua

### Unggah yang ditolak tidak menulis Attachment added
57. Baca Changelog Service Center dengan Service Center Name `Bengkel Tanpa Lampiran {runId}` dan catat jumlah entri Action `Attachment added` sebagai L4
58. Kirim Create dengan Name `Bengkel Tanpa Lampiran {runId}` tanpa lampiran, setelah unggahan `brosur-layanan-11mb.pdf` (PDF, 11 MB) ditolak
59. Baca ulang Changelog Service Center dengan Service Center Name `Bengkel Tanpa Lampiran {runId}`
60. Verifikasi jumlah entri Action `Attachment added` tetap L4, karena `Attachment added` hanya ditulis bila unggah berhasil
