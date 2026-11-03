---
id: TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung
title: "Defense-in-depth Delete: Request Langsung Ditolak Constraint D-03 dan D-14 pada Client Active, Suspended, dan Archived, serta Delete Suspended Tanpa Riwayat Diizinkan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-465
  - TC-AC-ACC-653
  - TC-AC-ACC-654
  - TC-AC-ACC-655
  - TC-AC-ACC-978
  - TC-AC-ACC-979
  - TC-AC-ACC-1025
  - TC-AC-ACC-1026
  - TC-AC-ACC-981
  - TC-AC-ACC-455
coverage:
  web: automated
---

# Defense-in-depth Delete: Request Langsung Ditolak Constraint D-03 dan D-14 pada Client Active, Suspended, dan Archived, serta Delete Suspended Tanpa Riwayat Diizinkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun, Step ganti akun eksplisit):
  - Active-Delete-Only A-07 `activeDeleteJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_DELETE_PASSWORD` (Manage active client: Delete + Read, exact-match Area Jakarta dan Cabang Menteng); TC-AC-ACC-465, 653, 654, 655, 978, 979, 1025, 1026, 981. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Archived-Delete-Only A-10 `archivedDeleteJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ARCHIVED_DELETE_PASSWORD`; TC-AC-ACC-455.
  - Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup (hanya dibaca kecuali TC-AC-ACC-981; request ditolak sehingga data tidak berubah): C-01 `PT Sejahtera Abadi` (term Active); C-07 `PT Cahaya Baru` (FAMS Waiting for Approval); C-02 `PT Teknologi Maju` (FAMS Grace); C-LIF-5 `PT Berakhir Belum Aktivasi` (FAMS Expired); C-08 `PT Mulai Esok` (FAMS Pending); C-LIF-16 `PT Aktif Plus Menunggu` (FAMS Active, SAMS Waiting for Approval); C-FX12-1 `PT Suspend Langganan Aktif` (Suspended, FAMS Active), C-FX12-2 `PT Suspend Masa Tenggang` (Suspended, FAMS Grace), C-FX12-3 `PT Suspend Berakhir` (Suspended, FAMS Expired), C-FX12-4 `PT Suspend Menunggu Persetujuan` (Suspended, FAMS Waiting for Approval), C-FX12-5 `PT Suspend Mulai Terjadwal` (Suspended, FAMS Pending); C-FX17-5 `PT Trial Aktif Saja` (Active, SAMS Trial Active satu-satunya term); C-FX18-3 `PT Suspend Trial Menunggu` (Suspended, SAMS Trial Waiting for Approval). TC-AC-ACC-455: Client Archived dengan term Active yang disediakan tim FE (TC tidak menyebut Client; lihat Temuan). C-FX12-6 `PT Suspend Hapus Langsung` (Suspended, Direct, Group Area Jakarta, belum pernah memiliki subscription; Dikonsumsi: dihapus oleh TC-AC-ACC-981, di-seed ulang tanpa syarat oleh Fixture BE di hook `before` dan `after`).
- ID Client untuk request langsung diambil dari keluaran skrip seed atau respons API (ID opaque UUID). Body Delete: `companyName` = nama Client persis, `confirm` = true.
- Kemampuan teknis (kelas a): klien HTTP yang mengirim request langsung ke server dengan token sesi API milik aktor blok yang sedang login (disediakan tim FE/BE; sesi API tidak dihitung sebagai sesi web, dinyatakan di `suite.md`); membaca keberadaan Client lewat List.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Delete-Only (penolakan constraint)

#### TC-AC-ACC-465: Server menolak Delete dari Active/Suspended untuk Client yang pernah memiliki subscription

1. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Sejahtera Abadi` (Active, ada term)
2. Verifikasi request ditolak server dengan respons 422 karena Client masih memiliki subscription berjalan (D-03)
3. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Cahaya Baru` (term Waiting for Approval)
4. Verifikasi request ditolak server dengan respons 422 karena permintaan subscription masih diproses (D-14)
5. Klik sub-tab Active, ketik Search `PT Sejahtera Abadi`, tekan Enter
6. Verifikasi Client `PT Sejahtera Abadi` tidak terhapus: baris tetap tampil di sub-tab Active
7. Ganti isi Search dengan `PT Cahaya Baru`, tekan Enter
8. Verifikasi Client `PT Cahaya Baru` tidak terhapus: baris tetap tampil di sub-tab Active

#### TC-AC-ACC-653: Delete langsung untuk Client dengan term Grace atau Expired ditolak server dengan respons 422 (D-03)

9. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Teknologi Maju`
10. Verifikasi request ditolak server dengan respons 422 karena Client masih memiliki subscription berjalan (D-03, term Grace)
11. Klik sub-tab Active, ketik Search `PT Teknologi Maju`, tekan Enter
12. Verifikasi baris `PT Teknologi Maju` tetap tampil di sub-tab Active
13. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Berakhir Belum Aktivasi`
14. Verifikasi request ditolak server dengan respons 422 karena Client masih memiliki subscription berjalan (D-03, term Expired)
15. Ganti isi Search dengan `PT Berakhir Belum Aktivasi`, tekan Enter
16. Verifikasi baris `PT Berakhir Belum Aktivasi` tetap tampil di sub-tab Active

#### TC-AC-ACC-654: Delete langsung untuk Client dengan term Pending ditolak server dengan respons 422 (D-14)

17. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Mulai Esok`
18. Verifikasi request ditolak server dengan respons 422 karena permintaan subscription masih diproses (D-14, term Pending)
19. Klik sub-tab Active, ketik Search `PT Mulai Esok`, tekan Enter
20. Verifikasi baris `PT Mulai Esok` tetap tampil di sub-tab Active

#### TC-AC-ACC-655: Delete langsung untuk Client dengan term Active dan permintaan Waiting for Approval: respons 422 D-03 mendahului D-14 dan D-04

21. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Aktif Plus Menunggu`
22. Verifikasi request ditolak server dengan respons 422 karena Client masih memiliki subscription berjalan (D-03, mendahului D-14)
23. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Sejahtera Abadi`
24. Verifikasi request ditolak server dengan respons 422 karena Client masih memiliki subscription berjalan (D-03, mendahului D-04)
25. Ganti isi Search dengan `PT Aktif Plus Menunggu`, tekan Enter
26. Verifikasi baris `PT Aktif Plus Menunggu` tetap tampil
27. Ganti isi Search dengan `PT Sejahtera Abadi`, tekan Enter
28. Verifikasi baris `PT Sejahtera Abadi` tetap tampil

#### TC-AC-ACC-978: Delete langsung untuk Client Suspended dengan term Active, Grace, atau Expired ditolak constraint D-03, bukan 403 baku

29. Ambil token sesi aktif milik Active-Delete-Only (hasil login Precondition a)
30. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Langganan Aktif` memakai token sesi tersebut, tanpa melalui UI
31. Verifikasi request ditolak server dengan penolakan constraint D-03 (Client memiliki term Active), bukan 403 entitas Suspended
32. Klik sub-tab Suspended, ketik Search `PT Suspend Langganan Aktif`, tekan Enter
33. Verifikasi baris `PT Suspend Langganan Aktif` tetap tampil di sub-tab Suspended
34. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Masa Tenggang` memakai token sesi yang sama, tanpa melalui UI
35. Verifikasi request ditolak server dengan penolakan constraint D-03 (Client memiliki term Grace), bukan 403 entitas Suspended
36. Ganti isi Search dengan `PT Suspend Masa Tenggang`, tekan Enter
37. Verifikasi baris `PT Suspend Masa Tenggang` tetap tampil di sub-tab Suspended
38. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Berakhir` memakai token sesi yang sama, tanpa melalui UI
39. Verifikasi request ditolak server dengan penolakan constraint D-03 (Client memiliki term Expired), bukan 403 entitas Suspended
40. Ganti isi Search dengan `PT Suspend Berakhir`, tekan Enter
41. Verifikasi baris `PT Suspend Berakhir` tetap tampil di sub-tab Suspended

