---
id: TC-GS-FILEMGR-E2E-029-retensi-teks-info-dan-auto-purge-in-recycle-bin
title: "Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-17
  - TC-GS-FILEMGR-19
  - TC-GS-FILEMGR-20
  - TC-GS-FILEMGR-21
  - TC-GS-FILEMGR-262
coverage:
  web: automated
---

# Retensi Recycle Bin: Teks Info dan Kolom Auto-Purge In Mengikuti Lifecycle Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`. Akun dan akses yang mengubah Lifecycle Settings (Admin Console) tidak disebut TC, PRD, atau LLD File Manager: disediakan tim FE.
- State global yang diubah (suite serial): durasi retensi Recycle Bin di Lifecycle Settings. Hook `before` memastikan nilai awal 30 hari dan mencatatnya; urutan nilai di spec: 30, 10, 30, 45, 1. Hook `after` memulihkan 30 hari dan memicu job reset countdown (fixture BE) walau spec gagal di tengah.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run, di Recycle Bin; Deleted Date relatif terhadap waktu seeding; pemilik adalah user klon milik spec; dipakai pada beberapa blok; sisa seed dibersihkan di hook `after`): `old-avatar-{runId}-029.png` (Deleted Date sekarang - 1 hari), `legacy-photo-{runId}-029.jpeg` (- 18 hari), `expired-avatar-{runId}-029.jpg` (- 29 hari), `due-photo-{runId}-029.png` (- 31 hari), `recycled-photo-01-{runId}-029.jpg` (- 2 hari), `recycled-photo-08-{runId}-029.jpg` (- 9 hari). Sesuai R01, R02, R03, R04, R05, R12 Tabel A3.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): seeding Recycle Bin dengan Deleted Date relatif; memicu job reset countdown (setelah retensi diubah) sampai selesai; job auto-purge harian dijeda selama spec (agar `due-photo-{runId}-029.png` tidak hilang sebelum diasersi, Q-3).
- Cleanup (hook `after`, tetap jalan walau spec gagal di tengah): hapus permanen sisa file seed `*-{runId}-029.*` di Recycle Bin tanpa mengasumsikan seeding berhasil seluruhnya (cari berdasarkan suffix `{runId}-029`, abaikan yang tidak ada), seperti spec 025 dan 030; job auto-purge harian tetap dijeda selama spec.
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-17 (bagian sebelum perubahan) dan TC-GS-FILEMGR-19: Retensi 30 hari

1. Klik tombol Recycle Bin di toolbar
2. Verifikasi teks info: "Files are permanently deleted after 30 days."
3. Ketik Search `{runId}-029`, tekan Enter
4. Verifikasi `old-avatar-{runId}-029.png` menampilkan Auto-Purge In `29 days`
5. Verifikasi `legacy-photo-{runId}-029.jpeg` menampilkan Auto-Purge In `12 days`
6. Verifikasi `expired-avatar-{runId}-029.jpg` menampilkan Auto-Purge In `1 day`
7. Verifikasi `due-photo-{runId}-029.png` menampilkan Auto-Purge In `0 days`
8. Verifikasi `due-photo-{runId}-029.png` tetap tampil di Recycle Bin
9. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-20: Retensi diperpendek memakai floor 48 jam

10. Buka Lifecycle Settings, ubah durasi retensi Recycle Bin menjadi 10, lalu klik [Save]
11. Picu job reset countdown lewat fixture BE sampai selesai
12. Buka Global Settings > File Manager, lalu klik tombol Recycle Bin di toolbar
13. Ketik Search `{runId}-029`, tekan Enter
14. Verifikasi `old-avatar-{runId}-029.png` menampilkan Auto-Purge In `9 days`
15. Verifikasi `recycled-photo-01-{runId}-029.jpg` menampilkan Auto-Purge In `8 days`
16. Verifikasi `recycled-photo-08-{runId}-029.jpg` menampilkan Auto-Purge In `2 days`
17. Verifikasi `expired-avatar-{runId}-029.jpg` menampilkan Auto-Purge In `2 days`
18. Verifikasi `legacy-photo-{runId}-029.jpeg` menampilkan Auto-Purge In `2 days`
19. Verifikasi `due-photo-{runId}-029.png` menampilkan Auto-Purge In `2 days`
20. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-21 dan TC-GS-FILEMGR-17 (bagian sesudah perubahan): Retensi 45 hari

21. Buka Lifecycle Settings, ubah durasi retensi Recycle Bin kembali menjadi 30, lalu klik [Save]
22. Picu job reset countdown lewat fixture BE sampai selesai
23. Ubah durasi retensi Recycle Bin menjadi 45, lalu klik [Save]
24. Picu job reset countdown lewat fixture BE sampai selesai
25. Buka Global Settings > File Manager, lalu klik tombol Recycle Bin di toolbar
26. Verifikasi teks info: "Files are permanently deleted after 45 days."
27. Verifikasi teks info tidak memuat nilai hardcode 30
28. Ketik Search `{runId}-029`, tekan Enter
29. Verifikasi `old-avatar-{runId}-029.png` menampilkan Auto-Purge In `44 days`
30. Verifikasi `expired-avatar-{runId}-029.jpg` menampilkan Auto-Purge In `16 days`
31. Verifikasi `due-photo-{runId}-029.png` menampilkan Auto-Purge In `14 days`
32. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-262: Bentuk tunggal saat retensi 1 hari

