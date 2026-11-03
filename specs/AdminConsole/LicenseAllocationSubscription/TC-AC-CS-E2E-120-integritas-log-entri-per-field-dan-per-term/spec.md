---
id: TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term
title: "Integritas Log: Entri per Field dan per Term"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-459
  - TC-AC-CS-460
  - TC-AC-CS-463
  - TC-AC-CS-461
  - TC-AC-CS-462
coverage:
  web: automated
---

# Integritas Log: Entri per Field dan per Term

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Group Manager scope Group Jawa, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Total Control Distributor PT Maju Bersama (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-120`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok:
  1. TC-AC-CS-459: Client `Apotek Sehat Sentosa+{runId}-120` dengan pengajuan FAMS plan Growth Waiting for Approval, Duration 1, Start Date `19/08/26`, Plan Owner PT Maju Bersama (Distributor), milik aktor `Fajar N` (bentuk Pre-setup #49).
  2. TC-AC-CS-460: Client `PT Sejahtera+{runId}-120` dengan term FAMS plan Professional status Active tanpa successor dan satu term lain Client yang sama (Trial FAMS Active), Plan Owner PT Maju Bersama (Distributor) (bentuk Pre-setup #60 dan #61).
  3. TC-AC-CS-463: Client `Toko Serba Ada+{runId}-120` dengan predecessor FAMS plan Professional Active (01/09/25 sampai 31/08/26) dan successor Renewal plan Enterprise Waiting for Approval (bentuk Pre-setup #67 dan #68).
  4. TC-AC-CS-461: Client `Percetakan Mega+{runId}-120` dengan term Pending FAMS plan Professional, Start Date 15/09/26, requester Group Manager `Dewi A` (bentuk Pre-setup #57).
  5. TC-AC-CS-462: Client `Klinik Harapan Bunda+{runId}-120` dengan Trial Active dan Client `Toko Konversi Lambat+{runId}-120` dengan Trial Expired (bentuk Pre-setup #71 dan #121 sampai #122), masing-masing dengan pengajuan Convert jalur request dari requester biasa Create-Only `Fajar N` (Pre-setup #6) lewat sesi API; keduanya diputuskan Approve oleh approver `Eko Saputra` (Pre-setup #9).

## Test Steps

### TC-AC-CS-459: Edit lebih dari satu field menghasilkan satu entri per field yang berubah

1. Ketik Search `Apotek Sehat Sentosa+{runId}-120`, tekan Enter
2. Klik ikon `⋯` pada baris pengajuan `Apotek Sehat Sentosa+{runId}-120 — FAMS`, pilih `Edit`, ubah Duration dari `1` menjadi `2` dan Start Date dari `19/08/26` menjadi `25/08/26`, lalu klik `[Save]`
3. Verifikasi modal Edit tertutup (pengajuan tersimpan)
4. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa+{runId}-120`, tekan Enter, dan cari entri term itu
5. Verifikasi tepat dua entri Changelog baru terhadap baseline untuk term itu
6. Verifikasi satu entri Action `Edit (Duration, mode New/Renewal)` Field `Duration` dengan Old `1 year(s)` dan New `2 year(s)`
7. Verifikasi satu entri Action `Edit (Start Date, mode New)` Field `Start Date` dengan Old `19/08/26` dan New `25/08/26`
8. Verifikasi setiap field yang berubah memiliki tepat satu entri
9. Verifikasi field yang tidak berubah (Plan, Client) tidak menghasilkan entri
10. Ganti akun: klik Logout dari akun sebelumnya
11. Login sebagai `Hendra Wijaya` (`totalControlSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_TC_PASSWORD`)

### TC-AC-CS-460: Satu aksi Cancel Subscription menghasilkan tepat satu entri untuk term yang berubah

12. Pemicu (sesi API): batalkan (Cancel Subscription) term Active tanpa successor `PT Sejahtera+{runId}-120 — FAMS` hingga status Archive tersimpan
13. Buka menu Allocation > Client Subscription, buka modal Changelog, ketik Search `PT Sejahtera+{runId}-120`, tekan Enter, dan hitung entri `Cancel` untuk `PT Sejahtera+{runId}-120 — FAMS`
14. Verifikasi tepat satu entri `Cancel` baru terhadap baseline untuk term itu
15. Verifikasi jumlah entri `Cancel` term itu tepat satu meski ada klik ganda atau retry
16. Verifikasi jumlah entri baru untuk term lain milik Client yang sama adalah nol

### TC-AC-CS-463: Cancel Subscription dengan successor menulis satu entri per term yang berubah

17. Pemicu (sesi API): batalkan (Cancel Subscription) predecessor `Toko Serba Ada+{runId}-120 — FAMS` yang punya successor Waiting for Approval hingga perubahan tersimpan
18. Buka modal Changelog, ketik Search `Toko Serba Ada+{runId}-120`, tekan Enter, dan cari entri Client `Toko Serba Ada+{runId}-120`
19. Verifikasi satu entri `Cancel` untuk predecessor dengan Old `Active` dan New `Archive`
20. Verifikasi satu entri `Cancel Request` untuk successor dengan Old `Waiting for Approval`, New `Canceled`, dan Modified By aktor Cancel Subscription (`Hendra W`)
21. Verifikasi jumlah entri baru untuk kedua term tepat dua (satu per term)
22. Ganti akun: klik Logout dari akun sebelumnya
23. Login sebagai `Dewi Anggraini` (`groupManagerSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_GM_PASSWORD`)

### TC-AC-CS-461: Save Edit yang mengaktifkan term menulis tepat dua record

24. Pemicu (sesi API): simpan Edit Start Date menjadi hari ini pada term Pending `Percetakan Mega+{runId}-120 — FAMS` hingga term Active tersimpan
25. Buka menu Allocation > Client Subscription, buka modal Changelog, ketik Search `Percetakan Mega+{runId}-120`, tekan Enter, dan cari entri pada waktu Save
26. Verifikasi tepat dua record pada waktu Save yang sama: Action `Edit (Start Date, mode New)` Field `Start Date` lalu Action `Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)` Field `Status`
27. Verifikasi tidak ada record ketiga
28. Buka Activity Log, saring Object `Client Subscription`, dan cari kedua record yang sama
29. Verifikasi Activity Log memuat kedua record yang sama
30. Buka Detail user Dewi A, tab System Log, dan cari kedua record yang sama
31. Verifikasi System Log aktor memuat kedua record yang sama
32. Ganti akun: klik Logout dari akun sebelumnya
33. Login sebagai `Eko Saputra` (`totalControlDistSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`)

### TC-AC-CS-462: Approve Convert jalur request menulis dua record

34. Pemicu (sesi API): Approve Convert jalur request yang diajukan requester biasa Create-Only (Pre-setup #6) untuk trial Active `Klinik Harapan Bunda+{runId}-120` dan untuk trial Expired `Toko Konversi Lambat+{runId}-120` hingga perubahan tersimpan
35. Buka menu Allocation > Client Subscription, buka modal Changelog, ketik Search `Klinik Harapan Bunda+{runId}-120`, tekan Enter, dan cari entri pada waktu Approve
36. Verifikasi Changelog memuat tepat satu record `Convert` untuk trial (Field `Subscription Type`)
37. Verifikasi Changelog tidak memuat Action `Approve`
38. Buka Activity Log dan System Log approver dan cari entri `Approve`
39. Verifikasi Activity Log dan System Log approver memuat `Approve`
40. Buka Allocation > Client Subscription (tab Current), ketik Search `Klinik Harapan Bunda+{runId}-120`, tekan Enter
41. Buka modal Subscription Log term paid `Klinik Harapan Bunda+{runId}-120`
42. Verifikasi Subscription Log term paid memuat `Subscription approved by Eko Saputra`
43. Tutup modal Subscription Log
44. Klik tab "History", ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-120`, tekan Enter
45. Buka modal Subscription Log baris Trial `Klinik Harapan Bunda+{runId}-120`
46. Verifikasi Subscription Log baris Trial memuat `Subscription converted by Eko Saputra`
47. Tutup modal Subscription Log
48. Klik tab "Current", ganti isi kotak search dengan `Toko Konversi Lambat+{runId}-120`, tekan Enter
49. Buka modal Subscription Log term paid `Toko Konversi Lambat+{runId}-120` (trial Expired saat Approve)
50. Verifikasi Subscription Log `Toko Konversi Lambat+{runId}-120` menampilkan sedikitnya satu entri (anchor positif)
51. Verifikasi Subscription Log term paid hanya memuat `Subscription approved by Eko Saputra`
52. Verifikasi tidak ada entri `Subscription converted` untuk `Toko Konversi Lambat+{runId}-120` pada Subscription Log
53. Tutup modal Subscription Log
54. Buka modal Changelog, ketik Search `Toko Konversi Lambat+{runId}-120`, dan tekan Enter
55. Verifikasi tabel Changelog menampilkan sedikitnya satu entri
56. Verifikasi tidak ada record Action `Convert` untuk `Toko Konversi Lambat+{runId}-120` di Changelog

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Urutan blok: TC-AC-CS-459 (Create-Only), TC-AC-CS-460 dan 463 (Principal), TC-AC-CS-461 (Group Manager), lalu TC-AC-CS-462 (Total Control Distributor), agar tiap akun hanya login satu kali (S-10).
- Spec ini 56 langkah, melewati sekitar 35 langkah. Alasannya: seluruh blok satu topik (integritas jumlah entri log per field dan per term) dengan pola pembacaan log yang sama dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log berpola tidak dihitung pada ambang (bagian 3, Smell).
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target (R-16), langkah ganti akun (Logout lalu login), langkah membuka Activity Log, System Log, serta Subscription Log term, dan langkah kembali ke daftar (menu Allocation > Client Subscription, tab Current atau History untuk trial yang Converted) dan Search term sebelum membuka Subscription Log term serta sesudah ganti akun sebelum membuka modal Changelog.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
  - TC-AC-CS-460 Expected b (tidak ada entri ganda akibat klik ganda atau retry) tidak punya aksi klik ganda atau retry di Langkah Uji; spec hanya menghitung entri `Cancel` setelah satu aksi pemicu dan tidak membangkitkan klik ganda atau retry.
  - TC-AC-CS-462 Expected a memuat dua klausa berbeda (Subscription Log term paid dan Changelog `Convert` untuk trial) dalam satu butir; spec memecahnya per klausa (S-01).
  - TC-AC-CS-462 Expected c (trial Expired saat Approve) mengacu `Toko Konversi Lambat`, sedangkan Langkah Uji 2 menyebut baris Trial `Klinik Harapan Bunda`; spec memakai keduanya sesuai urutan Langkah Uji.
