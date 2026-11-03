---
id: TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean
title: "Renew: Blokir, Clear Field, dan Nilai Clean"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-163
  - TC-AC-CS-167
  - TC-AC-CS-159
  - TC-AC-CS-158
  - TC-AC-CS-157
coverage:
  web: automated
---

# Renew: Blokir, Clear Field, dan Nilai Clean

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; tidak ada Submit sukses pada spec ini):
  - TC-AC-CS-163 dan 167: Client `Warung Kopi Senja A+{runId}-041`, FAMS plan Professional, status Active, 01/09/25 sampai 31/08/26, Plan Owner PT Maju Bersama (Distributor), tanpa successor (padanan Pre-setup #69).
  - TC-AC-CS-159: Client `PT Sejahtera+{runId}-041` dengan term paid FAMS Active (`SUBS-20260101-00001` padanan) dan trial FAMS Enterprise (badge Trial) Active 10/08/26 sampai 08/09/26, Plan Owner PT ABC (Principal) (padanan Pre-setup #38 dan #60).
  - TC-AC-CS-158: Client `Warung Kopi Senja B+{runId}-041` (kondisi sama seperti A).
  - TC-AC-CS-157: Client `Toko Serba Ada+{runId}-041` dengan predecessor FAMS plan Professional Active 01/09/25 sampai 31/08/26, Plan Owner PT Maju Bersama, tanpa successor pada awal TC (padanan Pre-setup #68); successor FAMS plan Enterprise Waiting for Approval, tanggal "—" (padanan Pre-setup #67) dibuat lewat sesi API pada langkah 33.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; sesi API aktor Principal): mengarsipkan term predecessor hingga tersimpan (TC-AC-CS-158); membuat successor Renewal Waiting for Approval hingga tersimpan (TC-AC-CS-157); membaca jumlah term per Client lewat fixture BE.

## Test Steps

### TC-AC-CS-163: Clear Field pada Renew tidak mengosongkan field terkunci

1. Ketik Search `Warung Kopi Senja A+{runId}-041`, tekan Enter
2. Klik `Renew` pada baris term Active, lalu isi Duration `3`
3. Klik `[Clear Field]`
4. Verifikasi Duration dikosongkan
5. Verifikasi Client `Warung Kopi Senja A+{runId}-041` dan Product `FAMS` tetap terisi dan Disabled
6. Verifikasi modal tetap terbuka tanpa dialog konfirmasi

### TC-AC-CS-167: Nilai dikembalikan identik dengan snapshot dianggap clean saat ditutup

7. Isi Duration `1`
8. Ubah Duration menjadi `3`, lalu kembalikan ke `1`
9. Klik `[✕]` pada header modal
10. Verifikasi dialog Unsaved Changes tidak muncul
11. Verifikasi modal tertutup
12. Klik `(←)` pada kotak Search

### TC-AC-CS-159: Row action dan tombol Detail Renew enabled dan membuka dialog blok V-27

13. Ketik Search `PT Sejahtera+{runId}-041`, tekan Enter
14. Klik ikon `⋯` pada baris term paid FAMS Active
15. Verifikasi item `Renew` tampil enabled, tanpa Disabled dan tanpa tooltip
16. Klik item `Renew`
17. Verifikasi dialog blok (Modal Imperative Alert) dengan Title "Cannot Renew Subscription", body bullet "• PT Sejahtera+{runId}-041 — FAMS", kalimat "This client has an active trial. Use Convert on the trial row.", dan tombol tunggal `[OK]`
18. Klik `[OK]`
19. Verifikasi form Renew tidak terbuka dan jumlah term Client tetap (tidak ada term baru, dibaca lewat fixture BE)
20. Buka Detail term paid FAMS Active dengan klik baris, lalu klik tombol Renew pada card Subscription Info
21. Verifikasi dialog blok tampil sama dengan row action (Title "Cannot Renew Subscription", body bullet, kalimat, dan tombol tunggal `[OK]`)
22. Klik `[OK]`, lalu buka Allocation > Client Subscription dari sidebar

### TC-AC-CS-158: Renew ditolak saat predecessor sudah tidak eligible

23. Ketik Search `Warung Kopi Senja B+{runId}-041`, tekan Enter
24. Klik `Renew` pada baris term Active, lalu isi Duration `1`
25. Arsipkan term predecessor lewat sesi API aktor hingga status Archive tersimpan
26. Klik `[Submit]`
27. Verifikasi dialog blok dengan Title "Cannot Renew Subscription", body bullet "• Warung Kopi Senja B+{runId}-041 — FAMS", kalimat "Subscription no longer eligible for renewal", dan tombol tunggal `[OK]`
28. Klik `[OK]`
29. Verifikasi tidak ada term baru untuk Client (jumlah term tetap, dibaca lewat fixture BE)
30. Klik `(←)` pada kotak Search

### TC-AC-CS-157: Renew kedua ditolak selagi successor pertama masih menunggu

31. Ketik Search `Toko Serba Ada+{runId}-041`, tekan Enter
32. Klik `Renew` pada baris predecessor Active (form dibuka sebelum successor ada), lalu isi Duration `1`
33. Buat successor Renewal Waiting for Approval untuk predecessor lewat sesi API aktor hingga tersimpan
34. Klik `[Submit]`
35. Verifikasi dialog blok dengan Title "Cannot Renew Subscription", body bullet "• Toko Serba Ada+{runId}-041 — FAMS", kalimat "You already have a renewal request pending for this subscription. Cancel or wait until it's resolved before submitting another.", dan tombol tunggal `[OK]`
36. Verifikasi tidak ada term baru dibuat (jumlah term tetap dua, dibaca lewat fixture BE)
37. Klik `[OK]`

## Notes

- TC-AC-CS-163 dan 167 memakai modal Renew yang sama (satu pembukaan untuk kasus tanpa submit); urutan TC-AC-CS-158 sebelum 157 hanya mengikuti kelompok state seed.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 1, 13, 23, 31), langkah 7 mengisi ulang Duration `1` agar form identik dengan snapshot, `(←)` pada kotak Search (langkah 12, 30), pindah halaman lewat sidebar (langkah 22).
- Langkah 30 mengasumsikan form Renew tertutup setelah `[OK]` dialog blok (TC-AC-CS-159 Expected c menyatakannya untuk dialog yang sama; TC-AC-CS-158 dan 157 tidak menyatakannya).
- Pembuatan successor dan pengarsipan term lewat sesi API ditulis "... hingga ... tersimpan" (R-20).
- Ukuran: 37 langkah, di atas 35 langkah. Alasan: semua blok satu kelas (fungsional Renew) dengan Client seed terpisah per blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-CS-158 dan 157 Expected tidak menyatakan apakah form Renew tetap terbuka setelah `[OK]`; spec mengasumsikan form tertutup seperti TC-AC-CS-159 dan QA perlu memastikannya.
  - TC-AC-CS-157 Langkah 1 menyebut "Dari sesi kedua kirim Renew" tanpa menyebut aktor sesi kedua; spec memakai form Renew di sesi UI aktor dan successor dari sesi API (S-13).
  - TC-AC-CS-157 dan 158 tidak menyebut cara membuat successor atau mengarsipkan term dari sesi lain; kemampuan disediakan tim FE/BE.
  - TC-AC-CS-159 judul menyebut "Row action dan tombol Detail Renew" sedangkan Expected a hanya soal row action; tombol Detail diasersi pada langkah 21.
