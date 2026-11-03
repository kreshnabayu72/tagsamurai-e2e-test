---
id: TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx
title: "Resilience A: Error Load Config, Code List, dan Changelog serta Toggle 5xx dan Koneksi Terputus"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-12
  - TC-FA-CAID-159
  - TC-FA-CAID-230
  - TC-FA-CAID-317
  - TC-FA-CAID-321
coverage:
  web: automated
---

# Resilience A: Error Load Config, Code List, dan Changelog serta Toggle 5xx dan Koneksi Terputus

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan asersi state backend, bagian 6 konvensi; bukan `Mode: mock` karena sebagian asersi membaca state server).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup: konfigurasi Company Alpha baseline B1 (Pre-setup No 10: Master Switch ON, Separator `/ (Slash)`, segmen Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dan aset Pre-setup No 11: A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`, A4 Disposed `JKT/LAP/T490/0926/4`, A5 Deleted (tidak tampil di UI).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE) (dipakai TC-FA-CAID-159). Data Pre-setup No 15 (`Company Changelog`, entri seed L1 sampai L7 bertanggal 10/09/26 sampai 15/09/26; entri log audit lain tidak dihapus dan tidak diasersi) dan Pre-setup No 27 (General Settings baseline: Date Format `dd/MM/yy`) dipakai TC-FA-CAID-230 (baris seed L1 sampai L7 diasersi pada langkah 26); di-seed lewat API di hook `before` pada Company aktor (kemampuan disediakan tim FE/BE). Audit trail Company aktor tumbuh dari spec lain (S-12), sehingga baris seed dicari lewat Filter Date pada tanggal seed (langkah 25), bukan lewat posisi teratas atau halaman.
- Alat uji (Pre-setup No 26): penyunting request/respons pada sesi otomasi (`Spectra.intercept()`) dan pemutus jaringan. Kebutuhan intercept, dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script (tidak dikarang di spec): respons konfigurasi Custom Asset ID jawab 5xx (TC-FA-CAID-12); respons data tab `Group Codes` jawab 5xx (TC-FA-CAID-159); respons data Changelog jawab 5xx (TC-FA-CAID-230); respons Toggle konfigurasi jawab 5xx (TC-FA-CAID-317); jaringan sesi diputus lalu dipulihkan (TC-FA-CAID-321).
- Kemampuan membaca jumlah entri Changelog Custom Asset ID sebelum aksi sebagai baseline N disediakan tim FE/BE (bagian 8b butir 10); jumlah entri tidak diasersi sebagai angka absolut (S-12). Surface log yang diperiksa adalah Modal Changelog: Custom Asset ID, karena TC menyebut "entri log" tanpa menyebut surface.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah bila hasil sesuai TC; Master Switch tetap ON dan Asset ID tidak berubah. Hook `after` spec ini melepas semua intercept dan memulihkan koneksi jaringan walau spec gagal di tengah, lalu `beforeEach` suite memulihkan baseline B1.

## Test Steps

### TC-FA-CAID-12: Error load konfigurasi

1. Pasang intercept pada respons konfigurasi Custom Asset ID: jawab 5xx
2. Muat ulang tab Custom Asset ID
3. Verifikasi tampil teks `Unable to load this data.` dengan tombol `[Try Again]`
4. Verifikasi yang tampil bukan form default dan bukan empty state
5. Lepas intercept respons konfigurasi
6. Klik `[Try Again]`
7. Verifikasi form memuat nilai konfigurasi tersimpan (baseline B1)

### TC-FA-CAID-159: Error load tab Code List

8. Klik tautan `[View Code List]`
9. Pasang intercept pada respons data tab `Group Codes`: jawab 5xx
10. Klik tab `Category Codes`
11. Klik tab `Group Codes`
12. Verifikasi tab `Group Codes` menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
13. Verifikasi yang tampil bukan empty state
14. Lepas intercept respons data tab `Group Codes`
15. Klik `[Try Again]`
16. Verifikasi tabel memuat enam baris Group

### TC-FA-CAID-230: Error load Changelog

17. Klik `[✕]` pada header Modal View Code List
18. Pasang intercept pada respons data Changelog: jawab 5xx
19. Klik tombol `[Changelog]` pada header kartu untuk membuka Modal Changelog
20. Verifikasi tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
21. Verifikasi yang tampil bukan empty state
22. Lepas intercept respons data Changelog
23. Klik `[Try Again]`
24. Verifikasi tabel memuat baris entri Changelog (sedikitnya satu baris)
25. Klik icon Filter, pilih rentang `10/09/26` sampai `15/09/26` pada field `Date`, klik `[Apply]`
26. Verifikasi tabel memuat baris seed L1, L2, L3, L4, L5, L6, L7
27. Klik `[✕]` pada header Modal Changelog

### TC-FA-CAID-317: Toggle gagal 5xx

28. Catat jumlah entri Changelog Custom Asset ID sebagai baseline N
29. Geser Master Switch ke OFF
30. Pasang intercept pada respons Toggle: jawab 5xx
31. Klik `[Disable]` pada dialog
32. Verifikasi Toast error `Error, failed to save configuration.` tampil tanpa tombol aksi
33. Verifikasi Master Switch kembali ke posisi ON
34. Lepas intercept respons Toggle
35. Buka Fixed Asset > Assets > All Assets
36. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) tampil
37. Verifikasi body dialog `You have unsaved changes. Are you sure you want to leave?`
38. Verifikasi tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
39. Klik `[Leave]`
40. Verifikasi halaman All Assets terbuka
41. Verifikasi Asset ID A1 sampai A4 tidak berubah (`JKT/LAP/T490/0926/1`, `JKT/LAP/T490/0926/2`, `JKT/LAP/T490/0000/3`, `JKT/LAP/T490/0926/4`)
42. Kembali ke Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu klik tombol `[Changelog]` pada header kartu
43. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)
44. Klik `[✕]` pada header Modal Changelog

### TC-FA-CAID-321: Toggle saat koneksi terputus

45. Geser Master Switch ke OFF
46. Putuskan koneksi jaringan pada sesi
47. Klik `[Disable]` pada dialog
48. Verifikasi Toast `Connection problem. Please try again.` tampil tanpa tombol aksi
49. Verifikasi Master Switch kembali ke posisi ON
50. Pulihkan koneksi jaringan pada sesi
51. Buka Fixed Asset > Assets > All Assets
52. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) tampil
53. Verifikasi body dialog `You have unsaved changes. Are you sure you want to leave?`
54. Verifikasi tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
55. Klik `[Leave]`
56. Verifikasi halaman All Assets terbuka
57. Verifikasi Asset ID A1 sampai A4 tidak berubah (`JKT/LAP/T490/0926/1`, `JKT/LAP/T490/0926/2`, `JKT/LAP/T490/0000/3`, `JKT/LAP/T490/0926/4`)
58. Kembali ke Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu klik tombol `[Changelog]` pada header kartu
59. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 59 langkah, di atas 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection, bagian 3 prinsip 13b) dengan baseline B1 yang sama, dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); langkah panjang berasal dari tiga blok load error yang masing-masing memasang dan melepas intercept serta dua blok Toggle yang masing-masing memverifikasi dialog `Unsaved Changes` (judul, body, tombol), Asset ID di All Assets, dan jumlah entri Changelog.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC: TC-FA-CAID-12, 159, 230 (baca), lalu 317 dan 321 (Toggle).
- Langkah penghubung (tanpa `Verifikasi`): pemasangan dan pelepasan intercept (dilepas segera setelah pemicu selesai, S-09), `[✕]` pada header Modal View Code List sebelum membuka Modal Changelog, `[✕]` pada header Modal Changelog (langkah 27 dan 44), langkah 25 (Filter Date untuk menemukan baris seed Changelog, R-16 dan S-12), serta langkah kembali ke tab Custom Asset ID dan membuka Modal Changelog sesudah membuka All Assets. Langkah 39 dan 55 (`[Leave]`) adalah langkah TC-FA-CAID-317 dan 321.
- Baseline N dicatat sekali pada langkah 28. TC-FA-CAID-317 memverifikasi jumlah entri sama dengan N; karena tidak ada entri bertambah, N yang sama dipakai TC-FA-CAID-321.
- Pembagian TC lintas spec: TC-FA-CAID-316, 319, 340, 155, dan 226 ada di spec 062; TC-FA-CAID-318, 320, dan 332 ada di spec 063.
- Temuan untuk QA:
  - TC-FA-CAID-317 dan 321 menyebut "tidak ada entri log baru" tanpa menyebut surface (Changelog, System Log, Activity Log). Spec memeriksa jumlah entri Modal Changelog terhadap baseline N sebagai asersi jumlah (bukan kelas g, bagian 3).
  - TC-FA-CAID-230 Expected b menyebut baris seed L1 sampai L7 tanpa menyebut cara menemukannya di audit trail permanen yang tumbuh; spec memakai Filter Date pada tanggal seed (langkah 25; S-12 dan S-14) dan hanya menambah langkah itu.
