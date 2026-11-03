---
id: TC-AC-ACAL-E2E-005-tampilan-sel-nama-singkat-teks-panjang-dan-tooltip-group
title: "Tampilan Sel: Nama Singkat, Teks Panjang, dan Tooltip Group"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-14
  - TC-AC-ACAL-15
  - TC-AC-ACAL-165
  - TC-AC-ACAL-181
coverage:
  web: automated
---

# Tampilan Sel: Nama Singkat, Teks Panjang, dan Tooltip Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (kemampuan seeding log disediakan tim FE/BE; lihat Temuan untuk QA):
  - Tab Session: entri milik `John Doe`, `Siti Rahmawati`, dan user satu kata `Wulan`; satu entri dengan Device / Browser `Microsoft Edge on Windows 11 Enterprise LTSC`. Nama subjek literal menurut Lampiran A-3 (S-12) karena asersi bergantung pada singkatan nama; seeding idempotent dan tidak dihapus.
  - Tab User Action: entri dengan Modified By `Hendra Pratama` dan `Wulan` (nama literal menurut Lampiran A-3); entri Name `PT Sejahtera Abadi Makmur Sentosa Internasional Teknologi Nusantara {runId}-005` dengan Old Value teks tepat 150 karakter termasuk suffix `{runId}-005`; entri Delete Object `Group` Name `Hapus Warn B1` dengan snapshot full path `Hapus Warn B > Hapus Warn B1` (Pre-setup No 14, nama literal karena asersi bergantung pada teks snapshot); entri Object `Brand` Name `Brand ActLog {runId}-005` (Pre-setup No 13).
- Data baris target dicari lewat Search (langkah penghubung); tidak ada total entri yang diasersi.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah (spec read-only).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-14: Tampilan nama singkat dan tooltip nama lengkap kolom User

1. Ketik Search `John Doe`, tekan Enter
2. Verifikasi sel User baris `John Doe` berupa plain text (bukan badge) `John D`
3. Arahkan kursor ke sel User tersebut
4. Verifikasi tooltip sel User `John Doe`
5. Ganti isi kotak search dengan `Siti Rahmawati`, tekan Enter
6. Verifikasi sel User baris `Siti Rahmawati` berupa plain text (bukan badge) `Siti R`
7. Arahkan kursor ke sel User tersebut
8. Verifikasi tooltip sel User `Siti Rahmawati`
9. Ganti isi kotak search dengan `Wulan`, tekan Enter
10. Verifikasi sel User baris dengan User satu kata berupa plain text (bukan badge) `Wulan`
11. Arahkan kursor ke sel User tersebut
12. Verifikasi tooltip sel User `Wulan`
13. Klik `(←)` pada kotak Search tab Session

### TC-AC-ACAL-165: Teks panjang tampil utuh tanpa dipotong, kedua tab

14. Klik tab "User Action"
15. Ketik Search `PT Sejahtera Abadi Makmur Sentosa Internasional Teknologi Nusantara {runId}-005`, tekan Enter
16. Verifikasi sel Name tampil utuh (lebar kolom mengikuti isi) tanpa `..`
17. Arahkan kursor ke sel Name
18. Verifikasi sel Name tanpa tooltip
19. Verifikasi sel Old Value tampil utuh (boleh terbungkus beberapa baris), tidak dipotong `..`
20. Klik `(←)` pada kotak Search tab User Action
21. Klik tab "Session"
22. Ketik Search `Microsoft Edge on Windows 11 Enterprise LTSC`, tekan Enter
23. Verifikasi sel Device / Browser tampil utuh `Microsoft Edge on Windows 11 Enterprise LTSC` tanpa `..`
24. Klik `(←)` pada kotak Search tab Session

### TC-AC-ACAL-15: Tampilan nama singkat dan tooltip nama lengkap kolom Modified By

25. Klik tab "User Action"
26. Ketik Search `Hendra Pratama`, tekan Enter
27. Verifikasi sel Modified By berupa plain text `Hendra P`
28. Arahkan kursor ke sel Modified By tersebut
29. Verifikasi tooltip sel Modified By `Hendra Pratama`
30. Ganti isi kotak search dengan `Wulan`, tekan Enter
31. Verifikasi sel Modified By berupa plain text `Wulan`
32. Arahkan kursor ke sel Modified By tersebut
33. Verifikasi tooltip sel Modified By `Wulan`
34. Klik `(←)` pada kotak Search tab User Action

### TC-AC-ACAL-181: Hover kolom Name entri Object Group menampilkan snapshot full path

35. Ketik Search `Hapus Warn B1`, tekan Enter
36. Verifikasi sel Name entri Object `Group` menampilkan nama leaf `Hapus Warn B1`
37. Arahkan kursor ke sel Name entri Object `Group`
38. Verifikasi tooltip snapshot full path `Hapus Warn B > Hapus Warn B1`
39. Ganti isi kotak search dengan `Brand ActLog {runId}-005`, tekan Enter
40. Verifikasi sel Name entri Object `Brand` tampil
41. Arahkan kursor ke sel Name entri Object `Brand`
42. Verifikasi sel Name entri Object `Brand` tidak menampilkan tooltip
43. Klik `(←)` pada kotak Search tab User Action

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-14, 15, 165, 181). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): Search untuk menemukan baris target pada langkah 1, 5, 9, 15, 22, 26, 30, 35, dan 39 (R-16), serta pengosongan kotak Search pada langkah 13, 20, 24, 34, dan 43 supaya Search tidak terbawa ke blok berikutnya (S-09).
- Urutan blok: TC-14, TC-165, TC-15, TC-181 (bukan urutan nomor) agar perpindahan tab minimal; TC-165 mencakup kedua tab sehingga blok User Action dan Session dikerjakan berurutan di dalamnya. Pada TC-14 dan TC-15 tiap `Verifikasi` tampilan sel diikuti hover dan `Verifikasi` tooltip per nama (state sementara; bagian 8b butir 5), bukan dikelompokkan a lalu b seperti di TC.
- Langkah "Verifikasi sel Name entri Object `Brand` tampil" adalah anchor positif untuk asersi absence tooltip pada TC-181 Expected c; hover menjadi anchor tooltip (bagian 8b butir 2). Hal yang sama berlaku untuk "Verifikasi sel Name tanpa tooltip" pada TC-165, dengan sel Name yang tampil utuh pada langkah sebelumnya sebagai anchor.
- Spec di atas smell 35 langkah (43 langkah). Alasan: seluruh blok satu kelas (tampilan sel read-only tanpa mutasi data) dan satu dataset log, empat TC berdiri sendiri dengan baris target sendiri yang dicari lewat Search, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-181 Expected b menyebut "rename atau penghapusan group sesudahnya tidak mengubah tooltip", tetapi tidak ada langkah uji untuk rename atau penghapusan; entri seed adalah hasil Delete Group sehingga grupnya sudah terhapus saat tooltip diamati. Klausa rename tidak punya langkah di TC dan tidak diasersi terpisah.
  - TC-165 Expected a tidak menyebut sel Name harus ditemukan lewat pencarian; spec memakai Search sebagai langkah penghubung. Nama Name bersuffix `{runId}-005` ditambahkan ke teks panjang TC supaya data unik per run.
  - TC-14 dan TC-15 menyebut "Entri Session/User Action milik ..." tanpa menyebut cara menemukan baris di tabel; spec memakai Search.
  - Mekanisme seeding entri log (termasuk Device / Browser, Old Value 150 karakter, dan snapshot full path Group) tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
