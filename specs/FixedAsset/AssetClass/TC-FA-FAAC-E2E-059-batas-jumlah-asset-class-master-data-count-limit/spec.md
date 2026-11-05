---
id: TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit
title: "Batas Jumlah Asset Class: Dialog Blok Asset Class Limit Reached pada Master Data Count Limit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-134
  - TC-FA-FAAC-135
  - TC-FA-FAAC-136
  - TC-FA-FAAC-137
  - TC-FA-FAAC-147
  - TC-FA-FAAC-267
coverage:
  web: automated
---

# Batas Jumlah Asset Class: Dialog Blok Asset Class Limit Reached pada Master Data Count Limit

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: plan client (Enterprise, Professional, Growth) dan Master Data Count Limit (Admin Console > Plans & Licensing > Lifecycle Settings). Akun atau mekanisme pelaku perubahan ini tidak disebut TC, PRD, atau LLD; fixture BE untuk mengatur plan dan Master Data Count Limit "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Hook `before` mencatat nilai awal dan hook `after` memulihkan plan dan Master Data Count Limit awal lewat fixture BE, juga bila spec gagal di tengah. Suite berjalan serial.
- Data Pre-setup: Asset Class `B-ANCHOR` (Active) sebagai sumber Duplicate (tidak diubah); Asset Class `B-DEL7` tanpa Asset Name dan belum pernah diposting (dihapus pada langkah 20). Seed disediakan fixture BE.
- Data yang dibuat spec: Asset Class `B-CAP` (langkah 36 dan 37), `B-FORM` (diisi pada langkah 45 tetapi tidak pernah tersimpan), dan `B-CAPRACE` (dibuat sesi API aktor pada langkah 46). Kode literal karena Class Code dibatasi 15 karakter (lihat Notes). Hook `before` menghapus ketiganya bila sisa run sebelumnya masih ada dan hook `after` menghapus yang dibuat spec ini lewat fixture BE.
- Kemampuan teknis: membaca jumlah Asset Class dan jumlah entri Changelog Asset Class, System Log aktor, dan Activity Log FAMS lewat fixture BE (audit trail permanen; asersi memakai selisih terhadap baseline, bukan angka absolut); sesi API aktor sebagai pelaku kedua yang hanya memicu perubahan state (dinyatakan di suite.md).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.

## Test Steps

### TC-FA-FAAC-134: Klik + Asset Class tepat saat jumlah Asset Class sama dengan batas

1. Atur lewat fixture BE: plan client `Enterprise` dan Master Data Count Limit sama dengan jumlah Asset Class saat ini (semua status dihitung); catat jumlah entri Changelog Asset Class (N1), System Log aktor (Ns1), dan Activity Log FAMS (Na1); muat ulang halaman
2. Klik tombol `[+ Asset Class]` di toolbar tabel
3. Verifikasi Dialog Blok `Asset Class Limit Reached` muncul dengan teks `You've reached the platform limit of {batas} asset classes. Contact support if you need a higher limit.` ({batas} berisi nilai batas yang diset) dan tombol `OK`
4. Verifikasi halaman Detail tidak dibuka
5. Verifikasi jumlah entri Changelog Asset Class tetap N1 (tidak ada log)
6. Verifikasi jumlah entri System Log aktor tetap Ns1 (tidak ada log)
7. Verifikasi jumlah entri Activity Log FAMS tetap Na1 (tidak ada log)
8. Klik `[OK]`
9. Verifikasi dialog menutup
10. Verifikasi tetap di tabel Asset Class

### TC-FA-FAAC-267: Duplicate saat batas jumlah Asset Class tercapai

11. Ketik Search `B-ANCHOR`, tekan Enter
12. Klik ikon `⋯` pada baris `B-ANCHOR` lalu pilih `Duplicate`
13. Verifikasi Dialog Blok `Asset Class Limit Reached` dengan teks `You've reached the platform limit of {batas} asset classes. Contact support if you need a higher limit.` dan tombol `OK`
14. Verifikasi halaman Detail tidak dibuka
15. Klik `[OK]`

### TC-FA-FAAC-147: Delete membebaskan kapasitas sehingga Create berikutnya diizinkan

16. Klik tombol `[+ Asset Class]` di toolbar tabel
17. Verifikasi Dialog Blok `Asset Class Limit Reached` muncul
18. Klik `[OK]`
19. Ganti isi kotak search dengan `B-DEL7`, tekan Enter
20. Hapus `B-DEL7` lewat row action Delete lalu konfirmasi
21. Tunggu aksi selesai
22. Klik tombol `[+ Asset Class]` di toolbar tabel
23. Verifikasi halaman Detail mode Create terbuka
24. Verifikasi tidak ada dialog blok
25. Klik breadcrumb `Asset Class` untuk kembali ke tabel

### TC-FA-FAAC-136: Klik + Asset Class saat batas lebih kecil dari jumlah Asset Class yang ada

26. Atur lewat fixture BE: plan client `Professional` dan Master Data Count Limit lebih kecil satu dari jumlah Asset Class saat ini; catat jumlah Asset Class (C); muat ulang halaman
27. Klik tombol `[+ Asset Class]` di toolbar tabel
28. Verifikasi Dialog Blok `Asset Class Limit Reached` muncul dengan batas yang diset
29. Verifikasi halaman Detail tidak dibuka
30. Verifikasi jumlah Asset Class tetap C (Asset Class yang sudah ada tidak berubah)
31. Klik `[OK]`