#### TC-AC-ACC-979: Delete langsung untuk Client Suspended dengan term Waiting for Approval atau Pending ditolak constraint D-14, bukan 403 baku

42. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Menunggu Persetujuan` memakai token sesi Active-Delete-Only, tanpa melalui UI
43. Verifikasi request ditolak server dengan penolakan constraint D-14 (Client memiliki term Waiting for Approval), bukan 403 entitas Suspended
44. Ganti isi Search dengan `PT Suspend Menunggu Persetujuan`, tekan Enter
45. Verifikasi baris `PT Suspend Menunggu Persetujuan` tetap tampil di sub-tab Suspended
46. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Mulai Terjadwal` memakai token sesi yang sama, tanpa melalui UI
47. Verifikasi request ditolak server dengan penolakan constraint D-14 (Client memiliki term Pending), bukan 403 entitas Suspended
48. Ganti isi Search dengan `PT Suspend Mulai Terjadwal`, tekan Enter
49. Verifikasi baris `PT Suspend Mulai Terjadwal` tetap tampil di sub-tab Suspended

#### TC-AC-ACC-1025: Delete langsung untuk Client Active dengan Trial Active sebagai satu-satunya term ditolak constraint D-03, dan Delete tidak tampil di row action

50. Klik sub-tab Active, ketik Search `PT Trial Aktif Saja`, tekan Enter
51. Klik `[⋯]` pada baris `PT Trial Aktif Saja` dan lihat daftar aksi
52. Verifikasi daftar aksi baris tidak memuat Delete
53. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Trial Aktif Saja` memakai token sesi Active-Delete-Only, tanpa melalui UI
54. Verifikasi request ditolak server (constraint D-03 untuk baris Trial Active); Client tidak terhapus
55. Ganti isi Search dengan `PT Trial Aktif Saja`, tekan Enter
56. Verifikasi baris `PT Trial Aktif Saja` tetap tampil di sub-tab Active

#### TC-AC-ACC-1026: Delete langsung ditolak server untuk Client Suspended dengan Trial Waiting for Approval (D-14, bukan 403 baku)

57. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Trial Menunggu` memakai token sesi Active-Delete-Only, tanpa melalui UI
58. Verifikasi request ditolak server dengan penolakan constraint D-14 untuk baris Trial Waiting for Approval, bukan 403 entitas Suspended; Client tidak terhapus
59. Klik sub-tab Suspended, ketik Search `PT Suspend Trial Menunggu`, tekan Enter
60. Verifikasi baris `PT Suspend Trial Menunggu` tetap tampil di sub-tab Suspended

#### TC-AC-ACC-981: Delete langsung untuk Client Suspended tanpa riwayat subscription diizinkan server: respons sukses, Client terhapus dan tercatat di Changelog (aksi menghabisi data, di akhir blok)

61. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Suspend Hapus Langsung` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Delete` (N0), lalu tutup modal
62. Ambil token sesi aktif milik Active-Delete-Only (hasil login Precondition a)
63. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Hapus Langsung` memakai token sesi tersebut, tanpa melalui UI
64. Verifikasi respons HTTP 200 (Delete diizinkan); bukan 403 Forbidden dan bukan penolakan constraint 409
65. Klik sub-tab Suspended, ketik Search `PT Suspend Hapus Langsung`, tekan Enter
66. Verifikasi baris `PT Suspend Hapus Langsung` tidak tampil di sub-tab Suspended
67. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Suspend Hapus Langsung` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu hitung baris Action `Delete` (N1)
68. Verifikasi jumlah baris Action `Delete` ber-Client Name `PT Suspend Hapus Langsung` bertambah tepat satu dibanding N0 (N1 = N0 + 1)
69. Verifikasi baris baru: Action `Delete`, Field `Company Name`, Old Value `PT Suspend Hapus Langsung`, New Value `—`
70. Tutup modal Changelog

