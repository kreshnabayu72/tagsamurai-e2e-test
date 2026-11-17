---
id: TC-FA-TDC-E2E-219-request-langsung-guard-deactivate-delete-dan-bulk-hanya-yang-lolos
title: "Request Langsung: Guard Deactivate dan Delete serta Bulk Memproses Hanya Class yang Lolos"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-834
  - TC-FA-TDC-835
  - TC-FA-TDC-836
  - TC-FA-TDC-837
  - TC-FA-TDC-838
sourceRules: ["F-FATDC-05.k1", "FATDC-LOGIC-08a", "F-FATDC-06.k1", "FATDC-LOGIC-09a", "F-FATDC-06.k2", "FATDC-LOGIC-09b", "F-FATDC-13.k2", "FATDC-LOGIC-14d", "L-04", "J-04", "FATDC-LOGIC-09d", "L-05", "F-FATDC-13.k9"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-05.k1": [2, 4]
  "FATDC-LOGIC-08a": 2
  "F-FATDC-06.k1": 7
  "FATDC-LOGIC-09a": [7, 9, 27]
  "F-FATDC-06.k2": 11
  "FATDC-LOGIC-09b": [11, 13]
  "F-FATDC-13.k2": [17, 18, 22]
  "FATDC-LOGIC-14d": 18
  "L-04": [20, 22]
  "J-04": [20, 29]
  "FATDC-LOGIC-09d": 26
  "L-05": [29, 31]
  "F-FATDC-13.k9": 31
coverage:
  web: automated
---

# Request Langsung: Guard Deactivate dan Delete serta Bulk Memproses Hanya Class yang Lolos

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, serta seed dan pemulihan lewat API (Used By lewat Asset Class pemakai dan class berkunci). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Kemampuan tambahan (disediakan tim FE/BE): membaca jumlah entri Changelog per class sebagai baseline. Changelog adalah audit trail permanen, sehingga jumlah entri tidak diasersi sebagai angka absolut (S-12).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb2` | `NB-2` | Active, Used By 3 (Asset Class pemakai disediakan tim FE), tanpa Last Posted Tax Year |
| `nbKhs` | `NB-KHS` | Last Posted Tax Year 2026, Used By 0 |
| `nb3` | `NB-3` | Active, Used By 0, tanpa Last Posted Tax Year |

- Pemulihan: hook `after` membuat ulang `NB-3` dan mengembalikan `NB-2` dan `NB-KHS` ke kondisi di atas lewat API.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-834: Request langsung Deactivate class dengan Used By lebih dari 0 ditolak server

1. Kirim request langsung dengan sesi API aktor Total Control untuk menonaktifkan class `NB-2` tanpa melalui UI
2. Verifikasi server menolak request tanpa mengubah data
3. Baca ulang status `NB-2` lewat request baca
4. Verifikasi status `NB-2` tetap Active

### TC-FA-TDC-835: Request langsung Delete class yang pernah diposting ditolak server

5. Baca jumlah versi class `NB-KHS` lewat request baca dan catat sebagai baseline
6. Kirim request langsung dengan sesi API aktor Total Control untuk menghapus class `NB-KHS` tanpa melalui UI
7. Verifikasi server menolak request tanpa mengubah data
8. Baca ulang daftar class lewat request baca
9. Verifikasi class `NB-KHS` tetap ada dengan jumlah versi sama dengan baseline langkah 5

### TC-FA-TDC-836: Request langsung Delete class dengan Used By lebih dari 0 ditolak server

10. Kirim request langsung dengan sesi API aktor Total Control untuk menghapus class `NB-2` tanpa melalui UI
11. Verifikasi server menolak request tanpa mengubah data
12. Baca ulang daftar class lewat request baca
13. Verifikasi class `NB-2` tetap ada

### TC-FA-TDC-837: Request langsung bulk Deactivate memproses hanya class yang lolos guard

14. Catat baseline jumlah entri Changelog Status class `NB-3` dan `NB-2` lewat kemampuan baca log
15. Kirim request langsung dengan sesi API aktor Total Control untuk bulk Deactivate `NB-3` dan `NB-2` tanpa melalui UI, hingga perubahan tersimpan
16. Baca ulang status `NB-3` dan `NB-2` lewat request baca
17. Verifikasi status `NB-3` menjadi Inactive
18. Verifikasi status `NB-2` tetap Active
19. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar, ketik Search `NB-3`, tekan Enter
20. Verifikasi Changelog memuat satu baris Status baru untuk `NB-3` (selisih satu dari baseline langkah 14)
21. Ganti isi kotak search dengan `NB-2`, tekan Enter
22. Verifikasi Changelog tidak memuat baris Status baru untuk `NB-2` (jumlah entri sama dengan baseline langkah 14)

### TC-FA-TDC-838: Request langsung bulk Delete memproses hanya class yang lolos guard

23. Catat baseline jumlah entri Changelog Delete class `NB-3` dan `NB-KHS` lewat kemampuan baca log
24. Kirim request langsung dengan sesi API aktor Total Control untuk bulk Delete `NB-3` dan `NB-KHS` tanpa melalui UI, hingga perubahan tersimpan
25. Baca ulang daftar class lewat request baca
26. Verifikasi class `NB-3` terhapus
27. Verifikasi class `NB-KHS` tetap ada
28. Muat ulang halaman, klik ikon Changelog di toolbar, ketik Search `NB-3`, tekan Enter
29. Verifikasi Changelog memuat satu baris Delete baru untuk `NB-3` (selisih satu dari baseline langkah 23)
30. Ganti isi kotak search dengan `NB-KHS`, tekan Enter
31. Verifikasi Changelog tidak memuat baris Delete baru untuk `NB-KHS` (jumlah entri sama dengan baseline langkah 23)

## Notes

- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE. Request dikirim tanpa browser; asersi respons dan state data lewat request baca (8b.1), sedangkan baris Changelog TC-FA-TDC-837 dan TC-FA-TDC-838 dibaca di UI.
- Klausa Expected c TC-FA-TDC-834, TC-FA-TDC-835, dan TC-FA-TDC-836 (tidak ada entri log baru di Changelog dan Activity Log) tidak diasersi di spec ini; asersinya ada di spec absence 261 dengan aksi nyata dan baseline sendiri per TC (S-05). Pada TC-FA-TDC-837 dan TC-FA-TDC-838, Changelog dibaca karena baris log adalah bagian aksi yang berhasil diproses (selisih satu baris untuk class yang lolos).
- Urutan TC: TC-FA-TDC-834 sampai 838 mengikuti nomor TC; TC-FA-TDC-838 menghapus `NB-3` di akhir spec. `NB-3` dinonaktifkan di TC-FA-TDC-837 lalu dihapus di TC-FA-TDC-838 (Inactive, Used By 0, tanpa Last Posted Tax Year tetap lolos guard Delete).
- Langkah penghubung (S-03): langkah 5 (baseline jumlah versi untuk asersi "jumlah versi yang sama"); langkah 14 dan 23 (baseline log per TC, S-12); langkah 19 (kembali ke modul asal dan membuka Changelog, Search `NB-3` untuk menemukan entri, R-16); langkah 28 (memuat ulang halaman dan membuka Changelog sesudah request TC-FA-TDC-838); langkah 21 dan 30 (mengganti Search); asersi absence langkah 22 dan 31 didahului asersi baris `NB-3` pada Changelog yang sama (anchor positif, 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-834 sampai 836 menulis "Server menolak request" tanpa status HTTP; spec mengasersi penolakan tanpa kode status.
  - TC-FA-TDC-837 dan TC-FA-TDC-838 Expected c menulis "Changelog memuat satu baris ... hanya untuk" tanpa menyebut Field dan nilai baris; spec mengasersi jumlah baris saja.
  - TC-FA-TDC-838 tidak menyebut status `NB-3` sesudah TC-FA-TDC-837 (Inactive); spec mengikuti urutan TC dan `NB-3` tetap lolos guard Delete.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