33. Buka Lifecycle Settings, ubah durasi retensi Recycle Bin menjadi 1, lalu klik [Save]
34. Buka Global Settings > File Manager, lalu klik tombol Recycle Bin di toolbar
35. Verifikasi teks info: "Files are permanently deleted after 1 day."
36. Tutup modal Recycle Bin dengan `✕` di header
37. Buka Lifecycle Settings, ubah durasi retensi Recycle Bin kembali menjadi 30, lalu klik [Save]
38. Picu job reset countdown lewat fixture BE sampai selesai

## Notes

- Mode: FE+BE. State global (retensi) diubah dan dipulihkan; langkah 37 dan 38 memulihkan state sebagai aksi tanpa `Verifikasi` (S-09), hook `after` sebagai cadangan. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (38 langkah nominal, tanpa blok yang diulang) hanya sedikit di atas ambang; alasan pertahanan: seluruh blok satu kelas (state global retensi pada satu dataset Recycle Bin) dan setiap blok menetapkan nilai retensinya sendiri sebelum diasersi, sehingga kegagalan satu asersi tidak membuat blok berikutnya kehilangan makna.
- TC-GS-FILEMGR-17 dibelah mengikuti perubahan retensi: butir a (30 hari) pada blok pertama (langkah 2), butir b (45 hari) pada blok ketiga (langkah 26 dan 27). Langkah TC-GS-FILEMGR-17 "tutup modal Recycle Bin, ubah retensi, buka kembali" terwujud sebagai langkah 9, 21 s.d. 25. TC-GS-FILEMGR-19 dan TC-GS-FILEMGR-17 butir a dijalankan dalam satu pembukaan modal.
- Urutan TC pada spec: 17a, 19, 20, 21 (dengan 17b), 262. Urutan mengikuti nilai retensi berurutan; langkah 21 sampai 24 (mengembalikan retensi ke 30, memicu job reset, lalu mengubah ke 45) memenuhi precondition TC-GS-FILEMGR-21 ("Retensi 30 hari"), sehingga TC-GS-FILEMGR-21 tidak mewarisi batas tersimpan hasil TC-GS-FILEMGR-20.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 3, 13, 28 (Search `{runId}-029` agar hanya baris seed spec yang diamati), 9, 20, 32, 36 (menutup modal), 12, 25, 34 (kembali ke File Manager), 21 s.d. 24, 37, 38 (memulihkan retensi 30 dan memicu job reset).
- Asersi tambahan di luar Expected TC (S-03): langkah 8 (`due-photo` tetap tampil, Expected d), 27 (Expected b "tanpa nilai hardcode 30").
- Job reset countdown (langkah 11, 22, 24, 38) hanya pemicu agar kondisi yang diuji (batas tersimpan baru) terbentuk, bukan objek asersi; asersi tetap pada teks info dan Auto-Purge In (P-2).
- Temuan untuk QA:
  - Q-3: `due-photo` (R04, Deleted Date sekarang - 31 hari) "tetap tampil sampai job auto-purge berikutnya"; bila job harian berjalan antara seeding dan asersi, baris itu hilang dan TC-GS-FILEMGR-19/20/21 menjadi flaky. Job dijeda di environment e2e (kemampuan yang diminta di Prerequisites).
  - Q-14: nilai turunan Auto-Purge In (mis. `2 days` dari 10 - 9 = 1 hari < 48 jam floor; `44`, `16`, `14` dari 45 - 1, 45 - 29, 45 - 31) berasal dari Tabel Data Uji, bukan PRD; aritmetika diperiksa konsisten.
  - Q-4: seeding Recycle Bin dengan Deleted Date relatif dan pemicu "job reset countdown" tidak punya mekanisme di TC; ditulis "disediakan tim FE/BE".
  - NC-03: perlakuan batas tersimpan setelah retensi diperpanjang kembali ke 30 lalu 45 tidak dinyatakan secara eksplisit di TC; spec mengembalikan retensi ke 30 sebelum 45 mengikuti precondition TC-GS-FILEMGR-21.
  - Q-5/Q-7: TC menyebut baris Pre-setup R01 s.d. R05, R12 (Tabel A3) dan tidak mengubah baris itu, tetapi perubahan retensi menggeser batas tersimpan seluruh baris Recycle Bin termasuk Pre-setup; spec memakai baris seed bersuffix untuk asersi dan mengembalikan retensi di akhir.
  - Akun yang mengubah Lifecycle Settings tidak disebut di TC (S-13).
