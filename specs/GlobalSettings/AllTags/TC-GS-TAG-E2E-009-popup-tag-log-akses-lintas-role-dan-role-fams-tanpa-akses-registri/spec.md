---
id: TC-GS-TAG-E2E-009-popup-tag-log-akses-lintas-role-dan-role-fams-tanpa-akses-registri
title: "Popup TAG Log: Terbuka untuk Semua Role dan Status, serta Role FAMS Manage asset & TAG Tanpa Akses Registri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-35
  - TC-GS-TAG-372
  - TC-GS-TAG-373
coverage:
  web: automated
---

# Popup TAG Log: Terbuka untuk Semua Role dan Status, serta Role FAMS Manage asset & TAG Tanpa Akses Registri

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Read Only) di hook `before`; ganti akun ke role FAMS ditulis sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.

Role yang diuji (Tabel Data Uji Pre-setup; Client A):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-35 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-372 | Manage asset & TAG (Read) FAMS | Bayu Prasetyo | `manageAssetTagRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FAMS_ASSETTAG_READ_PASSWORD` |
| TC-373 | Manage asset & TAG (Update) FAMS | Citra Dewanti | `manageAssetTagUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FAMS_ASSETTAG_UPDATE_PASSWORD` |

- `GS_FAMS_ASSETTAG_READ_PASSWORD` dan `GS_FAMS_ASSETTAG_UPDATE_PASSWORD` belum terdaftar di `.env.example` dan `spectra.config.ts` (dicatat di `suite.md` bagian Kredensial).
- Data Pre-setup (hanya dibaca): Seed Registri A; DD-01 (Paired ke aset yang tampil di Fixed Asset > TAG > Tab Paired) dengan entri TAG Log `Activated`, `Reserved`, `Paired` (fixture TAG Log Seed Registri A); DD-08 `E2801160600002054D8A0008` (Retired). Nama aset yang terpasang pada DD-01 disediakan tim FE (tidak ada di Pre-setup TC; lihat Temuan untuk QA). Seed di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Surface di luar modul: Fixed Asset > TAG > Tab Paired dan Popup Detail aset adalah selektor milik suite Fixed Asset; langkah dan selektornya disediakan tim FE (S-13, Q-9).
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach` untuk akun hook; setelah ganti akun, halaman dibuka lewat langkah.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true untuk akun Global Settings oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-35: TAG Log tersedia untuk semua role yang bisa melihat registri dan semua status

1. Buka menu baris DD-01 (Paired), klik `TAG Log`
2. Verifikasi Popup TAG Log terbuka untuk DD-01
3. Baca isi Popup TAG Log DD-01 (judul, badge Status, grid label:value, daftar entri) sebagai acuan TC-372
4. Tutup popup
5. Buka menu baris DD-08 (Retired), klik `TAG Log`
6. Verifikasi Popup TAG Log terbuka untuk DD-08
7. Tutup popup

### TC-GS-TAG-372: Role FAMS Manage asset & TAG (Read) tanpa akses registri membuka Popup TAG Log dari Fixed Asset > TAG

8. Logout, lalu login sebagai Manage asset & TAG (Read) FAMS (Bayu Prasetyo)
9. Amati sidebar Global Settings
10. Verifikasi sedikitnya satu item menu Global Settings lain tampil di sidebar
11. Verifikasi item `TAG` tidak tampil pada sidebar Global Settings
12. Ketik URL halaman Global Settings > TAG langsung di address bar, tekan Enter
13. Verifikasi toast error `You don't have permission to do this.`
14. Verifikasi daftar tag tidak termuat
15. Buka Fixed Asset > TAG > Tab Paired
16. Klik Asset Name aset bertag DD-01 untuk membuka Popup Detail
17. Klik TAG Code `E2801160600002054D8A0001`
18. Verifikasi Popup TAG Log terbuka untuk DD-01 dengan judul `TAG Log`
19. Verifikasi badge Status `Paired`
20. Verifikasi grid label:value tampil
21. Verifikasi daftar entri `Activated`, `Reserved`, `Paired` dengan entri terbaru di atas
22. Verifikasi isi popup sama dengan yang dibaca dari registri (langkah 3)
23. Verifikasi popup hanya memiliki ikon close
24. Verifikasi popup tidak memiliki Search, Filter, Sort, Download, footer, maupun kontrol edit atau hapus
25. Klik `[✕]` untuk menutup popup
26. Verifikasi popup tertutup

### TC-GS-TAG-373: Role FAMS Manage asset & TAG (Update) tanpa akses registri membuka Popup TAG Log read-only

27. Logout, lalu login sebagai Manage asset & TAG (Update) FAMS (Citra Dewanti)
28. Buka Fixed Asset > TAG > Tab Paired
29. Klik Asset Name aset bertag DD-01 untuk membuka Popup Detail
30. Klik TAG Code `E2801160600002054D8A0001`
31. Verifikasi Popup TAG Log terbuka untuk DD-01 dengan isi yang sama seperti dari registri
32. Verifikasi popup tetap read-only dengan hanya ikon close
33. Verifikasi popup tidak memiliki kontrol edit atau hapus
34. Verifikasi level Update tidak menambah aksi pada popup
35. Klik `[✕]` untuk menutup popup (langkah penghubung)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Sections 2 dan 7d/8). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3 (baca isi sebagai acuan perbandingan lintas surface), 4, 7, 35 (menutup popup), langkah ganti akun 8 dan 27 (Step ganti akun eksplisit, S-07), membuka surface (9, 15, 16, 17, 28 sampai 30). Langkah 10 adalah anchor positif absence menu (langkah 11); langkah 13 adalah anchor positif untuk langkah 14 (8b butir 2).
- Rujukan lintas spec: TC-374 (request langsung role FAMS Manage asset & TAG (Read): registri dan Delete ditolak, baca TAG Log berhasil) ada di spec 014.
- Role lain untuk TC-35 (Total Control, Manage TAG Update, Manage TAG Read) tidak diuji karena TC sumber hanya mendefinisikan Read Only; kombinasi dilaporkan sebagai usulan TC baru (bagian 3a).
- Temuan untuk QA:
  - TC-35 berjudul "semua role ... dan semua status" tetapi Precondition dan langkah hanya Read Only dengan dua status (Paired, Retired); role lain dan status lain tidak punya TC.
  - TC-372 dan TC-373 tidak menyebut nama aset yang terpasang pada DD-01 maupun Asset Name yang diklik; spec menulis "aset bertag DD-01" dan nama disediakan tim FE (S-13, Q-9).
  - TC-372 butir b: "sama seperti yang dibuka dari registri" dibandingkan dengan isi yang dibaca pada langkah 3; TC tidak mendefinisikan metode pembandingan.
  - Post Condition semua TC bernilai `-`.
- Alasan spec melewati sekitar 35 langkah (35 nominal, sedikit di atas ambang): tiga TC satu topik (akses Popup TAG Log) dengan tiga akun berbeda dan Step ganti akun eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3 konvensi kasus (b)).
