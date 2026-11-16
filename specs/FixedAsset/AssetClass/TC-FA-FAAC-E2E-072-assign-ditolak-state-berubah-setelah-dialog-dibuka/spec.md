---
id: TC-FA-FAAC-E2E-072-assign-ditolak-state-berubah-setelah-dialog-dibuka
title: "Assign Ditolak atau Dilewati saat State Berubah Setelah Dialog Dibuka"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-161
  - TC-FA-FAAC-162
  - TC-FA-FAAC-163
  - TC-FA-FAAC-164
sourceRules: ["F-FAAC-08.k4", "T-07", "FAAC-LOGIC-13b", "L-06", "§[F-FAAC-08] Assign Asset Names#b5", "F-FAAC-08.k5", "FI-12", "F-FAAC-08.k7", "D-20", "F-FAAC-08.k3"]
smoke: []
dependsOn: []
trace:
  "F-FAAC-08.k4": [7, 8]
  "T-07": [9, 20]
  "FAAC-LOGIC-13b": [10, 21]
  "L-06": 11
  "§[F-FAAC-08] Assign Asset Names#b5": 11
  "F-FAAC-08.k5": [18, 19, 22]
  "FI-12": [25, 31]
  "F-FAAC-08.k7": [28, 29, 30]
  "D-20": 39
  "F-FAAC-08.k3": [40, 42]
coverage:
  web: automated
---

# Assign Ditolak atau Dilewati saat State Berubah Setelah Dialog Dibuka

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Pelaku kedua: sesi API aktor (login API password, token tidak dihitung sebagai sesi web; lihat `suite.md`); bukan konteks UI kedua.
- Data milik spec (seed di hook `before` lewat API setelah menghapus sisa run sebelumnya, dihapus di hook `after`): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-072`, Class Name `Anchor Class {runId}-072` (disebut "anchor").
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after` dan di langkah penghubung): tanpa Asset Class: Pallet Jack Electric (0 aset aktif), Meeting Table (0 aset aktif); "Delivery Van" (9 aset aktif) di 'Vehicles' (VEHICLES); Asset Class 'Machinery' (MACHINERY). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; sesi API aktor untuk assign, hapus Asset Name, ubah status aset, dan nonaktifkan Asset Class; kemampuan baca BE untuk keanggotaan Asset Name.
- State global: keanggotaan Asset Name, status Asset Class anchor, dan status aset Delivery Van berubah; dipulihkan di hook `after`.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik link Class Code `ANCHOR-072`, lalu klik tab "Asset Names"

### TC-FA-FAAC-163: Assign melewati Asset Name yang sudah dipindahkan pengguna lain sejak dialog dibuka

2. Klik tombol "+ Assign Asset Names"
3. Centang "Pallet Jack Electric" dan "Meeting Table"
4. Assign "Pallet Jack Electric" ke Asset Class "Machinery" (MACHINERY) lewat sesi API aktor hingga tersimpan
5. Catat jumlah entri Changelog Asset Class yang memuat "Pallet Jack Electric" (Np) sebagai baseline lewat kemampuan baca log
6. Klik [Assign] pada sesi pertama
7. Verifikasi "Pallet Jack Electric" dilewati (tetap di MACHINERY)
8. Verifikasi "Meeting Table" diproses
9. Verifikasi muncul toast sukses: "Success, asset name has been assigned."
10. Verifikasi hanya "Meeting Table" tampil di tab Asset Names
11. Verifikasi jumlah entri Changelog Asset Class yang memuat "Pallet Jack Electric" sama dengan Np (dilewati tanpa log)

### TC-FA-FAAC-164: Assign melewati Asset Name yang sudah dihapus sejak dialog dibuka tanpa menulis log

12. Pulihkan "Pallet Jack Electric" dan "Meeting Table" menjadi Asset Name tanpa Asset Class lewat fixture BE
13. Klik tombol "+ Assign Asset Names"
14. Centang "Pallet Jack Electric" dan "Meeting Table"
15. Hapus Asset Name "Pallet Jack Electric" (setara Settings > Asset Master > Asset Name) lewat sesi API aktor hingga tersimpan
16. Catat jumlah entri Changelog Asset Class yang memuat "Pallet Jack Electric" (Np) sebagai baseline lewat kemampuan baca log
17. Klik [Assign] pada sesi pertama
18. Verifikasi "Pallet Jack Electric" dilewati (tidak tampil di tab Asset Names)
19. Verifikasi "Meeting Table" diproses
20. Verifikasi muncul toast sukses: "Success, asset name has been assigned."
21. Verifikasi hanya "Meeting Table" tampil di tab Asset Names
22. Verifikasi jumlah entri Changelog Asset Class yang memuat "Pallet Jack Electric" sama dengan Np (dilewati tanpa log)