### Blok 2: Archived-Delete-Only

71. Ganti akun: logout lalu login sebagai Archived-Delete-Only A-10

#### TC-AC-ACC-455: Delete Client Archived yang ternyata masih punya subscription Active ditolak (defense-in-depth)

72. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk Client Archived dengan term Active
73. Verifikasi request ditolak server dengan respons 422 karena Client masih memiliki subscription berjalan (D-03)
74. Klik sub-tab Archived dan ketik Search nama Client yang sama, tekan Enter
75. Verifikasi Client tidak terhapus: baris Client itu tetap tampil di sub-tab Archived

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: kesepuluh TC adalah kelas a dengan Expected berupa respons API dan state data; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`. Request langsung tidak melewati browser, sehingga asersi hanya kode/penolakan respons dan state data (bagian 8b butir 1); TC-AC-ACC-465, 653, 654, 655, dan 455 mengasersi respons 422 (D-03 atau D-14 sesuai tiap baris), tidak ada toast atau dialog yang diasersi.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas sepuluh TC satu kelas harness (kelas a, Delete langsung ditolak constraint) dengan dua akun; blok penolakan hanya membaca data, tiap blok memakai Client sendiri, dan satu-satunya aksi yang menghabisi data (TC-AC-ACC-981) ditaruh paling akhir di blok Active-Delete-Only (prinsip 5); ganti akun lewat Step eksplisit sah karena bagian sesudahnya tetap bermakna.
- Langkah penghubung (tanpa awalan Verifikasi): Search dan sub-tab untuk membaca keberadaan Client (R-16), langkah 29 (ambil token sesi, bagian TC-AC-ACC-978 langkah 1), langkah 61 (baseline jumlah baris Changelog Action `Delete`, N0, S-12), langkah 62 (ambil token sesi, TC-AC-ACC-981 langkah 2), langkah 63 (kirim Delete), langkah 67 (membuka Changelog dan menghitung N1 sesudah Delete), langkah 70 (menutup modal), dan langkah 71 (ganti akun). Asersi "Client tetap tampil" memakai hasil Search sebagai anchor positif; asersi absence baris pada langkah 66 berlandaskan respons 200 yang sudah diasersi (bagian 8b butir 2).
- Baseline (S-12): TC-AC-ACC-981 menyatakan baseline N0 (langkah 1 TC) dan Expected N1 = N0 + 1 (langkah 5 TC); Client `PT Suspend Hapus Langsung` di-seed ulang tiap run sehingga baris `Delete` lama bernama sama bisa ada. Spec menghitung jumlah baris Action `Delete` sebelum request (N0, langkah 61) dan sesudahnya (N1, langkah 67) dengan Search nama Client dan ukuran halaman 100, lalu mengasersi N1 = N0 + 1 (langkah 68) beserta Old/New Value baris baru (langkah 69).
- Pembagian TC lintas spec: TC-AC-ACC-465, 653, 654, 655, 978, 979, 1025, dan 1026 tidak punya Post Condition; TC-AC-ACC-981 ("Seed ulang C-FX12-6 tanpa syarat") dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-455 tidak menyebut Client Archived dengan term Active; spec memakai Client yang disediakan tim FE (TC-AC-ACC-1020 memakai C-FX17-4 `PT Arsip Trial Aktif` untuk UI).
  - TC-AC-ACC-978, 979, 1025, dan 1026 tidak menyebut kode status penolakan constraint; spec mengasersi "ditolak server (constraint ...)" untuk keempatnya.
