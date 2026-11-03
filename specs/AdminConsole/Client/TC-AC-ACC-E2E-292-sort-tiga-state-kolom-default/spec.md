---
id: TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default
title: "Sort Client List: Siklus Tiga State Ascending, Descending, dan Nonaktif pada Kolom Default dan Managed By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-394
  - TC-AC-ACC-395
  - TC-AC-ACC-396
  - TC-AC-ACC-397
  - TC-AC-ACC-398
  - TC-AC-ACC-399
  - TC-AC-ACC-400
  - TC-AC-ACC-401
  - TC-AC-ACC-402
  - TC-AC-ACC-403
  - TC-AC-ACC-986
coverage:
  web: automated
---

# Sort Client List: Siklus Tiga State Ascending, Descending, dan Nonaktif pada Kolom Default dan Managed By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 `PT Sortir Alfa`, C-LST-2 `PT Sortir Beta`, dan C-LST-3 `PT Sortir Gamma` tersedia dan hanya dibaca; spec memakai Search `Sortir` agar hanya ketiganya yang tersisa.
- Fixture residen A3 untuk TC-AC-ACC-986: C-FX13-2 `PT Urut Managed Alfa` (Distributor langsung PT Distribusi Nusantara, sel Managed By `PT Distribusi Nusantara (Direct)`), C-FX13-3 `PT Urut Managed Beta` (Partner CV Mitra Sejati, sel `CV Mitra Sejati`), C-FX13-4 `PT Urut Managed Gamma` (tanpa relasi manager, sel `Direct`). Untuk TC-AC-ACC-397: C-10 `PT Lintas Jaringan` (Anchor CV Mitra Sejati, relasi kedua CV Mitra Timur) dan C-12 `PT Timur Perkasa` (Partner CV Mitra Timur).
- Tabel parameter kolom (dipakai langkah 3 sampai 11; urutan ascending, descending adalah kebalikannya): Company Name: `PT Sortir Alfa`, `PT Sortir Beta`, `PT Sortir Gamma`; Client Code: `PT Sortir Beta` (SRT-100), `PT Sortir Gamma` (SRT-200), `PT Sortir Alfa` (SRT-301); PIC Name: `PT Sortir Beta` (Bagas Pratama), `PT Sortir Alfa` (Hendra Gunawan), `PT Sortir Gamma` (Sari Wulandari); Group: `PT Sortir Gamma` (Area Jakarta), `PT Sortir Alfa` (Cabang Menteng), `PT Sortir Beta` (Regional Timur); FAMS: `PT Sortir Gamma` (Active), `PT Sortir Alfa` (Grace), `PT Sortir Beta` (Pending); SAMS: `PT Sortir Alfa` (Active), `PT Sortir Beta` (Grace), `PT Sortir Gamma` (Pending); SIEM: `PT Sortir Beta` (Active), `PT Sortir Gamma` (Grace), `PT Sortir Alfa` (Pending); Last Updated: `PT Sortir Beta` (20 Jan 2026), `PT Sortir Alfa` (05 Mar 2026), `PT Sortir Gamma` (12 Jul 2026).
- Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Sort kolom default dengan Search Sortir (TC-AC-ACC-394, 395, 396, 398, 399, 400, 401, 403)

1. Ketik Search `Sortir`, tekan Enter
2. Verifikasi `PT Sortir Alfa`, `PT Sortir Beta`, dan `PT Sortir Gamma` tersisa di tabel
3. Untuk setiap baris tabel parameter kolom: klik header kolom itu satu kali
4. Verifikasi indikator sort kolom itu berupa panah naik (ascending)
5. Verifikasi urutan baris ascending sesuai tabel parameter
6. Klik header kolom itu untuk kedua kali
7. Verifikasi indikator sort kolom itu berupa panah turun (descending)
8. Verifikasi urutan baris descending adalah kebalikan tabel parameter
9. Klik header kolom itu untuk ketiga kali
10. Verifikasi indikator sort kolom itu nonaktif
11. Verifikasi urutan kembali ke default Company Name A-Z: `PT Sortir Alfa`, `PT Sortir Beta`, `PT Sortir Gamma`

### Sort Modified By dengan hover nama lengkap (TC-AC-ACC-402)

