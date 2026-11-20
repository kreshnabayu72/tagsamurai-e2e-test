---
id: TC-FA-FASVC-E2E-079-storage-penuh-lampiran-baru-ditolak
title: "Storage Penuh: Lampiran Baru Ditolak pada Create dan Edit, Tanpa Lampiran Baru Tetap Berjalan"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["FASVC-LOGIC-13a", "FASVC-LOGIC-13b", "FASVC-LOGIC-13c", "V-FASVC-40", "ER-FASVC-10", "TS-FASVC-10", "EC-FASVC-60", "EC-FASVC-61", "EC-FASVC-62", "RX-FASVC-33", "F-FASVC-07.k4"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-13a": [8, 31, 58]
  "FASVC-LOGIC-13b": [36, 38, 48, 49, 76, 82]
  "FASVC-LOGIC-13c": [11, 12, 13, 18, 21, 59, 64, 65, 70]
  "V-FASVC-40": [8, 31, 58]
  "ER-FASVC-10": [11, 12, 13, 14, 34, 36, 42]
  "TS-FASVC-10": [8, 10, 31, 58]
  "EC-FASVC-60": [8, 11, 12, 18, 21, 59, 64, 65]
  "EC-FASVC-61": [48, 49]
  "EC-FASVC-62": [36, 76, 82]
  "RX-FASVC-33": [18, 21, 65, 70]
  "F-FASVC-07.k4": [8, 31, 58]
anchor: [41, 54, 69]
coverage:
  web: automated
---

# Storage Penuh: Lampiran Baru Ditolak pada Create dan Edit, Tanpa Lampiran Baru Tetap Berjalan

## Prerequisites
- Aktor: Total Control `Tegar Penuh {runId}` pada entitas khusus `Klien Storage Penuh {runId}`. Spec ini memakai entitas khusus yang tidak dipakai spec lain.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-079-1: Entitas `Klien Storage Penuh {runId}`, Status `Active`, kuota Storage `10.0 GB`, usage ledger Storage `10.0 GB` (usage sama dengan kuota), tidak dipakai spec lain.
  - DU-079-2: Aktor `Tegar Penuh {runId}` dengan Role `Total Control`, ada di entitas `Klien Storage Penuh {runId}`.
  - DU-079-3: Service Center `Servis Penuh Edit {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Batu Pahat {runId}`, Company phone `+60 7555220303`, Attachments `izin-lama-079.pdf` (PDF, 300 KB), ada di entitas `Klien Storage Penuh {runId}`.
  - DU-079-4: Service Center `Servis Penuh Tanpa Lampiran {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Muar {runId}`, Company phone `+60 7555220404`, tanpa Attachments, ada di entitas `Klien Storage Penuh {runId}`.
  - DU-079-5: Berkas `brosur-baru-079.pdf` (PDF, 500 KB) dan `izin-baru-079.pdf` (PDF, 400 KB), dilampirkan oleh langkah.
  - DU-079-6: Berkas `katalog-besar-079.pdf` (PDF, 11 MB), dilampirkan oleh langkah.
- Kondisi:
  - Storage entitas `Klien Storage Penuh {runId}` penuh sepanjang spec: Used Storage `10.0 GB` dan Storage Quota `10.0 GB`.
  - Lisensi addon Maintenance aktif untuk entitas `Klien Storage Penuh {runId}`.
  - Akun `Tegar Penuh {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Create dengan lampiran baru ditolak saat Storage penuh dan tidak membuat apa pun
1. Klik `[+ Service Center]`
2. Isi Name `Servis Penuh Batal {runId}`
3. Centang Service type `Routine`
4. Isi City `Pontian {runId}`
5. Isi Company phone dengan Dial Code `+60` dan nomor `7555220101`
6. Unggah berkas `brosur-baru-079.pdf` (PDF, 500 KB) pada Attachments
7. Klik `[Submit]`
8. Verifikasi toast `Error, failed to upload attachment. Storage is full (10.0 GB of 10.0 GB used).` tampil
9. Tunggu 10 detik tanpa menutup toast
10. Verifikasi toast `Error, failed to upload attachment. Storage is full (10.0 GB of 10.0 GB used).` masih tampil
11. Verifikasi dialog `Add Service Center` masih terbuka
12. Verifikasi field Name masih berisi `Servis Penuh Batal {runId}`
13. Verifikasi baris file `brosur-baru-079.pdf` masih tampil di Attachments
14. Verifikasi tidak ada pesan inline di bawah field `Attachments`
15. Tutup toast error secara manual
16. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
17. Ketik Search `Servis Penuh Batal {runId}`, tekan Enter
18. Verifikasi tabel menampilkan empty state `No results found`
19. Klik `[Changelog]`
20. Ketik Search `Servis Penuh Batal {runId}`, tekan Enter
21. Verifikasi tabel Changelog menampilkan empty state `No results found`
22. Klik ikon close pada modal `Changelog: Service Center`
23. Klik `(←)` pada kotak Search

### Lampiran dihapus dari baris lalu Submit tanpa lampiran berhasil
24. Klik `[+ Service Center]`
25. Isi Name `Servis Penuh Create {runId}`
26. Centang Service type `Routine`
27. Isi City `Kluang {runId}`
28. Isi Company phone dengan Dial Code `+60` dan nomor `7555220202`
29. Unggah berkas `brosur-baru-079.pdf` (PDF, 500 KB) pada Attachments
30. Klik `[Submit]`
31. Verifikasi toast `Error, failed to upload attachment. Storage is full (10.0 GB of 10.0 GB used).` tampil
32. Tutup toast error secara manual
33. Hapus berkas pada baris file `brosur-baru-079.pdf` lewat ikon hapus
34. Verifikasi baris file `brosur-baru-079.pdf` tidak tampil di Attachments
35. Klik `[Submit]`
36. Verifikasi toast `Success, Servis Penuh Create {runId} has been added.` tampil
37. Ketik Search `Servis Penuh Create {runId}`, tekan Enter
38. Verifikasi baris `Servis Penuh Create {runId}` tampil di tabel
39. Klik `[Changelog]`
40. Ketik Search `Servis Penuh Create {runId}`, tekan Enter
41. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Servis Penuh Create {runId}`
42. Verifikasi baris dengan Action `Attachment added` tidak tampil pada hasil Search `Servis Penuh Create {runId}`
43. Klik ikon close pada modal `Changelog: Service Center`
44. Klik `(←)` pada kotak Search

### Berkas di atas batas ukuran ditolak lebih dulu dan bukan sebagai Storage penuh
45. Klik `[+ Service Center]`
46. Isi Name `Servis Penuh Ukuran {runId}`
47. Unggah berkas `katalog-besar-079.pdf` (PDF, 11 MB) pada Attachments
48. Verifikasi pesan `File size must not exceed 1 MB.` tampil di bawah field `Attachments`
49. Verifikasi toast `Error, failed to upload attachment. Storage is full (10.0 GB of 10.0 GB used).` tidak tampil
50. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Edit yang mengganti lampiran ditolak saat Storage penuh dan lampiran lama tetap
51. Ketik Search `Servis Penuh Edit {runId}`, tekan Enter
52. Klik `⋯` pada baris `Servis Penuh Edit {runId}`
53. Klik `Edit`
54. Verifikasi baris file `izin-lama-079.pdf` tampil di Attachments
55. Hapus berkas pada baris file `izin-lama-079.pdf` lewat ikon hapus
56. Unggah berkas `izin-baru-079.pdf` (PDF, 400 KB) pada Attachments
57. Klik `[Save]`
58. Verifikasi toast `Error, failed to upload attachment. Storage is full (10.0 GB of 10.0 GB used).` tampil
59. Verifikasi dialog `Edit Service Center` masih terbuka
60. Tutup toast error secara manual
61. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
62. Klik `⋯` pada baris `Servis Penuh Edit {runId}`
63. Klik `Edit`
64. Verifikasi baris file `izin-lama-079.pdf` tampil di Attachments
65. Verifikasi baris file `izin-baru-079.pdf` tidak tampil di Attachments
66. Klik `✕` pada form yang belum diubah
67. Klik `[Changelog]`
68. Ketik Search `Servis Penuh Edit {runId}`, tekan Enter
69. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Servis Penuh Edit {runId}`
70. Verifikasi baris dengan Action `Attachment removed` tidak tampil pada hasil Search `Servis Penuh Edit {runId}`
71. Klik ikon close pada modal `Changelog: Service Center`

### Edit yang hanya menghapus lampiran tidak diblokir saat Storage penuh
72. Klik `⋯` pada baris `Servis Penuh Edit {runId}`
73. Klik `Edit`
74. Hapus berkas pada baris file `izin-lama-079.pdf` lewat ikon hapus
75. Klik `[Save]`
76. Verifikasi toast `Success, Servis Penuh Edit {runId} has been updated.` tampil

### Edit tanpa lampiran baru tidak diblokir saat Storage penuh
77. Ganti isi kotak search dengan `Servis Penuh Tanpa Lampiran {runId}`, tekan Enter
78. Klik `⋯` pada baris `Servis Penuh Tanpa Lampiran {runId}`
79. Klik `Edit`
80. Ganti isi City dengan `Segamat {runId}`
81. Klik `[Save]`
82. Verifikasi toast `Success, Servis Penuh Tanpa Lampiran {runId} has been updated.` tampil
