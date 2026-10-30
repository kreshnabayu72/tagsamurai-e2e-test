---
id: TC-GS-USER-E2E-038-edit-foto-profil-hapus-ganti-dan-tutup-tanpa-save
title: "Edit User: Foto Profil (Tutup Tanpa Save, Ganti Foto Auto-Transition, dan Hapus Ditandai Sampai Save)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-205
  - TC-GS-USER-206
  - TC-GS-USER-207
coverage:
  web: automated
---

# Edit User: Foto Profil (Tutup Tanpa Save, Ganti Foto Auto-Transition, dan Hapus Ditandai Sampai Save)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup yang dipakai: Position `Staff` (No. 22), Division `Finance` (No. 23), dan produk `Fixed Asset` (No. 26); hanya dibaca. Spec tidak mengubah atau menghapus data Pre-setup (John Doe No. 18 diganti user seed milik spec, S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user dan unggah foto lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD):
  - U-1: Name `John Doe {runId}-038`, Email `johndoe+{runId}-038@qwertysystem.net`, Position `Staff`, Division `Finance`, Access `Fixed Asset` dan `Global Settings`, dengan foto profil file `john-{runId}-038.png` (foto lama).
  - File fixture `john2.png` untuk unggahan foto baru (disediakan tim FE).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 lewat API; hapus file `john-{runId}-038.png` dan `john2.png` milik U-1 dari File Manager dan Recycle Bin bila masih ada (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: hover avatar untuk menampilkan `[Edit]` dan `[Delete]`; memilih file pada dialog unggah; membaca sumber gambar avatar (foto lama, foto baru, atau inisial) dan membandingkannya dengan baseline; membaca daftar file File Manager dan Recycle Bin termasuk kolom deleter.
- State global yang diubah: tidak ada selain data U-1 dan file miliknya.

## Test Steps

### Persiapan: baseline File Manager

1. Buka Global Settings > File Manager
2. Catat jumlah file di File Manager (baseline)
3. Buka Global Settings > User > User List, sub-tab Login User

### TC-GS-USER-207: Ganti foto lalu tutup tanpa Save

4. Klik icon Search, ketik `John Doe {runId}-038`, tekan Enter
5. Buka row action baris `John Doe {runId}-038` lalu klik `Edit`
6. Catat sumber gambar avatar di Popup (foto lama, baseline avatar)
7. Hover avatar lalu klik `[Edit]`
8. Pilih file `john2.png`
9. Klik `[✕]`
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Klik Name `John Doe {runId}-038` untuk membuka Detail
13. Verifikasi avatar John Doe tetap foto lama (sama dengan baseline avatar langkah 6)
14. Buka Global Settings > File Manager
15. Verifikasi file `john-{runId}-038.png` tampil di File Manager
16. Verifikasi jumlah file di File Manager sama dengan baseline langkah 2 (tidak ada file baru)
17. Verifikasi tidak ada file `john2.png` di File Manager
18. Buka Global Settings > User > User List, sub-tab Login User

### TC-GS-USER-206: Ganti foto existing via Popup Edit

19. Klik icon Search, ketik `John Doe {runId}-038`, tekan Enter
20. Buka row action baris `John Doe {runId}-038` lalu klik `Edit`
21. Hover avatar lalu klik `[Edit]`
22. Pilih file `john2.png`
23. Klik `[Save]`
24. Verifikasi toast sukses: `Success, user has been updated.`
25. Verifikasi hanya 1 toast yang tampil (tanpa toast foto terpisah)
26. Klik Name `John Doe {runId}-038` untuk membuka Detail
27. Verifikasi avatar John Doe menampilkan foto baru (`john2.png`)
28. Buka Global Settings > File Manager > Recycle Bin
29. Verifikasi foto lama `john-{runId}-038.png` ada di Recycle Bin
30. Verifikasi deleter foto lama `System`
31. Buka Global Settings > User > User List, sub-tab Login User

### TC-GS-USER-205: Delete foto existing hanya menandai sampai Save

32. Klik icon Search, ketik `John Doe {runId}-038`, tekan Enter
33. Buka row action baris `John Doe {runId}-038` lalu klik `Edit`
34. Hover avatar lalu klik `[Delete]`
35. Verifikasi foto lama masih tampil di avatar Popup
36. Verifikasi tidak ada dialog konfirmasi
37. Klik `[Save]`
38. Verifikasi toast sukses: `Success, user has been updated.`
39. Klik Name `John Doe {runId}-038` untuk membuka Detail
40. Verifikasi avatar John Doe kembali ke inisial

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-205, 206, 207). Mode FE+BE; kelas harness: Edit foto profil (satu kelas), satu user seed.
- Urutan TC di spec: 207, 206, 205. Urutan sumber (205, 206, 207) diubah karena user seed hanya punya satu foto: TC-GS-USER-207 (tidak mengubah apa pun) lebih dulu, TC-GS-USER-206 (mengganti foto) sesudahnya, dan TC-GS-USER-205 (menghapus foto) paling akhir sebagai aksi yang menghabisi data (bagian 3 butir 5). "Foto lama" di TC-GS-USER-205 pada praktiknya `john2.png` hasil TC-GS-USER-206.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 6 (baseline File Manager dan baseline avatar, membuka layar), 12 (membuka Detail), 14 dan 18, 26 dan 28 dan 31, 39 (navigasi). `Verifikasi` dialog `Unsaved Changes` (langkah 10) adalah asersi tambahan penutupan deterministik S-08; Expected TC-GS-USER-207 tidak menyebutnya.
- Asersi absence TC-GS-USER-207 butir b ("tidak ada file baru") didahului `Verifikasi` file pembanding pada surface yang sama (langkah 15) sesuai bagian 8b butir 2, ditambah baseline jumlah file (langkah 2).
- Pembagian TC lintas spec: TC-GS-USER-205 sampai 207 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-205 Post Condition ("foto lama ter-soft-delete ke Recycle Bin, actor = admin yang login") tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-USER-205 dan 206 menyebut "foto lama" tanpa nama file, dan TC tidak menyebut lokasi atau folder foto user di File Manager; spec mengidentifikasi lewat nama file seed `john-{runId}-038.png` dengan asumsi nama file tersimpan sama dengan yang diunggah.
  - TC-GS-USER-206 menyebut deleter `System` untuk foto lama sedangkan TC-GS-USER-205 menyebut actor = admin yang login untuk foto yang dihapus lewat Delete; spec mengikuti masing-masing TC.
  - TC-GS-USER-206 menyebut `john2.png` tanpa menyebut ketersediaannya sebagai fixture; disediakan tim FE.
- Spec melewati sekitar 35 langkah (40 langkah) karena memuat satu kelas (Edit foto profil) pada satu user seed yang keadaannya dipakai berurutan, dan tiap blok TC berdiri sendiri; sebagian langkah adalah navigasi ke File Manager dan Recycle Bin.
