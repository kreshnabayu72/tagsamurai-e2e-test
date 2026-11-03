---
id: TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong
title: "Client Baru: Empty State Seed Default Group, Modified By System, Seed Tidak Dicatat Changelog, dan Modal Changelog Genuine Empty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-9
  - TC-FA-GRP-428
  - TC-FA-GRP-888
  - TC-FA-GRP-893
  - TC-FA-GRP-894
  - TC-FA-GRP-1128
coverage:
  web: automated
---

# Client Baru: Empty State Seed Default Group, Modified By System, Seed Tidak Dicatat Changelog, dan Modal Changelog Genuine Empty

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client automation baru. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE bersama client barunya. Password `Spectra.env.FA_NEWCLIENT_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control client baru; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk akun client baru disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (hook suite hanya menyetel akun aktor default suite).
- State awal wajib: client baru yang baru onboard, hanya berisi Default Group seed, tanpa entri Changelog, System Log, maupun Activity Log atas Default Group. Client baru disediakan tim FE/BE per run karena state awal ini hanya ada sekali per client.
- Data Dinamis: Description `Deskripsi {runId}-004` untuk Default Group (TC-FA-GRP-894); dipulihkan ke nilai awal di hook `after` lewat fixture BE.
- Kemampuan teknis: fixture BE (membaca waktu onboard client, mengembalikan Description Default Group), kemampuan membaca System Log dan Activity Log, serta sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Jam server dan jam browser sinkron untuk asersi Last Updated.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-9: Empty (Seed) client baru

1. Verifikasi tabel menampilkan 1 baris tunggal Default Group
2. Verifikasi Code Default Group `DG`
3. Verifikasi Function Default Group `—`
4. Verifikasi Total Asset Default Group `0`
5. Verifikasi Total User Default Group bernilai 1 atau lebih
6. Verifikasi Modified By Default Group `System`
7. Verifikasi tidak ada CTA pada area tabel
8. Verifikasi sidebar menampilkan `All Groups` dan `Default Group`

### TC-FA-GRP-893: Seed Default Group, Modified By System

9. Verifikasi Modified By Default Group `System`
10. Verifikasi Last Updated Default Group sama dengan waktu client onboard (dibaca lewat fixture BE) dalam format General Settings
11. Klik ikon `Filter`
12. Buka dropdown field Modified By
13. Verifikasi opsi filter Modified By memuat `System`
14. Tutup panel Filter dengan Esc

### TC-FA-GRP-428: Modal Changelog genuine empty

15. Klik ikon `Changelog`
16. Verifikasi tabel Modal Changelog menampilkan Illustration dengan title `No changelog yet` dan body `Activities and changes will appear here.`

### TC-FA-GRP-888: Seed tidak dicatat di Changelog

17. Verifikasi Modal Changelog tidak memuat baris Create untuk Default Group (jumlah baris 0 sebagai baseline; empty state tampil pada langkah 16)

### TC-FA-GRP-893 (lanjutan): seed tidak dicatat di log lain

18. Baca System Log dan Activity Log untuk entri atas Default Group lewat kemampuan baca log
19. Verifikasi jumlah entri System Log dan Activity Log atas Default Group adalah 0

### TC-FA-GRP-1128: Modal Changelog genuine empty, toolbar, Download, dan Filter

20. Verifikasi toolbar Modal Changelog menampilkan `Search`, `Filter`, dan `Download`
21. Klik `Download`
22. Klik `Download as CSV`
23. Verifikasi tidak ada toast yang tampil
24. Verifikasi berkas CSV terunduh
25. Verifikasi berkas CSV hanya berisi baris header kolom yang visible dan tanpa baris data
26. Klik ikon `Filter` pada Modal Changelog
27. Buka dropdown field Action
28. Verifikasi dropdown Action menampilkan teks `No options available`
29. Tutup panel Filter dengan Esc
30. Tutup Modal Changelog dengan ✕

### TC-FA-GRP-894: Setelah diedit, Modified By menjadi aktor

31. Klik (⋯) pada baris Default Group
32. Klik `Edit`
33. Isi Description `Deskripsi {runId}-004`
34. Klik [Save]
35. Verifikasi Modified By Default Group berubah menjadi nama aktor berformat `[First Name] [Last Initial]`
36. Verifikasi Last Updated Default Group sama dengan waktu save dengan toleransi satu menit
37. Klik ikon `Changelog`
38. Verifikasi Modal Changelog memuat tepat satu baris baru (selisih terhadap baseline 0 pada langkah 16) berupa Edit untuk Default Group
39. Tutup Modal Changelog dengan ✕
40. Pulihkan Description Default Group ke nilai awal lewat fixture BE

## Notes

- Spec melewati sekitar 35 langkah (40 langkah): seluruh TC bergantung pada keadaan client baru yang sama (hanya Default Group, log kosong) yang hanya ada sekali per client, sehingga blok TC-FA-GRP-894 yang mengubah Default Group wajib berada paling akhir dan tidak dapat dipisah tanpa menyediakan client baru kedua. Butir `P-1`: state berat (client baru) dipakai bersama oleh asersi absence TC-FA-GRP-888 dan TC-FA-GRP-893 (c) dengan baseline 0 dan anchor `No changelog yet`.
- Langkah penghubung (S-03): langkah 14, 29 (menutup panel Filter), langkah 30 dan 39 (menutup Modal Changelog), langkah 40 (pemulihan state).
- Urutan TC dalam spec: 9, 893, 428, 888, 1128, 894 (screening sebelum aksi; Edit yang menambah entri Changelog paling akhir, S-10).
- Temuan untuk QA:
  - Email akun Total Control client baru tidak ada di Tabel Data Uji Pre-setup.
  - TC-FA-GRP-893 (c) menyebut System Log dan Activity Log tanpa menyebut surface atau cara membacanya; spec memakai kemampuan baca log yang disediakan tim FE/BE.
  - TC-FA-GRP-1128 tidak menyebut label pilihan unduh selain `Download as CSV`; spec memakai teks itu persis.
  - TC-FA-GRP-894 tidak menyebut nilai Description; spec memakai nilai bersuffix.