### TC-FA-FAAC-162: Assign ditolak tanpa toast saat status aset aktif Asset Name berubah setelah dialog dibuka

23. Klik tombol "+ Assign Asset Names"
24. Hilangkan centang "Without asset class only", lalu centang "Delivery Van"
25. Verifikasi Effective From dan pratinjau dampak tampil (aset aktif 9)
26. Ubah seluruh aset Delivery Van menjadi tidak berlifecycle Active sehingga aset aktifnya 0 lewat sesi API aktor hingga tersimpan
27. Klik [Assign] pada sesi pertama
28. Verifikasi [Assign] ditolak tanpa perubahan data: "Delivery Van" tetap di VEHICLES
29. Verifikasi tidak ada toast
30. Verifikasi dialog Assign tetap terbuka
31. Verifikasi Effective From dan pratinjau dampak Hidden (aset aktif 0)
32. Klik [Cancel]
33. Pulihkan status aset Delivery Van menjadi Active lewat fixture BE
34. Pulihkan "Meeting Table" menjadi Asset Name tanpa Asset Class lewat fixture BE

### TC-FA-FAAC-161: Konfirmasi Assign ditolak saat Asset Class menjadi Inactive setelah dialog dibuka

35. Klik tombol "+ Assign Asset Names"
36. Centang "Meeting Table"
37. Nonaktifkan Asset Class anchor lewat sesi API aktor (toggle Active, konfirmasi Deactivate) hingga tersimpan
38. Klik [Assign] pada sesi pertama
39. Verifikasi Dialog Blok tampil: Title "Asset Class Unavailable", Body "• ANCHOR-072 – Anchor Class {runId}-072" dan "This asset class is inactive. Activate it first.", tombol [OK]
40. Verifikasi tidak ada toast tambahan
41. Klik [OK]
42. Verifikasi "Meeting Table" tidak ter-assign ke Asset Class anchor

## Notes

- Class Code `ANCHOR-072` ditulis literal tanpa `{runId}` karena Class Code dibatasi 15 karakter (TC-98) sehingga suffix itu tidak muat; `{runId}-072` dipindah ke Class Name agar unik per run (S-12; pola spec 066 sampai 069 dan 047/048); cleanup di hook `before` dan `after`.
- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 163, 164, 162, 161 (TC-161 menonaktifkan anchor sehingga diletakkan terakhir; TC-164 memerlukan Asset Name yang sudah di-assign TC-163 dipulihkan lebih dulu).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name dan Asset Class seed dipakai apa adanya; dipulihkan oleh fixture BE.
- Pelaku kedua memakai sesi API (keputusan 2026-10-30): bukan kelas c, tanpa butir `P-2`; langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (S-03): langkah 1 (membuka Detail anchor), 5 dan 16 (baseline Changelog, S-12), 12, 32, 33, dan 34 (pemulihan state seed atau menutup dialog; langkah 34 memulihkan "Meeting Table" yang di-assign ke anchor oleh blok TC-164 sebelum blok TC-161 mencentangnya), 41 (menutup Dialog Blok).
- S-05 dan P-1: Expected "tanpa log" pada TC-163 dan TC-164 diasersi di spec ini (langkah 11 dan 22) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class. Entri Assign untuk "Meeting Table" memang bertambah, sehingga baseline dan asersi dibatasi pada entri yang memuat Asset Name yang dilewati ("Pallet Jack Electric").
- Langkah 25 menjadi anchor positif bagi asersi Hidden langkah 31 (tambahan terhadap TC, dicatat sesuai S-03).
- Spec di atas 35 langkah (42 langkah): empat TC satu topik (Assign ditolak/dilewati karena state berubah) pada satu anchor dan satu pelaku kedua; Expected bermajemuk dipecah per klausa (S-01) dan pemecahan lagi menggandakan seed anchor tanpa pemisah nyata.
- Temuan untuk QA: TC-163 dan TC-164 menyebut "tidak dihitung pada toast" padahal teks toast tidak memuat jumlah; spec mengasersi teks toast persis. Teks toast hasil Assign sebagian dilewati tidak dibedakan dari Assign biasa.
