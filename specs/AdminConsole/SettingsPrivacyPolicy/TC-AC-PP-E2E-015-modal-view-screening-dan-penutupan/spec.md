---
id: TC-AC-PP-E2E-015-modal-view-screening-dan-penutupan
title: "Modal View: Screening Versi Active dan Superseded, Jalur Buka, serta Penutupan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-26
  - TC-AC-PP-27
  - TC-AC-PP-28
  - TC-AC-PP-30
coverage:
  web: automated
---

# Modal View: Screening Versi Active dan Superseded, Jalur Buka, serta Penutupan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, Andi Wijaya, env `Spectra.env.AC_TC_PASSWORD`), login di hook `before`; hook `after` mengembalikan sesi ke akun default suite yang sama.
- Dataset Riwayat A di-seed di hook `before` lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat versi append-only) dan dikembalikan ke Riwayat A di hook `after`:
  - Version 3 Active, 10 Aug 2026 pukul 20:30 UTC, `John Doe`; isi: H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`.
  - Version 2, 02 Jul 2026 pukul 09:14 UTC, `John Doe`; isi: paragraf `Old policy text for version two.`.
  - Version 1, 15 Jan 2026 pukul 02:11 UTC, `Jane Smith` (akun sudah dihapus).
- Spec tidak membuat atau mengubah versi. Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-26: Screening Modal View untuk versi Active

1. Buka Settings > Privacy Policy
2. Klik `[⋯]` pada baris `Version 3`
3. Pilih `Detail`
4. Tunggu konten termuat
5. Susuri modal dari atas ke bawah tanpa mengklik apa pun
6. Verifikasi `Settings > Privacy Policy > Popup Privacy Policy Detail` terbuka
7. Verifikasi Header: Title modal "Privacy Policy Detail" (flat, tanpa nomor versi)
8. Verifikasi Header: tombol close `[✕]` di kanan atas
9. Verifikasi Header: info bar satu baris read-only `Version 3 · Published At 10 Aug 26 · Published By John D`
10. Verifikasi Published At pada info bar hanya tanggal, tanpa jam
11. Verifikasi Published By pada info bar berupa komponen user dengan ikon user generik dan teks `John D`
12. Hover `John D` pada info bar
13. Verifikasi tooltip `John Doe` tampil
14. Verifikasi Body: konten rendered HTML read-only (H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`)
15. Verifikasi Body memiliki scroll vertikal bila konten panjang
16. Verifikasi Footer: hanya tombol `[Edit]`
17. Verifikasi Footer: tidak ada tombol Close atau Cancel
18. Klik `[✕]` pada header modal

### TC-AC-PP-27: Screening Modal View untuk versi Superseded dengan render identik dan footer kosong

19. Klik `[⋯]` pada baris `Version 2`
20. Pilih `Detail`
21. Tunggu konten termuat
22. Susuri modal dari atas ke bawah
23. Verifikasi Header: Title "Privacy Policy Detail"
24. Verifikasi Header: tombol close `[✕]`
25. Verifikasi Header: info bar `Version 2 · Published At 02 Jul 26 · Published By John D`
26. Verifikasi Published By pada info bar berupa komponen user dengan ikon user generik
27. Verifikasi Body: konten Version 2 (`Old policy text for version two.`) tampil rendered read-only, tanpa pembatasan berdasarkan usia versi
28. Verifikasi Footer kosong
29. Verifikasi tombol `[Edit]` tidak ada
30. Verifikasi tombol Close tidak ada
31. Klik `[✕]` pada header modal

### TC-AC-PP-28: Klik tautan Version dan row action Detail membuka Modal View yang identik

32. Klik teks tautan `Version 2`
33. Verifikasi `Popup Privacy Policy Detail` terbuka langsung di state View
34. Catat Title, info bar, konten, dan isi footer modal
35. Klik `[✕]` pada header modal
36. Klik `[⋯]` pada baris `Version 2`
37. Pilih `Detail`
38. Verifikasi Title modal sama dengan yang dicatat pada langkah 34
39. Verifikasi info bar modal sama dengan yang dicatat pada langkah 34
40. Verifikasi konten modal sama dengan yang dicatat pada langkah 34
41. Verifikasi footer modal kosong, sama dengan yang dicatat pada langkah 34
42. Verifikasi tidak ada navigasi halaman pada jalur tautan Version maupun jalur row action Detail
43. Klik `[✕]` pada header modal

### TC-AC-PP-30: Esc menutup Modal View sedangkan klik di luar modal diabaikan

44. Klik teks tautan `Version 3`
45. Verifikasi Modal View terbuka
46. Klik area gelap di luar modal
47. Verifikasi modal tetap terbuka
48. Tekan Esc
49. Verifikasi modal tertutup
50. Verifikasi tidak ada dialog yang tampil
51. Verifikasi tabel Version History tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-AC-PP-30 bertanda FE Test "UI Only" di TC tetapi dijalankan di spec FE+BE karena datanya dari backend nyata.
- Langkah penghubung: langkah 18, 31, dan 43 menutup modal bersih lewat `[✕]` (tanpa dialog) agar TC berikutnya mulai dari tabel.
- Penyimpangan kecil: langkah 34 dan 38-41 menerjemahkan Expected b TC-AC-PP-28 ("modal yang terbuka sama persis (Title, info bar, konten, footer kosong) dengan langkah 1") menjadi perbandingan nilai yang dicatat pada langkah 34, satu `Verifikasi` per bagian modal.
- Langkah 12 (hover `John D`) dan langkah 5/22 (menyusuri modal) adalah aksi pengamatan yang diperlukan Expected TC.
- Spec melewati sekitar 35 langkah (51 langkah) tanpa pengecualian P-1/P-2/P-3; tidak dipecah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01), seluruh TC memakai satu dataset (Riwayat A) dan akun yang sama, tidak ada kelas harness lain, dan tiap blok `###` berdiri sendiri (dimulai dari tabel setelah langkah penghubung penutupan modal) sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: TC-AC-PP-26 Expected b menyatakan "scroll vertikal bila panjang" tanpa batas ukuran konten pada dataset Riwayat A; spec hanya mengasersi bahwa area Body mendukung scroll vertikal, perilaku pada konten 200 paragraf ada di spec `TC-AC-PP-E2E-016`. Post Condition keempat TC ("Tidak ada perubahan data") tidak punya langkah observasi sehingga tidak diasersi.
