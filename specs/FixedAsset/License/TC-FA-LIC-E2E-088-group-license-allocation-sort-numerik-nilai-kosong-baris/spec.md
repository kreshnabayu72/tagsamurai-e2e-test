---
id: TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris
title: "Group License Allocation: Sort Numerik, Nilai Kosong, Baris Bernilai Sama, dan Reset State Saat Ganti Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-306
  - TC-FA-LIC-309
  - TC-FA-LIC-310
  - TC-FA-LIC-311
  - TC-FA-LIC-512
coverage:
  web: automated
---

# Group License Allocation: Sort Numerik, Nilai Kosong, Baris Bernilai Sama, dan Reset State Saat Ganti Node

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; hierarki Produksi, Kantor Pusat (Divisi Logistik (Allocated 500, Used 350), Divisi IT (Allocated 100, Used 60), Divisi Keuangan (belum beralokasi `—`, Used 0)), Cabang Surabaya, Cabang Medan. Tabel Group License Allocation pada node All Groups menampilkan empat baris level 1; urutan default Used by This Group tertinggi: Produksi (Used 1450, Allocated Quota 1.500), Cabang Medan, Cabang Surabaya, Kantor Pusat (Used 700, Allocated Quota 1.500). Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data untuk TC-FA-LIC-311: variasi Pre-setup #12 dengan node Kantor Pusat memiliki 12 child (fixture), kode grup berawalan `GRP-`, sehingga tabel child Kantor Pusat punya halaman kedua. Penerapan dan pemulihan variasi ini mengikuti pernyataan fixture BE pemulih Pre-setup #12 di `suite.md` dan dilakukan lewat langkah penghubung.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Tabel "Sort numerik per kolom" (parameter langkah 2 sampai 7); klik 3 selalu kembali ke urutan default Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat:

  | Kolom | Klik 1 (Ascending `↑`) | Klik 2 (Descending `↓`) |
  |---|---|---|
  | Allocated Quota | Cabang Surabaya, Cabang Medan, Produksi, Kantor Pusat | Produksi, Kantor Pusat, Cabang Medan, Cabang Surabaya |
  | Allocated to Subgroups | Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat | Kantor Pusat, Produksi, Cabang Medan, Cabang Surabaya |
  | Used by This Group | Kantor Pusat, Cabang Surabaya, Cabang Medan, Produksi | Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat |
  | Reserved by This Group | Cabang Medan, Kantor Pusat, Produksi, Cabang Surabaya | Cabang Surabaya, Produksi, Cabang Medan, Kantor Pusat |
  | Remaining Quota | Cabang Surabaya, Produksi, Cabang Medan, Kantor Pusat | Kantor Pusat, Cabang Medan, Produksi, Cabang Surabaya |
  | + Audit | Cabang Surabaya, Kantor Pusat, Cabang Medan, Produksi | Produksi, Cabang Medan, Kantor Pusat, Cabang Surabaya |
  | + Tracking | Cabang Surabaya, Kantor Pusat, Cabang Medan, Produksi | Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat |
  | + Maintenance Routine | Cabang Surabaya, Kantor Pusat, Cabang Medan, Produksi | Produksi, Cabang Medan, Kantor Pusat, Cabang Surabaya |
  | + Repair Ticketing | Cabang Surabaya, Kantor Pusat, Cabang Medan, Produksi | Produksi, Cabang Medan, Kantor Pusat, Cabang Surabaya |
  | + IT Inventory | Cabang Surabaya, Kantor Pusat, Cabang Medan, Produksi | Produksi, Cabang Medan, Kantor Pusat, Cabang Surabaya |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12.

## Test Steps

### TC-FA-LIC-306: Sort siklus 3-state per kelas kolom numerik kuota dan addon

1. Klik tab Allocation Quota di node All Groups
2. Untuk setiap baris tabel "Sort numerik per kolom" (langkah 2 sampai 7): klik header kolom pada baris itu sekali
3. Verifikasi urutan baris klik 1 sesuai tabel dengan indikator `↑`
4. Klik header kolom yang sama sekali lagi
5. Verifikasi urutan baris klik 2 sesuai tabel dengan indikator `↓`
6. Klik header kolom yang sama sekali lagi
7. Verifikasi urutan kembali ke default: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat

### TC-FA-LIC-512: Sort siklus 3-state kolom + Maps (semua nilai `—`)

8. Klik header kolom `+ Maps` sekali
9. Verifikasi urutan klik 1 `↑`: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
10. Klik header kolom `+ Maps` sekali lagi
11. Verifikasi urutan klik 2 `↓`: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
12. Klik header kolom `+ Maps` sekali lagi
13. Verifikasi urutan kembali ke default: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat (semua nilai sama `—`, baris bernilai sama mengikuti default sort Used by This Group tertinggi)

### TC-FA-LIC-310: Baris bernilai sama mengikuti default sort lalu identifier

14. Klik header kolom `Allocated Quota` sekali
15. Verifikasi Produksi (Used 1450) berada sebelum Kantor Pusat (Used 700) pada arah `↑` karena tie-break default sort Used by This Group tertinggi
16. Klik header kolom `Allocated Quota` sekali lagi
17. Verifikasi Produksi (Used 1450) berada sebelum Kantor Pusat (Used 700) pada arah `↓` karena tie-break default sort Used by This Group tertinggi
18. Klik header kolom `Allocated Quota` sekali lagi hingga sort netral

### TC-FA-LIC-309: Nilai kosong `—` di akhir saat Ascending dan di awal saat Descending

19. Klik node `Kantor Pusat`
20. Pada Child Groups Quota klik header `Allocated Quota` sekali
21. Verifikasi klik 1 (Ascending): Divisi IT (100), Divisi Logistik (500), Divisi Keuangan (`—`) di akhir
22. Klik header `Allocated Quota` sekali lagi
23. Verifikasi klik 2 (Descending): Divisi Keuangan (`—`) di awal, Divisi Logistik, Divisi IT
24. Klik header `Allocated Quota` sekali lagi
25. Verifikasi klik 3 urutan default Used by This Group tertinggi: Divisi Logistik (350), Divisi IT (60), Divisi Keuangan (0)

### Pindah ke variasi Pre-setup #12 dengan 12 child pada Kantor Pusat

26. Terapkan variasi Pre-setup #12 dengan 12 child pada node Kantor Pusat
27. Klik menu License pada sidebar, lalu tab Allocation Quota di node All Groups

### TC-FA-LIC-311: Ganti node Sidebar mereset Search, Filter, Sort, dan paginasi

28. Ketik Search `GRP-`, tekan Enter
29. Klik header `Allocated Quota` sekali
30. Klik node `Kantor Pusat` pada Sidebar
31. Verifikasi setelah ganti node kotak Search kosong
32. Verifikasi setelah ganti node tidak ada filter yang aktif (ikon Filter tanpa badge titik)
33. Verifikasi setelah ganti node Sort kembali ke Used by This Group Highest first
34. Verifikasi setelah ganti node tabel di halaman 1
35. Ketik Search `GRP-`, tekan Enter
36. Klik header `Allocated Quota` sekali
37. Pindah ke halaman 2
38. Klik node `All Groups` pada Sidebar
39. Verifikasi state tidak terbawa saat kembali ke All Groups: kotak Search kosong
40. Verifikasi state tidak terbawa saat kembali ke All Groups: tidak ada filter yang aktif
41. Verifikasi state tidak terbawa saat kembali ke All Groups: Sort Used by This Group Highest first
42. Verifikasi state tidak terbawa saat kembali ke All Groups: tabel di halaman 1

## Notes

- Langkah penghubung tanpa `Verifikasi`: mengembalikan sort ke netral di akhir TC-FA-LIC-310 (S-09), membuka node `Kantor Pusat`, dan blok "Pindah ke variasi Pre-setup #12 dengan 12 child pada Kantor Pusat" (menerapkan variasi lalu membuka ulang tab lewat sidebar yang mereset Search, Sort, dan Filter).
- Blok ulang: langkah 2 sampai 7 dijalankan 10 kali. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok adalah Sort satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA: (1) TC-FA-LIC-311 menyuruh "pindah ke halaman 2 jika ada" pada node All Groups yang hanya berisi empat baris; langkah bersyarat dilarang, sehingga spec membangun state halaman 2 pada node Kantor Pusat dengan 12 child. (2) TC-FA-LIC-310 butir a menambah "urutan deterministik antar halaman" tanpa data dua halaman; tidak diasersi.