### TC-FA-FAAC-135: Klik + Asset Class saat sisa kapasitas tepat satu

32. Atur lewat fixture BE: plan client `Growth` dan Master Data Count Limit sama dengan jumlah Asset Class saat ini ditambah 1; muat ulang halaman
33. Klik tombol `[+ Asset Class]` di toolbar tabel
34. Verifikasi halaman Detail mode Create terbuka
35. Verifikasi tidak ada Dialog Blok
36. Isi Class Code `B-CAP`, Class Name `Capacity Fixture`, Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`
37. Klik `[Submit]`
38. Tunggu aksi selesai
39. Klik breadcrumb `Asset Class` untuk kembali ke tabel
40. Klik tombol `[+ Asset Class]` di toolbar tabel
41. Verifikasi Dialog Blok `Asset Class Limit Reached` muncul
42. Klik `[OK]`

### TC-FA-FAAC-137: Batas jumlah tercapai antara klik + Asset Class dan Submit

43. Atur lewat fixture BE: Master Data Count Limit sama dengan jumlah Asset Class saat ini ditambah 1; muat ulang halaman
44. Klik tombol `[+ Asset Class]` di toolbar tabel
45. Isi Class Code `B-FORM`, Class Name `Form Fixture`, Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`; jangan klik `[Submit]`
46. Sesi API aktor membuat satu Asset Class `B-CAPRACE` hingga tersimpan sehingga jumlah mencapai batas
47. Tunggu aksi selesai, lalu catat jumlah Asset Class (C2) serta jumlah entri Changelog Asset Class (N2), System Log aktor (Ns2), dan Activity Log FAMS (Na2) lewat fixture BE
48. Kembali ke form dan klik `[Submit]`
49. Verifikasi Submit ditolak dengan Dialog Blok `Asset Class Limit Reached` dan tombol `OK`
50. Verifikasi halaman Detail tetap terbuka dengan isian utuh
51. Verifikasi tidak ada Asset Class dibuat (jumlah Asset Class tetap C2)
52. Verifikasi jumlah entri Changelog Asset Class tetap N2 (tidak ada log)
53. Verifikasi jumlah entri System Log aktor tetap Ns2 (tidak ada log)
54. Verifikasi jumlah entri Activity Log FAMS tetap Na2 (tidak ada log)
55. Klik `[OK]`
56. Klik breadcrumb `Asset Class`
57. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
58. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-134, 135, 136, 137, 147, 267). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-134, 267, dan 147 berbagi state "batas sama dengan jumlah saat ini" sehingga satu kali pengaturan fixture; TC-147 (Delete) terakhir dalam blok itu (aksi menghapus di akhir, S-10); TC-136 dan blok "batas + 1" (TC-135 lalu TC-137) mengatur state sendiri.
- Spec ini 58 langkah, di atas 35 langkah. Alasan: keenam TC satu topik (batas jumlah Asset Class pada Master Data Count Limit), tiap blok mengatur state batasnya sendiri lewat fixture BE dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1, 26, 32, dan 43 (mengatur state fixture, mencatat baseline, dan memuat ulang halaman agar batas terbaca), langkah 11 dan 19 (Search untuk menemukan baris target; langkah 19 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya, 8b.9), langkah 8, 15, 18, 31, dan 42 (menutup Dialog Blok), langkah 21, 38, dan 47 ("Tunggu aksi selesai"), langkah 25, 39 (kembali ke tabel), langkah 55 sampai 58 (menutup form dirty lewat dialog `Unsaved Changes`, S-08; langkah 57 adalah `Verifikasi` dialog yang diwajibkan S-08). Langkah 46 memakai sesi API aktor (R-20), bukan konteks kedua kelas c.
- "Tidak ada log" pada langkah 5 sampai 7 dan 52 sampai 54 adalah asersi selisih jumlah terhadap baseline di tiga surface (Changelog Asset Class, System Log aktor, Activity Log FAMS; S-12, prinsip 13g), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC-135 dan TC-137 tidak menyebut Class Code, Class Name, dan nilai field wajib untuk "satu Asset Class valid"; spec memakai nilai valid dari TC lain (Method `Straight Line`, Useful Life `60`, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`) dengan Class Code literal.
  - Class Code `B-CAP`, `B-FORM`, dan `B-CAPRACE` (bukan `B-RACE`, yang dipakai spec 089 sebagai seed bersama) ditulis literal tanpa suffix `{runId}-<NNN>` karena Class Code dibatasi 15 karakter sehingga suffix itu tidak muat (S-12, nama literal; pola spec 047 dan 048); cleanup di hook `before` dan `after`.
  - TC-136 Expected b ("Asset Class yang sudah ada tidak berubah") tidak menyebut cara pengamatan; spec membandingkan jumlah Asset Class terhadap baseline.
  - TC-267 dan TC-147 tidak menyebut plan client; spec mempertahankan plan dari blok sebelumnya (`Enterprise`).
  - TC-137 menandai dirinya "Manual Only (d) dua sesi paralel"; sesi kedua diganti sesi API aktor karena hanya memicu perubahan state (keputusan 2026-10-21/30), jadi tidak masuk kelas c.