12. Klik header kolom Modified By satu kali
13. Verifikasi ascending (panah naik): `PT Sortir Beta` (Andi Wijaya), lalu `PT Sortir Gamma` (Citra Sanjaya), lalu `PT Sortir Alfa` (Citra Santoso)
14. Arahkan kursor ke Modified By pada baris kedua lalu pada baris ketiga
15. Verifikasi hover Modified By baris kedua menampilkan `Citra Sanjaya` dan baris ketiga menampilkan `Citra Santoso` (urut berdasarkan nama lengkap, bukan teks tampilan `Citra S`)
16. Klik header kolom Modified By untuk kedua kali
17. Verifikasi descending (panah turun): `PT Sortir Alfa` (Citra Santoso), lalu `PT Sortir Gamma` (Citra Sanjaya), lalu `PT Sortir Beta` (Andi Wijaya)
18. Klik header kolom Modified By untuk ketiga kali
19. Verifikasi indikator sort kolom Modified By nonaktif
20. Verifikasi urutan kembali ke default Company Name A-Z: `PT Sortir Alfa`, `PT Sortir Beta`, `PT Sortir Gamma`
21. Klik `(←)` pada kotak Search

### Sort Managed By menurut nama Anchor (TC-AC-ACC-397)

22. Klik Filter, pilih Partner `CV Mitra Timur`, lalu klik [Apply]
23. Ubah ukuran halaman menjadi 100 baris
24. Klik header kolom Managed By satu kali
25. Verifikasi ascending (panah naik): `PT Lintas Jaringan` (Anchor CV Mitra Sejati, `+1 more`), lalu `PT Timur Perkasa` (Anchor CV Mitra Timur, tanpa `+N more`); bukan urutan menurut jumlah `+N more`
26. Klik header kolom Managed By untuk kedua kali
27. Verifikasi descending (panah turun): `PT Timur Perkasa`, lalu `PT Lintas Jaringan`
28. Klik header kolom Managed By untuk ketiga kali
29. Verifikasi indikator sort kolom Managed By nonaktif
30. Verifikasi urutan kembali ke default Company Name A-Z: `PT Lintas Jaringan`, lalu `PT Timur Perkasa`
31. Klik Filter, klik [Clear Field], lalu klik [Apply]

### Managed By Direct sebagai teks biasa (TC-AC-ACC-986)

32. Klik sub-tab Active, ketik Search `Urut Managed`, tekan Enter
33. Verifikasi default Company Name A-Z: `PT Urut Managed Alfa`, lalu `PT Urut Managed Beta`, lalu `PT Urut Managed Gamma`
34. Verifikasi sel Managed By ketiga baris berturut-turut `PT Distribusi Nusantara (Direct)`, `CV Mitra Sejati`, `Direct`
35. Klik header kolom Managed By satu kali
36. Verifikasi ascending (panah naik): `PT Urut Managed Beta` (`CV Mitra Sejati`), lalu `PT Urut Managed Gamma` (`Direct`), lalu `PT Urut Managed Alfa` (`PT Distribusi Nusantara (Direct)`)
37. Verifikasi nilai sel `Direct` diurutkan sebagai teks biasa di antara `CV Mitra Sejati` dan `PT Distribusi Nusantara`
38. Klik header kolom Managed By untuk kedua kali
39. Verifikasi descending (panah turun): `PT Urut Managed Alfa`, lalu `PT Urut Managed Gamma`, lalu `PT Urut Managed Beta`
40. Klik header kolom Managed By untuk ketiga kali
41. Verifikasi indikator sort kolom Managed By nonaktif
42. Verifikasi urutan kembali ke default Company Name A-Z: `PT Urut Managed Alfa`, `PT Urut Managed Beta`, `PT Urut Managed Gamma`
43. Klik `(←)` pada kotak Search

## Notes

- Langkah 3 sampai 11 diulang per baris tabel parameter (8 iterasi: Company Name, Client Code, PIC Name, Group, FAMS, SAMS, SIEM, Last Updated); satu `Verifikasi` per klausa Expected tiap iterasi. Spec melewati sekitar 35 langkah setelah ekspansi; alasan: semua blok satu kelas harness dan satu dataset (Sort List), blok berurutan tanpa state bersama dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Nama literal fixture A3 (`PT Sortir ...`, `PT Urut Managed ...`) dipakai sebagai pengecualian S-12 butir Q5 (asersi urutan/jumlah pada Population Pre-setup); fixture residen dan hanya dibaca.
- Langkah penghubung (S-03): Search `Sortir`, Filter Partner dan ukuran halaman 100 untuk TC-AC-ACC-397 mengikuti Langkah TC; [Clear Field]/[Apply] dan `(←)` memulihkan state (S-09).
- Temuan untuk QA
  - TC-AC-ACC-986: Langkah 1 TC memakai sub-tab Active; fixture C-FX13-4 ber-Group Cabang Menteng sedangkan C-FX13-2 dan C-FX13-3 Area Jakarta; tidak berdampak pada urutan Managed By.
  - TC-AC-ACC-397: Expected `urutan relatif` tidak mengasersi kolom lain; spec hanya mengasersi dua baris.
